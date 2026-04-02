TierS = [67, 69, 10, 21, 24, 7, 100]
TierA = [20, 30, 40, 50, 60, 70, 80, 90, 1, 5, 27, 17, 2, 13, 99]
TierB = [12, 3, 4, 6, 8, 9, 16, 32, 64, 49, 81, 68,
         22, 33, 44, 55, 66, 77, 88, 98, 97, 25, 18, ]

while True:

    try:
        numero = int(input("\nDigite um número de 1 a 100: "))

        if numero in TierS:
            print("\nTier S (goated)\n")
            break

        elif numero in TierA:
            print("\nTier A\n")
            break

        elif numero in TierB:
            print("\nTier B\n")
            break

        elif 1 <= numero <= 100:
            print("\nTier C (lixo)\n")
            break

        elif numero == 0:
            print("\nZero não mano\n")

        else:
            print("\nde 1 a 100 imbécil\n")

    except ValueError:
        print("\nTá bom cara mds\n")
