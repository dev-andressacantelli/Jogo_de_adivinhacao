print("*********************************")
print("Bem vindo ao jogo de adivinhação, melhor de três!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    #P/ concatenar string chamando variável: utilizar {} vazio + .format(var1,var2,var3 etc)
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    chute_eh_maior = chute > numero_secreto
    chute_eh_menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if(chute_eh_maior):
            print("Você errou! O seu chute foi maior do que o número secreto, tente um número menor!")
        elif(chute_eh_menor):
            print("Você errou! O seu chute foi menor do que o número secreto, tente um número maior!")

    rodada = rodada + 1

print("Fim do jogo!")