# Status — O Futuro Onde Te Perco

## Estado atual

**Fase:** pré-produção / arquitetura narrativa.

**Infraestrutura:** projeto consolidado no repositório `storytelling`. Este arquivo é o ponto de retomada entre chats.

Nenhum capítulo definitivo deve ser escrito ainda. Premissa, acidente, cadeia causal do futuro sombrio, regras sobrenaturais, mapa estrutural provisório dos sonhos e uma camada biográfica/social robusta dos personagens centrais já possuem direção aprovada.

## Progresso da sessão mais recente

Foi fechado e consolidado o primeiro pacote nominal, geográfico e social dos personagens.

### Núcleo central

- **Henrique Almeida**, 37 anos, irmão mais velho de Tomás, médico de emergência experiente;
- **Lívia Sampaio**, 34 anos, melhor amiga de Tomás desde a infância, professora de dança contemporânea/composição e coreógrafa freelancer;
- **Tomás Almeida**, 34 anos, irmão mais novo de Henrique, arquiteto e melhor amigo de Lívia.

### Setting

- **Belo Horizonte, Minas Gerais** é a cidade-base do romance;
- a residência coreográfica de Lívia acontece em **São Paulo, São Paulo**, por aproximadamente três meses;
- hospital, estúdio, escritório de arquitetura e instituição da residência devem ser fictícios;
- bairros, endereços e geografia fina de cena continuam abertos.

O setting global está consolidado em `canon/SETTING.md`.

### Rede social/familiar aprovada

- os pais de Henrique e Tomás estão vivos e a família é funcional; não há necessidade de pais abusivos usados como explicação totalizante para os defeitos dos irmãos;
- a família se habituou historicamente a olhar para Henrique, filho mais velho e médico, como referência em situações difíceis; isso ajuda a explicar sua influência durante o acidente/hospital sem legitimar o controle que exerceu;
- Tomás é o principal agregador social do núcleo histórico e cria ocasiões orgânicas para Henrique e Lívia continuarem dividindo espaços apesar da hostilidade;
- **Beatriz “Bia” Faria** é uma amizade importante de Lívia construída depois do acidente, ligada à produção cultural/dança e capaz de apoiar tratamento/adaptação sem tentar decidir pela amiga;
- **Camila** é amizade profissional importante de Henrique na emergência; sobrenome, idade exata e detalhes de carreira ainda estão abertos;
- Henrique e Tomás vivem sozinhos em Belo Horizonte; bairros e moradias específicas ainda estão abertos;
- Lívia trabalha a partir de um estúdio independente de dança contemporânea e não é dona do espaço no início do romance.

## Estrutura já fechada em alto nível

### Acidente

O acidente ocorreu seis anos antes. Lívia dirigia rápido demais para a pista molhada e tinha responsabilidade real pelo risco. Tomás, passageiro, entrou em pânico e agarrou o volante, tendo participação causal decisiva na perda de controle. Lívia omitiu essa interferência; Tomás mais tarde permitiu que a versão incompleta persistisse. Henrique passou seis anos acreditando que Lívia quase matou o irmão por culpa essencialmente dela.

Enquanto Tomás estava incapaz de decidir, Henrique pressionou família/equipe para impedir a visita de Lívia. A ferida central inclui a frase canônica: **“Você perdeu o direito de ficar perto dele quando quase matou ele.”**

Detalhes completos em `canon/ACCIDENT.md`.

### Personagens

Henrique tende a converter medo em ação, plano e intervenção. Medicina de emergência e seu papel histórico de irmão mais velho reforçam capacidades reais de agir sob pressão, mas não lhe dão autoridade pessoal sobre outros adultos. Seu arco exige distinguir cuidado, ajuda e controle.

Lívia construiu uma carreira genuinamente valiosa em ensino/coreografia depois do acidente. Quer consolidar-se como coreógrafa autoral. O tornozelo lesionado permite função ampla, mas carga acumulada pode produzir dor/limitação. Sua autonomia é uma força real que pode degenerar em ocultação e isolamento.

Tomás é profissionalmente competente e capaz de decidir. Seu evitamento é especificamente emocional/relacional. Seu silêncio de seis anos se consolidou gradualmente, e sua reparação precisa envolver aceitar consequências, não apenas revelar a verdade.

Detalhes em `canon/characters/`.

### Sobrenatural

- os sonhos mostram um futuro possível, não inevitável;
- o envio da candidatura para a residência torna a linha sombria causalmente alcançável e coincide com o início dos sonhos;
- informação emocional/sensorial atravessa melhor que identidade, cronologia ou causalidade explícita;
- o vínculo não funciona como alerta genérico de perigo;
- sonhos mudam perceptivelmente apenas quando escolhas alteram de modo relevante a cadeia causal;
- o leitor recebe confirmação sobrenatural parcial;
- fio vermelho é moldura simbólica/cultural, não sistema de magia explicado;
- não haverá autoridade explicadora nem linhagem familiar sobrenatural como chave expositiva;
- canon de funcionamento e crenças dos personagens devem permanecer separados.

