def Main():
    ValorDaHora = input("Insira o quanto você ganha por Hora: ")
    HorasTrabalhadas = input("Insira o total de horas trabalhadas no mês: ")
    
    SalarioBruto = CalculaSalario(int(ValorDaHora), int(HorasTrabalhadas))

    DescontoInss = CalculaDesconto(int(SalarioBruto), 0.11)
    DescontoIr = CalculaDesconto(int(SalarioBruto), 0.8)
    DescontoSindicato = CalculaDesconto(int(SalarioBruto), 0.5)

    SalarioLiquido = DescontoSindicato

    print("Seu salário bruto é:" + str(SalarioBruto))
    print("Valor pago ao inss: " + str(CalculaOValorDoDesconto(SalarioBruto, DescontoInss)))
    print("Valor pago ao imposto de renda: " + str(CalculaOValorDoDesconto(SalarioBruto, DescontoIr)))
    print("Valor pago ao sindicato: " + str(CalculaOValorDoDesconto(SalarioBruto, DescontoSindicato)))
    print("Após descontos, o seu salário líquido é: " + str(SalarioLiquido))

def CalculaSalario(ValorDaHora, HorasTrabalhadas):
    return ValorDaHora * HorasTrabalhadas

def CalculaDesconto(Salario, Desconto):
    return Salario - (Salario * Desconto)

def CalculaOValorDoDesconto(Salario, Desconto):
    return Salario - Desconto

Main()