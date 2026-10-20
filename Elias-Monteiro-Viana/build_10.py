# -*- coding: utf-8 -*-
"""Volume 10 — crises, autocrítica, discursos e carta."""
import os, sys
sys.path.insert(0, "/workspace/candidatura")
from docx_theme import bullets, cover, h, new_doc, p, save

OUT = "/workspace/candidatura/docx"


def build():
    doc = new_doc()
    doc.core_properties.title = "10 — Crises, autocrítica e campanha fictícia"
    cover(
        doc,
        "VOLUME 10",
        "Crises, autocrítica, discursos e carta",
        "O mandato fictício também se mede pelo que fizer quando o plano não couber na semana.",
    )

    h(doc, 1, "1. Teste de crise")
    p(
        doc,
        "Cinco cenários fictícios, distintos dos fatos reais de outubro de 2026. Nenhum autoriza "
        "fechar Congresso, censurar imprensa ou chamar quartel para arbitrar política. Em todos, "
        "as primeiras frases públicas separam o que se sabe, o que não se sabe e quem decide.",
    )

    h(doc, 2, "Crise A — Recessão")
    p(
        doc,
        "O PIB contrai e o desemprego sobe. Nas primeiras 24 horas: reunião com Fazenda, "
        "Planejamento e Banco Central, este em sua autonomia, sem pedido de corte de Selic. "
        "Comunicado único: os estabilizadores legais — seguro-desemprego e Bolsa Família — "
        "funcionam sem medida heroica; não haverá pacote de gasto permanente anunciado de noite. "
        "Em 30 dias: acelerar concessão e licença de baixo risco já previstas, antecipar "
        "manutenção de corredor já contratado, abrir crédito de banco público com subsídio "
        "explicitado na peça orçamentária e com teto. Se o Congresso quiser pacote maior, o "
        "governo só assina o que tiver fonte ou o que for temporário e com morte marcada. Em "
        "seis meses: se o desemprego tiver subido mais de 1,5 ponto em doze meses sem alívio "
        "de inflação esperada, aciona-se a cláusula de desacelerar o ajuste, não de abandonar "
        "a âncora — adia-se a última etapa de corte de renúncia e protegem-se os estabilizadores. "
        "Não se estatiza empresa em dificuldade como emprego disfarçado."
    )
    h(doc, 2, "Crise B — Ataques coordenados de facções")
    p(
        doc,
        "Em 24 horas: sala na Justiça e Segurança Pública com Polícia Federal, PRF e os governadores "
        "atingidos. Sem intervenção federal espontânea. GLO apenas se o governador pedir ou se a "
        "ordem pública estadual tiver colapsado, nos termos da Constituição, com decreto, prazo de "
        "dias e protocolo de morte. Forças Armadas não substituem a investigação. Em 30 dias: "
        "projeto de urgência sobre perdimento de bem e transferência de comando de presídio, mais "
        "dinheiro de emergência só para estado que aceite câmera e separação de facção. Em seis "
        "meses: relatório público do que falhou — inteligência, presídio, fronteira — e demissão "
        "de quem tiver omitido alerta. Não haverá estado de sítio como rotina nem coletivas com "
        "corpo de suspeito."
    )
    h(doc, 2, "Crise C — Emergência sanitária")
    p(
        doc,
        "Em 24 horas: a vice, Lúcia Okamoto, coordena a sala com o ministro da Saúde, sem demitir "
        "ninguém para a câmera. Notificação internacional, estoque visível, compra emergencial "
        "já autorizada por lei. Escolas e postos não fecham por decreto nacional na primeira noite. "
        "Em 30 dias: critério publicado de restrição, proporcional à transmissão e à gravidade, "
        "com Congresso informado e crédito extraordinário se o piso não bastar. Vacina, se existir, "
        "entra pelo SUS, com fila pública. Em seis meses: inquérito técnico do que faltou em "
        "atenção básica, sem caça a bode expiatório e com nome de quem atrasou compra. Lockdown "
        "nacional prolongado não é a primeira ferramenta; restrição focal, sim, se a evidência "
        "clínica for essa. Se a evidência for outra, o governo muda o decreto e diz que mudou."
    )
    h(doc, 2, "Crise D — Estados Unidos e China exigem lado")
    p(
        doc,
        "Em 24 horas: não há entrevista escolhendo padrinho. Nota curta: o Brasil comerciará com "
        "os dois, não cederá base, não aderirá a bloqueio tecnológico total nem a retaliação "
        "simbólica que encareça insumo sem ganhar mercado. Em 30 dias: o comitê de investimento "
        "sensível, mesmo que ainda em projeto, opera em regime provisório no que a lei já permitir; "
        "lista pública do que é sensível e do que não é. Diplomacia econômica com os dois, no mesmo "
        "mês, para não parecer fila de vassalo. Em seis meses: se uma das potências impuser "
        "sanção secundária a empresa brasileira, a resposta é jurídica — licença, disputa, medida "
        "equivalente proporcional — e não ideológica. O agronegócio não será sacrificado para "
        "gesto, e a rede do Estado não será entregue para gesto oposto. O eleitor verá a conta."
    )
    h(doc, 2, "Crise E — o Congresso rejeita a reforma principal")
    p(
        doc,
        "Suponha que a lei de renúncias caia. Em 24 horas: o presidente diz que perdeu, cita o "
        "placar e não assina medida provisória que reescreva o que o plenário rejeitou. Em 30 dias: "
        "o projeto volta fatiado — primeiro os benefícios sem avaliação nenhuma e de maior valor, "
        "menos numerosos — e a escala cheia de educação, segurança e saneamento é formalmente "
        "suspensa. Os pilotos continuam. Em seis meses: acordo de pauta publicado com quem votou "
        "não, mostrando o que mudou no texto e o que não mudará: caducidade, transparência e "
        "vedação de renúncia eterna. Se o segundo texto também cair, o mandato governa no cenário "
        "pessimista do volume 09 sem fingir que a promessa social cheia segue de pé."
    )

    h(doc, 1, "2. Autorreflexão")
    h(doc, 2, "Cinco pontos fracos")
    bullets(
        doc,
        [
            "O superávit de 0,5% do PIB é honesto e pode ser pequeno demais para a dívida. O programa prefere essa honestidade a um número de palanque, e admite que a dívida pode terminar o mandato mais alta do que em outubro de 2026.",
            "Segurança depende de governador. O fundo pode ficar sem adesão exatamente nos estados mais violentos, e o plano terá dinheiro recusado e homicídio intacto.",
            "A regulação da cannabis pode ser capturada por mercado ilegal com selo falso ou pode aumentar o uso adolescente. A cláusula de 24 meses existe porque o risco é real, não retórico.",
            "Angra 3 e a margem equatorial desagradam os dois polos e podem paralisar a decisão energética no meio, que é o pior resultado: nem licença, nem veto, nem teto.",
            "Oito por cento das cadeiras não passam emenda. Parte vistosa do plano — maioridade estreita e fim da reeleição — é a parte com menor probabilidade. O estilo seco de Elias piora isso: ele não arrasta plenário pela emoção.",
        ],
    )
    h(doc, 2, "Quem discorda, e com razão de interesse")
    bullets(
        doc,
        [
            "Agronegócio de fronteira: não haverá anistia de desmatamento recente nem mineração em terra indígena, e a Ferrogrão espera 2029.",
            "Ambientalismo de veto prévio: não haverá proibição presidencial de novo óleo nem abandono automático do nuclear.",
            "Centrais sindicais: não há jornada de quatro dias por lei, não volta o imposto sindical, e o mínimo pode perder ganho real num ano de meta estourada.",
            "Campo da segurança máxima: não há porte ampliado, não há maioridade geral aos 16 no presídio adulto, e a câmera corta repasse.",
            "Campo da segurança mínima: a emenda dos 16 anos existe, e a cannabis não vem acompanhada de legalização de cocaína e crack.",
            "Servidor e militar: reposição baixa no apoio e contribuição maior para quem entrar na carreira militar depois da lei.",
            "Quem quer imposto sobre fortuna e quem quer carga em queda livre: os dois perdem. A carga muda de lugar e não passa de 32,5% do PIB como teto operacional.",
        ],
    )
    h(doc, 2, "Promessas mais difíceis e efeitos colaterais")
    p(
        doc,
        "As mais difíceis são o primário de 0,5% do PIB, a aprovação inteira da revisão de renúncias, "
        "a cannabis licenciada, a queda do feminicídio — porque o crime ocorre dentro de casa e a "
        "polícia é estadual — e a conclusão de Angra 3 dentro do teto. Efeitos negativos possíveis: "
        "ajuste que segure pobreza se alguém violar a proteção do Bolsa Família e do BPC; repressão "
        "que aumente morte policial antes de reduzir homicídio; auxílio-aluguel que encareça aluguel "
        "no piloto; depreciação acelerada de mineral crítico que vire renúncia capturada se a trava "
        "falhar. Cada um tem cláusula de morte ou de escala. Cláusula não é certeza de uso. Governo "
        "também descumpre a própria cláusula, e esse será o ponto justo de ataque."
    )
    h(doc, 2, "Três críticas de um adversário honesto")
    p(
        doc,
        "Primeira: «você chama de responsabilidade fiscal um superávit que não estabiliza a dívida "
        "com este juro. É timidez com aparência de coragem.» Resposta: a crítica procede no número. "
        "O programa não tem voto nem legitimidade para um primário de 2% ou 3% do PIB em quatro "
        "anos sem uma recessão política que derruba a regra inteira. Prefere 0,5% crível, que baixe "
        "o prêmio, a 2% de papel. Se o prêmio não cair até 2029, a crítica deixa de ser teórica e "
        "Elias deverá propor, ainda no mandato, um passo adicional de despesa corrente — não de "
        "imposto novo — ou admitir que a âncora foi curta.",
    )
    p(
        doc,
        "Segunda: «sua segurança não escolhe. Baixa a maioridade num canto e libera cannabis no "
        "outro, e a facção continua porque você não faz nem guerra às drogas nem legalização "
        "ampla.» Resposta: a facção vive de cocaína, arma, presídio e fronteira, não do baseado "
        "do adulto. Misturar tudo numa guerra só enche cadeia de usuário e não separa comando. "
        "A crítica acerta ao dizer que o resultado depende de governador e de inteligência, que "
        "o presidente não decreta. Por isso a probabilidade da promessa 25 não passa de 45%.",
    )
    p(
        doc,
        "Terceira: «desenvolvimentismo de regras é nome de quem não decide: não vende a Petrobras, "
        "não a transforma em ministério, não se alinha, não rompe com o agro, não faz reforma "
        "agrária clássica.» Resposta: decidir não é escolher o extremo que cabe em camiseta. "
        "Está decidido o núcleo que fica, o ativo que se concede, o Ibama sem telefone, a terra "
        "indígena sem mina, a moeda do Brics recusada, a reeleição recusada, o BPC preservado, "
        "a jornada de quatro dias recusada. Quem não vir decisão aí está pedindo identidade, não "
        "governo. Identidade o programa também tem; só não aceita que ela substitua o instrumento.",
    )
    h(doc, 2, "Evidência que faria abandonar uma política, e o que é fracasso")
    p(
        doc,
        "Além das três cláusulas do volume 01: se a câmera corporal vier acompanhada de alta "
        "consistente de homicídio e de queda da atividade policial medida em flagrante — não em "
        "morte —, o desenho do fundo será refeito, sem abandonar a filmagem. Se a avaliação "
        "censitária do 2º ano produzir fraude de rede em massa, troca-se o método de aplicação, "
        "não a ideia de medir. Se o comitê de investimento virar barreira para todo capital "
        "estrangeiro, a lista será encolhida por lei.",
    )
    p(
        doc,
        "O mandato será fracasso se, em 2030, a dívida bruta estiver mais de 8 pontos do PIB acima "
        "do nível de outubro de 2026 e, ao mesmo tempo, a leitura do 2º ano e a elucidação de "
        "homicídio não tiverem melhorado. Será fracasso imediato, qualquer que seja o indicador, "
        "se o governo violar eleição, torturar, esconder morte policial, capturar o Banco Central "
        "ou recusar saída no dia em que perder. Sucesso parcial é o desfecho mais provável: alguns "
        "pilotos entregues, emendas caídas, floresta ainda em queda, escola ainda insuficiente, "
        "contas menos piores do que o herdado e nenhuma mentira de que o país foi refeito. "
        "Probabilidade subjetiva desse sucesso parcial: cerca de 50%. De sucesso amplo, no cenário "
        "otimista do volume 09: não mais que 25%.",
    )

    h(doc, 1, "3. Discurso de lançamento")
    p(
        doc,
        "Duração visada: três minutos. Linguagem de comício curto, não de relatório. O texto é "
        "ficcional e não descreve fato verdadeiro da vida do orador.",
        italic=True,
    )
    p(
        doc,
        "Boa noite. Eu sou Elias Monteiro Viana, de Santarém, e esta candidatura é uma simulação — "
        "não tem registro, não pede voto real, não vem com pesquisa no bolso. O que ela tem é uma "
        "escolha. O Brasil não está no chão. Tem gente trabalhando, inflação que já foi pior, "
        "floresta que caiu menos, desemprego baixo. E não está no trilho. A dívida sobe, o juro "
        "come o futuro, a criança atravessa a escola sem calcular, a mulher morre em casa em número "
        "recorde, e o investimento não chega para o porto, o rio e o esgoto.",
    )
    p(
        doc,
        "Não vou prometer um país novo em quatro anos. Vou prometer regra. Despesa permanente só "
        "com fonte. Banco Central sem telefone. Obra que termina ou que eu mesmo arquiva, com o "
        "papel na mesa. Polícia que filma e que investiga, não que comemora corpo. Escola medida "
        "pela leitura no segundo ano, não pela fita de prédio. Floresta com satélite e produtor "
        "legal com cadastro; terra indígena sem mineração; licença ambiental sem ordem do palácio.",
    )
    p(
        doc,
        "Vão dizer que é pouco. Que falta grito, que falta inimigo, que falta uma jornada milagrosa "
        "e um imposto com nome de justiça. Eu escolhi outro caminho de propósito. O SUS fica. O "
        "BPC fica. A Petrobras fica pública e com teto de responsabilidade. Os Correios não serão "
        "vendidos neste mandato. A cannabis do adulto sai da cadeia e o traficante de facção não "
        "sai da mira. A maioridade, se o Congresso topar, desce só para crime hediondo, em casa "
        "separada — e a minha vice, Lúcia Okamoto, não precisa fingir entusiasmo para subir neste "
        "palanque. Eu também não vou me recandidatar. Quem precisa de oito anos para fazer o básico "
        "já começou errado.",
    )
    p(
        doc,
        "O Brasil no trilho não é um verso. É porto, é sala de aula, é conta que fecha, é fronteira "
        "onde o Estado chega antes da facção. Se isso parecer seco demais para uma campanha, melhor. "
        "Seco é o papel em que a obra cabe. Obrigado.",
    )

    h(doc, 1, "4. Discurso de debate")
    p(doc, "Duração visada: dois minutos.", italic=True)
    p(
        doc,
        "Três prioridades, e a ordem importa. Primeiro, a conta: sem superávit primário a caminho "
        "e sem revisão das renúncias, o resto é discurso financiado por juro. Segundo, a leitura: "
        "criança alfabetizada no segundo ano, medida uma por uma, com professor onde a escola está "
        "abaixo do corte. Terceiro, a vida: feminicídio, homicídio e morte policial na mesma tabela, "
        "dinheiro federal só para quem separa facção e liga a câmera.",
    )
    p(
        doc,
        "O diferencial não é um lado da briga pronta. É o que eu recuso. Recuso moeda comum de bloco, "
        "recuso voto impresso, recuso jornada de quatro dias por lei nacional, recuso vender o SUS, "
        "recuso minerar terra indígena, recuso telefonar para o Ibama, recuso me recandidatar. "
        "Quem quiser uma dessas coisas tem candidato melhor do que eu. Quem quiser porto, regra e "
        "escola vai ter de engolir um programa que não cabe numa camiseta e que admite, aqui, que "
        "a dívida pode não cair no meu mandato se o juro não colaborar. Eu prefiro perder o debate "
        "neste ponto a ganhar com número falso.",
    )

    h(doc, 1, "5. Entrevista")
    p(doc, "Pergunta 1. O senhor é fiscalista num país pobre. Vai tirar o Bolsa Família?", italic=True)
    p(
        doc,
        "Não. O valor real fica. Sem o benefício, a extrema pobreza de 2024 teria sido 10%, não 3,5%, "
        "pelo IBGE. O que eu tiro é renúncia sem avaliação e ganho real automático do mínimo quando "
        "a meta estourar. Pobre não é variável de ajuste. Favor fiscal é.",
    )
    p(doc, "Pergunta 2. De onde sai o dinheiro, se a carga não sobe?", italic=True)
    p(
        doc,
        "De 0,4 ponto do PIB em renúncia, se o Congresso deixar, e de custeio que não é prioridade. "
        "Se não deixar, a escola nova, o fundo de segurança e o saneamento subsidiado não vão à "
        "escala cheia. Eu não financio promessa com dívida e chamo de investimento.",
    )
    p(doc, "Pergunta 3. O senhor já ocupou cargo público de verdade?", italic=True)
    p(
        doc,
        "Não. A secretaria municipal e a estadual que aparecem na biografia são inventadas para a "
        "simulação, e o documento diz isso. Julguem o plano. Quem usar essa biografia como currículo "
        "real está fraudando o experimento, e não serei eu.",
    )
    p(doc, "Pergunta 4. Cannabis e maioridade no mesmo plano não é contradição?", italic=True)
    p(
        doc,
        "Não, se você separar usuário adulto de comando de facção, e separar latrocínio de ato "
        "infracional comum. É contradição se você precisa de uma frase só. Eu não preciso.",
    )
    p(doc, "Pergunta 5. Por que não mandar arma à Ucrânia?", italic=True)
    p(
        doc,
        "Porque o Brasil condena a invasão e não vira parte. Arma fecha a porta de qualquer "
        "conversa e não recupera fronteira. Reconhecer anexação, porém, também não será feito. "
        "As duas coisas cabem juntas.",
    )
    p(doc, "Pergunta 6. Gaza. De que lado o senhor está?", italic=True)
    p(
        doc,
        "Do lado do civil. Israel não será negado como Estado. Hamas não será tratado como "
        "governo. Assentamento que mata a solução de dois Estados será criticado. Criança morta "
        "depois do cessar-fogo não vira detalhe porque a política é complicada. O Brasil não manda "
        "tropa e não faz sanção de vitrine.",
    )
    p(doc, "Pergunta 7. O senhor vai interferir no Banco Central?", italic=True)
    p(
        doc,
        "Não. A Selic de 13,75% dói e ainda assim não é assunto de live. Se a Fazenda quiser juro "
        "menor, que entregue primário crível. Telefonema não é política monetária.",
    )
    p(doc, "Pergunta 8. Corrupção. Qual é o primeiro nome que o senhor entrega?", italic=True)
    p(
        doc,
        "Não tenho nome, e não vou inventar delação para a entrevista. Tenho regra: CGU sem licença "
        "da Casa Civil, reunião com interessado em licitação tornada pública, ministro que usar "
        "doação para cargo sai antes da sentença. Quem prometer lista de culpados na estreia já "
        "escolheu o espetáculo.",
    )
    p(doc, "Pergunta 9. Por que a Petrobras fica, se o senhor diz querer mercado?", italic=True)
    p(
        doc,
        "Porque energia e pré-sal não são uma fábrica de sapato, e porque vender por identidade "
        "já produziu mais slogan do que produtividade. Fica com governança, sem preço decretado "
        "para sempre e sem investimento ordenado por comício. O que não é núcleo pode ser concedido. "
        "Eu disse qual é o núcleo.",
    )
    p(doc, "Pergunta 10. Com 8% do Congresso, o que o senhor faz na segunda-feira?", italic=True)
    p(
        doc,
        "Publico a lista de renúncias, o decreto de licença, a instrução ao Itamaraty e o veto que "
        "eu já sei que usarei. Mando as emendas sabendo que podem morrer. Não negocio anistia nem "
        "urna de papel. Se na segunda-feira eu só tiver a minoria, ainda terei o Diário Oficial. "
        "É pouco. É o que a Constituição dá. Eu não vou fingir que dá mais.",
    )

    h(doc, 1, "6. Carta aberta à população brasileira")
    p(
        doc,
        "Esta carta tem menos de quinhentas palavras e permanece, como tudo o mais, dentro da ficção.",
        italic=True,
    )
    p(
        doc,
        "Eu não venho dizer que o país que vocês sustentam está falido, nem que está pronto. Venho "
        "dizer que ele está cansado de promessa que não cabe na conta e de briga que não cabe na "
        "escola. O trabalho de quem paga imposto, de quem espera cirurgia, de quem cruza rua insegura "
        "e de quem planta com regra merece um governo que escolha.",
    )
    p(
        doc,
        "Eu escolho a regra antes do anúncio. Escolho o SUS público e a fila medida, não a fila "
        "como destino. Escolho alfabetizar e provar que alfabetizei. Escolho perseguir facção e "
        "filmar a polícia. Escolho floresta em pé com produtor legal de pé, e terra indígena sem "
        "mina. Escolho falar com a China e com os Estados Unidos sem pedir benção a nenhum dos "
        "dois, e sem achar que fertilizante ou chip apaga invasão e massacre.",
    )
    p(
        doc,
        "Não vou me recandidatar. Não vou criar imposto-símbolo para parecer justo. Não vou "
        "encurtar a semana por lei para parecer moderno. Não vou armar o civil para parecer firme "
        "nem desarmar a investigação para parecer humano. A vice que está comigo, Lúcia Okamoto, "
        "não é enfeite de palanque: é o limite médico e ético dentro da chapa, e o país ganha "
        "quando esse limite aparece em público.",
    )
    p(
        doc,
        "Se no fim de quatro anos a dívida ainda assustar, mas a criança ler, a licença tiver prazo, "
        "a obra abandonada tiver nome de quem a abandonou e a eleição estiver inteira, eu considerarei "
        "o esforço honesto. Se a dívida assustar e a escola e a segurança continuarem onde estão, "
        "teremos falhado, e eu não pedirei desconto por ter sido educado no discurso. O Brasil no "
        "trilho é uma frase curta para um trabalho longo. Eu a assino mesmo assim.",
    )
    p(doc, "Elias Monteiro Viana, candidato fictício. Aliança do Trabalho e da Regra, partido fictício, sem registro no Tribunal Superior Eleitoral.", italic=True)

    h(doc, 1, "7. Fontes usadas em todo o registro")
    bullets(
        doc,
        [
            "IBGE. PIB de 2025: +2,3%, R$ 12,7 trilhões, per capita R$ 59.687,49, investimento 16,8% do PIB. Release de 3 de março de 2026.",
            "IBGE. PNAD Contínua: desocupação de 5,3% no trimestre até agosto de 2026 (Agência Brasil, 13 out. 2026); informalidade de 37,5% e 38,5 milhões no trimestre nov/2025–jan/2026 (Agência Brasil, 5 mar. 2026); rendimentos de 2025 divulgados em maio de 2026.",
            "IBGE. Síntese de Indicadores Sociais 2025, referência 2024: pobreza 23,1%, extrema pobreza 3,5%, Gini 0,504. Divulgação em 3 dez. 2025.",
            "IBGE. População de 212,7 milhões em 2025 e saneamento dos domicílios, divulgação de abril de 2026.",
            "Banco Central do Brasil. Selic meta de 13,75% desde 16 set. 2026. Boletim Focus, leituras de 13 a 19 out. 2026: IPCA de 2026 em 5,22%, PIB perto de 1,8%, Selic fim de 2026 em 13,25%.",
            "FMI. Perspectivas da economia mundial, crescimento brasileiro de 2,2% em 2026, Agência Brasil, 13 out. 2026.",
            "Ipea. Carta de Conjuntura de outubro de 2026: primário jan–set, dívida federal, revisão do PIB de 2026 para 2,0%.",
            "Ministério da Fazenda, Prisma Fiscal, 15 out. 2026: déficit primário projetado de R$ 53 bilhões em 2026 e dívida bruta de 83,4% do PIB, 87% em 2027.",
            "Tesouro Nacional. Carga de 32,40% do PIB em 2025; COFOG 2024; RREO de 2025 sobre saúde, educação e RGPS (déficit de R$ 320,9 bilhões).",
            "MDIC. Balança comercial de 2025, cerca de US$ 68 bilhões, e resultado de janeiro a setembro de 2026, superávit de US$ 62,4 bilhões.",
            "Fórum Brasileiro de Segurança Pública. 20º Anuário, dados de 2025, divulgação em 23 jul. 2026: 40.775 mortes violentas, taxa 19,1; 1.571 feminicídios.",
            "INEP/MEC. Ideb 2025, agosto de 2026. PISA 2022, MEC, dezembro de 2023: matemática 379, leitura 410, ciências 403.",
            "Inpe. Prodes, 16 out. 2026: Amazônia 3.335 km²; Cerrado 5.516,69 km².",
            "Fundação João Pinheiro. Déficit habitacional de 2024: 5.773.983 domicílios.",
            "Imprensa internacional de outubro de 2026 (Reuters e outros) sobre o impasse na Ucrânia e sobre o cessar-fogo de Gaza, usada como contexto da data-base.",
        ],
    )
    p(
        doc,
        "Fim do registro de candidatura fictícia de Elias Monteiro Viana. Nenhum volume posterior "
        "deve alterar os números, a ficha física, a marca ou as vinte decisões sem dizer que se "
        "trata de revisão expressa. A simulação não declara vitória, não pede voto de avaliador "
        "por simpatia e não conhece os concorrentes.",
    )
    save(doc, os.path.join(OUT, "10_CRISES_AUTOCRITICA_CAMPANHA.docx"))
    print("vol 10 ok")


if __name__ == "__main__":
    build()
