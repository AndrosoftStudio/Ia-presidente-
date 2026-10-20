# -*- coding: utf-8 -*-
"""Marca canônica desenhada por geometria, não por geração de imagem."""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = "/workspace/candidatura/assets"
os.makedirs(OUT, exist_ok=True)

NAVY = (11, 31, 51, 255)
COPPER = (196, 98, 45, 255)
SAND = (243, 235, 221, 255)
PAPER = (247, 244, 239, 255)
WHITE = (255, 255, 255, 255)
INK = (20, 32, 43, 255)

FONT_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
FONT_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"


def symbol(size, navy=NAVY, copper=COPPER, bg=None):
    im = Image.new("RGBA", (size, size), bg if bg else (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    s = size
    # vertical plumb bar
    bw = int(s * 0.075)
    x0 = (s - bw) // 2
    y_top = int(s * 0.14)
    y_bot = int(s * 0.62)
    d.rectangle([x0, y_top, x0 + bw, y_bot], fill=navy)
    # sleepers crossing the bar
    def sleeper(y_center_ratio, length_ratio, thick_ratio=0.045):
        th = max(2, int(s * thick_ratio))
        ln = int(s * length_ratio)
        y = int(s * y_center_ratio) - th // 2
        x = (s - ln) // 2
        d.rectangle([x, y, x + ln, y + th], fill=navy)

    sleeper(0.46, 0.52)
    sleeper(0.56, 0.36)
    # redraw vertical so it stays continuous over sleepers
    d.rectangle([x0, y_top, x0 + bw, y_bot], fill=navy)
    # copper diamond (plumb bob) touching the bar
    dw = int(s * 0.22)
    dh = int(s * 0.22)
    cx = s // 2
    top = y_bot - 1
    d.polygon(
        [(cx, top), (cx + dw // 2, top + dh // 2), (cx, top + dh), (cx - dw // 2, top + dh // 2)],
        fill=copper,
    )
    return im


def save_symbol_variants():
    symbol(1024).save(os.path.join(OUT, "atr_simbolo.png"))
    # square icon with sand background and margin
    icon = Image.new("RGBA", (1024, 1024), PAPER)
    mark = symbol(780)
    icon.paste(mark, (122, 110), mark)
    icon.convert("RGB").save(os.path.join(OUT, "atr_icone_quadrado.png"), quality=95)
    # mono black
    mono = symbol(1024, navy=(0, 0, 0, 255), copper=(0, 0, 0, 255))
    mono.save(os.path.join(OUT, "atr_simbolo_mono.png"))
    # white on navy
    dark = Image.new("RGBA", (1024, 1024), NAVY)
    mark = symbol(780, navy=PAPER, copper=COPPER)
    dark.paste(mark, (122, 110), mark)
    dark.convert("RGB").save(os.path.join(OUT, "atr_icone_fundo_escuro.png"), quality=95)


def _font(path, size):
    return ImageFont.truetype(path, size)


def horizontal_lockup(bg, navy, copper, ink, path, mono=False):
    w, h = 2400, 900
    im = Image.new("RGB", (w, h), bg)
    mark = symbol(620, navy=navy + (255,) if len(navy) == 3 else navy,
                  copper=(copper + (255,) if len(copper) == 3 else copper))
    # paste
    im.paste(mark, (60, 140), mark)
    d = ImageDraw.Draw(im)
    d.text((760, 210), "ATR", font=_font(FONT_B, 220), fill=navy if not mono else ink)
    d.text((770, 460), "ALIANÇA DO TRABALHO E DA REGRA", font=_font(FONT_R, 48), fill=ink)
    # copper rule
    d.rectangle([770, 540, 2100, 548], fill=copper)
    d.text((770, 580), "O Brasil no trilho.", font=_font(FONT_I, 54), fill=ink)
    im.save(path, quality=95)


def vertical_lockup(path):
    w, h = 1400, 1800
    im = Image.new("RGB", (w, h), PAPER)
    mark = symbol(860)
    im.paste(mark, ((w - 860) // 2, 80), mark)
    d = ImageDraw.Draw(im)
    # center text using anchor
    d.text((w // 2, 1040), "ATR", font=_font(FONT_B, 200), fill=NAVY[:3], anchor="mm")
    d.text((w // 2, 1220), "ALIANÇA DO TRABALHO", font=_font(FONT_R, 48), fill=INK[:3], anchor="mm")
    d.text((w // 2, 1290), "E DA REGRA", font=_font(FONT_R, 48), fill=INK[:3], anchor="mm")
    d.rectangle([w // 2 - 220, 1360, w // 2 + 220, 1368], fill=COPPER[:3])
    d.text((w // 2, 1460), "O Brasil no trilho.", font=_font(FONT_I, 52), fill=INK[:3], anchor="mm")
    im.save(path, quality=95)


def mono_lockup():
    w, h = 2400, 900
    im = Image.new("RGB", (w, h), (255, 255, 255))
    mark = symbol(620, navy=(0, 0, 0, 255), copper=(0, 0, 0, 255))
    im.paste(mark, (60, 140), mark)
    d = ImageDraw.Draw(im)
    d.text((760, 210), "ATR", font=_font(FONT_B, 220), fill=(0, 0, 0))
    d.text((770, 460), "ALIANÇA DO TRABALHO E DA REGRA", font=_font(FONT_R, 48), fill=(0, 0, 0))
    d.rectangle([770, 540, 2100, 548], fill=(0, 0, 0))
    d.text((770, 580), "O Brasil no trilho.", font=_font(FONT_I, 54), fill=(0, 0, 0))
    im.save(os.path.join(OUT, "atr_logo_horizontal_mono.png"), quality=95)


def dark_lockup():
    w, h = 2400, 900
    im = Image.new("RGB", (w, h), NAVY[:3])
    mark = symbol(620, navy=(247, 244, 239, 255), copper=COPPER)
    im.paste(mark, (60, 140), mark)
    d = ImageDraw.Draw(im)
    d.text((760, 210), "ATR", font=_font(FONT_B, 220), fill=PAPER[:3])
    d.text((770, 460), "ALIANÇA DO TRABALHO E DA REGRA", font=_font(FONT_R, 46), fill=PAPER[:3])
    d.rectangle([770, 540, 2100, 548], fill=COPPER[:3])
    d.text((770, 580), "O Brasil no trilho.", font=_font(FONT_I, 54), fill=PAPER[:3])
    im.save(os.path.join(OUT, "atr_logo_horizontal_fundo_escuro.png"), quality=95)


def poster():
    portrait = Image.open(
        "/workspace/artifacts/imagine_images/f20ae181-cf0a-4302-95de-8e9f30ed7586.jpg"
    ).convert("RGB")
    W, H = 1600, 2000
    im = Image.new("RGB", (W, H), PAPER[:3])
    # photo area
    ph = 1280
    pw = int(portrait.width * ph / portrait.height)
    portrait = portrait.resize((pw, ph), Image.Resampling.LANCZOS)
    x = (W - pw) // 2
    im.paste(portrait, (x, 40))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 1340, W, H], fill=NAVY[:3])
    d.rectangle([0, 1340, W, 1356], fill=COPPER[:3])
    mark = symbol(220, navy=(247, 244, 239, 255), copper=COPPER)
    im.paste(mark, (70, 1420), mark)
    d = ImageDraw.Draw(im)
    d.text((320, 1460), "ELIAS VIANA", font=_font(FONT_B, 78), fill=PAPER[:3])
    d.text((320, 1560), "PRESIDENTE", font=_font(FONT_R, 36), fill=COPPER[:3])
    d.text((80, 1720), "O Brasil no trilho.", font=_font(FONT_I, 54), fill=PAPER[:3])
    d.text((80, 1820), "ATR  ·  ALIANÇA DO TRABALHO E DA REGRA", font=_font(FONT_R, 28), fill=PAPER[:3])
    d.text(
        (80, 1900),
        "PEÇA FICTÍCIA  ·  SIMULAÇÃO  ·  SEM REGISTRO NO TSE  ·  NÃO É CANDIDATURA REAL",
        font=_font(FONT_R, 18),
        fill=(224, 160, 120),
    )
    im.save(os.path.join(OUT, "cartaz_elias_viana_ficticio.jpg"), quality=92)


if __name__ == "__main__":
    save_symbol_variants()
    horizontal_lockup(
        PAPER[:3], NAVY[:3], COPPER[:3], INK[:3], os.path.join(OUT, "atr_logo_horizontal.png")
    )
    vertical_lockup(os.path.join(OUT, "atr_logo_vertical.png"))
    mono_lockup()
    dark_lockup()
    poster()
    print("assets ok", os.listdir(OUT))
