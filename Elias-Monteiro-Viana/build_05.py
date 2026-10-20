# -*- coding: utf-8 -*-
"""Volume 05 — eixos 1 a 10 do plano de governo."""
import os, sys
sys.path.insert(0, "/workspace/candidatura")
from docx_theme import cover, eixo, h, new_doc, p, save

OUT = "/workspace/candidatura/docx"


def build():
    doc = new_doc()
    doc.core_properties.title = "05 — Plano de governo 2027–2030, eixos 1 a 10"
    cover(
        doc,
        "VOLUME 05",
        "Plano de Governo 2027–2030 — Elias Monteiro Viana",
        "Eixos 1 a 10. Economia, fisco, trabalho, saúde, educação, segurança, justiça, defesa, infraestrutura e energia.",
    )
    h(doc, 1, "Como ler os eixos")
    p(
        doc,
        "Cada eixo separa diagnóstico, objetivo, propostas, instrumento, prazo, custo, fonte, "
        "indicador, risco e competência. Custo em «ordem de grandeza» usa a referência de que "
        "0,1% do PIB, sobre uma base nominal próxima de R$ 13 a 14 trilhões em 2026–2027, fica "
        "na casa de R$ 13 a 14 bilhões. Isso não é dotação orçamentária e não autoriza tratar "
        "o número como empenho. Onde o programa depende de lei, está escrito. Onde depende de "
        "governador, está escrito. Promessa que o presidente não pode cumprir sozinho não é "
        "prometida como ato de posse.",
    )
    p(
        doc,
        "Regra de compatibilização, válida para todos os eixos que criam despesa discricionária "
        "nova: a escala cheia só é executada se a lei de revisão de renúncias tributárias for "
        "aprovada. Sem ela, ficam os pilotos e o que couber no piso constitucional já existente. "
        "Essa trava é o oposto de um anexo de boas intenções.",
    )

    eixo(doc, 1, "Economia e desenvolvimento", {
        "diagnostico": (
            "O PIB per capita de 2025 foi de R$ 59.687, com crescimento de 2,3% no ano e investimento "
            "de apenas 16,8% do PIB. Em 2026 a atividade desacelerou: o intervalo de projeções na "
            "data-base ia de cerca de 1,8% (Focus) a 2,2% (FMI). A Selic estava em 13,75%, o IPCA "
            "esperado para 2026 estava acima do teto da meta, e o resultado nominal projetado pelo "
            "mercado rondava 9% do PIB por causa do juro. A agropecuária carregou 2025; a indústria "
            "cresceu 1,4%. O país não está em colapso de demanda. Está em escassez de produtividade, "
            "de investimento e de previsibilidade. Tratar isso com gasto corrente novo seria repetir "
            "o mecanismo que mantém o juro alto."
        ),
        "objetivo": (
            "Crescer de modo sustentável perto do potencial, e elevar esse potencial, sem choque "
            "inflacionário e sem truque fiscal. A meta de mandato não é um número de PIB. É um "
            "conjunto: inflação de volta ao intervalo da meta até 2028, taxa de investimento em "
            "trajetória para 19% do PIB em 2030 como ambição e não como cláusula pétrea, e nenhuma "
            "recessão provocada por experimento do próprio governo. Crescimento de 2,5% ao ano no "
            "fim do período é sucesso; 4% prometido de saída seria propaganda."
        ),
        "propostas": [
            "Respeito público e repetido à autonomia do Banco Central. O presidente não comentará a Selic da semana, não indicará maioria capturada e não usará banco público para compensar juro com crédito subsidiado escondido. A política anti-inflacionária do governo é fiscal, não telefônica.",
            "Lei do Investimento de Corredor: cinco conjuntos logísticos com orçamento plurianual, responsável nominal e cláusula de morte se o estudo de viabilidade, refeito, for negativo. Obra sem essa ficha não entra em discurso presidencial.",
            "Licenciamento federal com prazo fatal para atividade de baixo risco ambiental e silêncio positivo só nesse grupo. Alto impacto — mineração grande, óleo em área sensível, hidrelétrica nova — não tem silêncio positivo. Tem prazo de análise e veto técnico publicado, que o Planalto não derruba por telefone.",
            "Conselho de Produtividade, ligado à Casa Civil e ao Ministério da Fazenda, que todo mês de março publica a lista dos dez gargalos medidos (porto, alfândega, contencioso tributário, qualificação, energia de transmissão) e o que foi removido no ano anterior. Sem meta secreta e sem câmara setorial de amigo.",
        ],
        "instrumento": (
            "Autonomia do BC já é lei: o instrumento é não a violar. Corredores e licenciamento "
            "pedem lei ordinária e decretos regulamentares. O conselho cabe em decreto, com dever "
            "de publicar. Nada disso é emenda constitucional."
        ),
        "prazo": (
            "Decreto do conselho e portaria de prazos de licenciamento de baixo risco nos primeiros "
            "100 dias. Projeto dos corredores enviado ao Congresso até o sexto mês. Primeira lista "
            "pública de gargalos em março de 2028, com linha de base ainda em 2027."
        ),
        "custo": (
            "O conselho é despesa administrativa irrelevante. O licenciamento com prazo custa capacidade "
            "de análise no Ibama e em órgãos federais: ordem de 0,01% do PIB se for feito com gente, "
            "não com slogan. Os corredores custam sobretudo capital privado de concessão; o aporte "
            "público, quando houver, entra no eixo de infraestrutura e só depois da trava fiscal."
        ),
        "financiamento": (
            "Orçamento ordinário para a máquina de licenciamento. Concessão, debênture de infraestrutura "
            "já existente e, no caso de trecho que não se paga, verba do investimento federal condicionada "
            "à lei de renúncias. Sem essa lei, o corredor que depender de Tesouro espera."
        ),
        "indicador": (
            "IPCA anual dentro da banda em 2028 e mais perto do centro em 2029–2030 do que a mediana "
            "do Focus de outubro de 2026 sugeria para o horizonte. Taxa de investimento do IBGE. "
            "Tempo mediano de licença federal de baixo risco. Número de corredores com contrato "
            "assinado ou com arquivamento justificado — os dois contam, a eternidade não."
        ),
        "riscos": (
            "Choque externo de energia ou de tarifa pode recolocar a inflação acima do teto sem culpa "
            "da âncora fiscal. Congresso pode aprovar despesa permanente no lugar dos corredores. "
            "Silêncio positivo mal desenhado pode virar licença para dano: por isso fica restrito "
            "ao baixo risco e pode ser revogado por decreto se a auditoria do primeiro ano mostrar abuso."
        ),
        "competencia": (
            "O presidente indica diretores do BC nos termos da lei e não manda na taxa. Não decreta "
            "crescimento. Obra em estado depende de governador. Meta de inflação continua com o CMN, "
            "não com comício."
        ),
    })

    eixo(doc, 2, "Tributação e orçamento", {
        "diagnostico": (
            "A carga de 2025 foi 32,40% do PIB, com peso grande em bens e serviços. A dívida bruta "
            "já estava perto de 83% do PIB em agosto de 2026 e o mercado a via em 87% em 2027. O "
            "primário melhorou no acumulado até setembro de 2026 e ainda assim o Prisma apontava "
            "déficit do governo central. A reforma do consumo está em implantação operacional, não "
            "em debate de guardanapo. O estoque de renúncias segue politicamente intocado na prática, "
            "embora grande o bastante — historicamente, vários pontos do PIB — para financiar a "
            "diferença entre o discurso e a meta. O programa não cita um total oficial de 2026 de "
            "gastos tributários porque não reprocessou o demonstrativo linha a linha; cita a ordem "
            "de grandeza conhecida e a obrigação de publicar a lista no primeiro bimestre."
        ),
        "objetivo": (
            "Não aumentar a carga além de 32,5% do PIB como teto operacional do mandato. Entregar "
            "superávit primário do governo central de 0,5% do PIB em 2030, passando por algo não "
            "pior do que −0,25% em 2027 e zero em 2028, em cenário central. Completar IBS e CBS "
            "sem reabrir a emenda. Cortar o equivalente a 0,4 ponto do PIB em renúncias que não "
            "passem em avaliação, e usar parte disso para reduzir a contribuição patronal sobre a "
            "folha na base da remuneração, não para distribuir alívio a quem já tem benefício."
        ),
        "propostas": [
            "Lei de Revisão das Renúncias, com caducidade de quatro anos para benefício tributário federal novo e revalidação do estoque por critério publicado: quem não mostrar emprego, investimento ou pesquisa verificável perde o favor. Meta quantitativa: 0,4% do PIB até 2030, não a extinção de todo incentivo.",
            "Redução gradual de 2 pontos percentuais da contribuição patronal incidente sobre a faixa salarial até o teto do INSS, em quatro anos, só na parcela da folha, compensada peso a peso pela lei de renúncias. Sem compensação aprovada, a redução não começa.",
            "Imposto sobre grandes fortunas fica fora do programa. No lugar, o governo fecha brecha de alta renda: se, em 1º de janeiro de 2027, lucros e dividendos ainda estiverem isentos, envia projeto de alíquota de 15% com faixa de isenção anual familiar modesta e mecanismo contra bitributar o mesmo lucro já taxado na pessoa jurídica. Se a tributação de dividendos já estiver em vigor nessa data, não a eleva no primeiro biênio; audita o que passou e só então discute ajuste.",
            "Alongamento da dívida pública quando o prêmio cair, com menos peso de título pós-fixado. Isso é gestão do Tesouro, não palanque, e não será forçada se o mercado cobrar mais caro pelo prazo.",
        ],
        "instrumento": (
            "Lei complementar ou ordinária conforme a espécie do tributo. A transição do IBS/CBS "
            "já tem base constitucional: o trabalho é regulamentar e de sistemas, com a Receita e "
            "o Comitê Gestor. A trava de carga de 32,5% é compromisso de governo e, se o Congresso "
            "aceitar, diretriz da lei de diretrizes orçamentárias. Não é emenda."
        ),
        "prazo": (
            "Lista completa de renúncias publicada em até 60 dias, com responsável por cada item. "
            "Projeto de revisão enviado até o nono mês de 2027. Primeiro ponto da folha só em 2028, "
            "se a receita de substituição estiver sancionada. Superávit de 0,5% do PIB é meta de 2030, "
            "não de 2027."
        ),
        "custo": (
            "A redução de folha, na escala cheia, custa cerca de 0,20% do PIB por ano. A revisão de "
            "renúncias busca 0,40%. O líquido financia também os eixos sociais novos descritos nos "
            "volumes seguintes. Se o Congresso aprovar só metade da revisão, a folha cai 1 ponto, "
            "não 2, e os pacotes novos caem pela mesma régua."
        ),
        "financiamento": (
            "Substituição interna da carga, não aumento. Dividendos, se ainda isentos, são fonte "
            "complementar e incerta: o orçamento não conta com ela para fechar a meta. Conta com "
            "renúncia retirada e com despesa discricionária não prioritária congelada em termos reais."
        ),
        "indicador": (
            "Resultado primário do governo central, abaixo da linha do Banco Central, sem o artifício "
            "de tirar despesa da meta para comemorar. Carga tributária bruta do Tesouro. Participação "
            "da folha no custo do emprego formal, acompanhada com o Ministério do Trabalho. Estoque "
            "de renúncias em percentual do PIB, série publicada todo ano."
        ),
        "riscos": (
            "O Congresso protege renúncia com nome e sobrenome. A probabilidade de obter os 0,4 ponto "
            "inteiros é moderada-baixa; por isso os gastos novos são contingentes. Há risco de a "
            "transição do IBS gerar contencioso e perda temporária de arrecadação de estados: o "
            "governo federal não responderá a isso com alíquota paralela surpresa, e sim com o "
            "seguro de transição já previsto na emenda, auditado."
        ),
        "competencia": (
            "Tributo federal depende de lei. IBS é compartilhado com estados e municípios: o "
            "presidente não o altera por decreto. Meta fiscal depende do Congresso na lei orçamentária. "
            "O que é ato próprio: não criar despesa por medida provisória sem fonte, vetar benefício "
            "sem avaliação e publicar a lista."
        ),
    })

    eixo(doc, 3, "Emprego, trabalho e renda", {
        "diagnostico": (
            "Desocupação de 5,3% no trimestre até agosto de 2026 convive com 37,5% de informalidade "
            "no corte de novembro de 2025 a janeiro de 2026 — 38,5 milhões de pessoas. A carteira "
            "assinada privada, excluído o doméstico, estava em 39,4 milhões. O rendimento habitual "
            "bateu recorde e a desigualdade de 2025 voltou a abrir no topo. O desenho da proteção "
            "ainda trata como exceção quem trabalha por aplicativo, por conta própria ou sem CNPJ. "
            "A jornada semanal legal não é o gargalo estatístico principal; a porta de entrada na "
            "regra é."
        ),
        "objetivo": (
            "Reduzir a informalidade para baixo de 34% até 2030, sem recessão que derrube o número "
            "à força, como ocorreu em alguns trimestres de 2020 por motivo ruim. Manter o salário "
            "mínimo com ganho real apenas quando a regra fiscal e a produtividade permitirem. Não "
            "legislar jornada nacional de quatro dias."
        ),
        "propostas": [
            "Estatuto do trabalhador de plataforma: contribuição previdenciária obrigatória sobre base reduzida, seguro de acidente, direito a recurso humano contra desligamento algorítmico e transparência do critério de bloqueio. Não há vínculo empregatício automático. Há proteção. A plataforma que não recolher perde o direito de operar no mercado formal de pagamentos.",
            "Regra do salário mínimo: reajuste pela inflação mais a variação real do PIB per capita dos dois anos anteriores, com teto igual ao ganho de produtividade do trabalho formal medido pelo IBGE, e com suspensão do ganho real no ano em que a meta primária do ano anterior tiver sido descumprida. O piso constitucional de irreajustabilidade nominal pela inflação não é furado. O que se fura é a política de ganho real automático acima do que a economia e o orçamento aguentam.",
            "Licença nacional única para microempreendimento de baixo risco, prazo de dez dias, integrada ao que a transição do Simples, do IBS e da CBS já estiver exigindo em 2027. Não se eleva o teto do Simples sem a compensação da lei de renúncias.",
            "Negociação coletiva segue livre, sem volta da contribuição sindical obrigatória. O Ministério do Trabalho digitaliza o registro de acordo e publica, por setor, quantos acordos reduziram jornada com manutenção de salário — para que a redução exista onde a produtividade pagou, não onde a lei fingiu que pagou.",
        ],
        "instrumento": (
            "O estatuto de plataforma é lei ordinária. A regra do mínimo pode caber em lei ordinária "
            "que discipline a política de valorização; se o desenho vigente na posse for constitucionalmente "
            "amarrado de outro modo, o governo envia a alteração e, até lá, executa o ganho real só "
            "na parcela que a meta fiscal comportar, dizendo o número em vez de escondê-lo. A licença "
            "de dez dias é lei e integração de sistemas."
        ),
        "prazo": (
            "Projeto de plataforma nos primeiros nove meses. Nova política de mínimo válida para o "
            "reajuste de 2028, não como surpresa em janeiro de 2027. Licença única pilotada em 2027 "
            "e nacional em 2028 se o piloto não aumentar fraude cadastral."
        ),
        "custo": (
            "A contribuição de plataforma tende a aumentar receita previdenciária no médio prazo e "
            "a custar fiscalização. O ganho real mais contido do mínimo reduz pressão no INSS e no "
            "BPC relativamente a uma regra mais generosa — é economia contra um contrafactual, não "
            "corte nominal de benefício de quem já recebe. Não há promessa de abono novo."
        ),
        "financiamento": (
            "Dentro da folha e da contribuição. Sem fundo paralelo. A formalização é o financiamento."
        ),
        "indicador": (
            "Taxa de informalidade da PNAD, meta abaixo de 34% em 2030, com o emprego total não "
            "caindo. Número de trabalhadores de plataforma contribuintes. Diferença entre o reajuste "
            "do mínimo e a inflação, publicada contra a regra, não contra o desejo do ano eleitoral."
        ),
        "riscos": (
            "Plataformas podem repassar custo ao trabalhador ou sair de nichos. O recurso contra "
            "algoritmo pode virar contencioso de massa se a lei for vaga: o projeto terá prazo de "
            "resposta e tipologia fechada de infração. Centrais sindicais chamarão a regra do mínimo "
            "de arrocho sempre que o ganho real for zero. O governo preferirá esse conflito a estourar "
            "o RGPS para aplauso de um maio."
        ),
        "competencia": (
            "Direito do trabalho é federal. Salário de servidor estadual não é. Fiscalização do "
            "trabalho é da União; a formalização de fato depende de município na licença local, "
            "por isso a licença única precisa de adesão — quem não aderir não recebe prioridade "
            "de convênio federal de emprego."
        ),
    })

    eixo(doc, 4, "Saúde", {
        "diagnostico": (
            "O SUS existe, gasta e entrega mais cirurgia eletiva do que em 2022, se confirmado o "
            "número de quase 15 milhões em 2025 dado pelo próprio Ministério da Saúde. A União "
            "cumpriu o mínimo constitucional em 2025, com R$ 234,5 bilhões. Ao mesmo tempo, a "
            "tabela de procedimentos envelheceu quase 30 anos, o painel nacional de filas ainda "
            "era promessa de fim de 2026 na entrevista de 16 de outubro, e a atenção básica segue "
            "desigual no Norte e na periferia. Saúde mental e vacinação não têm, neste plano, meta "
            "numérica inventada: têm obrigação de publicar cobertura e capacidade de CAPS por "
            "região no primeiro ano, porque a linha de base nacional confiável não foi reunida aqui."
        ),
        "objetivo": (
            "Manter o SUS público e universal. Encurtar a espera de procedimento eletivo prioritário "
            "onde a fila for medida, não onde for anedota. Atualizar a tabela sem quebrar o teto "
            "fiscal. Tratar saúde mental como rede, não como internação de longa duração de volta."
        ),
        "propostas": [
            "Nos primeiros 100 dias, o painel de filas — se o governo de então o tiver entregue — vira linha de base oficial, auditada pela CGU em amostra. Se não tiver sido entregue, o ministério publica em 120 dias a espera dos procedimentos de maior volume nos serviços federais e nos contratados com recurso federal, e condiciona repasse voluntário de 2028 à alimentação do painel pelos entes.",
            "Mutirão comprado de capacidade privada e filantrópica, com teto de preço, auditoria prévia e lista nominal de paciente, apenas para a fila já medida. Não é abertura do SUS ao plano de saúde. É a União pagando cirurgia que o público local não zera, por contrato curto. Escala cheia só com a trava fiscal; piloto de qualquer modo em pelo menos uma região do Norte e uma capital do Nordeste.",
            "Revisão da tabela SUS em 24 meses, por grupo de procedimentos, com impacto fiscal explicitado na lei orçamentária. O que não couber não é «reajustado politicamente»; fica para o ano seguinte, dito em público.",
            "Vacinação: compra federal plurianual dos calendários já previstos, para acabar com a ruptura de estoque como modo de gestão. Saúde mental: cofinanciar CAPS e leito de curta permanência em crise nos municípios abaixo da cobertura mediana, e recusar a reabertura de hospital psiquiátrico asilar como política nacional.",
        ],
        "instrumento": (
            "Repasse e contrato são atos do Executivo dentro da lei do SUS. Condicionar transferência "
            "voluntária exige lei ou convênio com cláusula clara, não retaliação informal. Mudança "
            "de tabela é portaria com lastro orçamentário. Nada aqui privatiza o sistema; nada aqui "
            "exige emenda."
        ),
        "prazo": (
            "Linha de base em 2027. Primeiros mutirões ainda em 2027, em piloto. Tabela refeita "
            "até o fim de 2028 nos grupos de maior fila. Cobertura vacinal de rotina publicada "
            "mês a mês a partir do segundo semestre de 2027."
        ),
        "custo": (
            "Pilotos de mutirão e atualização parcial da tabela: começar em torno de 0,05% do PIB "
            "e só expandir até cerca de 0,10% se a lei de renúncias passar e se o painel mostrar "
            "queda real de espera, não apenas aumento de procedimento em quem já era atendido."
        ),
        "financiamento": (
            "Piso constitucional de saúde em primeiro lugar. A margem nova vem da trava fiscal, "
            "não de contribuição criada sobre o paciente. Operadora de plano não recebe o mutirão "
            "para sua própria carteira."
        ),
        "indicador": (
            "Mediana de espera dos dez procedimentos definidos no painel de 2027, meta de queda de "
            "20% até 2030 onde a série existir. Cobertura vacinal infantil das vacinas do calendário "
            "nacional de volta à meta do Programa Nacional de Imunizações nos estados que estiverem "
            "abaixo dela em 2027. Número de CAPS por 100 mil habitantes nos municípios do quartil "
            "inferior, sem meta nacional vazia."
        ),
        "riscos": (
            "Compra de mutirão pode vazar para duplicidade e para prestador sem qualidade. A lista "
            "nominal e a auditoria são a resposta, e serão caras. Estados podem boicotar o painel "
            "para não mostrar a fila. O repasse voluntário condicionado é o instrumento; o piso "
            "constitucional não será refém dessa briga."
        ),
        "competencia": (
            "Saúde é tripartite. O presidente não nomeia secretário municipal e não opera UBS. "
            "Opera política nacional, hospitais federais, compra estratégica e o dinheiro. A vice, "
            "Lúcia Okamoto, acompanha este eixo no palácio, sem acumulá-lo com o ministério: quem "
            "opera a pasta é ministro em dedicação exclusiva."
        ),
    })

    eixo(doc, 5, "Educação", {
        "diagnostico": (
            "O Ideb de 2025 mostrou o melhor ponto da série e, ao mesmo tempo, o fracasso relativo "
            "dos anos finais (5,3 contra meta 5,5) e do ensino médio público (4,3). O PISA 2022, "
            "última onda internacional consultada, deixou 73% dos alunos abaixo do nível básico de "
            "matemática. A União gastou acima do mínimo constitucional em 2025. O problema não é "
            "a inexistência de escola. É que a criança pobre atravessa o fundamental sem o domínio "
            "que o resto do plano precisa para existir: ler, calcular, terminar."
        ),
        "objetivo": (
            "Toda criança alfabetizada ao fim do 2º ano, medida por avaliação censitária, não por "
            "declaração da rede. Ensino médio público com meta de Ideb e de proficiência publicada "
            "por estado, sem prometer nota 7 em quatro anos. Pesquisa com orçamento que não suma "
            "num contingenciamento de agosto."
        ),
        "propostas": [
            "Avaliação censitária de leitura ao fim do 2º ano, a partir de 2028, com devolutiva por escola para a rede e versão pública por município. Estado ou município que piorar sem guerra, enchente ou epidemia documentada recebe assistência técnica federal obrigatória, não perda de Fundeb. Aluno não é punido por nota de sistema.",
            "Complemento federal temporário, por quatro anos, para professor alfabetizador em escola pública abaixo do corte de proficiência, pago como bolsa de dedicação e formação, não como reajuste geral nacional de piso — o piso continua lei própria. Escala cheia contingente à trava fiscal; piloto em 2027 nos estados de pior desempenho do Ideb dos anos iniciais.",
            "Ensino integral só onde houver sala e professor. Meta condicional: 1 milhão de novas matrículas integrais até 2030 se o Fundeb e a adesão local comportarem. Onde não houver prédio, a prioridade é alfabetização em turno único decente, não o anúncio de escola de tempo integral no papel.",
            "Ensino médio: português, matemática e um itinerário técnico com institutos federais, Sistema S e redes estaduais, em vez de grade encyclopédica nova. Universidade pública segue gratuita. A expansão de campus novo fica suspensa no mandato; o dinheiro vai para concluir obra parada, curso noturno e permanência, medida por evasão. Fies apenas com pagamento contingente à renda e com curso acima de um piso de qualidade no Enade. Cotas raciais e sociais já existentes em universidade e serviço público federais são mantidas no mandato e avaliadas em 2029; não há cota obrigatória nova para empresa privada.",
        ],
        "instrumento": (
            "Avaliação pode ser instituída pelo Inep com lei ou com reformulação de exame já "
            "autorizado; o governo preferirá lei curta para evitar disputa de atribuição. Bolsa de "
            "alfabetizador é lei com dotação. Fundeb é constitucional e não será reaberto. Pesquisa: "
            "piso real de CNPq e Capes na lei orçamentária, por compromisso de execução, não por emenda."
        ),
        "prazo": (
            "Desenho da avaliação em 2027, primeira aplicação censitária em 2028. Piloto de "
            "alfabetizadores em 2027. Decisão sobre campus novos: imediata, é uma suspensão. "
            "Relatório de cotas em 2029."
        ),
        "custo": (
            "Bolsa de alfabetização e apoio à avaliação, na escala cheia, em torno de 0,15% do PIB "
            "no fim do mandato, maior item social novo do programa junto com saneamento focalizado. "
            "Sem a lei de renúncias, o piloto cabe em menos de um terço disso, dentro da educação já financiada."
        ),
        "financiamento": (
            "Mínimo constitucional de educação primeiro. Margem nova: trava fiscal. Não haverá "
            "contribuição educacional extra sobre folha."
        ),
        "indicador": (
            "Percentual de crianças no nível adequado de leitura ao fim do 2º ano, quando a série "
            "passar a existir — a meta política é a maioria absoluta das crianças das redes públicas "
            "nesse nível em 2030, e o programa admite que partir de uma base ruim torna isso difícil. "
            "Ideb dos anos finais pelo menos na meta que hoje é 5,5. Evasão no médio público em queda. "
            "Execução real de CNPq/Capes não inferior à dotação corrigida pela inflação de 2026."
        ),
        "riscos": (
            "Avaliação censitária será chamada de ranqueamento punitivo. O desenho — sem corte de "
            "Fundeb e sem exposição humilhante de criança — é a resposta, e pode não bastar politicamente. "
            "Complemento salarial federal pode virar penduricalho permanente: a lei terá morte em 2030, "
            "só renovada por outra lei se o indicador mover."
        ),
        "competencia": (
            "A sala de aula do fundamental é de município e de estado. A União não nomeia professor "
            "da rede local nem impõe método único por decreto. Impõe avaliação, dinheiro condicionado "
            "e exemplo nos institutos federais. Universidade federal é da União: aí a suspensão de "
            "campus novo é ato próprio, respeitada a autonomia acadêmica do que já existe."
        ),
    })

    eixo(doc, 6, "Segurança pública", {
        "diagnostico": (
            "Em 2025 o Brasil teve 40.775 mortes violentas intencionais, taxa de 19,1 por 100 mil, "
            "a menor da série desde 2012, e 32.914 homicídios dolosos, taxa de 15,4. A queda é fato. "
            "Também é fato o recorde de 1.571 feminicídios e a alta das mortes por intervenção policial, "
            "6.602 numa das aberturas publicadas, cerca de 6% acima do ano anterior. Norte e Nordeste "
            "concentram as piores taxas. Facção segue organizando presídio, fronteira e mercado de "
            "droga. A Polícia Militar é estadual: qualquer plano federal que fale como se o presidente "
            "comandasse a ronda mente."
        ),
        "objetivo": (
            "Manter a queda de mortes violentas e inverter a alta de feminicídios e de letalidade "
            "policial. Subir a elucidação de homicídio nos dez estados de pior desempenho. Separar "
            "facção dentro do presídio que receba recurso federal. Não decretar guerra às drogas "
            "contra usuário e não tratar organização criminosa como questão social apenas."
        ),
        "propostas": [
            "Fundo federal de inteligência e de presídio só para estado que separar facções em unidades distintas, alimentar o sistema nacional de informações e publicar letalidade policial mês a mês. Quem não aderir não perde a polícia; perde o dinheiro voluntário.",
            "Câmera corporal obrigatória nas unidades táticas que recebam recurso federal, com cadeia de custódia e perda de repasse se a câmera «não funcionar» de modo sistemático em morte decorrente de intervenção. Não é meta de corpo. É meta de prova.",
            "Feminicídio: cofinanciar núcleo especializado de investigação e tornozeleira com dever de resposta em horas à violação de medida protetiva, nos municípios de maior taxa. A linha de base é 1.571 mortes em 2025. A meta é quebrar a série de recordes até 2028 e reduzir o número absoluto até 2030. Zero não será prometido.",
            "Fronteira: centros integrados em rios da Amazônia e nos eixos de entrada do arco norte e da faixa central, com Polícia Federal, PRF e Forças Armadas em papel subsidiário, por decreto com prazo. O alvo é a logística da facção — arma, combustível, dinheiro —, não o ribeirinho.",
            "Drogas, neste eixo apenas o ponto de segurança: cocaína, crack e sintéticos seguem como crime de organização, com perdimento de bens acelerado por lei. Cannabis para adulto é regulada no eixo das decisões controversas e não é anistia de tráfico.",
        ],
        "instrumento": (
            "Convênio e fundo são lei orçamentária e lei ordinária. Câmera em polícia estadual não "
            "se impõe por decreto a quem recusa o dinheiro. Garantia da Lei e da Ordem só com decreto "
            "formal, prazo curto e protocolo de morte publicado; não é política permanente. Maioridade "
            "penal é emenda e está no eixo de justiça, não se finge que seja portaria."
        ),
        "prazo": (
            "Sala nacional de homicídio e feminicídio com os estados, em 30 dias, mesmo antes de lei. "
            "Projeto do fundo nos primeiros seis meses. Primeiros centros de fronteira contratados "
            "até o fim de 2028. Curva de feminicídio julgada em 2028 e em 2030."
        ),
        "custo": (
            "Ordem de 0,08% do PIB no fim do período, somando fundo, tornozeleira, câmera e fronteira, "
            "se a trava fiscal liberar a escala. Piloto de fronteira e de núcleos de feminicídio cabe "
            "no orçamento de segurança já existente e começa de qualquer modo."
        ),
        "financiamento": (
            "Orçamento da União mais contrapartida estadual. Perdimento de bens de crime entra no "
            "fundo, mas o orçamento não conta com essa receita como se fosse certa: crime esconde ativo."
        ),
        "indicador": (
            "Taxa nacional de mortes violentas intencionais abaixo de 17 por 100 mil em 2030, sem "
            "alta de subregistro — a série do Fórum e a do DataSUS de óbitos por agressão terão de "
            "andar juntas. Feminicídios em número absoluto menor em 2030 do que em 2025. Letalidade "
            "policial em queda nos estados aderentes. Elucidação: publicar a taxa no primeiro ano "
            "e subi-la 5 pontos nos dez piores até 2030. Se a taxa de elucidação de partida nem "
            "existir de modo comparável, o primeiro indicador é passá-la a existir."
        ),
        "riscos": (
            "Repressão pode aumentar mortes policiais antes de reduzir homicídio. O corte de dinheiro "
            "para quem não filma é a trava, e governadores podem preferir o discurso à câmera. "
            "Separar facção em presídio provoca motim: o plano precisa de vaga federal e de calendário, "
            "não de anúncio de terça com transferência na quarta."
        ),
        "competencia": (
            "Polícia civil e militar: estados. Polícia Federal, PRF, presídio federal, fronteira e "
            "Forças Armadas: União, esta última em missão definida. O presidente não escolhe "
            "delegado de homicídio da capital e não deve fingir que escolhe."
        ),
    })

    eixo(doc, 7, "Justiça e instituições", {
        "diagnostico": (
            "O contencioso brasileiro é lento onde a vida econômica e a vida penal precisam de "
            "resposta: execução fiscal, terra, crime organizado, corrupção de colarinho. O sistema "
            "de justiça é independente e deve continuar. O problema não é falta de instituição. É "
            "excesso de processo repetido, prova que não chega e, no outro extremo, a tentação "
            "política de enfraquecer juiz e procurador quando a investigação sobe a rampa."
        ),
        "objetivo": (
            "Mais elucidação e mais perdimento de produto de crime, com garantia intacta. Menos "
            "tempo no contencioso tributário de massa. Nenhuma anistia de corrupção como moeda de "
            "coalizão. Emenda estreita da maioridade penal apenas para crime hediondo, em regime "
            "separado, sabendo que pode não passar."
        ),
        "propostas": [
            "Emenda constitucional: responsabilidade penal aos 16 anos somente para homicídio doloso, latrocínio, estupro e roubo com resultado morte, em estabelecimento separado do presídio adulto e do internato comum, com revisão obrigatória dos efeitos aos 36 meses. O Estatuto da Criança e do Adolescente permanece para o resto. Lúcia Okamoto registra divergência de ênfase: aceita a separação e a revisão; não fará campanha entusiasmada pela emenda. A chapa ainda assim a envia, porque Elias a considera devida e porque escondê-la seria pior.",
            "Lei de perdimento administrativo acelerado de bem já vinculado a organização criminosa, com contraditório e juiz, sem confisco sumário de patrimônio familiar não conectado. Meta de processo: reduzir pela metade o tempo mediano entre apreensão e destinação nos casos federais até 2030.",
            "Mutirão do contencioso tributário federal de baixo valor e consolidação do que já foi decidido de modo repetido no Carf e nos tribunais, por súmula administrativa vinculante onde a lei permitir, e por projeto de súmula legal onde não permitir. A intenção é tirar empresa pequena de uma fila de anos, não perdoar grande devedor.",
            "Transparência de acordos de leniência: valor, prazo e sócio beneficiado em base pública, ressalvado o que for diligência aberta. CGU e Polícia Federal não perdem atribuição. Não haverá projeto para intimidar o Ministério Público sob o nome de abuso de autoridade além de uma consolidação técnica das dúvidas já existentes, sem pena nova contra juiz por interpretação.",
        ],
        "instrumento": (
            "Maioridade: emenda, três quintos, dois turnos, duas casas. Com 8% das cadeiras, a "
            "probabilidade é baixa. O resto do eixo não depende dela. Perdimento e contencioso: "
            "lei ordinária. Transparência de leniência: decreto e, onde esbarrar em sigilo legal, lei."
        ),
        "prazo": (
            "Emenda apresentada no primeiro ano, sem tratá-la como fato consumado. Lei de perdimento "
            "no primeiro ano. Base de leniência em 180 dias para os acordos já assinados que a lei "
            "permitir revelar."
        ),
        "custo": (
            "Estabelecimentos separados para o regime de 16 anos, se a emenda passar, exigem investimento "
            "com estados: ordem de algumas centenas de milhões por ano, não de ponto de PIB, e só "
            "depois da emenda. Sem emenda, custo zero nesse item. Mutirão tributário é custo de "
            "servidor já existente, reorganizado."
        ),
        "financiamento": (
            "Orçamento da Justiça e transferências penitenciárias. Sem taxa judiciária nova sobre o pobre."
        ),
        "indicador": (
            "Se a emenda passar: reincidência do grupo aos 36 meses comparada à do internato atual, "
            "publicada mesmo se for pior — esse é o gatilho de revisão. Tempo mediano de destinação "
            "de bem apreendido na Justiça Federal. Estoque de processos tributários federais de "
            "valor inferior ao corte definido em 2027."
        ),
        "riscos": (
            "A emenda pode ser alargada no Congresso para um pacote penal que Elias vetará se alcançar "
            "crime não hediondo ou mistura com adulto. O perdimento acelerado pode atingir terceiro "
            "de boa-fé: o contraditório não é enfeite. Súmula tributária mal feita consolida erro; "
            "por isso só entra com precedente judicial estável."
        ),
        "competencia": (
            "O presidente não manda em juiz, em procurador nem em delegado de estado. Propõe lei, "
            "sanciona, veta e organiza a polícia e a advocacia públicas federais. Defensoria da "
            "União será fortalecida em terra e em execução penal federal, ato orçamentário próprio."
        ),
    })

    eixo(doc, 8, "Defesa nacional", {
        "diagnostico": (
            "O Brasil tem fronteira longa, Amazônia de difícil presença, mar e cabo submarino, e "
            "Forças Armadas profissionais sob comando civil. Não tem ameaça estatal iminente de "
            "invasão clássica na data-base, e tem ameaça real de crime transfronteiriço, de ataque "
            "cibernético e de soberania declarada sem sensor que a sustente. Este diagnóstico não "
            "crava o percentual exato do PIB gasto em defesa em 2026, porque não reprocessou o "
            "orçamento militar fechado; trata o patamar histórico recente, perto de pouco mais de "
            "1% do PIB, como ordem de grandeza a confirmar no primeiro mês de governo com o número "
            "oficial, não como casa decimal de comício."
        ),
        "objetivo": (
            "Elevar gradualmente o esforço de defesa em direção a 1,5% do PIB até 2030, só na medida "
            "em que a regra fiscal permitir, e mudar a composição: mais monitoramento, rio, satélite, "
            "cibernética e manutenção; menos projeto de prestígio sem peça de reposição. Comando "
            "civil mantido. Serviço militar obrigatório não será ampliado."
        ),
        "propostas": [
            "Programa de presença na Amazônia: sensores, embarcações de patrulha, destacamentos de fronteira já previstos e integração com o centro do eixo de segurança. As Forças não substituem a Polícia Federal. Fecham o vazio onde hoje só a facção tem logística.",
            "Comando cibernético sob o Ministério da Defesa, com autoridade civil, relatório público anual de incidentes contra a administração federal e separação clara entre defesa de rede pública e qualquer tentação de vigiar opositor. Vigilância política é causa de demissão.",
            "Satélite e indústria: continuar programas duais já contratados, com offset publicado e sem contrato secreto de conteúdo nacional que só beneficie um estaleiro amigo. Auditoria do que estiver atrasado nos primeiros 180 dias; o que não tiver peça e prazo é renegociado ou encerrado.",
            "Pensões militares: projeto de lei para militares que entrarem depois da sanção, com contribuição mais alta e regra mais próxima da civil, sem mexer em direito adquirido de quem já está na carreira. É proposta consciente de conflito com a corporação."
        ],
        "instrumento": (
            "Orçamento anual e plurianual. Missão subsidiária: decreto e lei de emprego das Forças. "
            "Pensão de futuro entrante: lei ordinária, possivelmente com disputa constitucional se "
            "tocar em regime próprio de modo amplo — o projeto será desenhado para não alcançar "
            "quem já ingressou."
        ),
        "prazo": (
            "Auditoria dos grandes projetos em 180 dias. Primeiro ciclo de patrulha fluvial ampliada "
            "em 2027–2028. Meta de 1,5% do PIB é de chegada em 2030 e pode não se cumprir se o "
            "primário exigir escolha; nesse caso, preserva-se Amazônia e cibernética e adia-se o resto."
        ),
        "custo": (
            "Ir de pouco mais de 1% em direção a 1,5% do PIB é aumento relevante, da ordem de alguns "
            "décimos do PIB, e por isso é condicionado. Não entra na lista do que fura a trava fiscal. "
            "Se a trava não abrir, o aumento real fica próximo de zero e a composição interna é que muda."
        ),
        "financiamento": (
            "Orçamento da Defesa, sem imposto novo e sem contribuição de emergência. Offset não é "
            "financiamento; é condição de compra."
        ),
        "indicador": (
            "Percentual de municípios da faixa de fronteira amazônica com cobertura de comunicação "
            "e tempo de resposta de patrulha publicado, linha de base em 2027. Número de incidentes "
            "cibernéticos graves na rede federal com recuperação dentro do prazo definido pelo "
            "comando. Relatório de projetos de defesa com custo, atraso e decisão de continuar ou parar."
        ),
        "riscos": (
            "Meta de gasto militar vira lobby de projeto caro. A condicionalidade fiscal e a auditoria "
            "de 180 dias existem para isso. Emprego interno das Forças em segurança, se banalizado, "
            "desgasta comando civil: cada GLO terá prazo e autópsia pública."
        ),
        "competencia": (
            "As Forças são da União. O presidente é o comandante supremo e não é o gerente de "
            "batalhão. Polícia de rua continua com o estado. Defesa não será usada como atalho "
            "para o eixo 6."
        ),
    })

    eixo(doc, 9, "Infraestrutura e transporte", {
        "diagnostico": (
            "A taxa de investimento de 16,8% do PIB não constrói o país que a soja, o minério, a "
            "indústria e a cidade exigem. Rodovia leva carga que ferrovia e rio deveriam levar. "
            "Porto e acesso urbano a porto seguem como gargalo conhecido, mesmo sem um índice único "
            "de 2026 citado aqui como verdade definitiva. Concessão avançou em ciclos anteriores e "
            "convive com contrato ruim, tarifa política e obra inaugurada sem manutenção. Mobilidade "
            "urbana depende de prefeito e de governador; a União que espalha metrô em discurso sem "
            "projeto executivo só cria expectativa e aditivo."
        ),
        "objetivo": (
            "Cinco decisões logísticas tomadas — contrato ou arquivamento — até 2029. Menos "
            "promessa de mapa, mais carga fora do caminhão onde o custo social do caminhão for "
            "maior. Concessão com indicador de serviço, não só com desconto de outorga."
        ),
        "propostas": [
            "Corredor 1, Tapajós–Amazônia: prioridade a hidrovia, dragagem contratada com estudo ambiental e acesso rodoviário de manutenção ao porto, no lugar de forçar a Ferrogrão nos dois primeiros anos. A ferrovia só volta à mesa em 2029 se consulta a povos afetados e o licenciamento tiverem sido refeitos e se a conta de emissão e de morte na estrada justificar o traçado. Até lá, não haverá canteiro político.",
            "Corredor 2: concluir gargalos da Ferrovia Norte-Sul que ainda interrompam a ligação útil, depois de auditoria do que está pronto e do que é só terrapleno. Corredor 3: FIOL e Porto Sul apenas se a auditoria de demanda e de contrato, em 2027, fechar sem subsídio oculto; se não fechar, o governo diz não.",
            "Corredor 4: acessos ferroviários curtos ao porto de Santos, por concessão, com o estado de São Paulo. Corredor 5: escoamento do Nordeste já estudado — não uma ferrovia nova desenhada em comício — mais a distribuição da transposição do São Francisco onde o canal existir e a rede de irrigação não. Água de transposição sem ramal é obra pela metade.",
            "Mobilidade: o orçamento federal voluntário de transporte urbano só entra em metrô, VLT ou BRT com projeto executivo, licença e contrapartida. Não financia estádio, passeio nem teleférico sem demanda medida.",
        ],
        "instrumento": (
            "Concessão e PPP são lei existente, mais edital. Dizer não à Ferrogrão no biênio é "
            "decisão de governo, não emenda. Completar ferrovia pode exigir verba na lei orçamentária "
            "e acordo com o Tribunal de Contas sobre contrato heredado. Tudo isso é federal onde a "
            "infraestrutura for federal, e compartilhado onde o porto ou o metrô forem de estado."
        ),
        "prazo": (
            "Auditoria dos cinco corredores no primeiro ano. Editais ou arquivamentos até 2029. "
            "Nenhum corredor «em estudo» pode permanecer assim em discurso depois dessa data sem "
            "uma página pública de motivo."
        ),
        "custo": (
            "O grosso é capital privado. Aporte público contingente, somado, não deve passar de "
            "cerca de 0,15% do PIB por ano no pico, e só com a trava fiscal. Dragagem e manutenção "
            "rodoviária de acesso são o mínimo que começa mesmo sem a escala cheia, dentro do "
            "orçamento de transporte já existente, reordenado — o que significa abandonar obra "
            "espalhada sem ficha."
        ),
        "financiamento": (
            "Outorga, tarifa, debênture de infraestrutura e Tesouro apenas no trecho que a tarifa "
            "não paga e que o estudo social justificar. Sem crédito subsidiado de banco público "
            "fora do orçamento."
        ),
        "indicador": (
            "Participação de ferrovia e hidrovia na carga geral, série do Ministério dos Transportes, "
            "em alta até 2030. Tempo de acesso rodoviário aos terminais escolhidos. Número de "
            "corredores com decisão tomada. Mortes em rodovia federal nos trechos de acesso duplicados "
            "ou mantidos, em queda — obra logística também se mede em corpo."
        ),
        "riscos": (
            "Dizer não à Ferrogrão custa apoio político no Centro-Oeste e no Pará. Dizer sim sem "
            "licença custa tribunal e floresta. O calendário de 2029 é a forma de não transformar "
            "a dúvida em paralisia eterna nem em fita antecipada. Concessão pode falhar se o edital "
            "mentir a demanda: a auditoria prévia é inegociável, e ainda assim pode errar."
        ),
        "competencia": (
            "Estrada estadual e ônibus urbano não são do presidente. A União condiciona dinheiro "
            "voluntário e opera a malha federal. Governador que quiser bandeira de metrô sem projeto "
            "não terá a bandeira financiada."
        ),
    })

    eixo(doc, 10, "Energia e recursos naturais", {
        "diagnostico": (
            "O Brasil é potência em hidroeletricidade, cresce em eólica e solar, e produz petróleo "
            "relevante — a extrativa ajudou a indústria em 2025. A transmissão, não a placa isolada, "
            "é o gargalo típico da renovável. O nuclear civil está incompleto. A margem equatorial "
            "é objeto de disputa entre licenciamento e pressa política. Mineração critica o mundo "
            "e o país, e também critica terra indígena quando alguém sugere abri-la. O programa "
            "separa essas decisões em vez de dissolvê-las num «equilíbrio»."
        ),
        "objetivo": (
            "Segurança energética sem rombo tarifário e sem telefonema sobre licença. Nuclear com "
            "teto. Óleo onde o órgão ambiental disser sim, e em nenhum lugar onde disser não. "
            "Renovável conectada à rede. Nenhuma mineração em terra indígena."
        ),
        "propostas": [
            "Angra 3: nos primeiros seis meses, auditoria independente com acompanhamento do TCU define teto real e ponto de não retorno. Abaixo do teto, a obra anda com cronograma público. Estouro superior a 25% antes desse ponto encerra o projeto. Não haverá decisão de nova grande usina nuclear antes de 2029. Estudo de reator modular fica no papel, em instituição pública, sem encomenda de canteiro.",
            "Margem equatorial e blocos sensíveis: a ANP pode estudar e o Ibama decide no mérito técnico. O presidente não determinará aprovação nem rejeição. Se a licença sair, a exploração obedece a condição. Se não sair, o governo não troca o presidente do órgão para fazer sair.",
            "Transmissão: manter leilões e priorizar as linhas que conectam renovável já contratada e que reduzem restrição de geração. Térmica a gás permanece como backup de ponta, não como base permanente subvencionada.",
            "Petrobras continua empresa de economia mista, com governança e diretoria técnica, sem congelamento político permanente de preço e sem ordem de investir onde o custo de capital não fechar. Conteúdo local será realista, medido em prática de fornecimento, não em percentual de vitrine que atrasa plataforma. Participação da União na renda do pré-sal segue a lei; a parte federal não será totalmente consumida em gasto corrente: uma fração definida na lei orçamentária, modesta e explícita, vai ao fundo de produtividade dos corredores quando a trava fiscal permitir.",
        ],
        "instrumento": (
            "Angra 3 é decisão de governo e de orçamento da estatal do setor nuclear, com o Congresso "
            "se houver aporte. Licenciamento é ato do Ibama. Leilão de transmissão é atribuição "
            "federal já existente. Mudança de governança da Petrobras que exija lei será enviada; "
            "o que for estatuto e indicação, o acionista controlador faz, sob a lei das estatais."
        ),
        "prazo": (
            "Auditoria de Angra 3 no primeiro semestre de 2027. Decisão de continuar ou parar no "
            "segundo semestre. Estudos de margem equatorial no tempo do Ibama, sem prazo político. "
            "Nenhuma usina nuclear nova licitada no mandato, além da decisão sobre Angra 3."
        ),
        "custo": (
            "Angra 3 já tem custo afundado e custo futuro incerto: exatamente por isso o teto vem "
            "antes da fita. O programa não publica um valor de conclusão que não auditou. Transmissão "
            "se paga na tarifa. Estudo modular é despesa de pesquisa, pequena, dentro do eixo de ciência."
        ),
        "financiamento": (
            "Tarifa, capital da empresa e, somente com teto e auditoria, aporte público explicitado. "
            "Sem encargo escondido na conta de luz para inauguração."
        ),
        "indicador": (
            "Decisão publicada sobre Angra 3 com custo auditado. Geração renovável cortada por falta "
            "de rede, em queda. Preço de combustível sem defasagem artificial prolongada — a série "
            "será mostrada, e o governo aceitará a crítica quando segurar preço além do colchão de "
            "caixa que a diretoria técnica recomendar. Zero título minerário novo em terra indígena."
        ),
        "riscos": (
            "Parar Angra 3 tem custo político e custo afundado. Continuar sem teto tem custo tarifário "
            "por década. As duas críticas virão; o programa escolhe a segunda só se o número couber. "
            "Licença da margem equatorial descontentará um dos lados de qualquer modo. Esse descontentamento "
            "é preferível à captura do Ibama."
        ),
        "competencia": (
            "Política energética é fortemente federal. Distribuição de gás canalizado e taxa local "
            "não são. O presidente não fixa o preço da gasolina por live. Meio ambiente federal "
            "licencia o que for de competência federal; estado licencia o resto, sem aval de palácio."
        ),
    })

    p(
        doc,
        "Os eixos 11 a 20 — agro e ambiente, cidades, previdência, ciência, Estado, cultura, "
        "direitos, regiões, comércio e reforma política — estão no volume 06, com a mesma trava "
        "fiscal e os mesmos números deste diagnóstico.",
    )
    save(doc, os.path.join(OUT, "05_PLANO_EIXOS_01_A_10.docx"))
    print("vol 05 ok")


if __name__ == "__main__":
    build()
