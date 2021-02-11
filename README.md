Automation QA - Release notes
---

**Version 2.9**                       
                                            
<em>09/02/2021</em>                         

- <font color="red">**__[Novo]__**</font> - Realiza o download dos arquivos durante o teste e armazena localmente;                                            
- <font color="red">**__[Novo]__**</font> - Nova versão do requirements que retira bibliotecas não utilizadas mais;
- <font color="red">**__[Novo]__**</font> - Nova versão do Driver do Edge (Chromium) - Versão 87.0.664.75.
- <font color="red">**__[Novo]__**</font> - Nova versão do Driver do Firefox - Versão 85.0.1 (64-bits);
- <font color="red">**__[Novo]__**</font> - Informa caso o token tenha expirado;
- <font color="red">**__[Novo]__**</font> - Corrigido erro que ocorria quando havia uma evidência com extensão html na Run;
- <font color="red">**__[Novo]__**</font> - Tratamento no nome do caso de teste caso contenha aspas duplas;
- <font color="red">**__[Novo]__**</font> - Tratamento para informar quando há um campo em branco no caso de teste do Azure.
- <font color="red">**__[Novo]__**</font> - Atualização do arquivo de requirements;
- <font color="red">**__[Novo]__**</font> - Inclusão do status "Aborted" para o caso de teste com download no IE11;
- <font color="red">**__[Novo]__**</font> - Tratamento da sintaxe quando informada uma senha.

**Version 2.8.20**                       
                                            
<em>15/01/2021</em>                         
                                            
- Correção na geração das evidências após execução automatizada.

**Version 2.8.19**    
                      
<em>15/01/2021</em>   

 - Retirada validação para execução no caminho do Pipeline; 
 - Correção para geração das evidências em espanhol da Espanha;
 - Correção na validação de caractere especial no nome do caso de teste;
 - Corrigido atalho do executável CMD;
 - Correção na execução do ciclo e gravação das evidências no teste errado;
 - Implementação da funcionalidade que trata o "Não", para ignorar o passo fora de uma variável;
 - Corrigido problema de ordenação das evidências nos arquivos de evidência;
 - Corrigido problema que retirava o último print do arquivo de evidência;
 - Melhorada a organização das evidências temporárias quando salva localmente.

**Version 2.8.18**    
                      
<em>08/01/2021</em>   

- Correção no problema da geração da evidência manual;
- Alteração da extensão do executável;
- Correção na acentuação / tradução para inglês e espanhol;  
- Alteração das senhas para asterisco nas evidências.


**Version 2.8.17**

<em>21/12/2020</em>

- Correção do tamanho da evidência na execução manual;
- Corrigido erro na geração da evidência quando o caso de teste não possui variável;
- Correção na estrutura do arquivo requirements.

**Version 2.8.16**

<em>14/12/2020</em>

- Atualização do driver do Edge;
- Atualização do arquivo de requirements com novas bibliotecas;
- Configuração para execução no pipeline do Azure;
- Validação do nome do caso de teste. Não deve conter mais de 50 caracteres e caracteres especiais.

**Version 2.8.15**

<em>11/03/2020</em>

- Novos verbos

|VERBOS     |DESCRIÇÃO                                                  |
|-----------|-----------------------------------------------------------|
|Abrir      |Abre uma nova aba em branco                                |
|Apagar     |Apaga o conteúdo de um campo de formulário já preenchido   |
|Atualizar  |Atualiza a página                                          |
|Avançar    |Avança um passo no histórico do navegador                  |
|Rolar      |Rola a página no eixo Y                                    |
|Voltar     |Retrocede um passo no histórico do navegador               |

- Novas formas de validação

