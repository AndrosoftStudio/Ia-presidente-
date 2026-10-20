# -*- coding: utf-8 -*-
"""Volume 08 — vinte decisões controversas."""
import os, sys
sys.path.insert(0, "/workspace/candidatura")
from docx_theme import cover, h, new_doc, p, rich, save

OUT = "/workspace/candidatura/docx"

DEC = [
    ("1. Empresas estatais: manter o núcleo, vender o que não é núcleo",
     "Petrobras permanece de economia mista. Banco do Brasil e Caixa permanecem públicos. Correios não são privatizados neste mandato; assinam contrato de resultado e só em 2029 o governo dirá se falharam. Participação minoritária não estratégica pode ser vendida depois do TCU. Autoridade portuária e ativo logístico já maduro vão a concessão. Não se cria estatal nova de inteligência artificial, de vacina monopolista ou de «campeã nacional». A alternativa de privatizar tudo perde o instrumento de energia e de crédito anticíclico transparente. A alternativa de ampliar estatais perde o foco e o caixa. A escolha é o núcleo."),
    ("2. Setor privado no SUS: comprar fila, não vender o sistema",
     "O SUS continua público e universal. Mutirão de cirurgia eletiva pode ser comprado de hospital privado e filantrópico, com lista nominal, teto e auditoria, apenas para fila medida. Plano de saúde não passa a operar o direito. A alternativa de fechar a porta à capacidade ociosa privada prolonga espera por pureza. A alternativa de converter o SUS em voucher geral não cabe no caixa nem na rede e será vetada se vier como projeto."),
    ("3. Impostos: não sobem no agregado; mudam de lugar",
     "Teto operacional de carga: 32,5% do PIB, diante dos 32,40% de 2025. Revisão de renúncias no valor de 0,4 ponto do PIB até 2030. Folha patronal menor em até 2 pontos na faixa até o teto do INSS, só se a revisão compensar. Imposto sobre grandes fortunas não será proposto. Dividendos: alíquota de 15% com faixa de isenção modesta apenas se ainda estiverem isentos em 1º de janeiro de 2027; se já tributados, não sobem no primeiro biênio. IBS e CBS não são reabertos."),
    ("4. Gasto: corta favor e sobe investimento escolhido, não o contrário",
     "Despesa corrente de favor tributário e transferência a estatal dependente é o lado que encolhe. Educação de alfabetização, inteligência de segurança, saneamento onde a tarifa não fecha e computação de pesquisa são o lado que pode crescer, e só na escala cheia se a lei de renúncias passar. Não é austeridade que zera obra. Não é investimento que fura a meta. Primário de 0,5% do PIB em 2030 é a âncora, insuficiente sozinha para derrubar a dívida se o juro real não cair — o volume 09 mostra isso sem maquiagem."),
    ("5. CLT: o núcleo fica; plataforma não vira vínculo automático",
     "Férias, 13º, FGTS e jornada máxima do emprego clássico permanecem. Não há revogação da CLT nem volta da contribuição sindical obrigatória. Trabalhador de aplicativo ganha estatuto próprio: previdência em base reduzida, seguro de acidente e recurso contra bloqueio algorítmico, sem vínculo empregatício automático. Quem quiser a CLT inteira para a plataforma terá de explicar o desemprego que a conta produz. Quem não quiser proteção nenhuma terá de explicar o acidente sem cobertura."),
    ("6. Jornada: sem lei nacional de quatro dias",
     "A semana legal não é reduzida por lei federal neste mandato. Acordo coletivo pode reduzir jornada se o salário for mantido por produtividade, e o ministério publicará quantos acordos fizeram isso de verdade. A alternativa de uma lei nacional ignora a diferença entre fábrica de alta produtividade e serviço público de fila. A alternativa de proibir o acordo é paternalismo."),
    ("7. Armas: não amplia o acesso civil; persegue a arma do crime",
     "O porte e a posse civis não serão ampliados. Proprietário já legal permanece, com revalidação psicológica e rastreio de série. Campanha de entrega voluntária não é política principal, porque a arma do homicídio não está no clube de tiro. A prioridade é a arma da facção: fronteira, investigação e perdimento. Desarmamento domiciliar forçado não será proposto. Liberalização de porte, tampouco."),
    ("8. Drogas: cannabis regulada para adulto; tráfico de droga pesada segue crime de organização",
     "Uso adulto de cannabis deixa de ser caso de cadeia e passa a mercado licenciado, com venda proibida a menor, propaganda proibida e imposto específico carimbado para tratamento. Cocaína, crack e sintéticos não são legalizados. Usuário de droga ilícita restante é tratado como saúde pública, não como prioridade penitenciária; traficante de organização é prioridade máxima. Cláusula de saída em 24 meses, já escrita no volume 01: se o uso adolescente ou a captura criminosa do selo disparar, o varejo para. A proibição total já convive com 40 mil mortes violentas de contexto mais amplo e com facção financiada; a legalização de tudo entrega o crack a um balcão. Nenhuma das duas extremas é a escolha."),
    ("9. Prisão: separar facção e medir reincidência, não inaugurar muralha",
     "Presídio federal e o fundo do eixo 6 exigem separação de facção. Trabalho e estudo dentro da unidade entram no convênio. Revista tecnológica para cortar celular de comando. Não haverá promessa de regime fechado perpétuo nem de privatização geral do sistema, que troca o Estado por contratante sem resolver o comando interno. Construir vaga sem quebrar o comando da facção é hotel de organização criminosa."),
    ("10. Maioridade penal: 16 anos só para crime hediondo, em regime separado",
     "Emenda limitada a homicídio doloso, latrocínio, estupro e roubo com morte, aos 16 anos, em casa separada do adulto e do internato comum, com avaliação obrigatória aos 36 meses. O ECA fica para o restante. A vice discorda da ênfase e aceita a trava da separação. Baixar tudo para 16 anos no presídio comum será vetado se o Congresso alargar a emenda. Manter 18 anos mesmo para latrocínio, na visão de Elias, falha com a vítima e com o adolescente capturado pela facção; por isso a chapa não fica no meio verbal."),
    ("11. Aborto: a lei vigente não se amplia nem se fecha",
     "Permanecem as hipóteses já legais de estupro, risco à vida e anencefalia. O SUS federal garantirá o procedimento nesses casos, sem peregrinação. Não há projeto de aborto eletivo. Não há projeto para criminalizar a mulher além do que a lei já dispõe. Contracepção e educação sexual avançam com a rede que aderir. É uma decisão de contenção jurídica, não uma fuga: os dois movimentos de mudança estão recusados."),
    ("12. Expressão e direitos civis: sem tipo penal novo de opinião; cotas federais mantidas",
     "Opinião ofensiva não ganha crime novo. Racismo, ameaça e calúnia continuam crime. Plataforma cumpre ordem judicial sobre conteúdo ilícito e mostra quem paga anúncio eleitoral. Cotas raciais e sociais já existentes na universidade e no serviço público federais ficam até a avaliação de 2029. Cota obrigatória em empresa privada não será proposta. Casamento civil igualitário e o direito já reconhecido a pessoas LGBTQIA+ não serão revogados. O programa não abre guerra de costumes para mobilizar bancada e não terceiriza a polícia a pauta religiosa."),
    ("13. Sistema eleitoral: urna fica; reeleição cai se o Congresso deixar; distrito puro não entra",
     "Voto impresso não será iniciativa deste governo. Financiamento público eleitoral não cresce em termos reais. Fim da reeleição para mandatos futuros, por emenda, mais o compromisso pessoal de Elias de não se recandidatar. Distritão e distrito uninominal puro são rejeitados: no Norte, o distrito grande cala o interior ou o incha de cacique. A cláusula de desempenho já existente permanece."),
    ("14. Privatizações e concessões: lista curta, não onda",
     "Concede-se logística madura. Não se privatiza SUS, universidade, banco público, Petrobras nem, neste mandato, Correios. A onda de privatização como identidade de governo é rejeitada porque vende o que é instrumento junto com o que é peso. A proibição de conceder é rejeitada porque o investimento de 16,8% do PIB não sobe só com obra pública."),
    ("15. Energia nuclear: Angra 3 com teto, ou para",
     "Auditoria em seis meses. Estouro real acima de 25% do teto antes do ponto de não retorno encerra a obra. Nenhuma usina grande nova no mandato. Estudo de reator modular sem canteiro. A alternativa de abandonar o nuclear por princípio deixa a base firme da rede na água e no gás. A alternativa de tratar nuclear como obra sem preço já foi feita e é o problema."),
    ("16. Recursos naturais: explorar com licença, nunca em terra indígena",
     "Óleo na margem equatorial só se o Ibama disser sim, sem telefone do Planalto. Mineração legal fora de terra indígena e de unidade de conservação, com rastreio. Dentro de terra indígena, não. Madeira só com manejo e cadastro validado. A proibição geral de novo óleo não será decreto deste governo. A liberação geral também não."),
    ("17. Redes sociais: dever sobre crime já escrito, não sobre verdade oficial",
     "Canal de denúncia obrigatório, transparência de impulsionamento eleitoral, ordem judicial para tirar conteúdo lícito controverso. Sem ministério da verdade, sem bloqueio administrativo de opinião, sem taxa disfarçada de regulação que quebre empresa pequena sem atingir a grande. A alternativa de deixar ameaça e estelionato sem canal é omissão. A alternativa de regular narrativa é censura."),
    ("18. Inteligência artificial: risco alto tem humano no recurso; modelo geral não tem licença prévia",
     "Saúde, crédito, investigação e reconhecimento facial em público são alto risco: supervisão e recurso. Modelo de fundamento não pede licença de Estado para existir. Peça eleitoral sintética se rotula. Sandbox para empresa pequena. Revisão da lei já marcada para 2029. Proibir modelo é atrasar pesquisa. Não regular reconhecimento facial é entregar a rua a erro de máquina sem recurso."),
    ("19. Moeda do Brics: não",
     "Não haverá adesão a moeda comum, cesta obrigatória ou substituto do real. Liquidação pontual em moeda local, com risco no Banco Central e não no Tesouro, pode continuar. A moeda comum não reduz a dependência do dólar; transfere a política monetária para um arranjo que o Brasil não controla e associa o real a sócios em guerra ou sob sanção. Quem chamar isso de soberania estará vendendo o nome."),
    ("20. Cooperação militar: mais capacidade própria, menos aliança",
     "Sem Otan, sem base estrangeira, sem tropa permanente em guerra de terceiro. Exercício com vários países, não com um padrinho. Ajuda a missão da ONU só com mandato, regra de engajamento e autorização do Congresso, e com data de saída. Cooperação de inteligência policial contra facção, sim. Cooperação que transforme o Brasil em parte de guerra alheia, não. Ampliar cooptação militar por prestígio de cúpula é a alternativa rejeitada; isolar as Forças de qualquer exercício também, porque equipamento sem padrão de operação conjunta enferruja."),
]


