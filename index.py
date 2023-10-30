def Incremento(Limite):
    x=1
    while x<=Limite:
        print(x)
        x+=1
        if x == 5: break

def Busca(Parametro):
    mensagem = "Oi, meu nome é carol e esse é o meu canal!"
    print (Parametro in mensagem)

    if(Parametro in mensagem):
        print (Parametro)

def DividirStrings(Parametro=" "):
    mensagem = "Oi, meu nome é Carol e esse é o meu canal!"
    print(mensagem.split(Parametro))

def Main ():
    DividirStrings()

Main()