Detalhes em `canon/SUPERNATURAL_RULES.md`.

### Mapa estrutural dos sonhos

Existe um esboço provisório aprovado de oito sonhos estruturalmente relevantes com progressão:

`terror → intimidade → identidade → investigação → erro causal → profecia autorrealizável → divergência → possibilidade`

O terceiro grande marco permite o reconhecimento de Lívia por correspondência corporal/movimento, aproximadamente na faixa de 25–30%. O sonho final continua além do antigo ponto fatal e mostra Lívia viva e mais velha. O fio vermelho não aparece literalmente nos sonhos.

O número e a progressão funcionam como arquitetura de desenvolvimento, não como sequência imutável por capítulo. Detalhes em `story/DREAM_MAP.md`.

### Cadeia causal do futuro sombrio

A residência não é a causa única nem direta da crise futura. A cadeia aprovada é:

**medo de vulnerabilidade → ocultação → medo dele → controle/intervenção → mais ocultação → isolamento → sobrecarga → rupturas → crise.**

Henrique rompe uma fronteira ao envolver Tomás para tentar intervir na residência. Isso amplia isolamento e quebra de confiança. A linha futura muda quando Lívia deixa de tratar autonomia como necessidade de sustentar tudo sozinha e Henrique aprende a apoiar sem transformar medo em autoridade.

Detalhes em `story/FUTURE_CAUSAL_CHAIN.md` e `story/CURRENT_OUTLINE.md`.

## Fluxo de colaboração e GitHub

- novas propostas narrativas, de canon ou estrutura devem ser apresentadas no chat antes de serem consolidadas;
- brainstorm não deve ser versionado como decisão aprovada sem essa etapa;
- blocos estruturais relevantes devem ser desenvolvidos em branches e pull requests, evitando commits diretos na `main`;
- o PR é a unidade de revisão antes de uma mudança estrutural chegar à `main`;
- o assistente deve revisar o PR, executar/ler a auditoria narrativa, corrigir problemas e realizar o merge quando a mudança aprovada estiver consistente; o usuário não precisa executar revisão operacional do GitHub.

## O que ainda NÃO está fechado

- nome/localização do hospital fictício, escala concreta e detalhes cotidianos da rotina médica de Henrique;
- sobrenome, idade exata e carreira de Camila;
- nome/localização do estúdio fictício, arranjo profissional detalhado e rotina doméstica de Lívia;
- idade exata/função concreta de Bia e família ampliada/conflitos sociais de Lívia;
- nome/formato da instituição fictícia responsável pela residência em São Paulo;
- área específica da arquitetura, escritório, rotina e vida afetiva/social adicional de Tomás;
- bairros/moradias exatos dos personagens;
- episódios concretos da dinâmica entre Henrique e Lívia antes do acidente;
- como a atração adulta começa sem apagar o ressentimento;
- cena exata, dentro do Ato 3, em que Lívia descobre os sonhos;
- primeiro ato claro de confiança, primeiro beijo e momento em que a relação deixa de ser ambígua;
- ações específicas da reconciliação;
- POV definitivo, pessoa verbal e distância narrativa;
- presença ou ausência de capítulos-sonho separados;
- detalhes sensoriais definitivos e posição por capítulo dos oito sonhos;
- gesto corporal específico do reconhecimento;
- objetos/sinais específicos da residência nos sonhos;
- grau de explicitude sexual;
- comprimento médio e número final de capítulos;
- título definitivo;
- amostras positivas/negativas de voz do próprio livro.

## Próximo passo recomendado

1. completar a última camada cotidiana dos personagens centrais sem excesso de worldbuilding;
2. fechar a dinâmica romântica detalhada e as ações de reconciliação;
3. definir POV, pessoa verbal e distância narrativa;
4. retornar ao mapa dos sonhos para calibrar detalhes corporais/sensoriais;
5. calibrar amostras originais de estilo e congelar `STYLE_EXAMPLES.md`;
6. completar mapa de conhecimento e revelações;
7. revisar o outline macro;
8. produzir outline por capítulos;
9. somente então iniciar prosa definitiva.

## Regra para retomada em outro chat

Ao continuar este projeto, não recomece da premissa. Leia os arquivos essenciais indicados em `PROJECT.md`, identifique a próxima decisão ainda aberta e avance a partir dela. Ao formular uma nova proposta narrativa, apresente-a ao usuário no chat antes de consolidá-la. Para blocos estruturais relevantes, trabalhe em branch e PR. Ao terminar uma sessão que altere o projeto, atualize este `STATUS.md`.
