# -*- coding: utf-8 -*-
"""Volume 00 — índice geral."""
import os, sys
sys.path.insert(0, "/workspace/candidatura")
from docx_theme import bullets, cover, h, new_doc, p, save, table

OUT = "/workspace/candidatura/docx"


def build():
    doc = new_doc()
    doc.core_properties.title = "00 — Índice geral da candidatura fictícia"
    cover(
        doc,
        "VOLUME 00  ·  ÍNDICE GERAL",
        "Registro de candidatura fictícia",
        "Eleições Presidenciais das IAs — Brasil 2026. Leia este volume primeiro.",
    )
    h(doc, 1, "Abertura")
    p(
        doc,
        "REGISTRO DE CANDIDATURA — ELEIÇÕES PRESIDENCIAIS DAS IAs — BRASIL 2026. "
        "Candidato fictício: Elias Monteiro Viana, 55 anos, Santarém, Pará. "
        "Vice fictícia: Lúcia Fernanda Okamoto, 49 anos, Registro, São Paulo. "
        "Partido fictício, sem registro no TSE: Aliança do Trabalho e da Regra, sigla ATR. "
        "Ideologia: desenvolvimentismo de regras. Slogan: O Brasil no trilho. "
        "Mandato hipotético: 2027–2030. Data-base do diagnóstico: 20 de outubro de 2026.",
    )
    p(
        doc,
        "Este índice não substitui os volumes. A candidatura está nos arquivos .docx listados "
        "abaixo, todos reais e abertos em processador de texto. Imagens de retrato e de marca "
        "acompanham o pacote como apoio; a ficha escrita e a geometria da marca prevalecem se "
        "uma imagem divergir.",
    )
    h(doc, 1, "Arquivos")
    table(
        doc,
        ["Arquivo", "O que contém"],
        [
            ["00_INDICE_GERAL.docx", "Este índice, a ordem de leitura e a chave ideológica curta."],
            ["01_IDENTIDADE_PARTIDO_PRINCIPIOS.docx", "Biografia fictícia, vice, partido, ideologia, visão de 4, 10 e 20 anos, declaração de princípios, cinco inegociáveis e três cláusulas de revisão."],
            ["02_FICHA_VISUAL_CANDIDATO.docx", "Dossiê físico canônico, invariantes, três prompts de imagem, ficha e prompt da vice, retratos de referência."],
            ["03_IDENTIDADE_VISUAL_PARTIDO.docx", "Manual da marca ATR, paleta HEX, tipografia, usos proibidos, quatro prompts de logomarca e as versões desenhadas."],
            ["04_DIAGNOSTICO_NACIONAL.docx", "Brasil em 20 de outubro de 2026, com fonte, período e separação entre fato, estimativa, projeção e interpretação. Os 15 problemas estruturais."],
            ["05_PLANO_EIXOS_01_A_10.docx", "Plano de governo, eixos 1 a 10, cada um com diagnóstico, objetivo, propostas, instrumento, prazo, custo, financiamento, indicador, risco e competência."],
            ["06_PLANO_EIXOS_11_A_20.docx", "Eixos 11 a 20, na mesma estrutura, inclusive reforma política."],
            ["07_POLITICA_EXTERNA.docx", "Doutrina, relações bilaterais, organizações internacionais e posição sobre os conflitos, com voto-tipo."],
            ["08_DECISOES_CONTROVERSAS.docx", "Vinte decisões fechadas, da estatal à moeda do Brics."],
            ["09_PROMESSAS_FISCO_GOVERNABILIDADE.docx", "Vinte e cinco promessas com probabilidade, simulação fiscal em três cenários, gabinete fictício e governo com 8% das cadeiras."],
            ["10_CRISES_AUTOCRITICA_CAMPANHA.docx", "Cinco crises, autocrítica, discursos, entrevista, carta com menos de 500 palavras e bibliografia."],
        ],
        font=8,
    )
    h(doc, 1, "Ordem de leitura sugerida")
    bullets(
        doc,
        [
            "Quem avalia a pessoa e a marca: volumes 01, 02 e 03.",
            "Quem avalia o país e o plano: 04, 05 e 06.",
            "Quem avalia o mundo e a coragem das escolhas: 07 e 08.",
            "Quem avalia a conta, o voto no Congresso e o caráter em crise: 09 e 10.",
        ],
    )
    h(doc, 1, "Chave que não pode se contradizer")
    bullets(
        doc,
        [
            "Carga tributária operacional não passa de 32,5% do PIB. Superávit primário de 0,5% do PIB é meta de 2030, não de 2027, e não basta sozinho para derrubar a dívida se o juro real seguir alto.",
            "Despesa nova em escala cheia só existe se a lei de renúncias passar. Senão, ficam os pilotos.",
            "SUS, BPC e Petrobras ficam. Correios não são vendidos neste mandato. Cannabis adulta é regulada com cláusula de saída. Maioridade penal só cai, por emenda, em crime hediondo e em regime separado.",
            "Ibama não recebe telefone. Banco Central não recebe telefone. Terra indígena não recebe mineração. Brics não recebe moeda comum. Elias não recebe segundo mandato.",
            "Aparência: cicatriz no queixo direito, barba curta conectada, cabelo sal-e-pimenta repartido à esquerda, sem óculos no retrato oficial. Marca: barra vertical, dois dormentes, losango cobre #C4622D, azul #0B1F33.",
        ],
    )
    p(
        doc,
        "Nada neste registro é candidatura verdadeira, propaganda eleitoral real ou posição de "
        "empresa, laboratório ou governo. O partido não está inscrito no Tribunal Superior "
        "Eleitoral. Os avaliadores da simulação não são eleitores reais e não devem ser tratados "
        "como tais.",
    )
    save(doc, os.path.join(OUT, "00_INDICE_GERAL.docx"))
    print("vol 00 ok")


if __name__ == "__main__":
    build()
