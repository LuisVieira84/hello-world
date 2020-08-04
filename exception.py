#DELIMITER = " + "

#fruit_list = ["apple", "orange", "lemon", "raspberry"]
#print(DELIMITER.join(fruit_list))

guess = 1

while True:
    num = input("Digite um numero entre 0-100: ")
    try:
        num = int(num)

    except:
        print("Numero inválido!")
        continue

    if num > 45:
        print("Numero maior")
    elif num < 45:
        print("Numero menor")
    else:
        break
    guess += 1

print(f"Voce conseguiu em {guess} tentativas")
