salario = input('Digite seu salário:')
salario = float(salario)

# dicionário faixa -> percentual de desconto
fDesc = {0: 0.0, 1: 7.5, 2: 15.0, 3: 22.5, 4: 27.5}

#dicionario faixa -> valor padrão
fVPad = {0: 0.0, 1: 169.44, 2: 381.44, 3: 662.77, 4: 896.00}

#verificador de qual faixa de imposto se enquadra o salario
if (salario <= 2259.20):
    faixa = 0
elif (salario >=2259.20) and (salario <=2826.65):
    faixa = 1
elif (salario >=2826.66) and (salario <=3751.05):
    faixa = 2
elif (salario >=3751.06) and (salario <=4664.86):
    faixa = 3
else: #salario implicito >= 4664.86
    faixa = 4
    
imposto = salario*(fDesc[faixa]/100)
vpad = fVPad[faixa]
impagar = imposto - vpad
liquido = salario - impagar

mensagem1 = "Bruto: %10.2f, Faixa: %d, Imposto: %5.2f" % (salario, faixa, imposto)
mensagem2 = "Padrão: %5.2f, Pagar: %5.2f, Líquido: %5.2f" % (vpad, impagar, liquido)
print(mensagem1)
print(mensagem2)

