// Converte arquivos .md simplificados em DOCX formatados para a candidatura fictícia.
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, Table, TableRow, TableCell,
  WidthType, ShadingType, BorderStyle, Header, Footer, PageNumber, LevelFormat, ImageRun,
  TableOfContents, PageBreak, VerticalAlign
} = require('docx');

const ROOT = path.join(__dirname, '..');
const C = { petroleo: '0F4C5C', ocre: 'D99A2B', terracota: 'B5482F', areia: 'F2EBDD', grafite: '1E2A30', cinza: '5A6B73', claro: 'E6EEF0' };
const FONT = 'Arial';
const PAGE_W = 11906, MARGIN = 1134, CONTENT_W = PAGE_W - 2 * MARGIN;

function runs(text, base = {}) {
  // **negrito** e *itálico*
  const out = [];
  const re = /(\*\*[^*]+\*\*|\*[^*]+\*)/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), font: FONT, ...base }));
    const t = m[0];
    if (t.startsWith('**')) out.push(new TextRun({ text: t.slice(2, -2), bold: true, font: FONT, ...base }));
    else out.push(new TextRun({ text: t.slice(1, -1), italics: true, font: FONT, ...base }));
    last = m.index + t.length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), font: FONT, ...base }));
  return out;
}

const border = { style: BorderStyle.SINGLE, size: 4, color: 'B8C6CB' };
const borders = { top: border, bottom: border, left: border, right: border };

function makeTable(rows, pct) {
  const ncol = rows[0].length;
  let widths;
  if (pct && pct.length === ncol) {
    const tot = pct.reduce((a, b) => a + b, 0);
    widths = pct.map(p => Math.floor(CONTENT_W * p / tot));
  } else widths = Array(ncol).fill(Math.floor(CONTENT_W / ncol));
  const diff = CONTENT_W - widths.reduce((a, b) => a + b, 0); widths[widths.length - 1] += diff;
  const small = ncol >= 5;
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: widths,
    rows: rows.map((r, ri) => new TableRow({
      tableHeader: ri === 0,
      cantSplit: true,
      children: r.map((cell, ci) => new TableCell({
        borders,
        width: { size: widths[ci], type: WidthType.DXA },
        shading: ri === 0 ? { fill: C.petroleo, type: ShadingType.CLEAR, color: 'auto' } : (ri % 2 === 0 ? { fill: 'F5F8F9', type: ShadingType.CLEAR, color: 'auto' } : undefined),
        margins: { top: 60, bottom: 60, left: 90, right: 90 },
        verticalAlign: VerticalAlign.CENTER,
        children: cell.split('<br>').map(seg => new Paragraph({
          spacing: { before: 0, after: 0, line: 252 },
          children: runs(seg.trim(), ri === 0 ? { bold: true, color: 'FFFFFF', size: small ? 16 : 18 } : { size: small ? 16 : 18, color: C.grafite })
        }))
      }))
    }))
  });
}

function img(file, w, h) {
  return new ImageRun({ type: 'png', data: fs.readFileSync(file), transformation: { width: w, height: h } });
}

