while True:
    useranme = input("username?")
    if useranme.lower() != "neo":
        print("Usuario não encontrado")
        continue
    senha = input("Qual a sua senha?")
    if senha == "1234":
        print("Bem-vindo, {}".format(useranme))
        print("Aceita um café?")
        break