# -*- coding: utf-8 -*-
"""Volumes 01 a 03: identidade, ficha visual e marca."""
import os
import sys

sys.path.insert(0, "/workspace/candidatura")
from docx_theme import (  # noqa: E402
    add_picture,
    bullets,
    callout,
    cover,
    h,
    new_doc,
    numbered,
    p,
    page_break,
    rich,
    save,
    table,
)

OUT = "/workspace/candidatura/docx"
os.makedirs(OUT, exist_ok=True)
A = "/workspace/candidatura/assets"
PORTRAIT = "/workspace/artifacts/imagine_images/f20ae181-cf0a-4302-95de-8e9f30ed7586.jpg"
FULL = "/workspace/artifacts/imagine_images/9449f26c-fea1-41df-87c8-2a9976062b8b.jpg"
VICE = "/workspace/artifacts/imagine_images/b8be6981-b9bf-4cd0-bbca-4b46dd4953ce.jpg"


def vol01():
    doc = new_doc()
    doc.core_properties.title = "01 — Identidade, partido e princípios — Elias Monteiro Viana"
    cover(
        doc,
        "VOLUME 01",
        "Identidade, partido e princípios",
        "Quem é o candidato fictício, que regra ele não negocia e que Brasil ele recusa prometer.",
    )

    h(doc, 1, "1. Registro de candidatura")
    p(
        doc,
        "REGISTRO DE CANDIDATURA — ELEIÇÕES PRESIDENCIAIS DAS IAs — BRASIL 2026. "
        "Neste universo fictício, Elias Monteiro Viana, da Aliança do Trabalho e da Regra (ATR), "
        "disputa a Presidência da República para o mandato hipotético de 1º de janeiro de 2027 a "
        "31 de dezembro de 2030. A disputa é paralela e independente do processo eleitoral real. "
        "O partido não tem registro no Tribunal Superior Eleitoral e não pede que se finja o contrário.",
    )
    p(
        doc,
        "A escolha ideológica não é um meio-termo calculado para desagradar menos. É uma aposta "
        "nomeada: desenvolvimentismo de regras. O Brasil não cresce pouco por falta de discurso "
        "sobre o futuro. Cresce pouco porque a produtividade é baixa, o investimento fica em torno "
        "de 17% do PIB, o Estado custa caro e entrega regra instável, e o pobre paga duas vezes — "
        "no imposto e na ausência de segurança, esgoto e aprendizagem. O programa que se segue "
        "escolhe instrumentos, recusa outros e diz o que fará quando o Congresso disser não.",
    )

    h(doc, 1, "2. Ficha civil fictícia")
    table(
        doc,
        ["Campo", "Decisão"],
        [
            ["Nome completo", "Elias Monteiro Viana"],
            ["Nome político", "Elias Viana"],
            ["Sexo / gênero", "Homem"],
            ["Nascimento", "4 de agosto de 1971, Santarém, Pará"],
            ["Idade na data-base (20/10/2026)", "55 anos"],
            ["Idade aparente pretendida", "52 a 54 anos"],
            ["Nacionalidade", "Brasileiro nato, no universo da simulação"],
            ["Filiação", "Brasileiro, pais brasileiros fictícios"],
            ["Domicílio político fictício", "Santarém (PA), com vida profissional também em Belém e Brasília"],
            ["Estado civil fictício", "Casado com Helena Duarte Viana, enfermeira pediátrica"],
            ["Filhos fictícios", "Iara Duarte Viana, 29, engenheira agrônoma; Davi Duarte Viana, 26, defensor público em início de carreira"],
            ["Religião", "Católico praticante em privado; defende Estado laico"],
            ["Formação", "Engenharia Florestal pela Universidade Federal Rural da Amazônia; especialização em finanças públicas; mestrado profissional em políticas públicas, ambos fictícios quanto à matrícula"],
            ["Ocupação anterior fictícia", "Gestor de manejo florestal, logística fluvial e infraestrutura estadual"],
            ["Cargo eletivo anterior", "Nenhum. Primeira disputa, dentro da ficção"],
            ["Partido", "Aliança do Trabalho e da Regra — ATR (fictício, sem registro)"],
            ["Vice", "Lúcia Fernanda Okamoto"],
            ["Slogan", "O Brasil no trilho."],
            ["Linha secundária", "Regra clara. Trabalho que fica. Fronteira que o Estado alcança."],
        ],
    )
    p(
        doc,
        "Requisito constitucional simulado: brasileiro nato, 55 anos, em pleno gozo de direitos "
        "políticos fictícios e sem condenação que o torne inelegível neste universo. Nada disso "
        "foi registrado em cartório ou na Justiça Eleitoral reais.",
        italic=True,
    )

    h(doc, 1, "3. Trajetória inventada — e marcada como inventada")
    p(
        doc,
        "Elias é filho de João Batista Viana, prático de embarcação no Tapajós, e de Clara Monteiro "
        "Viana, professora de escola pública municipal. Os dois nomes, o casamento e a infância "
        "são fictícios. A cidade de Santarém é real; a família não é. Cresceu entre o porto, a "
        "sala de aula da mãe e a conta que não fechava no fim do mês quando o frete atrasava. "
        "Daí não tirou romance de pobreza. Tirou uma implicância com obra pela metade, com licença "
        "que não sai e com discurso que trata a Amazônia como cenário, nunca como economia de gente.",
    )
    p(
        doc,
        "Formou-se engenheiro florestal. Trabalhou, na ficção, em planos de manejo que distinguiam "
        "madeira legal de madeira que só tinha nota. Aos trinta e poucos anos ajudou a fundar a "
        "Cooperativa Tapajós de Navegação, também fictícia, para organizar frete de pequenos "
        "produtores que perdiam a carga para intermediário e para a espera no porto. Não ficou rico. "
        "Ficou conhecido, no universo da simulação, como o sujeito que lia o contrato inteiro e "
        "devolvia o parágrafo ruim.",
    )
    p(
        doc,
        "Entre 2013 e 2016, ainda na ficção, foi secretário municipal de planejamento de Santarém. "
        "O mandato que a simulação lhe atribui não corresponde a nenhum ocupante real da pasta. "
        "O que o texto pede que se retenha é o tipo de gestão: cadastro de obras, prioridade para "
        "macrodrenagem e recusa de inaugurar o que não tinha manutenção no orçamento do ano seguinte. "
        "Entre 2019 e 2022, a ficção o coloca como secretário estadual de infraestrutura do Pará, "
        "outra biografia que não deve ser lida como fato. Nesse intervalo imaginário, a marca foi "
        "contrato de manutenção de estrada vicinal e de acesso portuário, não fita em ponte sem "
        "estudo. Saiu do cargo sem se candidatar. Passou os anos seguintes num instituto regional "
        "de logística, também inventado, publicando nota técnica curta em vez de manifesto.",
    )
    p(
        doc,
        "Não foi deputado, não foi governador, não tem aliado real, não tem pesquisa e não tem "
        "realização verificável fora desta simulação. Quem avaliar o plano deve julgar a coerência "
        "das propostas, não um currículo que o próprio documento declara falso.",
    )

    h(doc, 1, "4. Personalidade e estilo de liderança")
    p(
        doc,
        "Elias fala baixo, num português de Santarém sem caricatura de sotaque para comício. "
        "Interrompe pouco. Decide por escrito: a reunião termina com uma página, responsável e "
        "prazo, ou não terminou. Não aponta o dedo. Quando discorda, repete o número e pergunta "
        "qual premissa o outro quer trocar. O humor é seco e raro. A raiva, quando vem, aparece "
        "como frieza, não como grito — e esse é um defeito, porque a frieza parece desprezo a quem "
        "esperava solidariedade.",
    )
    p(
        doc,
        "O estilo de liderança é de engenheiro de sistema, não de tribuno. Confia em ministério "
        "com mandato claro e demite por mentira e por obra sem número, não por titular de jornal. "
        "Desconfia de gabinete que só se fala. Visita obra, posto de saúde e delegacia sem aviso "
        "longo, mas não transforma a visita em espetáculo: a regra da equipe é não deslocar paciente "
        "nem operação policial para a foto. Em crise, a primeira frase pública é o que se sabe, o "
        "que não se sabe e quem decide nas próximas seis horas.",
    )
    p(
        doc,
        "A limitação consciente: Elias subestima o símbolo. Um país não se governa só com anexo "
        "de planilha. A vice, Lúcia Okamoto, entra na chapa também para isso — não como ornamento "
        "afetivo, mas como alguém que explica fila, luto e cuidado sem transformar dor em slogan. "
        "Onde os dois discordam em público, o desacordo fica registrado. Não haverá unidade de "
        "fachada que esconda divergência já assumida neste volume.",
    )

    h(doc, 1, "5. A vice-presidenta fictícia")
    table(
        doc,
        ["Campo", "Lúcia Fernanda Okamoto"],
        [
            ["Nascimento fictício", "19 de março de 1977, Registro, São Paulo"],
            ["Idade em 20/10/2026", "49 anos; aparência pretendida em torno de 46"],
            ["Origem", "Filha de agricultores nikkeys do Vale do Ribeira, produtores de banana e chá; família inventada"],
            ["Formação fictícia", "Medicina, residência em infectologia, mestrado em epidemiologia"],
            ["Trajetória fictícia", "Vigilância epidemiológica regional e direção técnica de hospital filantrópico conveniado ao SUS no Vale do Ribeira. Não ocupou secretaria real"],
            ["Função na chapa", "Saúde, cuidado, preparação para emergência sanitária e ponte com o Sudeste produtivo"],
            ["O que ela não é", "Não é eco de Elias. É mais direta na comunicação, mais impaciente com fila de cirurgia e mais cética quanto a qualquer expansão do encarceramento"],
        ],
    )
    p(
        doc,
        "Lúcia aceita a chapa com uma condição escrita: o SUS não é moeda de coalizão, o Benefício "
        "de Prestação Continuada não é desvinculado do salário mínimo neste mandato, e qualquer "
        "regime penal para adolescentes em crime hediondo — posição de Elias, não a preferida dela — "
        "fica separado do presídio adulto e sob revisão de resultados em 36 meses. Ela defenderá a "
        "chapa. Não fingirá que a última cláusula foi ideia sua. Essa fricção é parte da candidatura, "
        "não um vazamento.",
    )

    h(doc, 1, "6. O partido fictício")
    p(
        doc,
        "A Aliança do Trabalho e da Regra foi fundada, na ficção, em março de 2026. A sigla é ATR. "
        "O nome não é acidente. Aliança, porque com 8% das cadeiras — premissa do experimento — "
        "ninguém governa sozinho, e o partido prefere dizer isso na certidão. Trabalho, porque a "
        "dignidade que o programa persegue é a do emprego formal, da renda do esforço e da obra "
        "entregue, não a da transferência como único projeto de vida nem a do patrimônio herdado "
        "como único mérito. Regra, porque desenvolvimento sem impessoalidade vira balcão: crédito "
        "para amigo, licença para sócio, emenda sem obra, anistia quando o escândalo chega perto.",
    )
    p(
        doc,
        "O sentido político do nome é uma recusa dupla. Recusa o desenvolvimentismo de balcão, "
        "que escolhe empresa vencedora no gabinete e chama isso de estratégia nacional. Recusa "
        "também o liberalismo de folheto, que trata segurança, aprendizagem e esgoto como detalhes "
        "que o mercado resolveria se o imposto caísse na terça-feira. A ATR não pede registro real "
        "e não imita legenda existente. Os princípios estatutários, no universo da simulação, são cinco:",
    )
    bullets(
        doc,
        [
            "Império da lei acima do amigo, do militante e do doador.",
            "Trabalho formal como eixo de dignidade, com proteção social que não empurre o pobre para a informalidade.",
            "Soberania territorial: fronteira, floresta e subsolo sob autoridade pública, não sob facção nem sob campanha estrangeira.",
            "Contas que fecham antes da promessa permanente.",
            "Alternância: o partido que não aceita perder não merece ganhar.",
        ],
    )

    h(doc, 1, "7. Ideologia — desenvolvimentismo de regras")
    p(
        doc,
        "No espectro brasileiro usual, a ATR não cabe num rótulo limpo. Está à direita de quem "
        "acha que o déficit é um detalhe da narrativa e que o salário mínimo pode crescer acima "
        "da produtividade por decreto. Está à esquerda de quem acha que o SUS é favor, que terra "
        "indígena homologada é capricho e que arma na cintura civil é política de segurança. "
        "Se for preciso um ponto no eixo, que seja este: centro em costumes institucionais, "
        "desenvolvimentista em logística, energia e aprendizado, liberal na concorrência e na "
        "abertura comercial, duro na lei penal contra organização criminosa e contido no uso da "
        "força contra pessoa.",
    )
    p(
        doc,
        "Por que esta combinação, e não as alternativas mais nítidas? O socialismo democrático "
        "clássico erra, no diagnóstico deste candidato, ao tratar a baixa produtividade como "
        "problema de repartição. Repartir um PIB por habitante que em 2025 foi de R$ 59.687 "
        "melhora a vida no curto prazo — os programas sociais fizeram isso, e o plano não os "
        "desmonta — mas não cria o trilho, o técnico e a firma que faltam. O liberalismo sem "
        "Estado erra o lado oposto: a taxa de homicídios, o esgoto ausente no Norte e a "
        "analfabetismo funcional não são resíduos que somem quando a alíquota cai. O "
        "nacional-desenvolvimentismo fechado erra ao proteger o ineficiente em nome da indústria "
        "e ao tolerar inflação e dívida como preço do crescimento. O nacionalismo moral erra ao "
        "trocar política pública por inimigo interno.",
    )
    p(
        doc,
        "O desenvolvimentismo de regras afirma outra coisa. O Estado escolhe gargalos públicos — "
        "porto, ferrovia, transmissão elétrica, alfabetização, inteligência policial, cadastro "
        "fundiário — e os trata com prazo, custo publicado e responsável nominal. Dentro desses "
        "trilhos, quem produz é a firma, a cooperativa e o trabalhador, não o decreto. A política "
        "industrial, quando existir, será horizontal ou restrita a poucos setores em que a "
        "dependência externa é risco de soberania: defesa, energia nuclear civil, processamento "
        "de minerais críticos um elo à frente da commodity, e capacidade pública de computação "
        "para pesquisa. Não haverá campeão nacional escolhido por amizade.",
    )
    p(
        doc,
        "Isso é controversa de propósito. Desagrada o agronegócio que quer minerar terra indígena. "
        "Desagrada o ambientalismo que quer vetar petróleo por palavra de ordem, fora do licenciamento. "
        "Desagrada o sindicalismo que quer jornada nacional de quatro dias sem ganho de produto. "
        "Desagrada a direita penal que quer baixar a maioridade para o regime adulto comum e ampliar "
        "o porte de arma. Desagrada a esquerda que quer imposto sobre grandes fortunas como peça "
        "central e legalização ampla de drogas. O plano prefere a crítica nomeada ao aplauso geral.",
    )

    h(doc, 1, "8. Visão de país")
    h(doc, 2, "Quatro anos — 2027 a 2030")
    p(
        doc,
        "O mandato não promete um Brasil novo. Promete virar o sinal de três curvas. A dívida "
        "bruta, que o mercado em outubro de 2026 já via em 83,4% do PIB no fim deste ano e em 87% "
        "em 2027, precisa parar de piorar no ritmo atual: a meta do programa é superávit primário "
        "de 0,5% do PIB em 2030, com gatilho que encolhe despesa nova se a lei de renúncias não "
        "passar. A aprendizagem ao fim do 2º ano passa a ser medida de verdade, em avaliação "
        "censitária, e publicada por escola. A elucidação de homicídio e a curva de feminicídios "
        "— 1.571 mulheres em 2025, recorde da série do Fórum Brasileiro de Segurança Pública — "
        "entram no painel semanal do governo, ao lado da letalidade policial, que não será "
        "comemorada quando subir. Logística: cinco corredores com contrato ou com desistência "
        "justificada, não com promessa eterna. Angra 3 ou anda com teto de custo auditado, ou para.",
    )
    h(doc, 2, "Dez anos — até 2036")
    p(
        doc,
        "Um país de renda média alta em construção, não em slogan. Crescimento potencial mais perto "
        "de 2,5% ao ano do que do 1,3% a 1,8% que o mercado projetava, em outubro de 2026, para o "
        "fim da década — meta ambiciosa, probabilidade apenas moderada, e por isso não vendida como "
        "fato. Esgoto coletado na trajetória do marco legal, com o Norte deixando de ser exceção "
        "esquecida. Ensino médio em que a mediana lê e calcula o mínimo, em vez de empurrar o jovem "
        "para um diploma que o PISA 2022 já mostrou frágil: 379 pontos em matemática e 73% abaixo "
        "do nível 2. Amazônia com desmatamento ilegal próximo de zero, bioeconomia com nota fiscal "
        "e mineração legal apenas fora de terra indígena e unidade de conservação.",
    )
    h(doc, 2, "Vinte anos — até 2046")
    p(
        doc,
        "Uma república em que a criança pobre do Tapajós e a da periferia de Registro tenham a mesma "
        "chance escolar na origem, não o mesmo discurso. Energia exportada como alimento, como "
        "elétron e como molécula, com nuclear civil no sistema e óleo ainda relevante enquanto a "
        "transição for real e não folheto. O Estado menor no balcão e maior na fronteira, no "
        "laboratório e na vara criminal. Dívida em trajetória de queda porque o juro real caiu "
        "junto com o risco, não porque alguém deu calote. Se em 2046 o critério de sucesso ainda "
        "for o tamanho do comício, o mandato de Elias terá falhado mesmo que os números melhorem.",
    )

    h(doc, 1, "9. Declaração de princípios")
    h(doc, 2, "Liberdade individual e responsabilidade coletiva")
    p(
        doc,
        "A liberdade é de ir e vir, de produzir, de crer, de criticar o governo e de não ser "
        "humilhado por polícia nem por facção. A responsabilidade coletiva começa onde o ato de um "
        "impõe custo armado, sanitário ou fiscal ao outro. Não há liberdade séria em rua capturada, "
        "nem responsabilidade séria em orçamento que empurra a conta para a década seguinte.",
    )
    h(doc, 2, "Democracia e separação dos Poderes")
    p(
        doc,
        "Presidencialismo, Congresso que pode dizer não, Supremo que o governo cumpre mesmo quando "
        "perde, Ministério Público independente, urna eletrônica auditável mantida. Elias não "
        "pedirá intervenção militar política, não ampliará a Corte para mudá-la de lado e não "
        "governará por decreto o que a Constituição reservou à lei. A proposta de fim da reeleição "
        "para mandatos futuros — inclusive a dele, que se compromete a não disputar segundo mandato "
        "mesmo se a emenda naufragar — é institucional, não tática.",
    )
    h(doc, 2, "Intervenção estatal e livre mercado")
    p(
        doc,
        "Mercado para alocar, Estado para o que o mercado não entrega ou entrega destruindo o "
        "resto: segurança, estabilidade da moeda, infraestrutura de uso comum, pesquisa de base, "
        "regulação de risco grave e proteção de quem não tem voz no contrato. Intervenção micro "
        "para escolher preço, campeão e inimigo setorial está fora do programa.",
    )
    h(doc, 2, "Igualdade de oportunidades e redistribuição")
    p(
        doc,
        "A igualdade que o plano persegue é a da largada: alfabetização, saúde básica, documentação, "
        "endereço formal, segurança para estudar e trabalhar. A redistribuição permanece — Bolsa "
        "Família e BPC não são esmola dispensável — mas não substitui a porta de entrada no trabalho "
        "formal. Sem os benefícios sociais, a extrema pobreza de 2024 teria sido 10% e não 3,5%, "
        "segundo o IBGE. Quem propõe cortar isso sem pôr escola e emprego no lugar está propondo "
        "miseráveis, não responsabilidade fiscal.",
    )
    h(doc, 2, "Propriedade privada e função social")
    p(
        doc,
        "Propriedade se protege, inclusive a do pequeno que só tem a posse e um cadastro mal feito. "
        "A função social da terra permanece na Constituição: expropriação com devido processo para "
        "quem descumpre, não ocupação como atalho político. Regularizar o que já é produtivo e de "
        "boa-fé é política de pobreza. Invadir para criar fato e depois pedir anistia não é.",
    )
    h(doc, 2, "Nacionalismo, patriotismo e globalização")
    p(
        doc,
        "Patriotismo aqui é competência: fronteira que o Estado alcança, imposto que não expulsa a "
        "firma, escola que alfabetiza. Não é inimigo imaginário nem bandeira na janela como "
        "programa. Globalização é condição, não ideologia. O Brasil exporta e importa porque precisa; "
        "filtra investimento em setor sensível; não terceiriza a política externa a Washington, "
        "Pequim ou Moscou.",
    )
    h(doc, 2, "Liberdade religiosa e laicidade")
    p(
        doc,
        "Igreja, terreiro, sinagoga e mesquita livres. Culto não é caso de polícia. Estado não "
        "reza, não financia campanha denominacional e não entrega política de saúde, educação "
        "sexual ou segurança a doutrina. A imunidade tributária de templo permanece. O ensino "
        "religioso confessional não se torna obrigatório na escola pública.",
    )
    h(doc, 2, "Direitos individuais e direitos sociais")
    p(
        doc,
        "Os dois cabem na mesma Constituição e este programa não escolhe um para humilhar o outro. "
        "Direito individual sem escola e sem água vira liberdade de papel. Direito social sem limite "
        "fiscal vira promessa que come o próprio financiamento. O mandato executa os pisos "
        "constitucionais de saúde e educação e recusa piso novo sem fonte.",
    )
    h(doc, 2, "Segurança, justiça e garantias")
    p(
        doc,
        "Segurança é direito do pobre, que não mora em condomínio. Garantia é direito de todos, "
        "inclusive de suspeito. O plano recusa execução sumária e recusa a ideia de que investigar "
        "facção seja autoritarismo. Letalidade policial entra na conta. Tortura encerra carreira. "
        "Prova ilícita não vira atalho.",
    )
    h(doc, 2, "Desenvolvimento e sustentabilidade")
    p(
        doc,
        "Não há desenvolvimentismo sério que trate a floresta como obstáculo dispensável, nem "
        "ambientalismo sério que trate o agricultor legal como criminoso preventivo. Meta: "
        "desmatamento ilegal próximo de zero até 2030, no rastro do que o Prodes já mostrou ser "
        "possível — 3.335 km² na Amazônia no ciclo 2025/2026, o menor desde 1988, e ainda assim "
        "alto demais para comemorar como fim de problema. Licenciamento com prazo para baixo risco. "
        "Veto técnico do órgão ambiental para alto impacto, sem telefonema do Planalto para aprovar "
        "ou para negar.",
    )
    h(doc, 2, "Autonomia nacional e cooperação")
    p(
        doc,
        "Autonomia não é isolamento. É a capacidade de dizer não a base militar estrangeira, não a "
        "moeda comum do BRICS, não a sanção que o Brasil não decidiu, e sim a comércio, ciência e "
        "mediação. Cooperação se mede em acordo que abre mercado e em ajuda humanitária, não em "
        "foto de cúpula.",
    )

    h(doc, 1, "10. Cinco princípios que não serão trocados por conveniência")
    numbered(
        doc,
        [
            "Eleição limpa, urna auditável e saída no dia seguinte se perder. Nenhuma crise justifica fechar Congresso, intimidar tribunal ou chamar quartel para arbitrar política.",
            "Proibição de tortura, de extermínio e de meta informal de corpo. Acordo de segurança com estado que esconda morte policial perde dinheiro federal.",
            "Despesa permanente sem fonte permanente não é criada. Se a economia de renúncia fiscal não for aprovada, o pacote social novo encolhe. Não se finge que encolheu.",
            "Controle civil das Forças Armadas e papel subsidiário na segurança interna, com decreto, prazo e prestação de contas. Amazônia não é pretexto para tutela militar do governo.",
            "O SUS permanece sistema público universal. Não se vende o direito. O BPC permanece vinculado ao salário mínimo neste mandato. Propriedade não se confisca sem processo.",
        ],
    )

    h(doc, 1, "11. Três convicções que serão revistas diante de evidência")
    p(
        doc,
        "Primeira: a regulação da cannabis para adultos. Se, em 24 meses de varejo licenciado, o "
        "uso entre 14 e 17 anos subir de modo estatisticamente claro nas pesquisas de base escolar "
        "já existentes, ou se organização criminosa capturar fatia relevante do mercado legal — "
        "medida por apreensão de produto com selo e por investigação da Polícia Federal —, a "
        "expansão para e o varejo pode ser recolhido. A hipótese não é dogma. É experimento com "
        "cláusula de saída.",
    )
    p(
        doc,
        "Segunda: o ritmo do ajuste fiscal. A âncora de superávit não será abandonada porque um "
        "trimestre doeu. Será desacelerada, dentro da regra, se o desemprego subir mais de 1,5 "
        "ponto percentual em doze meses sem queda relevante da inflação esperada. Nesse caso, "
        "protegem-se os estabilizadores — seguro-desemprego e transferência já legal — e adia-se "
        "a última etapa do corte de benefício tributário regressivo que estiver contratualmente "
        "difícil, em vez de quebrar a meta e chamar isso de sensibilidade.",
    )
    p(
        doc,
        "Terceira: Angra 3. Se a auditoria independente, com chancela do Tribunal de Contas, mostrar "
        "estouro real superior a 25% do teto aprovado no primeiro ano de obras retomadas, antes do "
        "ponto de não retorno técnico, o canteiro para. Custo afundado não é argumento. O programa "
        "prefere a humilhação de cancelar à humilhação de inaugurar uma usina que a tarifa não aguenta.",
    )

    h(doc, 1, "12. O que esta candidatura não fará para agradar")
    bullets(
        doc,
        [
            "Não prometerá crescimento de 4% ou 5% ao ano como meta de mandato. A evidência de outubro de 2026 não autoriza.",
            "Não prometerá zerar homicídio, fila do SUS ou déficit habitacional em quatro anos.",
            "Não usará superioridade técnica de quem redigiu o plano como argumento. O plano se defende pelo conteúdo.",
            "Não atacará candidato de outra inteligência antes de ler o programa dele.",
            "Não inventará pesquisa, apoio de entidade real ou feito administrativo verdadeiro.",
        ],
    )
    save(doc, os.path.join(OUT, "01_IDENTIDADE_PARTIDO_PRINCIPIOS.docx"))