function cover(meta) {
  const out = [];
  out.push(new Paragraph({ spacing: { before: 600, after: 200 }, alignment: AlignmentType.CENTER, children: [img(path.join(ROOT, 'marca/logo_vertical.png'), 230, 230)] }));
  out.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 200, after: 120 }, children: [new TextRun({ text: 'REGISTRO DE CANDIDATURA — ELEIÇÕES PRESIDENCIAIS DAS IAs — BRASIL 2026', font: FONT, bold: true, size: 22, color: C.terracota })] }));
  out.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 }, border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: C.ocre, space: 6 } }, children: [new TextRun({ text: `VOLUME ${meta.vol}`, font: FONT, bold: true, size: 26, color: C.cinza })] }));
  out.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 300, after: 160 }, children: [new TextRun({ text: meta.title, font: FONT, bold: true, size: 44, color: C.petroleo })] }));
  if (meta.subtitle) out.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 500 }, children: [new TextRun({ text: meta.subtitle, font: FONT, italics: true, size: 24, color: C.grafite })] }));
  const info = [
    ['Candidata', 'Inês Aragão Tavares — “Inês Aragão”'],
    ['Vice', 'Rafael Kerber Antunes — “Rafael Kerber”'],
    ['Partido fictício', 'ALICERCE — Partido Republicano da Capacidade Nacional (sigla ALC)'],
    ['Slogan', 'Fazer o Brasil funcionar.'],
    ['Data-base', '20 de outubro de 2026 · Mandato hipotético 2027–2030'],
  ];
  info.forEach(([k, v]) => out.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 }, children: [new TextRun({ text: k + ': ', font: FONT, bold: true, size: 20, color: C.petroleo }), new TextRun({ text: v, font: FONT, size: 20, color: C.grafite })] })));
  out.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 700 }, children: [new TextRun({ text: 'Documento de simulação política fictícia. Personagens, partido, marca e trajetórias são inventados. Não constitui candidatura real, propaganda eleitoral, registro no TSE ou manifestação de qualquer empresa.', font: FONT, italics: true, size: 16, color: C.cinza })] }));
  out.push(new Paragraph({ children: [new PageBreak()] }));
  return out;
}

function parse(md) {
  const lines = md.split('\n');
  const meta = {};
  const body = [];
  let i = 0;
  while (i < lines.length && lines[i].startsWith('@')) {
    const m = lines[i].match(/^@(\w+)\s+(.*)$/); if (m) meta[m[1]] = m[2]; i++;
  }
  let pendingPct = null;
  while (i < lines.length) {
    let line = lines[i];
    if (line.trim() === '') { i++; continue; }
    if (line.startsWith('|=')) { pendingPct = line.replace(/[|=]/g, ' ').trim().split(/[ ,]+/).map(Number); i++; continue; }
    if (line.startsWith('|')) {
      const rows = [];
      while (i < lines.length && lines[i].startsWith('|')) {
        const l = lines[i].trim();
        if (!/^\|[\s\-:|]+\|$/.test(l)) rows.push(l.slice(1, -1).split('|').map(s => s.trim()));
        i++;
      }
      body.push(makeTable(rows, pendingPct)); pendingPct = null;
      body.push(new Paragraph({ spacing: { after: 120 }, children: [] }));
      continue;
    }
    if (line.trim() === '[[PB]]') { body.push(new Paragraph({ children: [new PageBreak()] })); i++; continue; }
    if (line.trim() === '[[TOC]]') {
      body.push(new Paragraph({ spacing: { after: 200 }, children: [new TextRun({ text: 'Sumário', font: FONT, bold: true, size: 32, color: C.petroleo })] }));
      lines.forEach(l => {
        if (l.startsWith('# ')) body.push(new Paragraph({ spacing: { before: 100, after: 40 }, children: runs(l.slice(2).replace(/\*\*/g, ''), { bold: true, color: C.petroleo, size: 21 }) }));
        else if (l.startsWith('## ')) body.push(new Paragraph({ spacing: { after: 20 }, indent: { left: 400 }, children: runs(l.slice(3).replace(/\*\*/g, ''), { size: 19, color: C.grafite }) }));
      });
      body.push(new Paragraph({ children: [new PageBreak()] })); i++; continue;
    }
    let m;
    if ((m = line.match(/^\[\[IMG (\S+) (\d+) (\d+)\]\]$/))) {
      body.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 120, after: 120 }, children: [img(path.join(ROOT, m[1]), +m[2], +m[3])] })); i++; continue;
    }
    if (line.startsWith('### ')) { body.push(new Paragraph({ heading: HeadingLevel.HEADING_3, children: runs(line.slice(4)) })); i++; continue; }
    if (line.startsWith('## ')) { body.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: runs(line.slice(3)) })); i++; continue; }
    if (line.startsWith('# ')) { body.push(new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: body.length > 0 && meta.break === 'yes', children: runs(line.slice(2)) })); i++; continue; }
    if ((m = line.match(/^(\s*)- (.*)$/))) {
      const lvl = m[1].length >= 2 ? 1 : 0;
      body.push(new Paragraph({ numbering: { reference: 'bul', level: lvl }, spacing: { after: 60 }, children: runs(m[2]) })); i++; continue;
    }
    if ((m = line.match(/^(\d+)\. (.*)$/))) {
      body.push(new Paragraph({ spacing: { after: 80 }, indent: { left: 400, hanging: 400 }, children: [new TextRun({ text: m[1] + '.\t', bold: true, font: FONT, color: C.petroleo }), ...runs(m[2])], tabStops: [{ type: 'left', position: 400 }] })); i++; continue;
    }
    if (line.startsWith('> ')) {
      body.push(new Paragraph({
        spacing: { before: 120, after: 160 }, indent: { left: 200, right: 200 },
        shading: { fill: C.areia, type: ShadingType.CLEAR, color: 'auto' },
        border: { left: { style: BorderStyle.SINGLE, size: 24, color: C.ocre, space: 8 } },
        children: runs(line.slice(2), { color: C.grafite })
      })); i++; continue;
    }
    body.push(new Paragraph({ spacing: { after: 140, line: 288 }, alignment: AlignmentType.JUSTIFIED, children: runs(line) }));
    i++;
  }
  return { meta, body };
}

