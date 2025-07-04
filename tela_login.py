import PySimpleGUI as sg

usuarios = []
def adicionar_logins_anteriores():
    try:
        with open('cadastros.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            campos = linha.strip().split('|')
            nome = campos[0]
            email = campos[1]
            senha = campos[2]
            novo_usuario = {"nome":nome, "email":email, "senha":senha}
            usuarios.append(novo_usuario)
    except FileNotFoundError:
        arquivo = 'cadastros.txt'
        with open(arquivo, 'w') as arquivo:
            arquivo.write("")
        pass
    except IndexError:
        pass
adicionar_logins_anteriores()
# Criar a tela de login
def criar_tela_login():
    sg.theme("DarkGrey11")
    layout = [
        [sg.Text("Bem vindo, por favor Insira suas credênciais", size=(45,2), justification='center')],
        [sg.Text("Email:  "),sg.Input(key="email", size=(35,1))],
        [sg.Text("Senha: "),sg.Input(key="senha", size=(35,1), password_char='*'), sg.Button("Exibir", key="mostrar_senha", size=(5))],
        [sg.Text("", key="validacao")],
        [sg.Button("Cadastre-se",key="cadastro"), sg.Button("Acessar", key="acessar")]

    ]
    window = sg.Window("Login", layout)
    monitorar_eventos(window)

# Monitorar eventos da tela
def monitorar_eventos(window):
    mostrarsenha = False
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break
        if event == "mostrar_senha":    
            if mostrarsenha == False:
                mostrarsenha = True
            else:
                mostrarsenha = False
            if mostrarsenha == True:
                window["senha"].update(password_char='')
                window["mostrar_senha"].update("Ocultar")
            else:
                window["senha"].update(password_char='*')
                window["mostrar_senha"].update("Exibir")
        if event == "cadastro":        # Botão Cadastra-se - Menu Principal
                window.close()
                tela_cadastrar()
        if event == "acessar":          # Menu Principal
            email = values["email"]
            senha = values["senha"]
            validar_login(email,senha,window)
        if event == "voltar":           # Menu Cadastro e Logado
            window.close()
            criar_tela_login()
        if event == "voltar_credencial":           # Menu Cadastro e Logado
            window.close()
        if event == "salvar":          # Menu Cadastro
            nome = values["nome"]
            email = values["email"]
            senha = values["senha"]

            if nome and email and senha: 
                erro = cadastrar_acesso(nome,email,senha)
                if erro:
                    cadastrar_dados_invalidos(erro)
                else:
                    window.close()
                    tela_cadastro_realizado()

            else:
                erro = 'Preencha todos os campos corretamente'
                cadastrar_dados_invalidos(erro)
            

# Adiciona emails e senhas do txt na lista usuários       

def cadastrar_acesso(nome,email,senha):
    for usuario in usuarios:
        if usuario['email'] == email:
            erro = 'Esse email já esta sendo utilizado'
            return erro
    

    with open('cadastros.txt', 'a') as arquivo:
        dados = nome+"|"+email+"|"+senha+"\n"
        arquivo.write(dados)    
    arquivo.close()    
    novo_usuario = {"nome":nome, "email":email, "senha":senha}
    usuarios.append(novo_usuario)
    return False

# Cria a tela de cadastrar conta
def tela_cadastrar():
    layout = [
        [sg.Text("Insira os dados para Cadastrar-se", size=(45,2), justification='center')],
        [sg.Text("Nome:  "),sg.Input(key="nome", size=(35,1))],
        [sg.Text("Email:  "),sg.Input(key="email", size=(35,1))],
        [sg.Text("Senha: "),sg.Input(key="senha", size=(35,1), password_char='*'), sg.Button("Exibir", key="mostrar_senha", size=(5))],
        [sg.Button("Salvar",key="salvar"), sg.Button("Voltar", key="voltar")]
    ]
    window = sg.Window("Cadastrar Conta", layout)
    monitorar_eventos(window)

# Valida o login
def validar_login(email,senha,window):
    credenciais = False
    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            nome = usuario["nome"]
            credenciais = True
    if credenciais:
        window.close()
        tela_login_realizado(nome) 
    else:
        credencial_invalida()


def tela_login_realizado(nome):
    layout = [
        [sg.Text("Seja bem Vindo "+nome+", Login realizado com sucesso", size=(45,2), justification='center')],
        [sg.Button("Voltar", key="voltar")]
    ]
    window_logado = sg.Window("Conta Logada", layout)
 
    while True:
        event_logado, values_logado = window_logado.read()
        if event_logado == sg.WIN_CLOSED:
            window_logado.close()
            break
        elif event_logado == "voltar":
            window_logado.close()
            criar_tela_login()
            break


def credencial_invalida():
    layout = [
        [sg.Text("Credenciais inválidas, tente novamente!", size=(30,2),  justification='center')],
        [sg.Button("OK", key="ok_credencial")]
    ]
    window_credencial_invalida = sg.Window("Atenção", layout)
    while True:
        event_credencial, values_credencial = window_credencial_invalida.read()
        if event_credencial == sg.WIN_CLOSED:
            window_credencial_invalida.close()
            break
        if event_credencial == "ok_credencial":
            window_credencial_invalida.close()
            break

def cadastrar_dados_invalidos(erro):
    layout = [
        [sg.Text(f"{erro}", size=(30,2),  justification='center')],
        [sg.Button("OK", key="ok_cadastrar")]
    ]
    window_cadastrar_invalido = sg.Window("Atenção", layout)
    while True:
        event_cadastrar, values_cadastrar = window_cadastrar_invalido.read()
        if event_cadastrar == sg.WIN_CLOSED or event_cadastrar == "ok_cadastrar":
            window_cadastrar_invalido.close()
            break

def tela_cadastro_realizado():
    layout = [
        [sg.Text("Cadastro Realizado com sucesso", size=(45,2), justification='center')],
        [sg.Button("ok", key="ok_cadastro")]
    ]
    window_cadastro_realizado = sg.Window("Cadastro Realizado", layout)
 
    while True:
        event_cadastro, values_cadastro = window_cadastro_realizado.read()
        if event_cadastro == sg.WIN_CLOSED or event_cadastro == "ok_cadastro":
            window_cadastro_realizado.close()
            criar_tela_login()
            break
    

criar_tela_login()
