salar = float(input())
vendas = float(input())

def calculaComissao(salario, vendas, porcentagem):
    salarioFinal = salario + (vendas * ((porcentagem/100)))
    return salarioFinal

salarioFinal = calculaComissao(salar, vendas, 24)

print("Eileen Greenawalt deve receber R$ {:.2f} no final do mês".format(salarioFinal))
