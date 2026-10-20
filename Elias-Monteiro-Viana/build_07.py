# -*- coding: utf-8 -*-
"""Volume 07 — política externa."""
import os, sys
sys.path.insert(0, "/workspace/candidatura")
from docx_theme import bullets, cover, h, new_doc, p, save, table

OUT = "/workspace/candidatura/docx"


def build():
    doc = new_doc()
    doc.core_properties.title = "07 — Política externa — Elias Monteiro Viana"
    cover(
        doc,
        "VOLUME 07",
        "Política externa e geopolítica",
        "Autonomia que cabe no interesse brasileiro. Nem alinhamento automático, nem equidistância cínica diante de civil morto.",
    )
    h(doc, 1, "1. Doutrina em uma página")
    p(
        doc,
        "O Brasil não é potência militar global e é potência agroalimentar, ambiental e diplomática "
        "média. A política externa de Elias Viana se chama autonomia de interesse. Comércio com "
        "Estados Unidos, China e União Europeia ao mesmo tempo. Recusa de base militar estrangeira "
        "e de moeda comum. Recusa de reconhecer conquista territorial pela força. Condenação de "
        "ataque deliberado a civil, venha de Estado ou de grupo armado. Mediação quando as partes "
        "pedirem e quando o Brasil tiver canal, não quando a foto for boa. Sanção só com base "
        "jurídica clara, de preferência multilateral; sanção unilateral alheia não é lei brasileira. "
        "Itamaraty executa; presidência não faz política externa por rede social.",
    )
    p(
        doc,
        "Os fatos de outubro de 2026 que condicionam o texto: guerra na Ucrânia em impasse, sem "
        "tratado de paz; Gaza em cessar-fogo formal desde 10 de outubro de 2025, com violência "
        "continua, reféns daquele ciclo inicial já libertados, Hamas não desarmado e Israel no "
        "controle da maior parte da faixa; tarifas americanas já tendo reduzido exportação brasileira "
        "aos Estados Unidos em 2025. O que mudar depois da data-base muda a tática e não a doutrina, "
        "salvo se um fato novo cair numa das cláusulas de revisão do volume 01 — nenhuma delas é "
        "sobre bandeira estrangeira, e a revisão externa obedecerá a evidência, não a torcida.",
    )

    h(doc, 1, "2. Relações bilaterais")
    h(doc, 2, "Estados Unidos")
    p(
        doc,
        "Parceiro comercial, científico e militar ocasional, não aliado automático. O governo "
        "negociará a remoção das tarifas que atingiram a exportação em 2025 como contencioso de "
        "interesse, não como prova de lealdade. Cooperação em defesa fica em exercício e em "
        "compra pontual, sem status de aliado extrabloco e sem base. Tecnologia: o Brasil não "
        "aceita ser apenas mercado de nuvem nem entrará em bloqueio tecnológico contra a China "
        "que destrua a cadeia do agronegócio e da indústria sem ganho de segurança concreto. "
        "Onde o dado for sensível de Estado, vale o eixo 14. Democracia americana é assunto dos "
        "americanos; o Brasil não dá palpite de campanha e espera o mesmo."
    )
    h(doc, 2, "China")
    p(
        doc,
        "Principal destino comercial e fonte de investimento em infraestrutura. O investimento "
        "continua bem-vindo fora da lista sensível do comitê do eixo 19. Dentro da lista — porto "
        "junto a instalação militar, núcleo de telecom, controle de transmissão, mineral crítico, "
        "dado de Estado — há escrutínio, não veto étnico. O Brasil não endossa repressão, não "
        "finge que não existe, e não a transforma em condição única de compra de alimento, porque "
        "não tem com o que substituir esse mercado de um ano para o outro. A dependência se reduz "
        "abrindo a União Europeia e o próprio mercado interno de processamento, não com discurso "
        "de desacoplamento."
    )
    h(doc, 2, "Rússia")
    p(
        doc,
        "A invasão da Ucrânia violou a Carta da ONU. O Brasil não reconhece anexação, não manda "
        "arma para nenhum dos lados e não adere a sanção unilateral americana ou europeia que não "
        "tenha base no direito brasileiro ou em decisão do Conselho de Segurança que o país tenha "
        "apoiado. Cooperação agrícola e de fertilizante, onde não esbarrar em proibição legal "
        "vigente, não é aplauso a Moscou. Exercício militar conjunto que sirva de palanque de "
        "guerra não será agenda deste mandato. Soberania russa dentro das fronteiras reconhecidas "
        "não está em disputa; soberania russa sobre território ucraniano ocupado está."
    )
    h(doc, 2, "União Europeia")
    p(
        doc,
        "Acordo comercial: concluir, se o texto na mesa servir, com cláusula ambiental que coopere "
        "em vez de sancionar de modo automático e unilateral. O desmatamento brasileiro em queda "
        "é argumento de boa-fé e não é salvo-conduto. Direitos humanos entram em diálogo político, "
        "não em lição de uma via: o Brasil também perguntará sobre migrante e sobre o padrão "
        "industrial europeu quando a régua vier só contra o produtor tropical."
    )
    h(doc, 2, "Índia")
    p(
        doc,
        "Prioridade subaproveitada. O mandato abre negociação setorial em fármaco, software, "
        "alimento e defesa civil, e trata a Índia como sócio de peso no Brics sem aceitar que o "
        "Brics vire bloco antiocidental ou união monetária. Não há ilusão de atalho: acesso indiano "
        "é difícil, e o Itamaraty será cobrado por acordo pequeno e real, não por cúpula."
    )
    h(doc, 2, "Argentina")
    p(
        doc,
        "Vizinho incontornável. Mercosul permanece, com flexibilidade para acordo extra-bloco que "
        "hoje a regra de consenso muitas vezes impede. Fronteira: cooperação policial contra "
        "contrabando e facção, sem militarização política do relacionamento. Crise econômica "
        "argentina não será financiada pelo Tesouro brasileiro. Comércio em moeda local pode "
        "continuar de modo pontual, sob o Banco Central, se o risco de câmbio estiver na conta "
        "e não no contribuinte."
    )
    h(doc, 2, "Venezuela")
    p(
        doc,
        "O governo venezuelano, na leitura deste programa, concentra poder, reprime oposição e "
        "produziu êxodo. O Brasil não rompe o canal consular que protege brasileiro e migrante, "
        "não reconhece eleição sem condição mínima de competição quando essa for a evidência "
        "técnica disponível na posse, e não participa de intervenção militar. Migração: visto "
        "humanitário com checagem de identidade, acolhimento na fronteira com capacidade real e "
        "recusa de discurso que trate venezuelano como criminoso por nacionalidade. Sanção "
        "brasileira ampla que só encareça a vida do civil sem tocar quem decide não será o "
        "instrumento preferido; restrição a oficial envolvido em repressão grave, sim."
    )
    h(doc, 2, "Cuba")
    p(
        doc,
        "Embargo americano de alcance extraterritorial não é política brasileira. Autoritarismo "
        "cubano não é detalhe romântico. O Brasil manterá relação diplomática, cooperação de "
        "saúde se houver interesse mútuo e transparência, e voto a favor de resolução que condene "
        "preso político quando o texto for sobre preso político — não quando o texto for apenas "
        "instrumento de um dos polos. Não haverá financiamento público brasileiro a projeto sem "
        "prestação de contas."
    )
    h(doc, 2, "Irã")
    p(
        doc,
        "Relação diplomática mantida. Programa nuclear: o Brasil defende inspeção internacional "
        "efetiva e se opõe a arma nuclear iraniana, como se opõe a proliferação em geral. Não "
        "entrará em operação militar alheia contra instalação iraniana. Comércio que esbarre em "
        "sanção do Conselho de Segurança será cumprido; sanção unilateral será analisada caso a "
        "caso pelo direito brasileiro, sem heroísmo e sem obediência automática."
    )
    h(doc, 2, "África")
    p(
        doc,
        "Cooperação Sul-Sul deixa de ser frase de cúpula e vira pauta agrícola, de saúde e de "
        "ensino técnico, com embaixada cobrada por resultado de comércio e por proteção a "
        "brasileiro. Não há corrida contra a China no continente com cheque do Tesouro. Há "
        "presença diplomática estável e acordo fitossanitário que abra mercado aos dois lados. "
        "Golpe de Estado não recebe reconhecimento apressado; governo que torture não recebe "
        "elogio de irmandade."
    )
    h(doc, 2, "Oriente Médio e Indo-Pacífico")
    p(
        doc,
        "Interesse brasileiro: óleo e preço de energia, mercado, paz que não expulse gente, e "
        "liberdade de navegação. O Brasil não escolhe patrono regional. Com Israel, relação "
        "plena, comércio de tecnologia e condenação de terror contra civil. Com palestinos, "
        "apoio à autodeterminação e ajuda humanitária, sem confundir povo com Hamas. No "
        "Indo-Pacífico, apoio à liberdade de navegação e à solução pacífica no Estreito de Taiwan, "
        "sem reconhecimento de independência taiwanesa e sem aceitar bloqueio ou invasão como fato "
        "consumado. Estabilidade dessa rota também é estabilidade de semicondutor, do qual o "
        "Brasil é comprador."
    )

    h(doc, 1, "3. Organizações")
    table(
        doc,
        ["Foro", "Posição do mandato"],
        [
            ["ONU", "Permanecer. Defender reforma do Conselho de Segurança que amplie membros permanentes e não permanentes, com o Brasil como candidato a permanente apenas se o novo desenho não reproduzir o veto irresponsável. Enquanto o veto existir como está, o Brasil não finge que uma cadeira resolve a Ucrânia ou Gaza."],
            ["Brics", "Permanecer. Recusar moeda comum. Aceitar banco de desenvolvimento quando o projeto tiver análise de crédito e não for política disfarçada. Expansão do grupo não é vitória automática: cada novo membro será lido pelo que faz com civil e com regra comercial."],
            ["Mercosul", "Manter a união aduaneira com cláusula de flexibilidade para acordo externo. Sem isso, o bloco continua protegendo pouco e impedindo muito."],
            ["OMC", "Usar o contencioso. Apoiar reforma do órgão de apelação, hoje emperrado, porque regra comercial sem juiz vira tarifa do mais forte."],
            ["FMI e Banco Mundial", "Usar assistência técnica e linha de crédito se um dia forem necessárias, sem programa de ajustamento humilhante e sem tratá-los como inimigos. O Brasil na data-base não precisa de resgate e o mandato trabalhará para continuar não precisando."],
            ["Otan", "Não aderir e não pedir parceria que seja adesão disfarçada. A Otan é aliança do Atlântico Norte; o Brasil não é membro geográfico nem estratégico. Diálogo pontual não é filiação."],
            ["G20", "Pauta de dívida, fome e clima com número, não com comunicado. O Brasil cobra dos outros o que cobra de si: meta fiscal dita em voz alta e floresta medida por satélite."],
        ],
        font=8,
    )

    h(doc, 1, "4. Conflitos")
    p(
        doc,
        "Para cada conflito, a mesma grelha: fato e direito, posição oficial, condenação, "
        "instrumento, voto e interesse. População civil não é governo, governo não é grupo armado, "
        "grupo armado não é o povo.",
    )

    h(doc, 2, "Rússia e Ucrânia")
    p(
        doc,
        "Interpretação. A invasão em larga escala iniciada em 2022 violou o artigo 2(4) da Carta. "
        "A ocupação e as anexações, inclusive a Crimeia desde 2014 e os territórios orientais e "
        "meridionais reivindicados por Moscou, não criam título jurídico. Há crime de guerra a "
        "investigar de todos os lados quando o alvo for civil; a responsabilidade de começar a "
        "guerra não se reparte pela metade. Em outubro de 2026 o conflito seguia em impasse, com "
        "negociação intermitente e sem tratado.",
    )
    p(
        doc,
        "Posição oficial. Integridade territorial da Ucrânia dentro das fronteiras reconhecidas "
        "internacionalmente. Cessar-fogo útil é o que não consolida conquista à força. O Brasil "
        "pode oferecer canal, inclusive para arranjo de segurança recíproca, se Kiev e Moscou "
        "pedirem. Não imporá plano feito em Brasília.",
    )
    p(
        doc,
        "Condenação. Condena a invasão e o ataque a infraestrutura civil quando o fato estiver "
        "estabelecido. Condena também ataque ucraniano que atinja civil russo de modo "
        "indiscriminado, se comprovado, sem equacionar isso à invasão. Não condena o povo russo "
        "nem a existência do Estado russo.",
    )
    p(
        doc,
        "Instrumento. Não envia arma nem tropa. Ajuda humanitária, sim, pelos canais que cheguem "
        "a civil. Não adere a sanção unilateral extraterritorial. Cumpre sanção decidida pelo "
        "Conselho de Segurança. Não reconhece mudança de fronteira imposta.",
    )
    p(
        doc,
        "Voto. A favor de resolução de Assembleia Geral que reafirme a integridade territorial "
        "ucraniana, peça retirada de forças e peça proteção de civil, desde que o texto não "
        "inclua autorização aberta de uso da força por coalizão ad hoc nem transferência obrigatória "
        "de arma. Abstenção ou voto contrário se o texto for apenas punitivo de um povo inteiro, "
        "sem nexo com a agressão, ou se reconhecer anexação. No Conselho, se o Brasil lá estiver "
        "como eleito, o mesmo critério: sem veto cínico a texto humanitário e sem voto a texto "
        "que transforme o Brasil em parte.",
    )
    p(
        doc,
        "Interesse. Fertilizante, preço de alimento, princípio de fronteira — o mesmo princípio "
        "que o Brasil invoca na própria Amazônia — e recusa de um mundo em que a força reescreve "
        "mapa. Mandar arma não protege esse interesse; apaga a possibilidade de falar com os dois."
    )

    h(doc, 2, "Israel e Palestina")
    p(
        doc,
        "Interpretação. Israel é Estado soberano com direito a existir e a se defender. Os "
        "palestinos são povo com direito à autodeterminação. Ocupação, colonização de assentamento "
        "na Cisjordânia e controle prolongado de território palestino não criam, por si, solução "
        "de segurança. O ataque do Hamas em 7 de outubro de 2023 contra civis e a tomada de reféns "
        "foram crimes. A guerra subsequente em Gaza produziu destruição de escala civil incompatível "
        "com uma leitura indiferente do direito humanitário. O cessar-fogo de outubro de 2025 não "
        "encerrou a questão: um ano depois, a violência seguia, o desarmamento do Hamas não ocorrera "
        "e mortes de palestinos, inclusive crianças segundo o Unicef, continuavam sendo reportadas.",
    )
    p(
        doc,
        "Posição oficial. Solução de dois Estados, com fronteira negociada a partir das linhas de "
        "1967 e trocas acordadas, Jerusalém como assunto de negociação final e não de decreto "
        "unilateral celebrado em Brasília, segurança de Israel e Estado palestino viável. O Brasil "
        "não retira reconhecimento previamente concedido a Estado palestino, se vigente na posse, "
        "e não transforma reconhecimento em salvo-conduto para grupo armado.",
    )
    p(
        doc,
        "Condenação. Condena o Hamas pelo massacre e pelos reféns. Condena assentamento que torne "
        "o segundo Estado impossível. Condena ataque indiscriminado e deslocamento forçado de civil "
        "palestino, e condena ataque indiscriminado a civil israelense. Não condena a existência "
        "de Israel. Não condena o povo palestino.",
    )
    p(
        doc,
        "Instrumento. Ajuda humanitária a civil de Gaza e da Cisjordânia, com corredor que não "
        "seja controlado pelo Hamas como autoridade fiscal do socorro. Diálogo com o governo de "
        "Israel e com a Autoridade Palestina. Sem arma brasileira para qualquer parte. Sem sanção "
        "comercial ampla contra o conjunto de Israel, que puniria trabalhador e não assentamento; "
        "sem sanção que confunda Gaza inteira com o comando do Hamas. Restrição a indivíduo "
        "responsável por terror ou por grave violação, quando houver base jurídica, sim.",
    )
    p(
        doc,
        "Voto. A favor de texto que reafirme dois Estados, condene terror contra civil, exija "
        "acesso humanitário e peça fim de expansão de assentamento. Contrário a texto que negue "
        "o direito de Israel existir ou que trate todo israelense como alvo legítimo. Contrário "
        "a texto que trate todo palestino como associado ao Hamas. Abstenção quando o parágrafo "
        "operativo for apenas retórico e já tiver sido usado para evitar medida prática sobre "
        "refém, ajuda ou cessar-fogo verificável.",
    )
    p(
        doc,
        "Interesse. Comunidade, comércio, energia e o precedente humanitário. Não há interesse "
        "nacional em importar o conflito para a política doméstica brasileira nem em escolher "
        "dias de luto conforme a nacionalidade do civil."
    )

    h(doc, 2, "Hamas")
    p(
        doc,
        "O Hamas é organização armada e estrutura política autoritária em Gaza, não é sinônimo "
        "de palestino. Seus ataques a civis e a tomada de reféns são crimes. Mesmo com os reféns "
        "daquele ciclo libertados na fase inicial do cessar-fogo de 2025, o desarmamento não "
        "ocorreu. Posição: o Brasil não dialoga com o Hamas como se fosse governo legítimo de um "
        "Estado. Pode apoiar arranjo internacional de desarmamento e de administração civil "
        "transitória se as partes e os árabes envolvidos o propuserem. Não há negociação brasileira "
        "direta para legitimar o grupo. Condenação específica do método — foguete sobre civil, "
        "escudo humano se comprovado, execução de opositor palestino. Voto: a favor de texto que "
        "exija desarmamento e cessar de ataque a civil; contra texto que autorize punição coletiva "
        "da população de Gaza."
    )

    h(doc, 2, "Hezbollah")
    p(
        doc,
        "Grupo armado com poder de fato no Líbano e histórico de ataque a civil e de guerra com "
        "Israel, distinto do Estado libanês e do povo libanês. Em 2026 a violência na fronteira "
        "libanesa foi reportada como elevada. Posição: apoiar as instituições libanesas na medida "
        "em que existam, condenar o arsenal paralelo e o ataque a civil de qualquer lado, não "
        "tratar bombardeio amplo de bairro como política de segurança. Sem tropa brasileira nova "
        "além do que uma missão da ONU já legalmente constituída preveja, e só com mandato claro "
        "do Congresso se houver força. Interesse: não deixar que o colapso libanês e a escalada "
        "regional virem choque de energia."
    )

    h(doc, 2, "Irã e Israel")
    p(
        doc,
        "Tensão entre Estados, com programa nuclear iraniano sob suspeita permanente e com ataques "
        "e retaliações já ocorridos em ciclos recentes. Interpretação: proliferação nuclear no "
        "Golfo é risco global; ataque preventivo também o é, porque normaliza guerra sem último "
        "recurso. Posição brasileira: inspeção, diplomacia, condenação de ataque a civil e de "
        "ameaça de aniquilação de Estado, recusa de participar de campanha militar. Voto a favor "
        "de texto que exija cumprimento de salvaguarda nuclear e que peça contenção militar; "
        "contra texto que seja autorização de guerra por procuração. Interesse: preço do óleo e "
        "recusa de um precedente nuclear fora das regras."
    )

    h(doc, 2, "China e Taiwan")
    p(
        doc,
        "O Brasil mantém a política de uma só China, que é a posição diplomática já estabelecida "
        "e que este mandato não reabre para agradar plateia. Integridade territorial chinesa, "
        "nesse marco, não inclui o direito de resolver o Estreito por invasão ou bloqueio. "
        "Autodeterminação de Taiwan não será reconhecida como independência unilateral. Posição: "
        "solução pacífica, sem alteração do status quo pela força, liberdade de navegação, "
        "preocupação explícita com a cadeia de semicondutores. Condenação de uso da força se "
        "ocorrer, venha como desembarque ou como bloqueio que impeça alimento e medicina. Sem "
        "arma brasileira e sem sanção automática copiada de Washington. Voto a favor de texto "
        "que peça paz e comércio de estreito aberto; contra texto que declare independência "
        "taiwanesa ou que autorize uma potência a arbitrar o estreito com frota em nome do Brasil. "
        "Interesse: chip, comércio com a China e precedente de força."
    )

    h(doc, 2, "Outros focos")
    bullets(
        doc,
        [
            "Sudão: tratar como guerra civil com atrocidade contra civil, não como tabuleiro distante. Apoio a cessar-fogo humanitário, a investigação de massacre e a ajuda. Sem tropa. Voto conforme o texto proteja civil e acesso, e não conforme o patrono regional de cada general.",
            "Iêmen: condenar ataque a civil por todas as partes e ataque a navegação que encareça o comércio mundial. Apoiar a liberdade de rota. Sem adesão a coalizão militar.",
            "Haiti: a crise de gangues é humanitária e de segurança. O Brasil só entra em missão com mandato da ONU, comando claro, regra de engajamento e autorização do Congresso. Não repetirá presença longa sem critério de saída. Apoio a polícia haitiana e a sanção de quem arme gangue é preferível a ocupação sem fim.",
            "América Latina: não reconhecer ruptura constitucional. Não organizar cerco que produza migração em massa sem acolhimento. Não usar o BNDES como política externa de amizade.",
        ],
    )

    h(doc, 1, "5. Como os princípios se conciliam com o interesse")
    p(
        doc,
        "Há tensão real, e o programa não a chama de equilíbrio para fugir dela. O interesse "
        "comercial com a China é maior, no curto prazo, do que o interesse comercial com qualquer "
        "sermão sobre direitos. Ainda assim, o Brasil não votará a favor de texto que trate "
        "invasão de Taiwan como assunto interno indiferente, porque o dia em que a força valer "
        "no Estreito ela vale na fronteira de quem for fraco. O interesse em fertilizante russo "
        "não compra reconhecimento de oblast anexado. O interesse em tecnologia israelense não "
        "compra silêncio sobre criança morta em Gaza, e o horror a essa morte não compra o "
        "apagamento de israelense morto em festival ou em kibutz. Quando o princípio e o contrato "
        "baterem, o contrato lícito continua e o voto não mente. Quando o contrato depender de "
        "mentira sobre fronteira ou sobre civil, o contrato é que cede.",
    )
    p(
        doc,
        "Probabilidade de êxito diplomático visível em quatro anos: moderada-baixa. Política "
        "externa deste porte não produz troféu. Produz ausência de desastre — mercado que não "
        "fecha, fronteira que não é reconhecida como moeda de troca, e um Itamaraty que ainda "
        "pode telefonar para os dois lados. Esse é o critério de sucesso do eixo, e ele está "
        "escrito para não ser confundido com aplauso de cúpula.",
    )
    save(doc, os.path.join(OUT, "07_POLITICA_EXTERNA.docx"))
    print("vol 07 ok")


if __name__ == "__main__":
    build()
