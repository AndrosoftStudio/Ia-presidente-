# -*- coding: utf-8 -*-
"""Volume 09 — promessas, fisco e governabilidade."""
import os, sys
sys.path.insert(0, "/workspace/candidatura")
from docx_theme import bullets, cover, h, new_doc, p, save, table

OUT = "/workspace/candidatura/docx"


def build():
    doc = new_doc()
    doc.core_properties.title = "09 — Promessas, orçamento e governabilidade"
    cover(
        doc,
        "VOLUME 09",
        "Vinte e cinco promessas, plano fiscal e modo de governar",
        "Probabilidade nenhuma é 100%. Dinheiro nenhum é infinito. Minoria de 8% não vira maioria por retórica.",
    )

    h(doc, 1, "1. As 25 promessas")
    p(
        doc,
        "A probabilidade é juízo político do próprio programa sobre a chance de cumprir o indicador "
        "no prazo, não pesquisa. Ela já desconta o Congresso hostil, o federalismo e o erro de "
        "execução. Promessa de ato próprio do Executivo tem probabilidade maior do que promessa "
        "que é emenda constitucional.",
    )

    h(doc, 2, "Primeiros 100 dias")
    table(
        doc,
        ["#", "Promessa", "Resultado", "Medida", "Custo", "Indicador", "Prob."],
        [
            ["1", "Lista pública de renúncias", "Cada favor fiscal federal com valor, beneficiário-tipo e responsável", "Ato da Receita e da Fazenda", "Administrativo", "Lista no Diário Oficial em 60 dias", "75% — depende de dado interno, não de voto"],
            ["2", "Sala de homicídio e feminicídio", "Estados na mesma mesa, série semanal", "Decreto e convite; adesão é voluntária", "Baixo", "Pelo menos 20 UFs alimentando a série em 100 dias", "60% — governador pode recusar"],
            ["3", "Linha de base do SUS", "Fila medida ou confissão de que o painel não existe", "Portaria; CGU amostra", "Baixo", "Documento público com procedimento e espera", "70%"],
            ["4", "Prazo de licença de baixo risco", "Relógio correndo no Ibama federal", "Decreto", "Baixo; custa gente depois", "Decreto publicado e fila classificada", "80%"],
            ["5", "Auditoria de Angra 3 contratada", "Teto em construção, não em slogan", "Contrato com acompanhamento do TCU", "Dezenas de milhões, não ponto de PIB", "Contrato assinado e escopo público", "75%"],
            ["6", "Diretriz ao Itamaraty", "Embaixada sabe o voto-tipo dos conflitos do volume 07", "Instrução presidencial escrita", "Nulo", "Telegrama-síntese publicado em versão ostensiva", "90%"],
            ["7", "PEC da não reeleição protocolada", "Texto no Congresso, eficácia só para o futuro", "Mensagem presidencial", "Nulo", "Número de protocolo", "70% o protocolo; 25% a promulgação, que não é promessa destes 100 dias"],
        ],
        font=7.5,
    )

    h(doc, 2, "Primeiro ano")
    table(
        doc,
        ["#", "Promessa", "Resultado", "Medida", "Custo", "Indicador", "Prob."],
        [
            ["8", "Projeto de revisão das renúncias", "Caducidade de 4 anos e meta de 0,4 p.p. do PIB", "Lei", "Arrecada se passar; não custa", "Projeto com exposição de motivos e lista", "65% o envio; 40% a aprovação no mandato"],
            ["9", "Estatuto da plataforma", "Previdência e recurso sem vínculo automático", "Lei", "Fiscalização", "Lei sancionada ou veto fundamentado a texto inaproveitável", "45% a lei; 80% o projeto"],
            ["10", "Comitê de investimento sensível", "Lista fechada de setores, prazo de decisão", "Lei", "Servidores", "Lei ou, na falta, decreto limitado ao que já for competência", "50%"],
            ["11", "Regra de inteligência artificial por risco", "Sem licença prévia de modelo geral; recurso em alto risco", "Lei", "Autoridade já existente", "Texto aprovado ou corrigido", "45%"],
            ["12", "Fundo de segurança com câmera e separação de facção", "Dinheiro só para quem filma e separa", "Lei e convênio", "Piloto no orçamento atual; escala de 0,08% do PIB só com trava", "Pelo menos 5 UFs aderentes em 2028", "55% o piloto; 35% a escala cheia"],
            ["13", "Contrato de resultado dos Correios", "Meta de caixa e serviço, sem venda", "Contrato de direção e plano", "Depende do buraco herdado, explicitado em 90 dias", "Contrato publicado", "70%"],
            ["14", "Posição escrita Mercosul–UE", "Sim ou não com o texto real da mesa", "Nota do Itamaraty e mensagem ao Congresso se houver acordo", "Nulo", "Documento público", "80% a posição; a ratificação não é só brasileira"],
            ["15", "Piloto de alfabetizadores", "Rede pior do Ideb com professor extra de dedicação", "Lei ou Medida Provisória com fonte no piloto, não na escala", "Fração de 0,15% do PIB", "Piloto em sala em 2027", "60%"],
        ],
        font=7.5,
    )

    h(doc, 2, "Segundo e terceiro anos")
    table(
        doc,
        ["#", "Promessa", "Resultado", "Medida", "Custo", "Indicador", "Prob."],
        [
            ["16", "Avaliação censitária do 2º ano", "Leitura medida de verdade em 2028", "Lei curta e Inep", "Dentro do bloco de educação", "Microdado disponível ao gestor e índice municipal público", "65%"],
            ["17", "Decisão de Angra 3", "Obra com teto ou canteiro parado", "Ato com o TCU", "O teto auditado, ou o custo de parar", "Decisão motivada publicada", "70% decidir; 40% concluir a obra dentro do teto"],
            ["18", "Cannabis adulta licenciada", "Varejo com selo, sem venda a menor", "Lei, com cláusula de reversão em 24 meses", "Receita incerta, não contada no fisco", "Lei e primeira licença, ou arquivamento explícito", "35%"],
            ["19", "Tabela SUS dos grupos de maior fila", "Preço mais perto do custo, impacto orçado", "Portaria com lastro na LOA", "Até 0,10% do PIB só com trava", "Tabela nova publicada", "50%"],
            ["20", "Cadastro ambiental: estoque de validação em queda forte", "Produtor legal com papel; embargo sem crédito", "Convênio", "Dentro de 0,05% do PIB ambiental na escala", "Percentual validado publicado por UF", "55%"],
            ["21", "Cinco corredores com decisão", "Contrato ou arquivamento motivado até 2029", "Edital ou nota técnica", "Privado na maior parte; público contingente", "Cinco dossiês fechados", "50%"],
            ["22", "Folha menor, se a renúncia compensar", "Até 2 p.p. na faixa da base, ou nada", "Lei tributária", "0,20% do PIB só se houver fonte", "Alíquota publicada contra a compensação", "40%"],
        ],
        font=7.5,
    )

    h(doc, 2, "Quarto ano")
    table(
        doc,
        ["#", "Promessa", "Resultado", "Medida", "Custo", "Indicador", "Prob."],
        [
            ["23", "Superávit primário de 0,5% do PIB", "Governo central no positivo combinado", "Execução e leis do eixo 2", "O ajuste inteiro", "Resultado abaixo da linha do BC, sem despesa fora da conta", "35% — acima do que o Focus de out/2026 sugeria"],
            ["24", "Informalidade abaixo de 34%", "Queda sem queda do emprego total", "Estatuto, licença, folha", "Ver eixo 3", "PNAD", "40%"],
            ["25", "Feminicídio abaixo de 1.571 e mortes violentas abaixo de 17 por 100 mil", "Curva de 2025 quebrada nos dois sentidos certos", "Fundo, tornozeleira, investigação; polícia é estadual", "Eixo 6", "Anuário e DataSUS concordando na direção", "45% a taxa de mortes violentas; 40% o feminicídio"],
        ],
        font=7.5,
    )
    p(
        doc,
        "Nenhuma promessa acima depende de crescimento de 4% ao ano, de maioria parlamentar "
        "própria ou de paz mundial. As de número 7 (promulgação), 8 (aprovação), 18 e 23 são "
        "as mais frágeis. Se caírem, o mandato não se declara cumprido por terem sido «difíceis». "
        "Declara o que fez na parte executiva e o que o Congresso recusou, com número de voto.",
    )

    h(doc, 1, "2. Planejamento fiscal 2027–2030")
    p(
        doc,
        "Isto é simulação do programa, não projeção do Banco Central nem do Ministério da Fazenda "
        "de outubro de 2026. A base de partida, essa sim, é observação: Prisma de 15 de outubro "
        "via dívida bruta em 83,4% do PIB no fim de 2026 e 87% em 2027; Focus via primário ainda "
        "negativo e resultado nominal perto de −8,9% do PIB em 2026, com Selic a 13,75%. Aritmética "
        "que o programa não esconde: com dívida perto de 85% do PIB, um superávit primário de 0,5% "
        "não faz a dívida cair se o juro real exceder o crescimento por vários pontos. Ele apenas "
        "reduz a velocidade do estrago e, se for crível, ajuda o prêmio a cair. Queda firme da "
        "relação dívida/PIB pode ficar para depois de 2030. Prometer 70% do PIB em 2030 seria conto.",
    )
    h(doc, 2, "Movimento estrutural pretendido, em pontos do PIB, escala cheia")
    table(
        doc,
        ["Item", "Efeito no primário", "Natureza"],
        [
            ["Revisão de renúncias", "+0,40", "Receita que deixa de ser gasto tributário. Depende de lei. Pode sair pela metade."],
            ["Subsídio financeiro e estatal dependente", "+0,15", "Corte de gasto. Parte é ato de orçamento; parte enfrenta bancada."],
            ["Fraude e pagamento indevido", "+0,10", "Estimativa incerta. Não pode ser gasta antes de caixa."],
            ["Congelamento real de custeio não prioritário", "+0,20", "Ato orçamentário. Risco de parar serviço se for burro."],
            ["Alívio de folha", "−0,20", "Só ocorre se a renúncia compensar."],
            ["Educação, segurança, saneamento, ciência, pagamento ambiental", "−0,35", "Escala cheia contingente. Pilotos são menores e entram mesmo assim."],
            ["Líquido estrutural", "+0,30", "Mais o que o ciclo e a regra já herdada fizerem. Não é milagre de 2 pontos."],
        ],
        font=8,
    )
    p(
        doc,
        "Necessidade de lei: renúncia, folha, plataforma, fundo de segurança, cannabis, maioridade, "
        "reeleição, comitê de investimento, inteligência artificial. Ato próprio: decreto de licença, "
        "instrução diplomática, contrato dos Correios, auditoria de Angra 3, veto, indicação, "
        "não telefonar ao Ibama. Estados e municípios: polícia, escola, esgoto, fila local.",
    )
    h(doc, 2, "Cenários no fim de 2030")
    table(
        doc,
        ["", "Otimista", "Central", "Pessimista"],
        [
            ["O que acontece", "Lei de renúncias passa perto da meta; prêmio de risco cai cerca de 1,5 p.p.; crescimento real perto de 2,2%", "Metade da renúncia; Selic desce devagar, como o Focus já sugeria; crescimento perto de 1,8%", "Reformas emperram; choque externo; crescimento perto de 1%; juro volta a subir"],
            ["Primário em 2030", "+0,8% do PIB", "+0,5% do PIB", "ainda deficitário, cerca de −0,3%"],
            ["Dívida bruta", "estabiliza perto de 86% e começa a dobrar a curva", "sobe mais devagar e termina na casa de 90% a 92%", "caminho de 95% ou mais"],
            ["IPCA", "dentro da banda, perto de 3,5%", "na banda alta, perto de 4%", "de novo acima de 4,5%"],
            ["Crescimento médio do mandato", "perto de 2,2%", "perto de 1,8%", "perto de 1,2%"],
            ["O que se corta primeiro", "Nada da âncora; acelera-se investimento", "Escala cheia dos eixos sociais não abre", "Ficam só pilotos, pisos constitucionais e estabilizadores"],
        ],
        font=8,
    )
    p(
        doc,
        "Efeito esperado no cenário central: déficit nominal ainda alto por causa do juro herdado, "
        "porém menor do que a trajetória que o Prisma de outubro de 2026 já punha em 87% de dívida "
        "em 2027 se nada mudasse a credibilidade. Inflação não é instrumento de ajuste. Crescimento "
        "não é prometido acima do que a produtividade permitir. Se o cenário pessimista se instalar "
        "por erro próprio — gastança, telefone ao BC, licença vendida —, o critério de fracasso do "
        "volume 10 se aplica, não uma revisão cosmética.",
    )
    h(doc, 2, "Riscos de execução")
    bullets(
        doc,
        [
            "Congresso aprova a despesa do programa e rejeita a renúncia. Resposta já escrita: a despesa nova não escala. Se escalar por pressão política, o plano foi violado por quem o escreveu.",
            "Receita da transição do IBS/CBS decepciona. Resposta: usar o seguro de transição da emenda, não criar tributo paralelo de madrugada.",
            "Fraude previdenciária rende menos do que 0,10% do PIB. Resposta: não antecipar esse dinheiro em programa permanente.",
            "Choque de combustível ou de alimento recoloca o IPCA acima do teto. Resposta: BC autônomo e meta fiscal mantida; sem tabela de congelamento.",
            "Tentação eleitoral de 2028 e de 2030, mesmo sem reeleição de Elias, via governadores aliados. Resposta: o veto a despesa permanente sem fonte continua valendo no último ano.",
        ],
    )

    h(doc, 1, "3. Governabilidade com 8% das cadeiras")
    p(
        doc,
        "Premissa do experimento, não fato eleitoral: 8% da Câmara e 8% do Senado. Isso não faz "
        "maioria, não faz emenda e não faz sequer lei ordinária sem sócio. O programa foi escrito "
        "para essa aritmética. O que é decreto e veto não espera os 3/5. O que é emenda — maioridade "
        "penal e fim da reeleição — pode morrer sem levar o resto junto.",
    )
    h(doc, 2, "Perfil dos ministros")
    p(
        doc,
        "Critério único: competência de execução, ficha limpa no universo da simulação e disposição "
        "de assinar papel com número. Cota de partido da coalizão existirá, porque negar isso é "
        "mentir sobre o presidencialismo, e terá limite: pasta de orçamento, de polícia federal, "
        "de receita e de meio ambiente licenciador não é moeda. Ministro que usar o cargo para "
        "campanha pessoal ou para favorecimento de doador sai. A vice não acumula ministério, para "
        "não misturar a sucessão com a fila do SUS.",
    )
    h(doc, 2, "Gabinete hipotético")
    p(
        doc,
        "Nomes abaixo são fictícios, como o restante da biografia. Não correspondem a pessoas "
        "reais e não indicam apoio de ninguém.",
    )
    table(
        doc,
        ["Pasta", "Nome fictício", "Perfil"],
        [
            ["Casa Civil", "Renato Pacheco Leme", "Advogado público, negociador de pauta escrita, sem carreira de palanque"],
            ["Fazenda", "Sílvia Kalman", "Economista de quadro, mandato de dizer não ao presidente em voz alta"],
            ["Planejamento", "Otávio Braga Nunes", "Orçamento de investimento; separa obra de custeio"],
            ["Justiça e Segurança", "Ivo Lacerda", "Delegado federal aposentado da ficção; câmera e inteligência, não palanque penal"],
            ["Defesa", "Teresa Quaresma", "Civil, experiência em fronteira; Forças não tutelam o plano"],
            ["Relações Exteriores", "Paulo Estevão Kim", "Diplomata de carreira fictício; executa o volume 07"],
            ["Saúde", "Mariana Souza Leal", "Gestora do SUS, não celebridade; a vice acompanha sem comandar a pasta"],
            ["Educação", "Cícero Almeida Pontes", "Alfabetização e rede municipal; sem projeto de campus novo"],
            ["Trabalho", "Helena Ruiz Vidal", "Relações do trabalho; estatuto de plataforma sem aventura"],
            ["Transportes", "Jorge Mutran", "Concessão e hidrovia; autorizado a arquivar corredor"],
            ["Minas e Energia", "Lígia Dorneles", "Engenheira; guarda o teto de Angra 3"],
            ["Meio Ambiente", "André Valente Paxiuba", "Fiscalização e licença com prazo; não é cabo eleitoral do agro nem de ONG"],
            ["Agricultura", "Irene Campos do Prado", "Crédito condicionado a embargo; agro como setor, não como partido"],
            ["Cidades", "Davi Lemos Uhr", "Saneamento e Reurb; sem conjunto inaugurado sem papel"],
            ["Ciência e Tecnologia", "Noemi Adler", "Compute público e regra de IA; sem estatal nova"],
            ["Gestão", "Caio Ventura Lopes", "Digital e reposição de pessoal"],
            ["CGU", "Benedita Arraes Furtado", "Acesso direto ao presidente; leniência e obra de emenda"],
            ["Advocacia-Geral", "Mário Teixeira Salles", "Contencioso tributário de massa e parecer que o governo cumpre"],
        ],
        font=8,
    )
    p(
        doc,
        "Banco Central: o mandato de quem estiver no cargo na posse será cumprido. Vaga será "
        "preenchida com sabatina e com nome de reputação técnica, não de partido. Petrobras, "
        "BB e Caixa: indicação com critério publicado antes do nome.",
    )
    h(doc, 2, "Congresso, governadores, Supremo")
    p(
        doc,
        "A base se monta em três círculos. O primeiro é a ATR, pequena, que vota a pauta inteira. "
        "O segundo é o bloco de quem quer previsibilidade fiscal, obra com foto verdadeira e nenhuma "
        "guerra de costumes — a esse bloco se oferece corredor, saneamento e respeito ao Fundeb e "
        "ao piso da saúde. O terceiro não entra: quem exigir anistia de corrupção, voto impresso, "
        "orçamento sem rastro ou intervenção militar política. Melhor perder a lei do que comprar "
        "com isso.",
    )
    p(
        doc,
        "Governadores recebem critério publicado de convênio, não mala. Prefeitos idem, com o "
        "município pobre do Norte na frente do critério, não na frente da fila de aeroporto. "
        "O Supremo é cumprido. Derrota judicial encerra a via administrativa e, se o governo ainda "
        "quiser a política, vira projeto de lei, não maniobra. Não haverá recado de ministro a "
        "ministro do STF por interlocutor de empreiteira. Com a oposição, a pauta de segurança "
        "de fronteira e de alfabetização será oferecida por escrito, para dificultar o voto contra "
        "apenas por identidade. O veto será usado contra despesa permanente sem fonte, contra "
        "enfraquecimento de fiscalização ambiental, contra crime de opinião e contra benefício "
        "tributário sem avaliação e sem caducidade.",
    )
    h(doc, 2, "Corrupção dentro do governo e alternância")
    bullets(
        doc,
        [
            "Declaração de bem e de reunião com interessado em licitação, pública para ministro e para direção de estatal.",
            "CGU pode abrir caso sem pedir licença à Casa Civil. Interferência nisso é falta grave.",
            "Doação eleitoral, no universo da simulação, não compra cargo. Se comprar, o fato é publicado e o ministro sai, mesmo sem condenação ainda — o padrão interno é mais duro do que a sentença.",
            "Eleição livre em 2030, urna mantida, Elias fora da cédula por compromisso próprio. Uso da máquina federal em campanha de aliado é demissão. Transmissão de cargo documentada, inclusive se o sucessor for adversário.",
        ],
    )
    p(
        doc,
        "Empresário será recebido com pauta e ata. Sindicato também. Nenhum dos dois escreve a "
        "medida provisória. A sociedade civil que fiscaliza obra e floresta terá dado aberto; a "
        "que pedir veto de categoria inteira de atividade lícita será ouvida e poderá perder.",
    )
    save(doc, os.path.join(OUT, "09_PROMESSAS_FISCO_GOVERNABILIDADE.docx"))
    print("vol 09 ok")


if __name__ == "__main__":
    build()