|VERBO       | EXPRESSÃO | DESCRIÇÃO                                                            |
|------------|-----------|----------------------------------------------------------------------|
|            | (title)   |Valida se o título da página é igual ao informado no parâmetro        |
|            | (url)     |Valida se a Url da página é igual ao informado no parâmetro           |
|            |  *        |Valida que o texto obtido contem o passado por parâmetro              |
|            |  (?)      |Valida se o elemento está ativo ou inativo                            |
|            |  ($)      |Valida se o elemento está visível ou não                              |
|   Validar  |  (.)      |Valida se o elemento está selecionado ou não                          |
|            |  (!=)     |Valida que determinado campo NÃO possui o texto passado por parâmetro |
|            |  (!)      |Valida que determinado campo POSSUI o texto passado por parâmetro     |
|            |  (#title) |Valida que o elemento possua o título passado por parâmetro           |
|            |  (#href)  |Valida que o elemento possua o href passado por parâmetro             |
|            |  (#value) |Valida que o elemento possua o value passado por parâmetro            |

**Version 2.8.14**

<em>10/27/2020</em>

- IE browser correction.

**Version 2.8.13**

<em>10/01/2020</em>

 - Include the Inches library.

**Version 2.8.12**

<em>10/01/2020</em>

 - Correction the libraries path.

**Version 2.8.11**

<em>10/01/2020</em>

 - Organized the folders inside the project;
 - Start updating the ReadMe in English.

**Versão 2.8.10**

<em>29/09/2020</em>

 - Atualização do driver do Microsoft Edge 85.0.564.63 (64 bits);
 - Correção das mensagens de erros apresentados no Edge ao executar pela .bat ou por linha comando;
 - Tratamento da opção correta no primeiro menu da .bat;
 - Correção no problema de geração da evidência por linha de comando.

**Versão 2.8.9**

<em>25/09/2020</em>

 - Melhoria na leitura do token, realizado somente uma vez;
 - Inclusão da possibilidade de executar via linha de comando.

**Versão 2.8.8**

<em>22/09/2020</em>

 - Correção da função fechar para encerrar o browser;
 - Correção no fechamento da .bat após finalizar os teste.

**Versão 2.8.7**

<em>17/09/2020</em>

 - Gera as evidências manuais e verifica se há prints de tela e execuções;
 - Tratar ID Run para retirar os espaços, caso sejam digitados;
 - Alinhamento das palavras no log para a função Verificar;
 - Identificação da palavra "Google Chrome" e "Internet Explorer" para reconhecer os navegadores;
 - Corrigido erro que não destacava em verde na função Verificar.

**Versão 2.8.6**

<em>15/09/2020</em>

 - Tratamento para verificação do ID Run existente para a geração das evidências manuais;
 - Execução do arquivo .bat em qualquer diretório;
 - Validação na escolha da opção selecionada, apresenta erro caso não seja a correta;
 - Correção nas evidências manuais estão salvando na Run correta.

**Versão 2.8.5**

<em>15/09/2020</em>

 - Correção do driver do Chrome versão Versão 85.0.4183.102 com 32 bits, mesmo a instação sendo 64 bits.

**Versão 2.8.4**

<em>14/09/2020</em>

 - Renomeado o driver do IE.

**Versão 2.8.3**

<em>14/09/2020</em>

 - Corrigido erro na abertura dos navegadores Internet Explorer e Edge;
 - Adicionado novo navegador da Microsoft, o novo Edge;
 - Correção na leitura do idioma automática para a automação de geração das evidências;
 - Correção na leitura do tipo de browser independente se está em maiúscula ou minúscula.

**Versão 2.8.2**

<em>11/09/2020</em>

 - Inclusão da opção de escolha de projeto para a geração das evidências manuais;
 - Correção da geração de evidências quando não há variáveis;
 - Correção na função Verificar.

**Versão 2.8.1**

<em>11/09/2020</em>

 - Correção do problema na leitura das variáveis na nova função Slice.

**Versão 2.8.0**

<em>10/09/2020</em>

 - Criação do arquivo de evidências manuais automaticamente;
 - Alinhamento dos IDs na listagem apresentada;
 - Inclusão da opção de gerar o ETS na .BAT;
 - Correção do tamanho da imagem ao gerar uma evidência manual ou automatizada.

**Versão 2.7.3**

<em>04/09/2020</em>

- Corrigido problema que ocorria quando o passo possui a váriavel com o conteúdo "Sim" para não pular o passo.

**Versão 2.7.2**

<em>01/09/2020</em>

 - Simplificação do desmembramento das variáveis. Adaptado para receber n variáveis no futuro;
 - Inclusão da palavra "Google" para aceitar como navegador.

**Versão 2.7.1**

<em>28/08/2020</em>

 - Atualização do novo driver do Google Chrome - Versão 85.0.4183.83 (Versão oficial) 64 bits;
 - Inclusão do tratamento da palavra "Não" ou "No" antes de cada passo para ignorá-lo;
 - Correção na apresentação dos logs do Google Chrome durante a execução da .bat;
 - Destaque na cor vermelha para os novos items do ReadMe na página do GitHub.
 
**Versão 2.7.0**

<em>26/08/2020</em>

 - Correção da leitura do idioma da máquina;
 - Remoção da quebra de linha '\n' para a função de Validar e Informar;
 - Melhoria na verificação do Test Suit vazio;
 - Correção da função Informar;
 - Redução do tempo de espera do componente para 3 segundos;
 - Adicionada a finalização da automação, caso não houvesse test plan para o projeto;
 - Incluída a opção Sair no menu de seleção;
 - Correção da ortografia de algumas palavras do log;
 - Correção na geração da evidência em espanhol, pois gravava a primeira evidência na página seguinte.

**Versão 2.6.1**

<em>24/08/2020</em>

 - Inclusão do arquivo de .bat na árvore do projeto;
 - Correção do loop no log quando ocorre um erro;
 - Alterando verificação do login do usuário para antes da geração da evidência. A evidência é gerada mais rápido.

**Versão 2.5.5**

<em>21/08/2020</em>

- Correção da tabulação do ReadMe.md.

**Versão 2.5.4**

<em>21/08/2020</em>

 - Correção da tabulação do ReadMe.md.

**Versão 2.5.3**

<em>20/08/2020</em>

 - Correção do problema de execução do caso de teste quando não possui variáveis;
 - Correção na geração dos idiomas, controlando inglês e espanhol em arquivos diferentes;
 - Geração dos arquivos de evidências tanto para os três idiomas (Português, Espanhol e Inglês);
 - Atualização dos arquivos de evidência. Estrutura e log;
 - Retirada de bibliotecas que não eram mais utilizadas;
 - Exclusão de variáveis não mais utilizadas;
 - Correção de palavras que ainda estavam em português.

**Versão 2.5.2**

<em>19/08/2020</em>

 - Novo arquivo de layout de log para idioma espanhol e inglês;
 - Possibilidade de preencher o campo com vazio, basta escrever uma das opções: Vazio, Vacío ou Empty;
 - Correção do problema na seleção do DropDownList, todas as opções são deselecionadas antes. 

**Versão 2.5.1**

<em>18/08/2020</em>

 - Adicionado verbos em espanhol;
 - Incluído arquivo .bat para executar a automação;
 - Correção nas cores da fonte para o arquivo .bat;
 - Limpeza das telas a cada opção escolhida.  

**Versão 2.4.2**

<em>17/08/2020</em>

 - Não será mais gerada uma Run no Azure quando a opção para não gravar evidências for escolhida;
 - Incluída mensagem informativa para o idioma Português.

**Versão 2.3.2**

<em>14/08/2020</em>
- Correção da função de criação dos diretórios de log e evidências.
- Correção das mensagens informativas de tradução;
- Inclusão dos verbos em inglês.

**Versão 2.3.1**

<em>14/08/2020</em>
- Detecção automática de alterações do arquivos .yml e tradução dos arquivos para outros idiomas.

**Versão 2.3.0**

<em>13/08/2020</em>
- Detecção do idioma da máquina a tradução de todas as mensagens automaticamente;
- Alteração do .yml para realizar as traduções das mensagens;
- Adaptação dos comandos de log em todos os arquivos.


**Versão 2.2.12**

<em>07/08/2020</em>
- Finalização da automação quando o TestSuit não possuir casos de teste;
- Utilização do Kwargs como argumento das funções;
- Possível utilizar a descrição "Internet Explorer" para escolher o navegar também, além da sigla "IE".

**Versão 2.2.11**

<em>30/07/2020</em>
- Retirada da função Escolher, pois já estava sendo realizada pela função Selecionar.
- Realizada a limpeza do campo antes de preenchê-lo

**Versão 2.2.10**

<em>29/07/2020</em>
- Correção da criação da pasta de Logs caso não existisse.

**Versão 2.2.9**

<em>27/07/2020</em>
- **__[Novo]__** Inclusão do Readme.md;
- **__[Novo]__** Configuração de 5 segundos para encontrar o componente na tela.

**Versão 2.2.8**

<em>24/07/2020</em>
- Substituição da funções para encontrar o elemento para o By.

**Versão 2.2.7**

<em>24/07/2020</em>
- Possibilidade de executar no IE 11; 
- Alteração da função RemoverHTML.

**Versão 2.2.6**

<em>22/07/2020</em>
- Tratamento do espaço no nome do caso de teste;
- Correção na execução da sequência dos casos de teste na TestSuit, pois só executava o primeiro;
- Aumento do tempo para verificar uma frase IE, Edge e Firefox.

**Versão 2.2.5**

<em>21/07/2020</em>
- Correção do problema de VerificarValor no Firefox e no Edge; 
- Retirada de variáveis que não eram mais utilizadas.

**Versão 2.2.4**

<em>21/07/2020</em>
- Caso um passo fique em branco uma mensagem será apresentada, tanto no PyCharm quanto no log.

**Versão 2.2.3**

<em>20/07/2020</em>
- Correção no título principal do log; 
- Correção na função Informar.

**Versão 2.2.2**

<em>20/07/2020</em>
- Quando a função de “Verificar” falhar agora está alterando o status do caso de teste para “Failed” no Azure.
