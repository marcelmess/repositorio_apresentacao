#apresentação
#python

print("Olá!")
print("Gostaria de saber algo sobre o perfil marcel mess? Posso apresentar informações sobre 'identidade' e 'programação', caso digite tais termos no console.")
print("Se não for o caso, digite 'sair'")

#todas possibilidades de texto
text_identidade = "marcel mess é o perfil público de Marcel Messias Cardoso no Github. Marcel estuda Ciências Sociais (UFPR) e tenciona se tornar professor em breve. Satisfazendo uma curiosidade pessoal, ele passou a estudar Python no final de dezembro de 2024. Para salvar os seus humildes projetos de estudo, explorar a comunidade dev e aprender mais, ele fez um perfil no GitHub."
text_programação = "Sobre o que exatamente? Sobre o tempo de experiência que marcel mess tem com programação em Python, digite 'tempo'. Sobre a razão para marcel mess ter escrito e subido no Github o código por trás da presente apresentação, digite 'razão'"
tempo = "marcel  mess começou a estudar Python no final de dezembro de 2024. O código que estrutura esta apresentação foi criado por ele no dia 24 de dezembro de 2024, exatamente 1 dia antes de completar sua primeira semana estudando Python."
razão = "O presente código visa colocar em prática o que marcel mess aprendeu durante a sua primeira semana estudando Python. Ele foi subido no GitHub para que marcel mess iniciasse um hábito que, de acordo com o que ele ficou sabendo, é conveniente para sua experiência enquanto (aspirante a) dev."
erro = "Requisição inválida!"
mensagem_saída = "Você finalizou o programa. Tchau!"
mais1 = "Algo mais? ('identidade', 'programação')"

#código pra informar sobre o que foi solicitado
loop = True
while loop == True:
    entrada_usuário1 = str(input(""))
    if entrada_usuário1 == "identidade":
        print(text_identidade)
        print(mais1)
    elif entrada_usuário1 == "programação":
        print(text_programação)
        programação1 = str(input(""))
        if programação1 == "tempo":
            print(tempo)
            print(mais1)
        elif programação1 == "razão":
            print(razão)
            print(mais1)
        else:
            print(erro)
    elif entrada_usuário1 == "sair":
        loop == False
        print(mensagem_saída)
    else:
        print(erro)

