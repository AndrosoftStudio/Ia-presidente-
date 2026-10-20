# -*- coding: utf-8 -*-
"""Volume 06 — eixos 11 a 20."""
import os, sys
sys.path.insert(0, "/workspace/candidatura")
from docx_theme import cover, eixo, new_doc, p, save

OUT = "/workspace/candidatura/docx"


def build():
    doc = new_doc()
    doc.core_properties.title = "06 — Plano de governo 2027–2030, eixos 11 a 20"
    cover(
        doc,
        "VOLUME 06",
        "Plano de Governo 2027–2030 — Elias Monteiro Viana",
        "Eixos 11 a 20. Terra, cidade, previdência, ciência, Estado, cultura, direitos, regiões, comércio e governabilidade política.",
    )
    p(
        doc,
        "Vale a mesma trava do volume 05: despesa discricionária nova em escala cheia só sai do "
        "papel se a lei de revisão das renúncias for aprovada. Os números de diagnóstico são os "
        "do volume 04 e não são reabertos aqui.",
    )

    eixo(doc, 11, "Agricultura e meio ambiente", {
        "diagnostico": (
            "A agropecuária cresceu 11,7% em 2025 e segue como pilar externo do país. O desmatamento "
            "por corte raso na Amazônia caiu a 3.335 km² no ciclo 2025/2026, menor marca desde 1988, "
            "e o Cerrado a 5.516 km², menor desde 2001. Pará ainda concentrou 1.130 km². O Prodes "
            "não mede toda degradação nem todo fogo. O cadastro ambiental rural segue, há anos, "
            "mais rápido na declaração do que na validação. Terra indígena homologada não é terra "
            "sem gente em volta, e terra pública não destinada continua sendo o convite ao grileiro. "
            "Agricultura familiar e agronegócio de exportação não são o mesmo sujeito e não serão "
            "tratados como um único inimigo ou um único herói."
        ),
        "objetivo": (
            "Desmatamento ilegal próximo de zero em 2030, sem tratar produtor legal como suspeito "
            "permanente. Validar o cadastro ambiental. Concluir demarcação já instruída tecnicamente. "
            "Nenhuma mineração em terra indígena. Crédito rural que cobre quem produz e punição que "
            "chegue a quem desmata e ainda exporta."
        ),
        "propostas": [
            "Manter e apertar a meta de desmatamento ilegal zero até 2030, com o corte raso amazônico como indicador público semestral e um indicador separado de degradação assim que o Inpe consolidar a série — o programa não inventa esse segundo número hoje. Operação de fiscalização continua permanente, não sazonal de coletiva de imprensa.",
            "Força-tarefa de validação do Cadastro Ambiental Rural até 2028, com meta de estoque publicada por estado. Estado que não validar não perde o produtor legal; perde prioridade de convênio ambiental voluntário. O produtor com cadastro validado e sem embargo recebe licença mais rápida. O produtor com embargo não recebe crédito oficial.",
            "Pagamento por serviço ambiental com verificação satelital, contrato curto e teto orçamentário. Não é renda universal da floresta. É pagamento a quem mantém área que poderia ser derrubada legalmente ou que está sob pressão, mediante prova. Escala cheia só com a trava fiscal.",
            "Terra indígena: concluir processos cuja instrução técnica já esteja publicada, no rito constitucional, sem atalho e sem recuo por pressão de bancada. Mineração dentro de terra indígena não será proposta. Infraestrutura que cruze área indígena só com consulta e com alternativa estudada — é o mesmo critério que segura a Ferrogrão até 2029.",
            "Reforma agrária: prioridade à destinação de terra pública já identificada e à regularização de ocupante pequeno de boa-fé. Desapropriação por descumprimento da função social permanece como instrumento constitucional, com processo, não com ocupação como etapa oficial. Anistia de desmatador recente não entra no plano.",
        ],
        "instrumento": (
            "Fiscalização e homologação são atos federais, a homologação por decreto depois do "
            "rito. Validação do cadastro depende de convênio com estados. Pagamento por serviço "
            "ambiental já tem lei-quadro; o programa fixa teto e verificação, por decreto e por "
            "dotação. Mudança de regra de mineração em terra indígena seria lei e emenda em alguns "
            "desenhos: este governo não a enviará."
        ),
        "prazo": (
            "Meta de 2030 para o ilegal. Validação massiva do cadastro até 2028. Primeiros contratos "
            "de pagamento por serviço em 2027, em piloto no arco do desmatamento. Relatório anual "
            "de processos indígenas instruídos e não concluídos, a partir de 2027, com nome da etapa "
            "que travou."
        ),
        "custo": (
            "Fiscalização reforçada e pagamento por serviço, na escala cheia, em torno de 0,05% do "
            "PIB. Piloto e fiscalização básica começam dentro do orçamento ambiental existente, "
            "reordenado contra divulgação espalhada. Crédito rural não é gasto primário quando é "
            "empréstimo que volta; subsídio de juros, se houver, entra na conta da renúncia e passa "
            "pela mesma revisão do eixo 2."
        ),
        "financiamento": (
            "Orçamento do meio ambiente, fundo já existente e trava fiscal para a escala. Embargo "
            "e multa não são tratados como receita certa."
        ),
        "indicador": (
            "Área de corte raso no Prodes, Amazônia e Cerrado, em queda até 2030, com 2030 abaixo "
            "de 1.000 km² na Amazônia como ambição — não como número que se finge já garantido, "
            "porque 3.335 km² em um ano de queda forte mostram quão longe ainda é o zero. Percentual "
            "de cadastro validado. Hectares de terra pública destinada com papel. Zero lavra nova "
            "autorizada em terra indígena."
        ),
        "riscos": (
            "Queda de desmatamento pode reverter com commodity alta e fiscalização frouxa num ano "
            "eleitoral futuro. O programa amarra a série semestral para dificultar o apagão de dado. "
            "Demarcação gera conflito local: o rito e a presença policial civil são a resposta, não "
            "a suspensão silenciosa dos processos. Pagamento por serviço pode ser capturado por "
            "grande proprietário se o desenho for burro; o piloto terá teto por beneficiário."
        ),
        "competencia": (
            "Floresta pública federal e terra indígena são da União. Licença estadual e zoneamento "
            "são do estado. O presidente não regulariza o país inteiro por decreto e não deve "
            "prometer isso. Crédito agrícola de banco público é federal e será usado como alavanca "
            "sobre quem tem embargo, isso sí é ato próprio."
        ),
    })

    eixo(doc, 12, "Habitação, cidades e saneamento", {
        "diagnostico": (
            "Em 2024 faltavam 5.773.983 moradias, 7,4% dos domicílios ocupados, com queda de 3,4% "
            "e ainda assim o menor número da série recente da Fundação João Pinheiro, não a solução. "
            "Quase três quartos desse déficit estavam em famílias até dois salários mínimos. Mulheres "
            "chefiavam 60,9%. A inadequação urbana subiu para 27,6 milhões de domicílios. Esgoto por "
            "rede chegava a 71,4% em 2025, contra 8,9% no rural; água de rede, a 86,1% no país e "
            "60,9% no Norte. O marco legal joga a universalização, cuja conta histórica é de centenas "
            "de bilhões até 2033, sobretudo para tarifa e capital privado. Tratar isso como obra só "
            "de Tesouro é mentira orçamentária."
        ),
        "objetivo": (
            "Reduzir o déficit habitacional sem reabri-lo pela porta da inadequação. Levar esgoto "
            "e água primeiro aonde a tarifa não fecha: Norte, periferia pobre e rural denso. "
            "Regularizar o que já é cidade antes de empurrar mais conjunto para longe do emprego."
        ),
        "propostas": [
            "Subsídio habitacional federal concentrado em famílias até dois salários mínimos, que são cerca de 74% do déficit. Faixa de renda média deixa de ser prioridade de dinheiro público novo e segue com financiamento de mercado e FGTS, sem perdão de dívida.",
            "Meta de regularização fundiária urbana (Reurb) com cartório e município: o governo federal paga assistência técnica e o ato registral do pobre, não o metro quadrado de luxo. Onde a casa existe e o papel não, papel é mais barato que unidade nova.",
            "Saneamento: garantia federal e subsídio de tarifa apenas nos contratos do Norte e de município pobre que o leilão puro não cobrir. A escolha do operador continua sendo do titular do serviço, em geral o município, sob a lei. A União não estatiza companhia estadual por ideologia nem a entrega por ideologia.",
            "Piloto de auxílio-aluguel, até 100 mil famílias, em regiões metropolitanas de aluguel caro, para déficit de quem não cabe em conjunto na periferia distante. Avaliação obrigatória em 2029 antes de qualquer ampliação. Se o aluguel local subir e capturar o auxílio, o piloto morre.",
        ],
        "instrumento": (
            "Minha Casa Minha Vida e FGTS já são instrumentos: o programa muda a régua de foco por "
            "lei e por regulamento. Reurb tem lei. Subsídio de saneamento cabe em contrato e em "
            "dotação. Auxílio-aluguel piloto é lei ordinária com teto de famílias e cláusula de morte."
        ),
        "prazo": (
            "Régua de subsídio na seleção de 2028. Pilotos de Reurb e de aluguel em 2027–2028. "
            "Garantias de saneamento ao longo do mandato, com pelo menos um contrato relevante na "
            "Amazônia legal até 2029, ou justificativa pública de por que o edital falhou."
        ),
        "custo": (
            "Subsídio focalizado de saneamento em torno de 0,08% do PIB na escala cheia, contingente. "
            "Auxílio-aluguel de 100 mil famílias é pequeno em ponto de PIB e grande em risco de "
            "desenho: cabe no piloto mesmo sem a escala cheia dos outros itens, com teto duro."
        ),
        "financiamento": (
            "FGTS para financiamento, Tesouro só no subsídio ao muito pobre e ao contrato que a "
            "tarifa não fecha. Não se cria contribuição habitacional nova sobre folha."
        ),
        "indicador": (
            "Déficit da Fundação João Pinheiro em queda adicional até a próxima leitura cheia, com "
            "foco medido na faixa até dois mínimos. Percentual de domicílios com esgoto adequado no "
            "Norte, série IBGE, em alta mais rápida do que a média nacional. Famílias tituladas na "
            "Reurb cofinanciada. Resultado do piloto de aluguel: queda de ônus excessivo de aluguel "
            "sem alta anormal do preço no bairro tratado, medido contra bairro de controle."
        ),
        "riscos": (
            "Construtora e prefeitura preferem conjunto novo, que se inaugura. A régua de regularização "
            "perderá disputa local se o dinheiro federal não for teimoso. Auxílio-aluguel pode inflacionar "
            "aluguel: por isso é piloto com morte programada. Saneamento concedido com tarifa alta "
            "demais para o pobre exige subsídio explícito, não desconto escondido que quebra a companhia."
        ),
        "competencia": (
            "Moradia popular é política federal indutora e execução municipal. Água e esgoto são do "
            "titular municipal ou de bloco regional. O presidente não liga o esgoto da casa e não "
            "deve visitar obra para anunciar ligação que o contrato não prevê."
        ),
    })

    eixo(doc, 13, "Previdência e assistência social", {
        "diagnostico": (
            "O Regime Geral fechou 2025 com déficit de R$ 320,9 bilhões, 5,7% acima de 2024. O "
            "regime próprio federal, com R$ 62,6 bilhões. A seguridade como um todo, R$ 392,1 bilhões. "
            "A população com menos de 30 anos encolheu 10,4% desde 2012, e o total de habitantes "
            "chegou a 212,7 milhões crescendo só 0,4% ao ano. Sem programas sociais, a extrema "
            "pobreza de 2024 teria sido 10%, não 3,5%. O BPC e o Bolsa Família não são o déficit "
            "previdenciário, mas a política social que a demografia e o mercado formal ainda não "
            "substituem. Uma reforma ampla no primeiro ano, com 8% das cadeiras, não passa e ainda "
            "paralisa o resto."
        ),
        "objetivo": (
            "Estabilizar o déficit do RGPS como proporção do PIB depois de 2028, não zerá-lo no "
            "mandato — quem prometer zerar mente. Cortar fraude e pagamento indevido. Manter o BPC "
            "vinculado ao salário mínimo. Manter o Bolsa Família com valor real preservado e cadastro "
            "limpo. Não desidratar a aposentadoria rural de quem de fato trabalhou a terra."
        ),
        "propostas": [
            "Plano de combate a benefício indevido do INSS, com prova de vida digital, cruzamento "
            "com óbito e com emprego formal, e meta publicada de valor cancelado que não volte por "
            "liminar em massa. O que for erro contra o segurado de boa-fé é corrigido com fila própria "
            "de até 60 dias, porque caça a fraude que pune o analfabeto digital não é reforma.",
            "Aposentadoria rural: manter a idade e o valor constitucional, exigir prova de atividade "
            "mais clara — cadastro, nota, sindicato, testemunha com responsabilidade — e separar "
            "fraude de roçado. Não haverá medida provisória de véspera cortando o benefício.",
            "BPC: manter um salário mínimo. Revisar o cadastro para cortar acúmulo irregular, não "
            "para reduzir o valor de quem tem direito. Qualquer desvinculação fica explicitamente "
            "fora deste mandato, por compromisso com a vice e por juízo de que o ganho fiscal não "
            "compensa o dano ao idoso e à pessoa com deficiência pobres.",
            "Bolsa Família: valor real preservado pela inflação. Recadastro de quem não cumpre "
            "condicionalidade de saúde e escola, com suspensão depois de oportunidade de retorno, "
            "não com corte sumário. Não se cria programa paralelo de transferência para disputar "
            "marca com o que já existe.",
            "Militares futuros: a mesma proposta do eixo de defesa, contribuição maior para quem "
            "entrar depois da lei. Servidor civil futuro já está no regime pós-reforma; o governo "
            "não reabre essa porta para afrouxar.",
        ],
        "instrumento": (
            "Fraude e cadastro são atos administrativos e, onde a lei impedir o cruzamento de dados, "
            "projeto curto de autorização com proteção da LGPD. Mudança de regra rural de prova é "
            "lei ou regulamento, conforme o que já estiver em decreto na data da posse — o governo "
            "não inventará requisito impossível por portaria. Desvinculação do BPC seria lei e talvez "
            "emenda: não será enviada."
        ),
        "prazo": (
            "Cruzamentos principais em 2027. Relatório semestral de benefício cancelado e de "
            "benefício restabelecido por erro. Regra de prova rural, se precisar de lei, no primeiro "
            "ano. Avaliação do efeito sobre o déficit do RGPS em proporção do PIB a cada ano, sem "
            "comemoração antes de 2028."
        ),
        "custo": (
            "Preservar BPC e Bolsa Família em termos reais custa o que a inflação e o mínimo "
            "impuserem, e essa conta entra na meta fiscal em vez de ser tratada como intocável "
            "invisível. A economia esperada com fraude é da ordem de 0,10% do PIB no cenário "
            "central, com intervalo largo: pode ser menos. O orçamento não gasta essa economia "
            "antes de ela aparecer no caixa."
        ),
        "financiamento": (
            "Receita previdenciária da formalização do eixo 3 e menor crescimento real automático "
            "do mínimo quando a meta estourar. Não há imposto previdenciário novo no mandato além "
            "do que a folha já contém e da contribuição de militar futuro."
        ),
        "indicador": (
            "Déficit do RGPS sobre PIB não superior, em 2030, ao de 2026, que será cravado como "
            "linha de base no primeiro mês com o número fechado do Tesouro. Percentual de benefícios "
            "cancelados que retornam por erro — se for alto, a operação está ruim e será revista. "
            "Extrema pobreza, na métrica do Banco Mundial usada pelo IBGE, sem reversão da queda "
            "estrutural de 2024 por causa de desenho deste governo."
        ),
        "riscos": (
            "Caça a fraude vira caça a pobre se o sistema for burro. A fila de correção de 60 dias "
            "é a trava, e pode falhar na ponta do município. Não fazer reforma estrutural deixa a "
            "dívida de longo prazo para o próximo mandato: este programa assume isso em voz alta "
            "no volume de autocrítica, em vez de prometer uma emenda que não tem voto."
        ),
        "competencia": (
            "INSS e BPC são federais. Assistência social de execução é municipal. O presidente não "
            "administra CRAS e não deve anunciar benefício no palanque antes do sistema reconhecer "
            "o direito, prática que produz exatamente a fila e o favor."
        ),
    })

    eixo(doc, 14, "Ciência, tecnologia e inteligência artificial", {
        "diagnostico": (
            "O país tem universidades capazes, um mercado digital grande e uma dependência dura de "
            "chip, nuvem e plataforma estrangeiros. Não tem, e não terá em quatro anos, fábrica de "
            "semicondutor de fronteira. A regulação de inteligência artificial ainda é disputa "
            "legislativa na data-base; o programa não finge que um marco único já resolveu o tema "
            "e não cita artigo de lei que não tenha confirmado. PISA e Ideb mostram que a base "
            "humana da inovação continua fraca: supercomputador sem aluno que calcule é vitrine."
        ),
        "objetivo": (
            "Capacidade pública de computação para pesquisa, formação em desenho de chip e software, "
            "regulação de inteligência artificial por risco, e soberania de dado sensível do Estado "
            "sem localizar à força todo dado privado. Inovação como produtividade, não como ministério "
            "de comunicado."
        ),
        "propostas": [
            "Cluster público de computação, contratado por licitação aberta, hospedado em universidade ou laboratório nacional já existente, com acesso por edital de pesquisa e não por amizade. Sem empresa estatal nova de inteligência artificial.",
            "Formação: 10 mil profissionais adicionais em trilha de semicondutor, verificação e software embarcado até 2030, via institutos federais e pós-graduação existente, número ambicioso e ainda assim mais honesto do que uma fab. Meta intermediária de 3 mil até 2028. Se a demanda das empresas não absorver, a meta de 2030 é revista para baixo em vez de produzir diploma oco.",
            "Lei de inteligência artificial, se ainda não estiver sancionada na posse, ou lei de ajuste, se estiver: abordagem por risco. Alto risco — decisão médica, crédito que nega sem recurso, investigação criminal, reconhecimento facial em espaço público — exige supervisão humana e recurso. Modelo de uso geral não precisa de licença prévia. Publicidade eleitoral sintética tem de ser rotulada. Sandbox regulatório para empresa pequena. Proibido órgão que classifique opinião lícita como desinformação punível.",
            "Nuvem: dados sensíveis da administração federal em ambiente com controle jurídico brasileiro. Sem obrigação de localizar no território todo dado de empresa privada. Compras públicas de software com padrão aberto sempre que houver alternativa madura, para não ficar refém de um fornecedor.",
        ],
        "instrumento": (
            "Cluster e bolsas: orçamento e lei de licitação. Regulação de IA: lei ordinária. "
            "Rotulagem eleitoral pode exigir ajuste na lei eleitoral, de competência do Congresso "
            "e com quórum próprio se tocar em regra eleitoral específica — o governo enviará o "
            "projeto e não a fará por decreto de véspera de eleição."
        ),
        "prazo": (
            "Edital do cluster em 2027, máquina em operação até 2029. Primeira turma da trilha de "
            "chip em 2027. Projeto de IA nos primeiros nove meses, ou projeto de correção nos "
            "primeiros cem dias se a lei já existir e contiver licença prévia de modelo geral — "
            "essa parte seria proposta para revogação."
        ),
        "custo": (
            "Cerca de 0,04% do PIB na escala cheia, somando compute e bolsas adicionais. É dos "
            "menores itens novos e um dos mais fáceis de proteger dentro do piso de pesquisa "
            "prometido no eixo de educação, corrigido pela inflação."
        ),
        "financiamento": (
            "FNDCT e dotações de ciência, com execução não contingenciada abaixo do piso real "
            "definido na lei orçamentária. Se o contingenciamento legal obrigar, o governo corta "
            "antes divulgação do que o cluster, e diz isso."
        ),
        "indicador": (
            "Horas de computação pública entregues a projeto selecionado por edital. Pessoas formadas "
            "na trilha e empregadas no setor dois anos depois. Existência de recurso humano efetivo "
            "nos sistemas públicos de alto risco que usem modelo estatístico. Percentual de peças "
            "eleitorais sintéticas flagradas sem rótulo, em queda depois da lei."
        ),
        "riscos": (
            "Cluster parado por briga de campus é o risco clássico: o edital terá uma sede, não "
            "cinco. Regulação de IA pode envelhecer em um ano; a lei precisa de revisão já marcada "
            "para 2029, não de princípio eterno. A meta de 10 mil pode virar caça a certificado: "
            "o indicador de emprego no setor existe para constranger essa saída."
        ),
        "competencia": (
            "Ciência federal é indução e universidades federais. O presidente não manda em currículo "
            "de universidade estadual nem em plataforma estrangeira além da lei que o Congresso "
            "aprovar e que o juiz aplicar. Bloqueio administrativo de conteúdo lícito não será "
            "instrumento deste governo."
        ),
    })

    eixo(doc, 15, "Administração pública e reforma do Estado", {
        "diagnostico": (
            "O governo geral gastou 45,79% do PIB em 2024. Parte relevante é proteção social e juro, "
            "não mordomia, e ainda assim a máquina federal reproduz trâmite, empresa estatal "
            "dependente e serviço digital que para na porta do município. Concurso virou, em muitos "
            "debates, sinônimo de solução ou de inimigo. Nenhuma das duas coisas. Correios, bancos "
            "públicos e Petrobras são alvos fáceis de frase e difíceis de substituir sem desenho. "
            "O programa nomeia o que não será privatizado e o que pode ser concedido."
        ),
        "objetivo": (
            "Estado menor no balcão e constante na fronteira, na escola técnica e na auditoria. "
            "Digital como padrão do serviço federal. Estatal com meta e sem Tesouro cativo, exceto "
            "subsídio explicitado em lei. Nenhuma privatização por lista ideológica."
        ),
        "propostas": [
            "Taxa de reposição abaixo de 100% nas carreiras administrativas de apoio da União, e de 100% em auditoria, Polícia Federal investigativa, professor e técnico de instituto federal, e carreira ambiental de fiscalização. Sem demissão em massa. Sem concurso genérico para «fortalecer o Estado» sem dizer qual fila o servidor novo vai encurtar.",
            "Serviço federal digital até 2029 para qualquer ato que não exija presença física por segurança ou perícia. Identidade digital única já em implantação será a porta, não um login novo por ministério.",
            "Petrobras permanece de economia mista. Banco do Brasil e Caixa permanecem públicos, com governança e sem crédito dirigido oculto. Correios não são privatizados neste mandato; têm contrato de resultado para deixar de depender de Tesouro, e a concorrência na entrega, já aberta pela lei, é mantida. Em 2029 o governo publica se o contrato funcionou e só então o próximo mandato decide venda. Participações minoritárias não estratégicas da União podem ser vendidas depois de avaliação do TCU.",
            "Concessão de autoridade portuária e ativo logístico já estudado, onde o serviço universal não esteja em jogo. Empresa estatal dependente — do tipo que só vive de repasse — entra em contrato de desempenho; quem não cumprir perde cargo de direção, não ganha subsídio maior."
        ],
        "instrumento": (
            "Reposição de pessoal é decreto de concursos e lei orçamentária. Venda de participação "
            "e concessão são lei existente de desestatização e licitação, com TCU. Privatização dos "
            "Correios exigiria lei específica: não será enviada neste mandato. Governança de estatal "
            "já tem lei; o ato próprio é cumpri-la na indicação, com critério técnico publicado."
        ),
        "prazo": (
            "Mapa de reposição em 90 dias. Plano digital em 2027, marco de 2029. Contrato de "
            "resultado dos Correios no primeiro ano. Lista de participações vendáveis em 180 dias, "
            "vendas só depois do TCU, ao longo do mandato."
        ),
        "custo": (
            "Digitalização bem feita custa investimento pequeno e evita custeio. Venda de participação "
            "é receita de uma vez, que não será usada para criar despesa permanente — vai para "
            "dívida ou para investimento já autorizado. Economia de transferência a estatal "
            "dependente: ambição de 0,05% do PIB até 2030, incerta."
        ),
        "financiamento": (
            "Orçamento administrativo e receita de alienação não recorrente, carimbada. Sem taxa "
            "nova sobre o cidadão para ser atendido no digital."
        ),
        "indicador": (
            "Percentual de serviços federais concluídos sem balcão. Transferência do Tesouro a "
            "estatais dependentes, em queda real. Tempo de nomeação de direção de estatal com o "
            "critério publicado antes do nome. Número de concursos de apoio vis-à-vis concursos "
            "das carreiras protegidas — a proporção tem de aparecer, para a promessa não virar "
            "discurso."
        ),
        "riscos": (
            "Reposição baixa em apoio pode paralisar agência se o corte for burro: a revisão anual "
            "do mapa existe para devolver vaga onde a fila crescer. Correios sem privatização e sem "
            "melhora continuarão deficitários; o contrato de 2029 é a prestação de contas, e o "
            "fracasso possível está assumido na autocrítica. Venda apressada de participação vira "
            "escândalo: por isso TCU antes do edital, mesmo que atrase o aplauso."
        ),
        "competencia": (
            "Administração federal é do presidente. Servidor estadual não é. Empresa municipal não é. "
            "O presidente indica ministro e diretor e responde por eles. Não indica juiz de tribunal "
            "de contas estadual e não deve negociar essa indicação como moeda."
        ),
    })

    eixo(doc, 16, "Cultura, turismo e esporte", {
        "diagnostico": (
            "Cultura brasileira é ativo econômico e simbólico que a política trata, em ciclos, como "
            "ornamento ou como trincheira. O mecanismo de incentivo fiscal concentra captura em "
            "grandes produções do eixo Rio–São Paulo. Patrimônio pequeno deteriora longe da câmera. "
            "Turismo depende de segurança, voo e visto mais do que de slogan de país bonito. Esporte "
            "de base vive de professor municipal; o de alto rendimento, de centro de treinamento "
            "que muitas vezes não conversa com a escola. Este eixo não tem um índice único de 2026 "
            "que o programa finja ter auditado. Tem prioridades."
        ),
        "objetivo": (
            "Incentivo cultural menos capturado, patrimônio de cidade média com obras pequenas e "
            "terminadas, turismo cobrado por permanência e por receita, esporte escolar medido por "
            "participação e não por medalha de discurso."
        ),
        "propostas": [
            "Lei Rouanet mantida, com teto por projeto e direcionamento de pelo menos 40% do valor incentivado a proponentes sediados fora do Rio de Janeiro e de São Paulo, sem excluir produção boa desses estados — a cota é de piso do restante do país, não de veto. Prestação de contas digital já exigida, com lista de quem captou e não executou.",
            "Fundo pequeno de restauração de patrimônio em município fora de capital, com obra de até um teto baixo, licitação curta e proibição de usar o recurso para centro cultural novo sem acervo e sem plano de custeio.",
            "Turismo: continuar a facilitação de visto quando o fluxo justificar, medir gasto por visitante e não só desembarque, e condicionar promoção internacional de destino à taxa de crime violento local publicada. Destino que esconde número não entra na campanha paga pela União.",
            "Esporte: dinheiro federal novo, se a trava permitir, vai para escola e para centro de treinamento já existente e subutilizado. Não se financia arena nova no mandato sem legado de uso público contratado. Atleta de rendimento segue com bolsa da lei, com meta de transparência do valor."
        ],
        "instrumento": (
            "Rouanet é lei: teto e cota regional pedem alteração legal. Patrimônio é convênio com "
            "município. Turismo e visto são atos do Executivo e, no visto, coordenação com a lei "
            "migratória. Arena é orçamento: o presidente pode não propor a verba."
        ),
        "prazo": (
            "Projeto da Rouanet no primeiro ano. Primeiras restaurações em 2028. Regra de promoção "
            "turística vinculada a crime violento em portaria no primeiro semestre."
        ),
        "custo": (
            "Este eixo não é onde o programa busca efeito macroeconômico. A cota regional da Rouanet "
            "realoca incentivo já existente; não o amplia. Restauração pequena cabe em dotação "
            "atual reordenada. Se alguém esperar ministério grande, este não é o plano."
        ),
        "financiamento": (
            "Renúncia já dada, com regra melhor, e orçamento cultural ordinário. Sem contribuição "
            "compulsória nova sobre ingresso."
        ),
        "indicador": (
            "Percentual do incentivo fora de Rio e São Paulo, meta de pelo menos 40% depois da lei. "
            "Número de obras de patrimônio concluídas sem aditivo superior a 25%. Gasto médio do "
            "visitante estrangeiro. Participação de aluno da rede pública em competição escolar "
            "estadual cofinanciada, publicada por unidade da federação."
        ),
        "riscos": (
            "Cota regional pode produzir projeto fraco só para cumprir percentual. O teto de qualidade "
            "mínima da aprovação técnica permanece; cota não dispensa parecer. Vincular turismo a "
            "crime pode punir cidade pobre que está melhorando e ainda assusta a tabela: a portaria "
            "olhará tendência de dois anos, não um mês ruim."
        ),
        "competencia": (
            "Cultura local é de município e de estado. A União incentiva e cuida do patrimônio "
            "federal. O presidente não cura o carnaval nem o campeonato e não deve tentar."
        ),
    })

    eixo(doc, 17, "Direitos civis e questões sociais", {
        "diagnostico": (
            "A Constituição já garante expressão, crença, igualdade perante a lei e proteção da "
            "criança. O que falta, em geral, não é declaração. É proteção que chega: mulher sob "
            "medida protetiva que não é cumprida, criança em exploração que a polícia não prioriza, "
            "pessoa com deficiência diante de prédio federal sem acesso, dado pessoal tratado como "
            "ativo de campanha. Em 2024, brancos recebiam 65,9% a mais do que pretos ou pardos. "
            "Isso não se resolve com um artigo novo e também não se nega com a palavra mérito."
        ),
        "objetivo": (
            "Liberdade de expressão sem ministério da verdade. Igualdade perante a lei com política "
            "social que mude escola, emprego e homicídio. Proteção de mulher e de criança com "
            "instrumento, não com data comemorativa. Laicidade sem humilhar crente."
        ),
        "propostas": [
            "Não criar tipo penal novo para opinião ofensiva. Manter os crimes já existentes de "
            "ameaça, racismo, calúnia e incitação à violência. Plataformas: dever de canal de "
            "denúncia para crime já tipificado, com ordem judicial para remoção de conteúdo lícito "
            "controverso. Transparência de anúncio eleitoral, inclusive o impulsionado por "
            "segmentação. Isso conversa com o eixo de inteligência artificial e não o repete como "
            "censura.",
            "LGPD: fortalecer a Autoridade Nacional com auditores, não criar agência paralela. "
            "Dado de cidadão em poder do governo federal não pode ser usado em campanha; a violação "
            "é falta grave do servidor, proposta em lei se a falta administrativa vigente for fraca.",
            "Mulheres: o pacote de feminicídio do eixo 6, mais a exigência de que empresa média e "
            "grande contratada pela União publique diferencial salarial por sexo em cargo equivalente. "
            "Não é teto salarial decretado. É luz. Creche entra como política de emprego e de "
            "aprendizagem, coordenada com o eixo de educação, não como favor setorial.",
            "Criança: prioridade da Polícia Federal à exploração sexual e à rede de abuso de imagem, "
            "com cooperação internacional já prevista em tratado. O ECA não é revogado. A emenda "
            "estreita de maioridade, se passar, não alcança ato infracional comum.",
            "Aborto: manter o quadro legal vigente na data-base — estupro, risco de vida e anencefalia, "
            "conforme a disciplina jurídica já firmada — sem projetar ampliação para aborto eletivo "
            "e sem projetar criminalização da mulher além da lei. O que o governo faz em ato próprio "
            "é garantir o procedimento já legal no SUS, com serviço que não empurre a mulher de "
            "hospital em hospital, e ampliar contracepção e educação sexual na rede que aderir.",
            "Pessoa com deficiência: cronograma de acessibilidade dos prédios federais de atendimento "
            "até 2030 e BPC preservado. Religião: imunidade de templo mantida, ensino confessional "
            "não obrigatório na escola pública, festa religiosa sem verba secreta de ministério.",
            "Igualdade racial: manter cotas federais já existentes e avaliá-las em 2029. O centro "
            "da política é alfabetização, emprego formal e redução de homicídio onde o jovem negro "
            "morre mais, não uma secretaria nova sem instrumento."
        ],
        "instrumento": (
            "Tipo penal e cota privada exigiriam lei: a cota privada não será proposta, o tipo penal "
            "novo de opinião tampouco. Publicação de diferencial salarial em contrato público cabe "
            "em lei de licitação. Acesso a aborto já legal é portaria e gestão do SUS. Acessibilidade "
            "de prédio federal é orçamento e decreto de cronograma."
        ),
        "prazo": (
            "Portaria do procedimento já legal do aborto nos primeiros cem dias, porque é gestão, "
            "não doutrina nova. Projeto de transparência salarial em contrato até o fim do primeiro "
            "ano. Cronograma de acessibilidade em 2027. Avaliação de cotas em 2029."
        ),
        "custo": (
            "Auditores da autoridade de dados e acessibilidade física são os itens materiais. Cabem "
            "em orçamento administrativo. Não há programa de transferência novo neste eixo: o BPC e "
            "o Bolsa Família estão no eixo 13."
        ),
        "financiamento": (
            "Orçamento ordinário. Sem fundo especial com marketing próprio."
        ),
        "indicador": (
            "Tempo entre medida protetiva e resposta à violação, nos municípios aderentes ao eixo 6. "
            "Percentual de prédios federais de atendimento acessíveis em 2030. Existência de serviço "
            "SUS de aborto legal em cada estado, sem fila punitiva — meta de cobertura estadual, não "
            "de aumento do número de procedimentos como se número alto fosse vitória. Diferencial "
            "salarial publicado pelas contratadas, simplesmente publicado: a luz é o primeiro indicador; "
            "a queda do diferencial, o segundo, e pode não ocorrer em quatro anos."
        ),
        "riscos": (
            "O equilíbrio sobre aborto será atacado pelos dois polos. O programa aceita o ataque e "
            "não o resolve com ambiguidade: não amplia e não restringe o direito já reconhecido, e "
            "faz o serviço funcionar. Transparência salarial sem sanção pode virar relatório bonito; "
            "a sanção inicial é não contratar quem não publica, e só isso."
        ),
        "competencia": (
            "Direito civil e penal é lei federal. Escola municipal decide horário e método dentro "
            "da base nacional; educação sexual obrigatória detalhada não será imposta por decreto "
            "contra a lei de diretrizes. O presidente dá o exemplo no SUS federal e no contrato da União."
        ),
    })

    eixo(doc, 18, "Desenvolvimento regional", {
        "diagnostico": (
            "O Norte tem água de rede em 60,9% dos domicílios e esgoto rural nacional em 8,9%. O "
            "Nordeste e o Norte concentram as piores taxas de morte violenta. O déficit habitacional "
            "absoluto ainda é maior no Sudeste, onde está a gente. O rendimento e a indústria "
            "seguem concentrados. Fundos constitucionais de financiamento regional existem e, com "
            "frequência, espalham crédito subsidiado sem mudar o gargalo físico. Elias é de Santarém "
            "e não tratará o Sudeste como inimigo: o porto de Santos e a fábrica paulista também "
            "são o país. Lúcia, do Vale do Ribeira, impede que a chapa vire só discurso nortista."
        ),
        "objetivo": (
            "Interiorizar investimento de verdade — rio, escola técnica, saneamento, segurança — "
            "e parar de chamar subsídio espalhado de desenvolvimento. Reduzir a distância de "
            "aprendizado e de morte violenta entre regiões, não decretar igualdade de PIB per capita "
            "em quatro anos, o que seria impossível."
        ),
        "propostas": [
            "Fundos constitucionais regionais: publicar taxa de inadimplência e emprego por contrato, e deslocar a margem administrável do crédito subsidiado para infraestrutura e ensino técnico, dentro do que a Constituição permitir sem emenda. Onde a Constituição obrigar o desenho financeiro atual, o governo não finge que decreto o muda; envia projeto e, enquanto isso, usa a governança que já cabe.",
            "Nenhum campus federal novo no mandato. Conclusão dos que estão pela metade no Norte e no Nordeste, com prioridade sobre obra nova no Sul e no Sudeste que já tenha oferta densa. Isso repete o eixo 5 de propósito: é a mesma decisão.",
            "Compras públicas federais com cota de participação de pequena empresa regional apenas onde o preço não exceder uma banda publicada sobre o menor lance. Cota sem banda vira sobrepreço com bandeira regional. A banda será curta.",
            "Convênio de segurança e de saneamento do programa terá peso explícito para Norte e Nordeste nos critérios de seleção, escrito no decreto, para não depender do governador que grita mais alto em Brasília."
        ],
        "instrumento": (
            "Critério de convênio é decreto e lei orçamentária. Fundos constitucionais, se precisarem "
            "mudar de natureza, pedem emenda: a probabilidade é baixa, e o plano não depende dela "
            "para o resto. Campus é ato do Ministério da Educação."
        ),
        "prazo": (
            "Decreto de critérios regionais de convênio no primeiro semestre. Publicação de "
            "inadimplência dos fundos em 2027. Obras de campus herdadas: cronograma único até o "
            "fim de 2027, com o que será terminado e o que será desistido."
        ),
        "custo": (
            "Realocação, não programa novo de dezenas de bilhões com nome de região. O custo está "
            "nos eixos de saneamento, segurança e educação. Região não ganha um terceiro orçamento "
            "paralelo."
        ),
        "financiamento": (
            "Os mesmos. A honestidade regional é não somar duas vezes o mesmo real numa tabela de "
            "«investimento no Norte» e de «investimento em saneamento»."
        ),
        "indicador": (
            "Diferença de taxa de mortes violentas entre Nordeste e a média nacional, em queda até "
            "2030. Diferença de domicílios com esgoto adequado entre Norte e Sudeste, em queda. "
            "Inadimplência dos fundos regionais publicada e não crescente. Campi herdados: percentual "
            "de obra com laudo de conclusão ou de desistência."
        ),
        "riscos": (
            "Bancada regional tratará critério publicado como menos útil do que emenda individual. "
            "Esse conflito é o do eixo 20 e não será resolvido prometendo as duas coisas. Desistir "
            "de campus pela metade gera protesto local legítimo: a lista será pública e visitável, "
            "não um anexo secreto."
        ),
        "competencia": (
            "Governador continua governador. A União não intervém em estado por motivo de "
            "desenvolvimento regional. Intervém apenas nas hipóteses constitucionais, que este "
            "programa não banaliza."
        ),
    })

    eixo(doc, 19, "Comércio exterior e indústria estratégica", {
        "diagnostico": (
            "O superávit comercial de janeiro a setembro de 2026 foi de US$ 62,4 bilhões, e o de "
            "2025 ficou na casa de US$ 68 bilhões. A pauta segura o país e concentra risco: China "
            "como destino decisivo, tarifas americanas já tendo reduzido a venda aos Estados Unidos "
            "em 6,6% em 2025, Argentina volátil mesmo quando compra mais. A indústria cresceu pouco "
            "em 2025. Semicondutor de fronteira não será produzido aqui no mandato. Minerais críticos "
            "saem muitas vezes sem o elo seguinte de processamento. Mercosul trava e protege ao "
            "mesmo tempo. Conteúdo nacional mal desenhado atrasou obra de energia no passado sem "
            "criar fronteira tecnológica."
        ),
        "objetivo": (
            "Abrir mercado sem desmontar o setor que compete, e sem proteger o que não compete. "
            "Um elo a mais na cadeia de mineral crítico onde energia e licença existirem. Defesa "
            "comercial só com prova de dano, via regra da OMC, não por humor da semana."
        ),
        "propostas": [
            "Concluir o acordo Mercosul–União Europeia se a versão à mesa na posse ainda for "
            "mutuamente aplicável, aceitando cláusula ambiental cooperativa e recusando sanção "
            "unilateral automática que não caiba em diálogo prévio. Se o texto for outro, o "
            "Congresso vê o texto real; o governo não vende acordo genérico.",
            "Tarifa americana: negociar como contencioso comercial, retaliar só na medida e no "
            "produto em que a análise jurídica mostrar ganho, e levar à OMC quando o caso for "
            "forte. Não transformar tarifa em plebiscito de alinhamento ideológico.",
            "Comitê de investimento estrangeiro em setor sensível — porto próximo de instalação "
            "militar, núcleo de telecomunicação, controle de transmissão elétrica, processamento "
            "de mineral crítico e dado sensível de Estado. Lei ordinária, prazo curto de decisão, "
            "não um veto político genérico a capital chinês, americano ou europeu. Fora da lista, "
            "o investimento é bem-vindo.",
            "Política industrial estreita: processamento de níquel, lítio e terras raras um elo "
            "à frente, apenas com energia contratada e licença ambiental, por meio de depreciação "
            "acelerada horizontal e não de campeão escolhido. Defesa e nuclear civil entram nessa "
            "lista curta. O resto compete.",
            "Moeda comum do BRICS: rejeitada. Liquidação em moeda local, quando o parceiro e o "
            "Banco Central julgarem o risco cambial aceitável, pode ser usada em operação pontual "
            "e não vira sistema monetário novo."
        ],
        "instrumento": (
            "Acordo internacional: negociação do Executivo e aprovação do Congresso quando a "
            "Constituição exigir. Comitê de investimento: lei. Depreciação acelerada: lei tributária, "
            "dentro da revisão de renúncias — se não couber na meta, não se cria o benefício. "
            "Defesa comercial: órgãos já existentes."
        ),
        "prazo": (
            "Posição escrita sobre o acordo com a União Europeia nos primeiros cem dias, com o "
            "texto que estiver em vigor na mesa. Projeto do comitê de investimento no primeiro ano. "
            "Nenhuma tarifa nova no primeiro semestre, salvo direito antidumping já instruído."
        ),
        "custo": (
            "Depreciação acelerada é renúncia e só existe se a lei do eixo 2 a comportar dentro "
            "do teto de carga. O comitê custa servidores. Retaliação tarifária custa o consumidor "
            "brasileiro: por isso é última linha, não primeira."
        ),
        "financiamento": (
            "Não há fundo industrial grande. Há regra tributária horizontal condicionada e agência "
            "de análise de investimento. Quem prometer BNDES sem limite como política industrial "
            "deste plano leu outro documento."
        ),
        "indicador": (
            "Número de acordos preferenciais concluídos ou explicitamente recusados com razão "
            "publicada — os dois contam. Participação de produtos manufaturados de maior intensidade "
            "na exportação, sem meta mágica de percentual que o mundo não controla. Decisões do "
            "comitê de investimento no prazo legal, com a lista do que foi condicionado. Zero "
            "adesão a moeda comum."
        ),
        "riscos": (
            "Dizer não a campeão nacional irrita indústria que vive de favor e também irrita "
            "trabalhador dessa indústria. A resposta é a folha mais barata do eixo 2 e o corredor "
            "logístico, não o subsídio eterno. O comitê de investimento pode virar barreira "
            "xenófoba se a lista sensível crescer por pressão: a lei trancará a lista e a ampliação "
            "exigirá projeto novo, não portaria."
        ),
        "competencia": (
            "Comércio exterior é da União. O presidente não impede estado de captar fábrica fora "
            "da lista sensível e não deve usar a Receita como instrumento de política industrial "
            "informal."
        ),
    })

    eixo(doc, 20, "Reforma política e governabilidade", {
        "diagnostico": (
            "O experimento impõe uma premissa: a ATR teria 8% da Câmara e 8% do Senado. Mesmo sem "
            "essa premissa, o presidencialismo brasileiro se governa em coalizão. Emenda parlamentar "
            "é parte do preço, hoje em larga medida obrigatória. Orçamento secreto já foi declarado "
            "incompatível com a transparência e não voltará com outro nome. Voto eletrônico "
            "auditável é infraestrutura democrática, não penduricalho. Reeleição presidencial "
            "encurta o horizonte e alonga a campanha permanente."
        ),
        "objetivo": (
            "Governar com minoria sem comprar ilegalidade. Reduzir o crescimento real das emendas "
            "obrigatórias se houver voto. Acabar com a reeleição para mandatos futuros. Manter a "
            "urna. Não prometer distritão nem semiparlamentarismo, que não passam e mudariam o "
            "sistema no meio do jogo de representação do Norte, onde o distrito único geográfico "
            "engoliria a voz do interior."
        ),
        "propostas": [
            "Emenda para extinguir a reeleição de presidente, governador e prefeito, eficaz só para "
            "mandatos seguintes ao da promulgação, de modo que Elias não escreva regra para se "
            "beneficiar. Ele se compromete, além disso, a não se recandidatar mesmo se a emenda "
            "cair. A vice assume o mesmo compromisso quanto a uma eventual chapa própria imediata "
            "à derrota dessa emenda? Não. Lúcia permanece livre para disputar o futuro. O compromisso "
            "pessoal de não reeleição é de Elias.",
            "Projeto para limitar o crescimento real do conjunto das emendas obrigatórias à inflação, "
            "no que a Constituição depois da série de emendas permitir. Onde a Constituição exigir "
            "percentual, a conversa é emenda, e a probabilidade é baixa. Enquanto isso, execução "
            "transparente: cada emenda com objeto, foto da obra ou ausência dela, e nome do autor.",
            "Manutenção da urna eletrônica com auditoria pública já prevista. Rejeição do voto "
            "impresso que recria cadeia de custódia frágil. Financiamento público de campanha "
            "mantido e proposto em valor real não crescente, com teto de gasto efetivamente fiscalizado. "
            "Não se volta à doação empresarial oculta.",
            "Base de governo: acordo publicado por pauta — quais projetos a ATR cede, quais não "
            "cede — em vez de acordo só por cargo. Cargo haverá, porque o sistema é esse. Cargo "
            "sem pauta escrita não é acordo; é hospedagem."
        ],
        "instrumento": (
            "Fim da reeleição: emenda constitucional. Emenda parlamentar: emenda constitucional se "
            "o teto atual for constitucional, ou lei orçamentária na margem. Urna: não mexer é ato "
            "político de não enviar projeto. Transparência de emenda: portais já existem e serão "
            "chefiados, ato próprio."
        ),
        "prazo": (
            "Emenda da reeleição apresentada no primeiro ano. Portal de obra de emenda com padrão "
            "único em 2027. Nenhum projeto de voto impresso será de iniciativa deste governo, em "
            "tempo algum do mandato."
        ),
        "custo": (
            "Reforma política bem feita é barata. Financiamento eleitoral não crescente em termos "
            "reais é economia pequena e simbólica. O custo político é que é alto: bancada não "
            "aplaude limite de emenda."
        ),
        "financiamento": (
            "Não se aplica além do orçamento eleitoral já existente, proposto sem crescimento real."
        ),
        "indicador": (
            "Emenda promulgada ou arquivada com voto registrado — o governo não dirá que «quase "
            "passou». Percentual de emendas com objeto verificável fotografado ou georreferenciado. "
            "Zero projeto do Executivo sobre voto impresso. Existência dos acordos de pauta "
            "publicados a cada semestre, mesmo que curtos e constrangedores."
        ),
        "riscos": (
            "Publicar acordo de pauta mostra a concessão e irrita eleitor que queria pureza. "
            "Escondê-lo é pior. A emenda da reeleição pode ser acusada de pose, porque provavelmente "
            "não passa: o compromisso pessoal de Elias, que não depende de voto, existe para a pose "
            "não ser vazia. Limite de emenda, se aprovado de modo atabalhoado, pode ser derrubado "
            "pelo Supremo; o projeto será escrito para sobreviver a esse exame, não para aplauso de rede."
        ),
        "competencia": (
            "Quase tudo aqui é do Congresso. O presidente propõe, veta e organiza a sua minoria. "
            "Não dissolve a Câmara, não edita medida provisória de sistema eleitoral e não condiciona "
            "empenho legal a fidelidade — esse condicionamento, se aparecer, é o escândalo que "
            "demite o ministro que o praticar."
        ),
    })

    p(
        doc,
        "O conjunto dos vinte eixos cabe numa frase que não substitui o texto: regra fiscal que "
        "trava promessa, escola que mede leitura, polícia que filma e investiga, obra que termina "
        "ou é cancelada, floresta que não volta a ser fronteira de crime, e um Estado que não se "
        "vende inteiro nem se imagina dono da economia. A política externa, as vinte decisões "
        "controversas, as vinte e cinco promessas e o número do orçamento vêm nos volumes seguintes "
        "e não podem contradizer o que está acima. Se contradisserem, vale este volume e o 05, e "
        "o erro deve ser corrigido, não explorado.",
    )
    save(doc, os.path.join(OUT, "06_PLANO_EIXOS_11_A_20.docx"))
    print("vol 06 ok")


if __name__ == "__main__":
    build()
