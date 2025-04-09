user = input("Digite o seu nome de Usuário: ")
password = input("Digite a sua Senha: ")

print("Conta criada com sucesso!")

def login(user, password):
    i = 0
    while i < 3:
        user2 = input("Digite o nome de Usuário: ")
        password2 = input("Digite a sua Senha: ")

        if user == user2 and password == password2:
            print(" Usuário correto! Login bem-sucedido.")
            break
        else:
            print(f" Login incorreto. Você ainda possui {2 - i} tentativas.")
            i += 1

    if i == 3:
        print(" Conta bloqueada após 3 tentativas.")

login(user, password)
