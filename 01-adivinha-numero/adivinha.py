# 1. O computador sorteia um número de 1 a 100
# 2. Pedir um chute ao jogador
# 3. Comparar o chute com o número sorteado
# 4. Se for maior, dizer "menor"; se for menor, dizer "maior"
# 5. Repetir até o jogador acertar
# 6. Mostrar em quantas tentativas ele acertou

import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    chute = int(input("Digite um numero entre 1 e 100: "))
    tentativas += 1
    if chute > numero_secreto:
        print("Menor")
    elif chute < numero_secreto:
        print("Maior")
    else:
        print("PARABENS VC ACERTOU !!")
        print(f"VC ACERTOU COM {tentativas} TENTATIVAS !!")
        break