def build():
    doc = new_doc()
    doc.core_properties.title = "08 — Vinte decisões controversas"
    cover(
        doc,
        "VOLUME 08",
        "Decisões políticas controversas",
        "Vinte escolhas fechadas. Onde há condição, a condição tem número, prazo ou veto. «Equilíbrio» não é resposta.",
    )
    p(
        doc,
        "Cada item diz o que será feito, o que foi recusado e por quê. As escolhas repetem os "
        "eixos 05 e 06 de propósito. Se um adversário encontrar contradição, a contradição é defeito "
        "deste registro e deve ser cobrada; não é nuance estratégica.",
    )
    for title, body in DEC:
        h(doc, 1, title)
        p(doc, body)
    h(doc, 1, "O que estas vinte decisões recusam como método")
    p(
        doc,
        "Recusam a frase «não se pode extremar». Extremar é que está sendo evitado com instrumento, "
        "não com adjetivo. Cannabis tem cláusula de saída. Angra 3 tem teto de 25%. Folha só cai "
        "se a renúncia cair. Maioridade só desce em quatro crimes e em prédio separado. Correios "
        "não são vendidos antes de um contrato de quatro anos. Quem pedir uma resposta ainda mais "
        "curta pode parar na lista: mantém SUS, Petrobras e BPC; não mantém reeleição, moeda do "
        "Brics, voto impresso, jornada de quatro dias por lei, imposto sobre fortuna, porte ampliado, "
        "mineração em terra indígena nem licença prévia de modelo de inteligência artificial.",
    )
    rich(
        doc,
        [
            ("Probabilidade de o Congresso aceitar o pacote inteiro: baixa. ", True, False),
            ("Probabilidade de o Executivo cumprir sozinho a parte que não depende de emenda — Ibama sem telefone, trava fiscal interna, urna intocada, compromisso pessoal de não recandidatura, painel de fila, auditoria de Angra 3: moderada-alta, e é por essa parte que o mandato pede para ser julgado se as emendas caírem.", False, False),
        ],
    )
    save(doc, os.path.join(OUT, "08_DECISOES_CONTROVERSAS.docx"))
    print("vol 08 ok")


if __name__ == "__main__":
    build()
