# Tela de Login

## Descrição do projeto:

Este repositório tem como objetivo criar uma interface gráfica simples, representando uma tela de cadastro, login e telas de feedback (login efetuado, erros de login ou cadastro).

Verificações:

Na interface é possivel cadastrar e efetuar o login, tudo isso com as devidas verificações, conforme descrito abaixo:
- Ao tentar efetuar o login verifica se as credências foram preenchidas e se válidas;
- Na tela de cadastro verificar se todos os campos estão preenchidos corretamente;
- Ao tentar cadastrar um novo usuário, verificar se o email já esta cadastrado;

Feedback:

- Quando houver sucesso em efetuar login ou em cadastrar, um novo usuário uma tela informando aparece;
- Se o usuário preencher incorretamente algum campo na tela de login ou cadastro, uma pop-up será apresentado.

Base de dados:

Nesse projeto esta sendo usado o arquivo "cadastros.txt" para armazenar os dados dos usuários cadastrados.
Assim que o programa é executado esse arquivo de texto é lido e armazenado. Isso possibilita que cadastros feitos em sessões anteriores tambem sejam válidos em novas sessões.
 
>Utilizei um arquivo de texto, por ser um projeto simples, mas pode ser facilmente adaptado para outras fontes de dados, se necessário. 

<br />

# Desenvolvimento

O programa foi desenvolvimento em Python, utilizando apenas as bibliotecas nativas e PySimpleGUI para a criação da interface gráfica.

<br />


# Como instalar:
1- Clone o repositório:
```sh
git https://github.com/Gabrielnunesilva/tela_login.git
```

2- Entre na pasta do repositório que você acabou de clonar:
```sh
cd tela_login
```

3- Instale as dependências dos projeto:
```sh
pip install PySimpleGUI
```
4- Execute o programa:
```sh
tela_login.py  
```
<br />

# Como utilizar:
Após executar, você verá uma tela para preencher dados de email e senha, botão de login e cadastro. 
<br />
Caso seja o primeiro acesso, clique em cadastro, preencha os dados e salve.
<br />
Após se cadastrar, basta preencher os dados e clicar em login.
<br />