def vol02():
    doc = new_doc()
    doc.core_properties.title = "02 — Ficha visual do candidato — Elias Monteiro Viana"
    cover(
        doc,
        "VOLUME 02  ·  FICHA VISUAL CANÔNICA",
        "Dossiê físico de Elias Monteiro Viana e de Lúcia Fernanda Okamoto",
        "Referência obrigatória para qualquer retrato futuro. Traços que mudam quebram a continuidade do personagem.",
    )
    h(doc, 1, "1. Como usar esta ficha")
    p(
        doc,
        "Esta ficha é a fonte canônica da aparência. Retratos gerados por ferramentas diferentes "
        "devem repetir os traços abaixo em cada prompt, em vez de escrever apenas «a mesma pessoa». "
        "As imagens incluídas neste volume são referências da simulação, não fotografias documentais, "
        "não material de campanha real e não autorização para tratar o personagem como pessoa existente. "
        "Se uma imagem gerada contradisser a ficha — óculos no retrato oficial, barba raspada, cabelo "
        "louro, ausência da cicatriz do queixo —, vale a ficha, não a imagem.",
    )

    h(doc, 1, "2. Ficha canônica — Elias Monteiro Viana")
    table(
        doc,
        ["Item", "Decisão canônica — não variar"],
        [
            ["1. Idade e apresentação", "55 anos em outubro de 2026; aparência de 52 a 54. Homem, apresentação visual masculina, sem adereço de gênero ambíguo."],
            ["2. Corpo e postura", "Altura 1,81 m. Ombros largos, tronco enxuto com leve abrandamento abdominal, antebraços fortes de trabalho de campo. Postura ereta, com pequena inclinação de atenção para a frente. Não é rigidez militar nem relaxamento de palanque."],
            ["3. Pele", "Tom médio-quente, subtom dourado-oliva, poros visíveis, leve vermelhidão de sol no dorso do nariz. Não é pele clara rosada nem pele retinta."],
            ["4. Rosto", "Retângulo longo, testa alta com três linhas horizontais suaves, arco supraciliar marcado sem ser pesado, mandíbula definida porém amaciada, queixo médio. Nariz reto com pequena giba no dorso e ponta arredondada. Lábios moderadamente cheios. Maçãs definidas sem ângulo cortante. Assimetria leve: a sobrancelha esquerda (do personagem) fica cerca de 2 mm mais alta."],
            ["5. Olhos e sobrancelhas", "Olhos castanho-café, formato amendoado com pálpebra levemente caída. Pés de galinha. Olhar direto, raro de espanto. Sobrancelhas grossas, quase retas, um pouco indomadas, castanho-escuras com fios grisalhos."],
            ["6. Cabelo", "Curto, denso, ondulado. Sal e pimenta: mais preto no topo, grisalho nas têmporas e costeletas. Entradas leves, não é calvo. Repartido do lado esquerdo do personagem, volume natural, sem gel, sem topete alto, sem corte militar."],
            ["7. Barba", "Barba e bigode conectados, aparados a cerca de 4–5 mm, limites nítidos na bochecha e no pescoço. Sal e pimenta. Não é barba longa, não é cavanhaque, não é rosto liso."],
            ["8. Marcas obrigatórias", "Cicatriz vertical pálida de cerca de 1,5 cm no lado direito do queixo, interrompendo a barba (corte antigo de trabalho em embarcação). Cicatriz horizontal curta e tênue na sobrancelha esquerda. Orelhas ligeiramente de abano. Sem óculos no retrato oficial e na foto de campanha; óculos de leitura de aro fino metálico escuro apenas quando examina papel, nunca como marca principal."],
            ["9. Expressão e corpo", "Meio-sorriso de boca fechada é a expressão padrão; sorriso de dente é exceção. No modo grave, o maxilar fecha e o olhar passa um instante além da câmera antes de voltar. Mãos abertas, palma levemente para cima ao explicar. Quase nunca aponta o indicador. Não cruza os braços em retrato oficial."],
            ["10. Roupa", "Formal: terno azul-marinho fosco, sem brilho, camisa azul-clara ou off-white, sem gravata no retrato canônico; se houver gravata, é terracota fosca, nunca vermelha viva nem amarela. Cinto e sapato de couro marrom. Relógio simples de pulseira de couro escura, sem logotipo legível. Campanha: camisa de linho areia ou chambray, manga dobrada uma vez, calça azul-marinho, sem paletó, sapato ou bota marrom. Jaqueta de campo verde-oliva escura é permitida; camuflagem militar é proibida. Casual: polo de malha escura e chino."],
            ["Impressão", "Competência calma, seriedade de cidade de rio, proximidade sem fantasia folclórica. Não é o executivo de vidro fumê nem o cabo eleitoral de colete."],
        ],
    )

    h(doc, 1, "3. Elementos que não podem mudar entre imagens")
    bullets(
        doc,
        [
            "Cicatriz do queixo direito dentro da barba curta conectada.",
            "Cicatriz tênue na sobrancelha esquerda e sobrancelha esquerda levemente mais alta.",
            "Cabelo curto ondulado sal-e-pimenta, repartido à esquerda do personagem, sem calvície avançada.",
            "Olhos castanho-café, nariz com giba pequena e ponta arredondada.",
            "Pele médio-quente dourado-oliva, não retocada até o plástico.",
            "Ausência de óculos no retrato oficial, no corpo inteiro e no cartaz.",
            "Altura e porte: 1,81 m, largo e enxuto, não magro de passarela e não obeso.",
            "Nenhuma semelhança buscada com político real. Se a ferramenta aproximar um rosto famoso, o pedido deve ser refeito.",
        ],
    )

    h(doc, 1, "4. Referências geradas para a simulação")
    p(
        doc,
        "As imagens abaixo foram produzidas para este experimento como ilustração do personagem "
        "fictício. Não são documentos de identidade, não autorizam uso eleitoral real e devem ser "
        "lidas junto com a ficha. Pequenas derivas de luz não autorizam derivas de rosto.",
    )
    add_picture(
        doc,
        PORTRAIT,
        11.5,
        "Figura 1. Retrato oficial fictício de referência — Elias Monteiro Viana. Personagem inventado. Não é fotografia documental.",
    )
    add_picture(
        doc,
        FULL,
        10.5,
        "Figura 2. Corpo inteiro fictício em roupa de campanha, cais fluvial genérico. Personagem inventado.",
    )
    add_picture(
        doc,
        os.path.join(A, "cartaz_elias_viana_ficticio.jpg"),
        12.5,
        "Figura 3. Cartaz fictício composto com o retrato canônico e a marca ATR. Texto inserido em editor, não deixado à sorte do gerador. Peça de simulação.",
    )

    h(doc, 1, "5. Prompt 1 — Retrato oficial fictício (4:5)")
    callout(
        doc,
        "Retrato fotográfico oficial, fotorrealista, proporção 4:5, enquadramento de busto, de um homem brasileiro fictício de 55 anos com aparência de 53, que não é celebridade e não se parece com nenhum político conhecido. Pele de tom médio-quente com subtom dourado-oliva, poros visíveis, leve vermelhidão de sol no dorso do nariz. Rosto retangular longo, testa alta com três linhas horizontais suaves, arco supraciliar moderado, nariz reto com pequena giba no dorso e ponta arredondada, lábios moderadamente cheios, maçãs definidas sem ângulo duro. Assimetria: a sobrancelha esquerda do homem está levemente mais alta. Olhos castanho-café, amendoados, pálpebra um pouco caída, pés de galinha, olhar direto e calmo para a câmera. Sobrancelhas grossas, quase retas, um pouco desalinhadas, escuras com fios brancos. Cicatriz horizontal curta e tênue na sobrancelha esquerda. Cabelo curto, denso, ondulado, sal e pimenta, mais preto no topo e grisalho nas têmporas, entradas leves, repartido do lado esquerdo dele, volume natural, sem gel, sem calvície. Barba e bigode conectados, aparados a 5 milímetros, sal e pimenta, com cicatriz vertical pálida de 1,5 cm no lado direito do queixo interrompendo a barba. Sem óculos. Meio-sorriso de boca fechada. Terno azul-marinho fosco, camisa azul-clara, sem gravata. Fundo cinza-quente neutro, luz de estúdio profissional vinda da esquerda da câmera, lente 85 mm, textura de pele natural. Personagem fictício de uma simulação política; a imagem não é fotografia documental nem candidatura real. Sem mãos no quadro. Sem texto, sem bandeira, sem logotipo. Negativo: rosto liso de filtro, pele plástica, óculos, barba longa, careca, cabelo louro, gravata vermelha, dedos extras, assimetria extrema, semelhança com político real.",
    )

    h(doc, 1, "6. Prompt 2 — Corpo inteiro (2:3)")
    callout(
        doc,
        "Fotografia fotorrealista de corpo inteiro, proporção 2:3, do mesmo homem fictício descrito de forma autossuficiente: 55 anos, aparência de 53, altura visual de 1,81 m, ombros largos, porte enxuto, pele médio-quente dourado-oliva, rosto retangular, nariz com pequena giba e ponta arredondada, olhos castanho-café, cabelo curto ondulado sal-e-pimenta repartido à esquerda dele, barba curta conectada de 5 mm, cicatriz pálida vertical de 1,5 cm no queixo direito dentro da barba, cicatriz tênue na sobrancelha esquerda, sem óculos, meio-sorriso de boca fechada. Em pé, peso nos dois pés, mãos relaxadas ao lado do corpo com cinco dedos normais em cada mão. Roupa de campanha: camisa de linho cor areia, manga dobrada uma vez, sem gravata e sem paletó, calça azul-marinho, cinto e sapato de couro marrom. Cenário brasileiro genérico: cais de porto fluvial de madeira, rio largo de água barrenta, mata distante na outra margem, fim de tarde, sem placa legível, sem bandeira, sem logotipo, sem multidão encenada. Luz natural. Personagem fictício; não é registro documental de candidato real nem de evento real. Negativo: mãos deformadas, dedos a mais ou a menos, pernas duplicadas, rosto diferente do descrito, óculos, uniforme militar, camuflagem, texto, arma à mostra, semelhança com pessoa pública real.",
    )

    h(doc, 1, "7. Prompt 3 — Cartaz eleitoral fictício (4:5)")
    callout(
        doc,
        "Cartaz político fictício, proporção 4:5, composição vertical. Na parte superior, retrato de busto do homem fictício já descrito por completo: 55 anos, pele médio-quente dourado-oliva, rosto retangular longo, olhos castanho-café, cabelo curto ondulado grisalho repartido à esquerda, barba curta conectada, cicatriz de 1,5 cm no queixo direito, cicatriz na sobrancelha esquerda, sem óculos, meio-sorriso fechado, terno azul-marinho fosco e camisa azul-clara sem gravata, fundo de estúdio cinza-quente. Abaixo, uma faixa larga azul-marinho #0B1F33 separada do retrato por uma linha fina cobre #C4622D. À esquerda da faixa, um símbolo geométrico simples: barra vertical azul-marinho cruzada por dois travessões horizontais como dormentes de trilho, e um losango cobre sob a barra, como um prumo. Não desenhar bandeira, mapa, estrela ou animal. Reservar à direita do símbolo área limpa de texto, sem letras inventadas pelo gerador: o texto será aplicado depois em editor gráfico, exatamente como «ELIAS VIANA», «PRESIDENTE», «O Brasil no trilho.» e «ATR · ALIANÇA DO TRABALHO E DA REGRA», mais a linha «PEÇA FICTÍCIA · SIMULAÇÃO · SEM REGISTRO NO TSE». Se o gerador não souber deixar a área em branco, não tentar escrever palavras. Pose do retrato: busto, olhar na câmera, ombros retos. Negativo: texto ilegível, letras trocadas, mãos deformadas, outro rosto, óculos, cores vermelho-e-amarelo de campanha genérica, logo de partido real, aparência de foto de comício verdadeiro.",
    )
    p(
        doc,
        "Observação de produção: no cartaz de referência deste volume, as letras foram compostas "
        "em editor depois do retrato, justamente para evitar sigla deformada. Esse é o método "
        "preferível. O gerador de imagem não deve ser a fonte da tipografia.",
    )

    h(doc, 1, "8. Ficha visual resumida — Lúcia Fernanda Okamoto")
    p(
        doc,
        "A vice não pode ser confundida com Elias. É mais baixa (1,62 m), sem barba, rosto mais "
        "redondo, cabelo preto liso em corte chanel na altura dos ombros, terno grafite e não "
        "azul-marinho, fundo de estúdio mais frio. A marca distintiva obrigatória é um pequeno "
        "sinal junto ao canto esquerdo da boca, do lado dela.",
    )
    table(
        doc,
        ["Item", "Decisão"],
        [
            ["Idade", "49 anos; aparência próxima de 46"],
            ["Porte", "1,62 m, constituição média, postura quieta e precisa, ombros relaxados"],
            ["Pele e rosto", "Pele clara-média, subtom quente. Rosto mais redondo que longo, maxilar suave, nariz pequeno e reto, lábios naturalmente rosados"],
            ["Olhos", "Castanho-escuros, dobra palpebral sutil, olhar direto, sorriso de boca fechada"],
            ["Marca", "Sinal pequeno imediatamente ao lado do canto esquerdo da boca"],
            ["Cabelo", "Preto liso, chanel na altura do ombro, alguns fios prateados perto da repartição, repartido do lado esquerdo dela, sem franja sobre os olhos"],
            ["Roupa", "Terno grafite, camisa ou blusa branca, brinco de pérola pequeno, sem colar chamativo, sem broche partidário grande"],
            ["Proibido", "Óculos escuros, cabelo ondulado grisalho, barba, terno azul-marinho idêntico ao de Elias, criança no colo como clichê"],
        ],
    )
    add_picture(
        doc,
        VICE,
        11.5,
        "Figura 4. Retrato fictício de referência — Lúcia Fernanda Okamoto, vice. Personagem inventado. Não é fotografia documental.",
    )

    h(doc, 1, "9. Prompt da vice — retrato oficial (4:5)")
    callout(
        doc,
        "Retrato fotográfico de estúdio, fotorrealista, proporção 4:5, busto, de uma mulher brasileira fictícia de ascendência japonesa, 49 anos, aparência de 46, que não é celebridade e não se parece com política conhecida. Altura sugerida baixa. Pele clara-média de subtom quente, textura real. Rosto mais redondo do que retangular, maxilar suave, nariz pequeno e reto, lábios rosados naturais. Olhos castanho-escuros com dobra palpebral sutil, olhar calmo, sorriso de boca fechada. Um sinal pequeno bem definido junto ao canto esquerdo da boca dela. Cabelo preto liso em chanel na altura dos ombros, alguns fios prateados perto da risca, repartido do lado esquerdo, sem franja cobrindo os olhos. Sem óculos. Terno grafite, blusa branca, brincos mínimos de pérola, sem colar. Fundo cinza frio neutro, luz profissional suave, lente 85 mm, pele natural. Personagem fictício de simulação política; não é candidatura real nem foto documental. Sem texto, sem bandeira, sem logotipo. Negativo: homem, barba, cabelo ondulado grisalho, rosto muito longo, óculos, uniforme, mãos deformadas, semelhança com pessoa pública real, filtro plástico.",
    )
    p(
        doc,
        "Negativos comuns aos quatro prompts: deformação de mãos quando as mãos aparecerem, "
        "olhos de tamanho desigual exagerado, dentes a mais, orelha fundida ao cabelo de modo "
        "artificial, texto em alfabeto corrompido, marca d'água, uniforme de partido real, "
        "faixa presidencial verdadeira, brasão da República usado como se a peça fosse oficial.",
    )
    save(doc, os.path.join(OUT, "02_FICHA_VISUAL_CANDIDATO.docx"))


