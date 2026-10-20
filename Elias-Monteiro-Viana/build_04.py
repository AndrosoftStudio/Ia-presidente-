# -*- coding: utf-8 -*-
"""Volume 04 — diagnóstico nacional com fontes e classificação epistemológica."""
import os, sys
sys.path.insert(0, "/workspace/candidatura")
from docx_theme import bullets, callout, cover, h, new_doc, p, save, table

OUT = "/workspace/candidatura/docx"


def build():
    doc = new_doc()
    doc.core_properties.title = "04 — Diagnóstico do Brasil — 20 de outubro de 2026"
    cover(
        doc,
        "VOLUME 04",
        "Diagnóstico nacional na data-base",
        "Fatos, estimativas, projeções e interpretações separados de propósito. Onde a fonte é de segunda mão, o texto diz.",
    )

    h(doc, 1, "1. Método")
    p(
        doc,
        "A data-base é 20 de outubro de 2026. O diagnóstico usa o que estava publicado até essa "
        "véspera e, no caso do Focus, leituras de mercado circuladas entre 13 e 19 de outubro. "
        "Não há número inventado para preencher lacuna. Quando duas fontes civis divergem em "
        "décimo — o superávit comercial de 2025 aparece como US$ 68,1 bilhões numa matéria e "
        "US$ 68,3 bilhões noutra, ambas atribuídas ao MDIC —, o texto registra a divergência "
        "em vez de escolher a casa decimal que convém ao argumento.",
    )
    p(doc, "Classificação usada em todo o volume:")
    bullets(
        doc,
        [
            "Fato confirmado: número publicado por órgão estatístico ou reproduzido de modo consistente a partir de release oficial, com período e fonte.",
            "Estimativa: cálculo de órgão público ainda sujeito a revisão, ou mediana de mercado sobre variável ainda não fechada.",
            "Projeção: cenário para período futuro. Projeção não é promessa do candidato e não é fato.",
            "Interpretação política: juízo do programa sobre o que o número significa. Pode ser contestada sem que o número caia.",
            "Hipótese da simulação: premissa do experimento, como os 8% de cadeiras, ou inferência não medida.",
        ],
    )
    callout(
        doc,
        "Limitação explícita: este volume não reprocessou microdados. Não consultou, linha a linha, "
        "o demonstrativo de gastos tributários de 2026, a execução orçamentária completa de outubro "
        "nem o texto integral do 20º Anuário de Segurança Pública — usou releases, notas oficiais "
        "e a imprensa que os reproduz com número. Onde isso importa, a frase o diz. PISA 2022 segue "
        "como a última avaliação internacional publicada consultada; não se localizou, até a data-base, "
        "resultado de um PISA posterior.",
    )

    h(doc, 1, "2. Economia")
    h(doc, 2, "Produto, investimento e setor")
    p(
        doc,
        "Fato confirmado. O IBGE divulgou, em 3 de março de 2026, que o PIB de 2025 cresceu 2,3% "
        "e somou R$ 12,7 trilhões. O PIB per capita chegou a R$ 59.687,49, alta real de 1,9%. "
        "A agropecuária cresceu 11,7%, os serviços 1,8% e a indústria 1,4%. A taxa de investimento "
        "foi de 16,8% do PIB, ante 16,9% em 2024. A poupança foi de 14,4%, ante 14,1%. No quarto "
        "trimestre de 2025, a variação dessazonalizada frente ao terceiro foi de apenas 0,1%, "
        "sinal de desaceleração já no fechamento do ano. Fonte: IBGE, Contas Nacionais Trimestrais, "
        "release de 3 de março de 2026.",
    )
    p(
        doc,
        "Fato de segunda mão, tratado com essa ressalva. Sínteses de imprensa sobre a série do "
        "IBGE situam o crescimento de 2024 em 3,4% e o de 2023 em torno de 3,2%. O número fechado "
        "que este diagnóstico segura com release lido é o de 2025. A interpretação não depende do "
        "décimo de 2023: o biênio anterior foi mais forte do que 2025, e 2026 desacelerou de novo.",
    )
    p(
        doc,
        "Fato e estimativa de 2026. O Ipea, na Carta de Conjuntura de outubro de 2026, registrou "
        "crescimento de 0,5% no segundo trimestre frente ao primeiro, depois de 1,1% no primeiro "
        "frente ao quarto de 2025, e revisou a projeção de 2026 de 2,3% para 2,0%, com inflação "
        "de IPCA revista de 5,3% para 5,0% no ano. O FMI, no World Economic Outlook circulado em "
        "12 e 13 de outubro de 2026, projetou 2,2% para o PIB brasileiro em 2026 e inflação de "
        "4,4% no fim de 2026 e 4,1% em 2027. O Focus, na leitura de 13 de outubro, mantinha o PIB "
        "de 2026 em 1,85% e o de 2027 em 1,40%; relato de 19 de outubro apontou 1,83% e, para 2027, "
        "1,32%. Projeções discordam entre si. Nenhuma é fato. Interpretação: o intervalo honesto "
        "para 2026, na data-base, é crescimento real perto de 2%, não uma expansão folgada.",
    )

    h(doc, 2, "Inflação, juros e câmbio")
    p(
        doc,
        "Fato: a meta de inflação é 3%, com banda de 1,5 ponto, teto de 4,5%. Fato: a meta da Selic "
        "está em 13,75% ao ano desde a decisão do Copom de 16 de setembro de 2026, depois de um "
        "ciclo de cortes de 0,25 ponto a partir de um patamar que a imprensa situou em 15% no pico "
        "recente e em 14% na reunião anterior à de setembro. A próxima reunião estava marcada para "
        "4 de novembro de 2026. Estimativa de mercado (Focus, meados de outubro): Selic de 13,25% "
        "no fim de 2026, 12% no fim de 2027 e 10,50% no fim de 2028. IPCA de 2025: 4,26%, segundo "
        "síntese de imprensa do índice oficial — dentro da banda daquele ano, e o menor fechamento "
        "anual citado nessa síntese desde 2018. Projeção Focus para o IPCA de 2026: 5,22%, acima "
        "do teto de 4,5%, estável na semana de 19 de outubro depois de alta nas semanas anteriores. "
        "Para 2027, a mediana estava em torno de 4,30% a 4,32%. Dólar de fim de 2026: mediana "
        "entre R$ 5,13 e R$ 5,15 conforme a semana do Focus. Interpretação do programa: o Banco "
        "Central autônomo está certo em não comemorar desinflação que a expectativa ainda não "
        "entregou. Um governo que pressione a Selic no primeiro mês de 2027 estará escolhendo "
        "inflação, não crescimento.",
    )

    h(doc, 2, "Fisco, dívida e carga")
    p(
        doc,
        "Fato de execução, via Ipea em preços de setembro de 2026: de janeiro a setembro, o déficit "
        "primário do governo central caiu de R$ 103,2 bilhões no mesmo período de 2025 para R$ 89,0 "
        "bilhões. Em setembro, a receita líquida foi de R$ 205,8 bilhões e a despesa total de "
        "R$ 200,4 bilhões. A dívida pública federal mobiliária e contratual estava em cerca de "
        "R$ 9,3 trilhões em agosto de 2026, 96% interna, prazo médio perto de quatro anos, com "
        "predomínio de títulos pós-fixados. Estimativa de imprensa atribuída ao Banco Central: "
        "dívida bruta do governo geral em 82,9% do PIB em agosto de 2026, cerca de R$ 11,1 trilhões, "
        "vinda de 73,5% em dezembro de 2022. Projeção Prisma Fiscal de 15 de outubro de 2026, "
        "Secretaria de Política Econômica: déficit primário do governo central de R$ 53,0 bilhões "
        "em 2026 e R$ 44 bilhões em 2027; dívida bruta de 83,4% do PIB no fim de 2026 e 87% no fim "
        "de 2027. A meta oficial citada na mesma cobertura é superávit de 0,25% do PIB em 2026 "
        "(R$ 34,3 bilhões) e de 0,50% em 2027 (R$ 73,2 bilhões), com banda de tolerância de 0,25 "
        "ponto e despesas fora do cômputo da meta. O Focus de meados de outubro via resultado "
        "primário de 2026 ainda deficitário, em torno de 0,4% do PIB, e resultado nominal perto "
        "de −8,9% do PIB — o buraco dos juros, não só o primário.",
    )
    p(
        doc,
        "Fato: a carga tributária bruta do governo geral foi de 32,40% do PIB em 2025, mais 0,18 "
        "ponto sobre 2024, segundo o Tesouro Nacional em boletim de abril de 2026. Impostos sobre "
        "bens e serviços seguem como o maior bloco, cerca de 13,8% do PIB. Fato institucional: a "
        "reforma do consumo da Emenda Constitucional 132 está em implantação. Em outubro de 2026, "
        "empresas escolhiam regime de IBS e CBS para 2027, e testes de documentos fiscais haviam "
        "sido adiados para até 26 de outubro, com entrada em produção ainda anunciada para 16 de "
        "novembro de 2026. Interpretação: a carga já é alta para um país de produtividade média. "
        "Subi-la de novo para fechar conta é a saída preguiçosa. Desfazê-la no meio da transição "
        "do IVA dual é a saída caótica. O programa não fará nenhuma das duas.",
    )
    p(
        doc,
        "Fato de despesa, COFOG, Ministério da Fazenda, dezembro de 2025, ano de referência 2024: "
        "despesa do governo geral de R$ 5.377,5 bilhões, 45,79% do PIB. Saúde passou a 5,03% do PIB, "
        "educação a 5,10%, habitação e serviços comunitários a 1,36%. Proteção social ainda era a "
        "maior função, 16,53% do PIB. Em 2023, ordem pública e segurança estavam em 2,85% do PIB, "
        "acima da média internacional citada no mesmo relatório. Interpretação: o Brasil não é um "
        "Estado mínimo que precise «chegar» ao gasto social. É um Estado caro, cuja composição "
        "protege renda de benefícios e paga juro, e investe pouco para o tamanho da necessidade.",
    )

    h(doc, 2, "Trabalho, setor externo e crédito de investimento")
    p(
        doc,
        "Fato: a PNAD Contínua, no trimestre encerrado em agosto de 2026, registrou desocupação de "
        "5,3%, a menor para aquele período desde 2012, segundo a Agência Brasil ao noticiar o IBGE "
        "em 13 de outubro de 2026. No trimestre de novembro de 2025 a janeiro de 2026, a informalidade "
        "foi de 37,5%, 38,5 milhões de pessoas, o menor patamar desde o trimestre encerrado em julho "
        "de 2020; o rendimento real habitual de todos os trabalhos chegou a R$ 3.652. Empregados "
        "privados com carteira, excluído o doméstico, estavam em 39,4 milhões naquele corte. "
        "Interpretação: o mercado de trabalho está aquecido no indicador de desemprego e ainda é "
        "estruturalmente informal. Comemorar 5,3% sem olhar os 37,5% é meia política.",
    )
    p(
        doc,
        "Fato de comércio, MDIC, reproduzido em 6 de outubro de 2026: superávit de US$ 7,741 bilhões "
        "em setembro; no acumulado de janeiro a setembro, US$ 62,396 bilhões, exportações de "
        "US$ 284,654 bilhões e importações de US$ 222,259 bilhões. A projeção oficial de superávit "
        "para 2026 foi reduzida de US$ 90 bilhões para US$ 84,4 bilhões, com exportações projetadas "
        "em US$ 364,2 bilhões. Para 2025, o fechamento divulgado em janeiro de 2026 foi da ordem de "
        "US$ 68 bilhões (US$ 68,3 bilhões numa nota, com exportações de US$ 348,6 bilhões e "
        "importações de US$ 280,3 bilhões; US$ 68,1 bilhões na referência posterior do próprio "
        "governo ao revisar 2026). Exportações aos Estados Unidos caíram 6,6% em 2025, no contexto "
        "de tarifas do governo Trump; vendas à Argentina subiram 31,4%, à China 6% e à União "
        "Europeia 3,2%, segundo essa cobertura de janeiro. Estimativa de imprensa para investimento "
        "estrangeiro direto: US$ 89,3 bilhões nos doze meses até junho de 2026, 3,58% do PIB. "
        "Interpretação: o setor externo segura o país, e segura com commodity e com parceiro "
        "concentrado. Isso é força e é vulnerabilidade ao mesmo tempo.",
    )

    table(
        doc,
        ["Indicador", "Valor", "Período", "Tipo", "Fonte"],
        [
            ["PIB", "+2,3%; R$ 12,7 tri", "2025", "Fato", "IBGE, 03/03/2026"],
            ["PIB per capita", "R$ 59.687", "2025", "Fato", "IBGE"],
            ["Investimento", "16,8% do PIB", "2025", "Fato", "IBGE"],
            ["PIB 2026", "1,8% a 2,2%", "projeção 2026", "Projeção", "Focus, Ipea, FMI, out/2026"],
            ["Selic meta", "13,75% a.a.", "desde 16/09/2026", "Fato", "Copom"],
            ["IPCA 2026", "5,22% (Focus); 5,0% (Ipea)", "projeção", "Projeção", "Focus 19/10; Ipea out/2026"],
            ["Meta de inflação", "3% ± 1,5 p.p.", "vigente", "Fato", "CMN"],
            ["Dívida bruta", "82,9% do PIB; projeção 83,4% no fim de 2026", "ago/2026 e Prisma", "Estimativa", "BC via imprensa; SPE 15/10/2026"],
            ["Déficit primário central jan–set", "R$ 89,0 bi", "2026 até setembro", "Fato", "Ipea, preços de set/2026"],
            ["Carga tributária", "32,40% do PIB", "2025", "Fato", "Tesouro, abr/2026"],
            ["Desocupação", "5,3%", "trimestre até ago/2026", "Fato", "IBGE/PNAD via Agência Brasil"],
            ["Informalidade", "37,5%; 38,5 milhões", "nov/2025–jan/2026", "Fato", "IBGE/PNAD"],
            ["Superávit comercial jan–set", "US$ 62,4 bi", "2026", "Fato", "MDIC"],
        ],
        font=8,
    )

    h(doc, 1, "3. Sociedade")
    p(
        doc,
        "Fato, Síntese de Indicadores Sociais do IBGE, divulgação de 3 de dezembro de 2025, ano de "
        "referência 2024, linhas do Banco Mundial de US$ 6,85 e US$ 2,15 PPC de 2017: a pobreza "
        "caiu de 27,3% para 23,1%, 8,6 milhões de pessoas a menos; a extrema pobreza caiu de 4,4% "
        "para 3,5%, 1,9 milhão a menos. São os menores percentuais da série desde 2012. Sem "
        "programas sociais, a extrema pobreza teria sido 10% e a pobreza 28,7%. O Gini do rendimento "
        "domiciliar per capita foi a 0,504 em 2024, ante 0,517 em 2023; sem benefícios, seria 0,542. "
        "Pessoas brancas recebiam, em 2024, 65,9% a mais do que pretas ou pardas no rendimento médio "
        "de todos os trabalhos. Extrema pobreza: 2,2% entre brancos, 3,9% entre pretos e 4,5% entre pardos.",
    )
    p(
        doc,
        "Fato mais recente e menos confortável. Em 2025, o rendimento médio de todas as fontes "
        "chegou a R$ 3.367, alta de 5,4%, recorde da série da PNAD. O rendimento domiciliar per "
        "capita médio foi a R$ 2.264, alta de 6,9%. Os 10% mais ricos chegaram a R$ 9.117 per capita "
        "(+8,7%) e os 10% mais pobres a R$ 268 (+3,1%). O Gini do rendimento domiciliar per capita "
        "subiu de 0,504 para 0,511, segunda menor marca da série, mas alta. Os 10% mais ricos "
        "recebiam 13,8 vezes o rendimento per capita dos 40% mais pobres (R$ 663). Fonte: IBGE, "
        "rendimentos de 2025, divulgação de maio de 2026, reproduzida pela Folha e pelo UOL. "
        "Há também um Gini de 0,491 citado para rendimento individual de todas as fontes, vindo de "
        "0,487 — outro conceito, não contradição a esconder. Interpretação: a rede social segurou "
        "a base; o topo voltou a capturar mais o crescimento de 2025. Política que só transfere "
        "e política que só celebra o mercado falham as duas, cada uma pela metade que ignora.",
    )
    p(
        doc,
        "Demografia. Fato, IBGE, divulgação de abril de 2026: a população chegou a 212,7 milhões "
        "em 2025, alta de 0,4% sobre 2024. O número de pessoas com menos de 30 anos caiu 10,4% "
        "desde 2012. Interpretação: o bônus demográfico não é mais desculpa para adiar previdência "
        "e aprendizagem. O país envelhece com escola ainda fraca e com informalidade ainda alta. "
        "Essa combinação é o problema previdenciário real, maior do que qualquer discurso sobre "
        "privilégio isolado.",
    )
    p(
        doc,
        "Moradia. Fato, Fundação João Pinheiro, números de 2024 divulgados em 2026: déficit "
        "habitacional de 5.773.983 domicílios, 7,4% dos particulares ocupados, queda de 3,4% frente "
        "ao ano anterior, menor marca da série da FJP desde 2016. Sudeste: 2,35 milhões; Nordeste: "
        "1,46 milhão; Sul: 743 mil; Norte: 674 mil; Centro-Oeste: 537 mil. São Paulo sozinho: "
        "1.252.830. Domicílios chefiados por mulheres: 60,9% do déficit. Até um salário mínimo: "
        "40,7%; de um a dois mínimos: 33,8%. Inadequação: 27,6 milhões de domicílios urbanos, em "
        "alta. Fato de saneamento, IBGE, domicílios em 2025: 86,1% ligados à rede geral de água "
        "(60,9% no Norte; 31,7% no rural); esgoto por rede coletora em 71,4% dos domicílios "
        "permanentes, vindo de 68,1% em 2019; no rural, só 8,9% têm rede coletora. Outra leitura "
        "da PNAD 2024, reproduzida em outubro de 2026, apontava 70,4% com rede ou fossa ligada e "
        "29,5% sem esse acesso, com o Norte em situação crítica. Os conceitos não são idênticos; "
        "os dois dizem a mesma coisa política: universalização até 2033, meta do marco legal, não "
        "está garantida pelo ritmo, e o Norte não pode ser média nacional disfarçada.",
    )

    h(doc, 1, "4. Serviços públicos")
    p(
        doc,
        "Saúde. Fato fiscal: em 2025 a União executou R$ 234,5 bilhões em ações e serviços públicos "
        "de saúde, 103% do mínimo constitucional, ante R$ 215,9 bilhões em 2024 (Tesouro, RREO, "
        "janeiro de 2026). Fato de oferta, segundo o ministro da Saúde em entrevista de 16 de "
        "outubro de 2026 — portanto fala de governo, não auditoria independente: quase 15 milhões "
        "de cirurgias eletivas no SUS em 2025, 42% acima de 2022, com projeção verbal de 16 milhões "
        "em 2026; painel nacional de filas prometido para o fim de 2026 e ainda não tratado aqui "
        "como dado publicado. A mesma entrevista reconhece que a tabela do SUS vigente há quase "
        "30 anos segue sendo o problema de preço. Interpretação: há mais cirurgia do que em 2022 "
        "e não há, até a data-base, uma fila nacional auditável que permita a um candidato honesto "
        "prometer «reduzir a espera em X%» sem linha de base. O primeiro ato de saúde deste programa "
        "é cravar a linha de base, não o milagre.",
    )
    p(
        doc,
        "Educação. Fato, Ideb 2025, divulgação de agosto de 2026: anos iniciais do fundamental "
        "foram de 6,0 em 2023 para 6,3, acima da meta 6,0. Anos finais foram de 5,0 para 5,3, "
        "abaixo da meta 5,5. Nas escolas públicas, anos iniciais 6,1, anos finais 5,0, ensino médio "
        "4,3 (era 4,1). A série, iniciada em 2005, está no ponto mais alto, e o ensino médio público "
        "em 4,3 não é vitória — é a etapa que ainda não formou o jovem. Fato internacional, PISA "
        "2022, MEC, dezembro de 2023, última onda consultada: matemática 379, leitura 410, ciências "
        "403, estáveis desde 2009 em termos práticos. Em matemática, 73% dos estudantes brasileiros "
        "ficaram abaixo do nível 2, contra 31% na OCDE; 1% chegou ao nível 5 ou mais. Gasto: a "
        "União aplicou R$ 129,9 bilhões em manutenção e desenvolvimento do ensino em 2025, 106,4% "
        "do mínimo. Interpretação: o Brasil não sofre de escassez absoluta de dinheiro educacional "
        "no agregado constitucional. Sofre de aprendizagem que não acompanha o gasto, sobretudo "
        "depois do 5º ano.",
    )
    p(
        doc,
        "Previdência. Fato, Tesouro, resultado de 2025: déficit da seguridade de R$ 392,1 bilhões "
        "(receitas de R$ 1,449 trilhão, despesas de R$ 1,841 trilhão). O Regime Geral teve déficit "
        "de R$ 320,9 bilhões, 5,7% acima de 2024. O regime próprio dos servidores federais, "
        "R$ 62,6 bilhões, 12,1% acima. Interpretação: outra reforma ampla no primeiro ano de mandato "
        "seria teatro, porque a de 2019 ainda amadurece e o Congresso de 8% não a entrega. Fraude, "
        "prova de vida rural e contribuição de futuros militares são o terreno possível. Fingir que "
        "o déficit de R$ 321 bilhões se resolve com caça a um privilégio anedótico é desonestidade.",
    )
    p(
        doc,
        "Segurança. Fato, 20º Anuário Brasileiro de Segurança Pública, Fórum Brasileiro de Segurança "
        "Pública, divulgação de 23 de julho de 2026, ano de 2025: 40.775 mortes violentas "
        "intencionais, taxa de 19,1 por 100 mil, queda de 8,2% sobre 2024 e menor taxa desde 2012. "
        "Homicídios dolosos: 32.914, taxa de 15,4 por 100 mil, queda próxima de 10%, meta nacional "
        "de 16 por 100 mil atingida antes de 2027. Latrocínio e lesão seguida de morte também caíram. "
        "Mortes por intervenção policial: 6.602 numa das aberturas de imprensa, alta de cerca de 6%, "
        "e já perto de 16% das mortes violentas do ano. Feminicídios: 1.571, alta de 4% sobre 1.504 "
        "em 2024, recorde da série desde a tipificação em 2015, taxa de 1,4 por 100 mil mulheres, "
        "cerca de quatro por dia; 44,4% das mulheres assassinadas morreram por razão de gênero. "
        "Sete estados subiram no homicídio, entre eles Rio de Janeiro e Rio Grande do Norte. Norte "
        "e Nordeste seguem com as piores taxas de mortes violentas — a literatura do próprio Fórum "
        "citou 25,3 e 31,6 por 100 mil nessas regiões. Interpretação: a queda nacional é real e não "
        "autoriza discurso de colapso único, nem discurso de missão cumprida. O pobre, o jovem negro "
        "e a mulher não moram na média.",
    )

    h(doc, 1, "5. Instituições")
    p(
        doc,
        "Fato institucional, não estatística: a República segue presidencialista, com Supremo "
        "atuante, Congresso fragmentado e federalismo em que a polícia, a escola fundamental e o "
        "posto de saúde são, em regra, de estado e de município. Em outubro de 2026 o país estava "
        "em calendário eleitoral real, alheio a esta simulação; o diagnóstico não entra nessa "
        "disputa e não atribui voto. Interpretação do programa, e só interpretação: o desenho "
        "de coalizão torna emenda parlamentar e ocupação de cargo os preços visíveis da governabilidade. "
        "Isso não será abolido por estilo pessoal. Pode ser limitado por transparência, por teto "
        "real de crescimento da emenda obrigatória e por recusa pública de orçamento secreto. "
        "Corrupção não tem, neste volume, um índice único apresentado como verdade oficial de 2026; "
        "o programa trata o risco como estrutural — licitação, estatais, emenda e influência — e "
        "não como propriedade de um campo.",
    )
    p(
        doc,
        "Sistema tributário: a transição para IBS e CBS é o fato dominante. Reabri-la por ideologia "
        "em 2027 custaria mais certeza do que qualquer alíquota marginal renderia. O problema que "
        "permanece é a regressividade do consumo, a folha que pune o emprego formal e o estoque de "
        "renúncias que ninguém revisa inteiro porque cada uma tem dono no Congresso.",
    )

    h(doc, 1, "6. Posição internacional na data-base")
    p(
        doc,
        "Fatos de contexto, não doutrina. Os Estados Unidos, sob Donald Trump, aplicaram tarifas "
        "que reduziram a exportação brasileira àquele mercado em 2025 e, em outubro de 2026, "
        "conduziam negociação sobre a guerra na Ucrânia, inclusive um acordo envolvendo diesel "
        "russo criticado por Kiev. A China segue como principal destino comercial, com compras em "
        "alta em 2025. A União Europeia permanece parceira e contraparte difícil em cláusulas "
        "ambientais. A guerra da Rússia contra a Ucrânia não terminou: em 8 e 9 de outubro de 2026 "
        "o Kremlin dizia concordar com o secretário de Estado Marco Rubio quanto a um impasse; "
        "cessar-fogo energético era negociado de modo intermitente e já havia sido abandonado por "
        "Kiev depois do acordo do diesel; a Rússia anunciou tomada de Dobropillia, em Donetsk, sem "
        "confirmação de Kiev na cobertura de 16 de outubro. Em Gaza, um cessar-fogo de 10 de outubro "
        "de 2025, associado a um plano americano, libertou os últimos reféns do ataque do Hamas em "
        "2023, mas um ano depois Israel controlava a maior parte do território, o Hamas não estava "
        "desarmado, e o Ministério da Saúde de Gaza — fonte local, que não separa de modo claro "
        "combatente e civil — contabilizava mais de 1.400 mortos desde o cessar-fogo; o Unicef "
        "falou em mais de 340 crianças mortas nesse período. A violência no Líbano foi descrita por "
        "analistas como elevada no mesmo ciclo. Interpretação reservada ao volume de política "
        "externa: o Brasil não é parte beligerante de nenhum desses conflitos e não ganha nada "
        "fingindo que é árbitro nato. Ganha não reconhecendo conquista territorial pela força e "
        "não embarcando em moeda comum nem em base militar.",
    )

    h(doc, 1, "7. Ciência, energia, agro e floresta")
    p(
        doc,
        "Fato, Inpe e governo federal, 16 de outubro de 2026: desmatamento na Amazônia de 3.335 km² "
        "entre agosto de 2025 e julho de 2026, queda de 41,8% sobre os 5.731 km² do ciclo anterior "
        "e menor taxa da série do Prodes desde 1988. O piso anterior era 2012, com 4.571 km². "
        "Pará ainda liderou, com 1.130 km², mesmo caindo 45,3%. Cerrado: 5.516,69 km², queda de "
        "23,8%, menor valor desde 2001. Frente a 2022, a queda amazônica citada foi de 71,2%, de "
        "11.594 km² para 3.335 km². O Prodes mede corte raso anual, não toda degradação nem todo "
        "fogo. Interpretação: a fiscalização funcionou e não acabou o problema. Tratar 3.335 km² "
        "como zero, ou tratar a queda como conspiração contra o produtor, são duas falsificações.",
    )
    p(
        doc,
        "Agropecuária foi o setor que puxou 2025. Isso entra no programa como ativo estratégico, "
        "não como setor suspeito. Energia: o país é potência hídrica, eólica e solar em expansão, "
        "com petróleo relevante na indústria extrativa — o próprio IBGE apontou extrativa em alta "
        "forte em 2025 — e com Angra como ativo nuclear incompleto. Não se localizou, para este "
        "volume, um percentual oficial único de 2026 para perda de transmissão ou para o custo "
        "atualizado de Angra 3 que pudesse ser citado sem hesitação; o programa trata o custo de "
        "Angra 3 como variável a auditar no primeiro semestre, não como número de campanha. "
        "Tecnologia: o Brasil tem mercado digital grande, pesquisa pontual de qualidade e quase "
        "nenhuma produção de semicondutor de fronteira. Prometer fab de ponta em quatro anos seria "
        "ficção dentro da ficção. A hipótese do programa é outra: desenho de chip, montagem, "
        "computação pública para universidade e regulação de risco, não autossuficiência heroica.",
    )

    h(doc, 1, "8. Os 15 problemas estruturais, na ordem deste candidato")
    p(
        doc,
        "A ordem mistura urgência, impacto sobre a vida do pobre e o quanto um presidente pode "
        "de fato mover, sozinho ou com o Congresso. Urgência e impacto vão de 1 a 5. Alavancagem "
        "presidencial também: 5 seria decreto puro; 1 seria quase só cultura. Nenhum item tem "
        "alavancagem 5. Quem prometer o contrário não leu a Constituição.",
    )
    table(
        doc,
        ["#", "Problema", "Urg.", "Impacto", "Alav.", "Por que nesta posição"],
        [
            ["1", "Juro real alto e dívida bruta em alta, com resultado nominal perto de 9% do PIB", "5", "5", "4", "Come a política inteira. Sem prêmio de risco menor, investimento público e privado perdem. Depende de meta crível e do Congresso."],
            ["2", "Aprendizagem ruiu no caminho: Ideb do médio público em 4,3 e 73% abaixo do nível 2 em matemática no PISA 2022", "5", "5", "3", "É o teto do país em 2046. Presidente não comanda a sala do município; comanda incentivo, avaliação e dinheiro condicionado."],
            ["3", "Facção, homicídio ainda massivo em números absolutos, feminicídio recorde e letalidade policial em alta", "5", "5", "3", "Polícia é estadual. União tem fronteira, presídio federal, dinheiro e inteligência. Média nacional em queda não absolve o recorde contra mulheres."],
            ["4", "Investimento em 16,8% do PIB e produtividade baixa", "4", "5", "3", "Sem isso, o social redistribui uma torta pequena. Obra e regra concorrem com emenda."],
            ["5", "Informalidade de 37,5% com desemprego baixo", "4", "4", "3", "O problema deixou de ser só falta de vaga. É custo de entrar na regra e desenho da proteção."],
            ["6", "Carga de 32,4% do PIB, consumo pesado, folha inimiga do formal e renúncia sem revisão", "4", "4", "3", "A transição do IBS/CBS não pode ser reaberta; o estoque de favor fiscal pode."],
            ["7", "Fila e preço do SUS sem linha de base nacional fechada, e tabela defasada", "4", "4", "3", "Direito universal com espera opaca é fila como política. Compra complementar não é privatizar o sistema."],
            ["8", "Saneamento incompleto e 5,77 milhões de domicílios em déficit, inadequação em alta", "4", "4", "2", "Marco legal joga o grosso na tarifa e no privado. O Tesouro não universaliza sozinho; abandona se não mirar o Norte e o muito pobre."],
            ["9", "Previdência: RGPS com déficit de R$ 320,9 bi em 2025 e população que envelhece", "3", "5", "2", "Impacto enorme, pressa de nova emenda ampla é falsa. O espaço imediato é fraude, cadastro e pensionista futuro das Forças."],
            ["10", "Desigualdade territorial e racial de renda, com o topo acelerando em 2025", "3", "4", "3", "Não se resolve com um imposto-símbolo. Resolve-se se escola, emprego formal e homicídio mudarem onde o número é pior."],
            ["11", "Pauta exportadora concentrada e quase nenhuma capacidade em semicondutor e defesa de alto conteúdo", "3", "4", "2", "Quatro anos não industrializam o país. Dão para escolher elo, não para fantasia de autarquia."],
            ["12", "Desmatamento ainda de 3.335 km² na Amazônia e cadastro fundiário incompleto", "3", "4", "4", "Aqui a União tem comando de verdade: fiscalização, terra pública, homologação. Por isso a alavancagem é mais alta do que a urgência relativa."],
            ["13", "Insegurança jurídica: tempo de processo, terra sem papel, licença sem prazo", "3", "3", "2", "Crescimento trava em vara e em cartório tanto quanto em alíquota. Presidente propõe lei e dá o exemplo no licenciamento federal."],
            ["14", "Fronteira amazônica, rio e rede: presença do Estado abaixo da soberania que o discurso afirma", "3", "3", "4", "Defesa e polícia federal são da União. Prometer porta-aviões em vez de sensor, rio e cibernética é erro de prioridades."],
            ["15", "Coalizão que fragmenta o orçamento e captura a regra", "4", "4", "2", "É a condição de todos os outros itens. Com 8% das cadeiras, ignorá-la é plano de papel."],
        ],
        font=7.5,
    )
    p(
        doc,
        "Ficaram de fora da lista dos quinze, não porque sejam pequenos, mas porque entram dentro "
        "de algum dos quinze ou porque o presidente não é o ator principal: cultura, esporte, "
        "turismo, regulação fina de plataforma, disputa de costumes. Eles têm eixo próprio no "
        "plano. Não têm o direito de furar a fila do fisco, da escola, do homicídio e do trilho.",
    )

    h(doc, 1, "9. O que o diagnóstico recusa")
    bullets(
        doc,
        [
            "Recusa dizer que o país quebrou. Desemprego de 5,3%, pobreza no menor nível da série em 2024 e superávit comercial não são retrato de colapso.",
            "Recusa dizer que o essencial está resolvido. Dívida projetada a 87% do PIB em 2027, IPCA de 2026 acima do teto na mediana do Focus, 1.571 feminicídios e investimento de 16,8% não são retrato de arranjo estável.",
            "Recusa atribuir cada número bom ou ruim a uma pessoa, para transformar estatística em palanque. O plano que começa no volume seguinte parte destes números e escolhe política. A escolha é que será julgada.",
        ],
    )

    h(doc, 1, "10. Fontes deste volume")
    bullets(
        doc,
        [
            "IBGE. Contas Nacionais Trimestrais. PIB cresce 2,3% em 2025 e fecha o ano em R$ 12,7 trilhões. Release, 3 mar. 2026.",
            "IBGE. PNAD Contínua. Desocupação no trimestre até agosto de 2026 em 5,3%, noticiada pela Agência Brasil em 13 out. 2026; informalidade de 37,5% no trimestre nov/2025–jan/2026, Agência Brasil, 5 mar. 2026.",
            "IBGE. Síntese de Indicadores Sociais 2025, referência 2024, divulgada em 3 dez. 2025. Rendimentos de 2025 divulgados em maio de 2026 (Folha e UOL).",
            "IBGE. Domicílios e população, divulgação de abril de 2026: 212,7 milhões de habitantes; água e esgoto.",
            "Banco Central. Meta da Selic, 13,75% desde 16 set. 2026. Boletim Focus, leituras de 13 a 19 out. 2026.",
            "FMI. World Economic Outlook, crescimento de 2,2% em 2026, noticiado pela Agência Brasil em 13 out. 2026.",
            "Ipea. Carta de Conjuntura, finanças públicas, outubro de 2026.",
            "Ministério da Fazenda, SPE. Prisma Fiscal, 15 out. 2026.",
            "Tesouro Nacional. Carga tributária bruta de 2025, boletim de abril de 2026; RREO em Foco, janeiro de 2026 (saúde, educação, seguridade); COFOG 2024, nota de dezembro de 2025.",
            "MDIC / Secex. Balança comercial, fechamento de 2025 e resultado até setembro de 2026.",
            "Fórum Brasileiro de Segurança Pública. 20º Anuário, 2026, dados de 2025. Reprodução numérica: G1, CNN Brasil, Valor, Estadão e Veja, 23 jul. 2026.",
            "INEP / MEC. Ideb 2025, Agência Brasil, 5 ago. 2026. PISA 2022, MEC, 5 dez. 2023.",
            "Inpe. Prodes Amazônia e Cerrado, taxas divulgadas em 16 out. 2026.",
            "Fundação João Pinheiro. Déficit habitacional 2024, divulgação coberta em junho de 2026.",
            "Cobertura de outubro de 2026 sobre Ucrânia (Reuters) e Gaza (CNN Brasil, Unicef, OCHA) usada apenas como contexto fático da data-base, não como doutrina.",
        ],
    )
    save(doc, os.path.join(OUT, "04_DIAGNOSTICO_NACIONAL.docx"))
    print("vol 04 ok")


if __name__ == "__main__":
    build()
