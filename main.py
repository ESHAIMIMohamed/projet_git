import random
number = random.randint(1,20)
guess =int(input("Je pense à un chiffre de 1 à 20. Qu'est-ce que c'est?"))
while guess != number:
    if guess < number:
        print("Votre nombre était trop bas...")
    else:
        print("Votre nombre était trop élevé...")
    guess = int(input("Veuillez réessayer..."))
print("Toutes nos félicitations! Bonne réponse!")