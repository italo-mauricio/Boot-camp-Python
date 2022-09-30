while True:
    texto = input("Informe um texto: ")
    VOGAIS = "AEIOU"
    numero = ['0','1','2','3','4','5','6','7','8','9']
    for letra in texto:
        if letra.upper() in VOGAIS:
            print(letra, end="")
    else:
        if texto == numero:
            print('Digite apenas letras!')
            
    print() 


