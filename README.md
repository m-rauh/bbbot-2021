# BBBot - 2021
## Robozinho em python para "automatizar" a votação no paredão do BBB

### Intro

Queremos automatizar a votação no BBB. No passado isso era possível usando Selenium, porém o mesmo estava automaticamente ativando o captcha e exigindo preenchimento do mesmo. A solução então foi um robô que encontrasse imagens na tela e clicasse, em outras palavras, um simulador do clique humano, só que sem precisarmos operar o mouse. Não trabalhaos em nenhuma solução em segundo plano, portanto, para usar a aplicação você não pode mexer na tela.

### O projeto
O projeto usa as libs *pyautogui* para reconhecimento de imagens na tela e movimento do mouse e *PIL*.

*pip install pyautogui* e *pip install pillow*

O processo trabalha em loop em 3 etapas:
  - Encontra e clica no nome do brother que você vai votar, a partir de uma imagem do nomes (ver pasta: img)
  - Encontra e clica no captcha
  - Encontra e clica em votar novamente


### Como usar
Se sua resolução de tela e tamanho da fonte do no site da Gshow for diferente a primeira coisa que precisa é tirar novos prints e salvar na pasta *img*.
Abra o site do Gshow e o programa em python. Você pode colocar eles lado a lado, ou rodar o programa e clicar alt-tab rapidinho.

### Possíveis Erros
A tela do site pode demorar pra responder, caso aconteça isso e o programa já tenha tentado encontrar e clicar na imagem, ele vai parar e dar um erro.

Caso de um erro logo na largada, tente tirar um print denovo, ele pode não estar encontrando a imagem que você salvou.

Depois de 40/50 votos o site exige um captcha mais complicado, isso é evitável colocando um espaçamento maior entre os votos, e colocando uma pausa longa depois de 30 votos. Porém ainda é possível que o site peça o captcha aleatoriamente.