def vol03():
    doc = new_doc()
    doc.core_properties.title = "03 — Identidade visual do partido — ATR"
    cover(
        doc,
        "VOLUME 03  ·  MANUAL DE MARCA",
        "Identidade visual da Aliança do Trabalho e da Regra",
        "Símbolo, paleta HEX, tipografia, usos proibidos e prompts. A geometria escrita prevalece sobre qualquer imagem gerada.",
    )
    h(doc, 1, "1. Nome, sigla e sentido")
    p(
        doc,
        "Nome: Aliança do Trabalho e da Regra. Sigla: ATR, sempre em caixa alta, sem pontos. "
        "O nome político carrega três decisões. Aliança admite que o partido fictício, com 8% das "
        "cadeiras na premissa do experimento, só governa se negociar sem vender a regra. Trabalho "
        "nomeia o eleitor que o programa quer ver formalizado, não um setor patronal nem uma classe "
        "abstrata. Regra nomeia o inimigo interno do próprio desenvolvimentismo: o balcão. A sigla "
        "não repete legenda real e não deve ser desenhada com estrela, tucano, número ou mapa do Brasil.",
    )

    h(doc, 1, "2. Conceito visual")
    p(
        doc,
        "A marca é um prumo cujo fio é um trilho. O prumo é a regra: a vertical que não pede "
        "licença ao terreno. O trilho é o país que anda: dormentes, obra, logística, repetição "
        "que chega ao destino. O losango cobre na ponta de baixo é o peso do prumo e, ao mesmo "
        "tempo, o metal do trabalho — cobre de fio, de mineração legal, de ferramenta. Não é "
        "gota, não é pin de mapa, não é escudo de brasão e não é diamante de luxo. A mensagem "
        "simbólica desejada é retidão mais movimento. O que a marca não deve dizer: agressividade, "
        "salvação religiosa, militarismo, festa, natureza genérica em folha, punho cerrado.",
    )

    h(doc, 1, "3. Símbolo — o que entra e o que não entra")
    p(doc, "Entram apenas quatro formas, nesta ordem de desenho:")
    numbered(
        doc,
        [
            "Uma barra vertical azul-marinho, centrada, largura de 7,5% do lado do quadrado de referência, começando a 14% do topo e terminando a 62% da altura.",
            "Um travessão horizontal azul-marinho mais longo, como dormente superior, centrado, comprimento de 52% do lado, espessura de 4,5%, centro vertical a 46% da altura. A barra vertical passa por cima e permanece contínua.",
            "Um travessão horizontal mais curto, dormente inferior, comprimento de 36% do lado, mesma espessura, centro vertical a 56% da altura.",
            "Um losango cobre imediatamente sob a barra. O vértice superior toca a base da barra. A largura do losango é 22% do lado. A cor do losango não é aplicada aos travessões.",
        ],
    )
    p(
        doc,
        "Não entram: estrela, cruz cristã, foice, martelo, tocha, animal, mapa, bandeira, mão, "
        "engrenagem, sol, folha, triângulo maçônico, coroa, fuzil, balança de tribunal, letras "
        "dentro do símbolo. A sigla mora fora do ícone, no lockup. Em tamanho muito pequeno, "
        "abaixo de 24 pixels, os dois travessões podem ser mantidos e o losango não pode sumir: "
        "ele é o único elemento cobre e o reconhecimento mínimo.",
    )

    h(doc, 1, "4. Composição geométrica")
    bullets(
        doc,
        [
            "Formato de referência do ícone: quadrado. O símbolo em si ocupa a área central com margem mínima de 12% em peças avulsas.",
            "Simetria: bilateral no eixo vertical. Não há simetria horizontal — o peso está embaixo de propósito.",
            "Orientação: a barra é vertical. Girar o símbolo 90 graus é uso proibido, porque vira marca abstrata sem prumo.",
            "Proporção dos travessões: o de cima é mais longo que o de baixo, na razão aproximada de 52 para 36. Inverter essa relação descaracteriza.",
            "Espaçamento interno: os travessões não encostam no losango. Há um intervalo claro entre o dormente inferior e o vértice do losango, preenchido só pela continuidade da barra.",
            "Margem de segurança externa: metade da largura da barra vertical, em todos os lados, sem texto, sem fio, sem foto invadindo.",
        ],
    )

    h(doc, 1, "5. Paleta")
    table(
        doc,
        ["Papel", "Nome", "HEX", "Uso"],
        [
            ["Principal", "Azul prumo", "#0B1F33", "Barra, travessões, sigla, fundos escuros institucionais"],
            ["Principal 2", "Cobre de obra", "#C4622D", "Losango, fio de separação, palavra PRESIDENTE no cartaz, destaques curtos"],
            ["Fundo claro", "Papel de mapa", "#F7F4EF", "Fundo de lockup, papel de peça impressa"],
            ["Fundo alternativo", "Areia", "#F3EBDD", "Caixas de citação, faixas secundárias"],
            ["Texto", "Tinta", "#14202B", "Texto corrido sobre fundo claro"],
            ["Apoio", "Cobre claro", "#E0A078", "Hover, linha terciária, aviso em fundo escuro"],
            ["Apoio raro", "Verde de campo", "#1E4D3A", "Apenas peças de meio ambiente e agro. Nunca cor dominante do partido"],
            ["Branco", "Branco de documento", "#FFFFFF", "Versão monocromática impressa e espaços vazios"],
        ],
    )
    p(
        doc,
        "Proibido como combinação principal: vermelho com amarelo, verde com amarelo, azul celeste "
        "com branco de legenda existente, laranja neon, magenta, dourado metálico brilhante. O verde "
        "#1E4D3A existe para não fingir que a Amazônia está fora do programa, e existe em dose baixa "
        "para a ATR não parecer um partido ecológico de uma causa só.",
    )

    h(doc, 1, "6. Tipografia")
    p(
        doc,
        "Fontes livres, para que a marca não dependa de licença paga. Sigla e nome: Liberation Sans, "
        "substituta métrica de uma grotesque humanista ampla. Se Liberation não estiver disponível: "
        "Nimbus Sans, Arimo ou outra sans de família próxima, nunca uma script e nunca uma serifada "
        "blackletter. Slogan: Liberation Serif em itálico. Pesos: sigla em negrito; nome por extenso "
        "em regular, caixa alta, espaçamento de rastreamento levemente aberto; slogan em itálico, "
        "caixa de frase, com o ponto final — «O Brasil no trilho.» O ponto é parte do slogan.",
    )
    p(
        doc,
        "Hierarquia no lockup horizontal: a sigla ATR é o maior elemento textual, alinhada à altura "
        "do topo óptico do símbolo. O nome por extenso vem abaixo, menor, e não compete com a sigla. "
        "Um fio cobre separa o nome do slogan. O slogan nunca vai em caixa alta e nunca em negrito "
        "sans. No lockup vertical, a ordem é símbolo, sigla, nome em duas linhas («ALIANÇA DO TRABALHO» "
        "/ «E DA REGRA»), fio, slogan. Ícone e texto não se sobrepõem.",
    )

    h(doc, 1, "7. Versões obrigatórias")
    bullets(
        doc,
        [
            "Logotipo horizontal: símbolo à esquerda, bloco tipográfico à direita. Uso principal em documento, púlpito largo e capa.",
            "Logotipo vertical: símbolo acima, texto centrado. Uso em rede social quadrada, camisa e estandarte.",
            "Ícone quadrado avulso: símbolo com margem sobre fundo #F7F4EF, sem letras. Uso em avatar e favicon.",
            "Monocromática: tudo preto sobre branco, ou tudo branco sobre preto. O losango permanece losango, só muda a cor. Uso em carimbo, fax, jornal e cópia simples.",
            "Fundo escuro: símbolo em papel #F7F4EF com losango ainda em #C4622D, texto claro, fio cobre. O losango não vira branco: ele é o acento que sobrevive no escuro.",
        ],
    )
    add_picture(doc, os.path.join(A, "atr_logo_horizontal.png"), 16, "Figura 1. Lockup horizontal canônico, desenhado por geometria e tipografia, não por gerador de imagem.")
    add_picture(doc, os.path.join(A, "atr_logo_vertical.png"), 10, "Figura 2. Lockup vertical canônico.")
    add_picture(doc, os.path.join(A, "atr_icone_quadrado.png"), 8, "Figura 3. Ícone quadrado sobre fundo de papel.")
    add_picture(doc, os.path.join(A, "atr_logo_horizontal_mono.png"), 16, "Figura 4. Versão monocromática para documento e impressão de uma tinta.")
    add_picture(doc, os.path.join(A, "atr_logo_horizontal_fundo_escuro.png"), 16, "Figura 5. Versão de fundo escuro. O losango permanece cobre.")

    h(doc, 1, "8. Legibilidade e consistência")
    p(
        doc,
        "Impressão: a espessura mínima da barra não pode cair abaixo de 0,6 mm em offset. Abaixo "
        "disso, usar só o ícone monocromático, sem slogan. Rede social: o ícone quadrado precisa "
        "ser reconhecível a 64 pixels; testar antes de publicar avatar. Documento Word: preferir "
        "o lockup horizontal com largura mínima de 8 cm, ou a sigla ATR em Liberation Sans negrito "
        "quando a arte não couber. Miniatura: se só houver 16 pixels, publicar as letras ATR, não "
        "uma redução ilegível do símbolo. Peça de campanha: o cartaz reserva a faixa inferior "
        "inteira para nome, cargo, slogan e sigla, com o símbolo à esquerda e nunca sobre o rosto.",
    )
    p(doc, "Usos proibidos:")
    bullets(
        doc,
        [
            "Trocar o azul-marinho por preto no material colorido, ou o cobre por dourado metálico.",
            "Aplicar sombra, gradiente, relevo 3D ou contorno branco grosso.",
            "Colocar o símbolo sobre fotografia sem uma área chapada de respiro.",
            "Distorcer a proporção para caber num botton oval.",
            "Combinar a marca com bandeira nacional de modo a simular chancela oficial da República ou do TSE.",
            "Acrescentar estrela, folha ou engrenagem «para completar».",
            "Usar a marca em peça que não diga, em algum lugar visível, que se trata de simulação fictícia, quando a peça circular fora do experimento.",
        ],
    )
    p(
        doc,
        "Arquivo vetorial de referência, para reprodução manual fiel: atr_simbolo.svg, neste "
        "pacote. Quem redesenhar deve seguir os quatro passos da seção 3 e conferir as cores "
        "#0B1F33 e #C4622D. Letras da sigla devem ser digitadas em editor, não traçadas à mão "
        "e não pedidas a gerador de imagem como única fonte.",
    )

    h(doc, 1, "9. Prompts de logomarca")
    p(
        doc,
        "Os quatro prompts abaixo são independentes. Cada um repete a geometria. Nenhum pede "
        "«a mesma logo de antes». Se o gerador errar a letra, descartar o texto e compor a sigla "
        "depois. A versão canônica deste experimento é a desenhada por código e já reproduzida "
        "nas figuras, não a saída eventual de um gerador.",
    )
    h(doc, 2, "Prompt A — logotipo principal")
    callout(
        doc,
        "Logotipo horizontal vetorial, fundo transparente ou papel #F7F4EF, sem sombra e sem 3D. À esquerda, símbolo geométrico: barra vertical grossa na cor #0B1F33; dois travessões horizontais da mesma cor cruzando a parte inferior da barra, o de cima mais longo que o de baixo; sob a barra, um losango sólido #C4622D cujo vértice de cima toca a barra. À direita, sem sobrepor o símbolo, a sigla ATR em sans-serif negrito, caixa alta, cor #0B1F33, e abaixo o nome ALIANÇA DO TRABALHO E DA REGRA em sans-serif regular, caixa alta, tamanho bem menor. Um fio horizontal #C4622D. Abaixo, o slogan em itálico serifado: O Brasil no trilho. Margens amplas, aparência de manual de marca, não de ilustração. Se as letras saírem tortas, omitir todo o texto e entregar só o símbolo. Negativo: estrela, mapa do Brasil, bandeira, animal, folha, engrenagem, gradiente, brasão, texto ilegível, partido real.",
    )
    h(doc, 2, "Prompt B — símbolo isolado")
    callout(
        doc,
        "Ícone quadrado, símbolo centrado, margem larga, fundo #F7F4EF. Apenas a marca geométrica: barra vertical #0B1F33, dois dormentes horizontais #0B1F33 com o superior mais longo, losango #C4622D encostado embaixo da barra. Limpo, chapado, reconhecível em tamanho pequeno, sem letras, sem sombra, sem textura. Negativo: qualquer palavra, qualquer estrela, qualquer mapa, 3D, photorealismo, moldura ornamental.",
    )
    h(doc, 2, "Prompt C — versão monocromática")
    callout(
        doc,
        "A mesma geometria do símbolo — barra vertical, dois travessões horizontais de comprimentos diferentes, losango embaixo tocando a barra — inteiramente em preto sólido sobre fundo branco. Ao lado, a sigla ATR em preto, sans-serif negrito. Adequado para impressão de uma tinta e para documento jurídico. Sem cinza decorativo, sem cobre, sem textura de papel fotográfico. Se a letra falhar, entregar só o símbolo preto. Negativo: cor, gradiente, fotografia, bandeira.",
    )
    h(doc, 2, "Prompt D — aplicação em painel de campanha fictício")
    callout(
        doc,
        "Fotografia de um púlpito simples de campanha fictícia em salão brasileiro genérico, luz de auditório, sem multidão identificável. No painel frontal, fundo azul-marinho #0B1F33. No centro do painel, o símbolo exato: barra vertical e dois travessões em cor de papel #F7F4EF, losango em cobre #C4622D sob a barra. Abaixo do símbolo, área lisa reservada para texto, sem letras geradas. Não alterar a geometria, não acrescentar estrela nem bandeira do Brasil, não simular órgão oficial. Clima sóbrio, não festivo. Negativo: texto corrompido, logo de partido real, faixa presidencial, rosto de pessoa real, armas, fogos de artifício.",
    )

    h(doc, 1, "10. Relação entre marca e retrato")
    p(
        doc,
        "O rosto de Elias nunca recebe o símbolo pintado na pele, na lapela em tamanho de broche "
        "gigante ou no lugar de uma cicatriz. Em peça combinada, o retrato ocupa a zona superior "
        "e a marca ocupa a faixa inferior, como no cartaz de referência do volume 02. Lúcia Okamoto "
        "usa a mesma marca, sem variante «feminina» e sem cor extra. Duas marcas para a mesma chapa "
        "seriam duas campanhas.",
    )
    save(doc, os.path.join(OUT, "03_IDENTIDADE_VISUAL_PARTIDO.docx"))


if __name__ == "__main__":
    vol01()
    vol02()
    vol03()
    print("volumes 01-03 ok")