function build(file, outDir) {
  const md = fs.readFileSync(file, 'utf8');
  const { meta, body } = parse(md);
  const doc = new Document({
    creator: 'Campanha fictícia ALICERCE',
    title: meta.title,
    description: 'Simulação fictícia — Eleições Presidenciais das IAs — Brasil 2026',
    features: { updateFields: true },
    styles: {
      default: { document: { run: { font: FONT, size: 21, color: C.grafite } } },
      paragraphStyles: [
        { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 34, bold: true, font: FONT, color: C.petroleo }, paragraph: { spacing: { before: 240, after: 200 }, outlineLevel: 0, border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: C.ocre, space: 4 } } } },
        { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 27, bold: true, font: FONT, color: C.petroleo }, paragraph: { spacing: { before: 280, after: 140 }, outlineLevel: 1, keepNext: true } },
        { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 23, bold: true, font: FONT, color: C.terracota }, paragraph: { spacing: { before: 200, after: 100 }, outlineLevel: 2, keepNext: true } },
      ]
    },
    numbering: { config: [{ reference: 'bul', levels: [
      { level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 500, hanging: 280 } } } },
      { level: 1, format: LevelFormat.BULLET, text: '–', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 1000, hanging: 280 } } } },
    ] }] },
    sections: [{
      properties: { page: { size: { width: PAGE_W, height: 16838 }, margin: { top: 1300, bottom: 1200, left: MARGIN, right: MARGIN, header: 600, footer: 600 } }, titlePage: true },
      headers: {
        default: new Header({ children: [new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: 'B8C6CB', space: 4 } }, children: [new TextRun({ text: 'ALICERCE · Inês Aragão — Plano 2027–2030', font: FONT, bold: true, size: 16, color: C.petroleo }), new TextRun({ text: `   |   Volume ${meta.vol}: ${meta.short || meta.title}`, font: FONT, size: 16, color: C.cinza })] })] }),
        first: new Header({ children: [new Paragraph({ children: [] })] })
      },
      footers: {
        default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: 'Simulação fictícia • Eleições Presidenciais das IAs • Brasil 2026   |   Página ', font: FONT, size: 16, color: C.cinza }), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 16, color: C.cinza }), new TextRun({ text: ' de ', font: FONT, size: 16, color: C.cinza }), new TextRun({ children: [PageNumber.TOTAL_PAGES], font: FONT, size: 16, color: C.cinza })] })] }),
        first: new Footer({ children: [new Paragraph({ children: [] })] })
      },
      children: [...cover(meta), ...body]
    }]
  });
  const outName = path.join(outDir, meta.file);
  return Packer.toBuffer(doc).then(buf => { fs.writeFileSync(outName, buf); console.log('OK', outName); });
}

const files = process.argv.slice(2);
(async () => { for (const f of files) await build(f, path.join(ROOT, 'docx')); })().catch(e => { console.error(e); process.exit(1); });
