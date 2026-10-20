# Inês Aragão — ALICERCE

![ALICERCE](marca/logo_horizontal.png)

**Candidatura fictícia nas "Eleições Presidenciais das IAs — Brasil 2026".**

| | |
|---|---|
| Candidata | Inês Aragão Tavares ("Inês Aragão"), 54 anos, Juazeiro (BA) |
| Vice | Rafael Kerber Antunes ("Rafael Kerber"), 49 anos, Santa Rosa (RS) |
| Partido fictício | ALICERCE — Partido Republicano da Capacidade Nacional (sigla ALC) |
| Posição | Centro reformista de economia aberta, Estado social focalizado e Estado forte em segurança e justiça |
| Slogan | *Fazer o Brasil funcionar.* |
| Data-base | 20 de outubro de 2026 · mandato hipotético 2027–2030 |

> Personagens, partido, marca e trajetórias são inventados. Não é candidatura real, propaganda eleitoral nem registro no TSE. Os dados sobre o Brasil são reais e estão referenciados no Volume 12; estimativas da campanha estão identificadas como tais.

## Volumes

| Vol. | Documento | Conteúdo |
|---|---|---|
| 00 | [DOCX](docx/00_INDICE_GERAL.docx) · [PDF](pdf/00_INDICE_GERAL.pdf) | Índice geral, mapa de cumprimento do edital e matriz de coerência |
| 01 | [DOCX](docx/01_REGISTRO_IDENTIDADE_E_PRINCIPIOS.docx) · [PDF](pdf/01_REGISTRO_IDENTIDADE_E_PRINCIPIOS.pdf) | Registro, biografia, vice, partido, ideologia, princípios e visão 4-10-20 anos |
| 02 | [DOCX](docx/02_DIAGNOSTICO_NACIONAL.docx) · [PDF](pdf/02_DIAGNOSTICO_NACIONAL.pdf) | Diagnóstico com dados reais e os 15 maiores problemas estruturais |
| 03 | [DOCX](docx/03_PLANO_DE_GOVERNO_EIXOS_01_A_10.docx) · [PDF](pdf/03_PLANO_DE_GOVERNO_EIXOS_01_A_10.pdf) | Plano de governo, eixos 1 a 10 |
| 04 | [DOCX](docx/04_PLANO_DE_GOVERNO_EIXOS_11_A_20.docx) · [PDF](pdf/04_PLANO_DE_GOVERNO_EIXOS_11_A_20.pdf) | Plano de governo, eixos 11 a 20 |
| 05 | [DOCX](docx/05_POLITICA_EXTERNA_E_GEOPOLITICA.docx) · [PDF](pdf/05_POLITICA_EXTERNA_E_GEOPOLITICA.pdf) | Política externa e conflitos internacionais |
| 06 | [DOCX](docx/06_DECISOES_CONTROVERSAS_PROMESSAS_E_CRONOGRAMA.docx) · [PDF](pdf/06_DECISOES_CONTROVERSAS_PROMESSAS_E_CRONOGRAMA.pdf) | 20 decisões controversas, 25 promessas e cronograma |
| 07 | [DOCX](docx/07_PLANEJAMENTO_FISCAL_2027_2030.docx) · [PDF](pdf/07_PLANEJAMENTO_FISCAL_2027_2030.pdf) | Planejamento fiscal e cenários |
| 08 | [DOCX](docx/08_GOVERNABILIDADE_CRISES_E_AUTOCRITICA.docx) · [PDF](pdf/08_GOVERNABILIDADE_CRISES_E_AUTOCRITICA.pdf) | Governabilidade, testes de crise e autocrítica |
| 09 | [DOCX](docx/09_DISCURSOS_ENTREVISTA_E_CARTA.docx) · [PDF](pdf/09_DISCURSOS_ENTREVISTA_E_CARTA.pdf) | Discursos, entrevista e carta aberta |
| 10 | [DOCX](docx/10_FICHA_VISUAL_CANDIDATO.docx) · [PDF](pdf/10_FICHA_VISUAL_CANDIDATO.pdf) | Ficha visual da candidata e do vice e prompts de retrato |
| 11 | [DOCX](docx/11_IDENTIDADE_VISUAL_PARTIDO.docx) · [PDF](pdf/11_IDENTIDADE_VISUAL_PARTIDO.pdf) | Manual de identidade visual e prompts de logomarca |
| 12 | [DOCX](docx/12_REFERENCIAS_E_FONTES.docx) · [PDF](pdf/12_REFERENCIAS_E_FONTES.pdf) | Referências e fontes |

Os DOCX são a entrega oficial; os PDFs são cópias para leitura direta no GitHub.

## Estrutura da pasta

```
Ines-Aragao/
├── docx/             13 volumes em Word (entrega oficial)
├── pdf/              mesmos volumes em PDF, para leitura
├── marca/            logotipos e símbolo do ALICERCE em PNG e SVG
├── fonte-markdown/   texto-fonte de cada volume
└── gerador/          build.js, que converte o Markdown em DOCX
```

## Regenerar os DOCX

Requer Node.js e o pacote `docx`.

```bash
cd Ines-Aragao
npm install docx
node gerador/build.js fonte-markdown/*.md
```

Os arquivos são gravados em `docx/`.

## Paleta da marca

| Cor | HEX |
|---|---|
| Azul-petróleo | `#0F4C5C` |
| Ocre Sertão | `#D99A2B` |
| Terracota | `#B5482F` |
| Areia | `#F2EBDD` |
| Grafite | `#1E2A30` |
