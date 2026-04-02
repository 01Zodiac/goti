#Calcula a média do boletim(quatro médias) e define se com a média passa ou não(nota pra passar: 7)

media1 = float(input("Digite sua primeira média: "))
media2 = float(input("Sua segunda média: "))
media3 = float(input("Sua terceira média: "))
media4 = float(input("Sua quarta méida: "))

media_geral = (media1 + media2 + media3 + media4)/4

if media_geral > 7:
    print("Passou, pabéns")

elif 7 > media_geral >= 6.5:
    print("Arredondamo pra 7 ae, passou")

else:
    print("Ficou de xereca")
