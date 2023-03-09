import requests
import random

url = "https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt"
response = requests.get(url)

palavras = response.content.decode("utf-8").split()

palavra = random.choice(palavras)

letras_adivinhadas = ["_" for letra in palavra]

vidas = 6

while vidas > 0:
    print("Palavra: ", " ".join(letras_adivinhadas))
    print("Vidas restantes: ", vidas)

    letra = input("Digite uma letra: ").lower()

    if letra in letras_adivinhadas:
        print("Você já tentou essa letra antes.")
    else:
        letras_palavra = list(palavra)
        letras_certas = [i for i in range(len(letras_palavra)) if letras_palavra[i] == letra]
        if letras_certas:
            for i in letras_certas:
                letras_adivinhadas[i] = letra
            if "_" not in letras_adivinhadas:
                print("Você venceu! A palavra é", palavra)
                break
        else:
            vidas -= 1
            print("Você errou! Você tem", vidas, "vidas restantes.")
else:
    print("Você perdeu! A palavra era", palavra)
