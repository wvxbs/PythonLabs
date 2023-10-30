lista_notas = []

def Main():
    for i in range(4):
        RecebeNota(i)
    
    ExibeNotas()
    print("A média é: " + str(CalculaMedia()))

def RecebeNota(Indice):
    nota = input("Insira a nota número " + str(Indice + 1))
    lista_notas.append(float(nota))

def CalculaMedia():
    Acumulador = 0
    for i in lista_notas:
        Acumulador += i
    
    return Acumulador/len(lista_notas)

def ExibeNotas():
    Indice = 0
    for i in lista_notas:
        print("" + str(Indice + 1) + "a nota: " + str(i))
        Indice +1

Main()