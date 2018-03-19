# Teste básico Allgoo

Caros candidatos, leiam atentamente as instruções neste README para realizar o teste.

> Antes de começar, prepare seu ambiente.

**Este teste requer:**
- Sua IDE favorita
- Ambiente de desenvolvimento com Python 3.5+
- Banco de dados (MongoDB, MySQL)

--------

## Tarefas do teste:

**NOTE:** Você está livre em usar o que desejar. Apenas, gostaria de uma explicação do porquê da sua escolha.

1. Criar um front-end simples para postagens entre usuários.
  - O usuário precisa se cadastrar e se logar via Rede Social (Facebook ou Twitter ou Google)
  - O usuário poderá compartilhar uma informação pessoal e ter a possibilidade de marcar se ela é verdadeira ou não
  - Ao compartilhar irá para o mural que será visível por todos os usuários
  - Neste post terá dois botões para que outros possam dizer se acreditam ou não na informação
  - Mostrar no perfil o ranking do usuário de acordo com as assertividades dos usuários classificando entre honesto ou mentiroso 
  
2. Criar um back-end
  - Criar a lógica para o registro e login via rede social
  - Criar os endpoints necessários para envio da informação, leitura no moral por todos e escolha da veracidade da informação.
  - Se mais de 3 usuários acertarem o que a informação é, o usuário que deu a informação perde 1 ponto que será dividido entre os 3 e a cada novo usuário o ponto dobra. Exemplo:


    - 3 pessoas acertam = 1 ponto / 3 usuários
    - 4 pessoas acertam = 2 pontos / 4 usuários
    - 5 pessoas acertam = 4 pontos / 5 usuários

    O mesmo vale para os erros, quando os usuários erram a informação, o ponto é calculado pela quantidade de usuários que erraram (usando o mesmo critério acima), todos os pontos vão para o usuário que deu a informação e são retiradas as porcentagens dos usuários que erraram.

  - Apenas participa quem vota
  - Toda transação de pontos deve ser mapeada e garantindo a retirada e envio dos pontos de cada participante.
   
## Instruções adicionais

- Faça um fork do repositório
- Testes não são opcionais
- Depois de terminado, envie-nos o link do repositório.
- Deixe comentários, caso tenha alguma dúvida.
- Implementações sem um README serão automaticamente rejeitadas.

## Bonus / Atividades Opcionais

- Código limpo
- Conhecimento do fluxo da aplicação
- Conhecimento das melhores práticas.
- Componentização.
- Conhecimento de Docker.
- Prover o sistema em alguma cloud como a Heroku.
- Criar um endpoint para healthcheck 
   - para a rota `/healthcheck`
   - proponha quais seriam as informações essenciais em um healthcheck ou se não tem necessidade.
- nginx ou alternativa simples de webserver


## feitos

- Tela de login (frontEnd e back pela metade):
- Inicio para se logar com rede social:
- Tempo utilizado: 12h - 3h/dia;


## o que foi utilizado

- IDE= Atom;
- Systema operacional = Arch linux;
- BD = sqlalchemy -obs tentei utilizar dos BD requeridos mas estou aprendendo Python e Flask ainda entao utilizei do que estou familiarizado com o que estou aprendendo, ate tenho conhecimento e exp em Mysql e Docker, mas nao consegui implementar nesse projeto;



