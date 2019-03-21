"""
v and v = v
v and f = f
f and v = f
f and f = f

v or v = v
v or f = v
f or v = v
f or f = f

not (v = f) e (f = v)
"""
"""
Construa um programa que recebe três valores, A, B e C. Em seguida, apresente
na tela somente o maior deles.
"""
# a = int(input("Digite o valor de A: "))
# b = int(input("Digite o valor de B: "))
# c = int(input("Digite o valor de C: "))
#
# if(a>b and a>c):
#     print("A é o maior!")
# elif(b>a and b>c):
#     print("B é o maoir!")
# elif(c>b and c>a):
#     print("C é o maoir!")
# else:
#     print("Não pode ter valores iguais")

"""
Construa um programa que recebe três valores, A, B e C. Em seguida, apresente
na tela os números em ordem crescente.
"""
# a = int(input("Digite o valor de A: "))
# b = int(input("Digite o valor de B: "))
# c = int(input("Digite o valor de C: "))
#
# if(a>b>c or a>c>b):
#     if(b>c):
#         print("A, B e C")
#     else:
#         print("A, C e B")
# elif(b>a>c or b>c>a):
#     if(a>c):
#         print("B, A e C")
#     else:
#         print("B, C e A")
# elif(c>a>b or c>b>a):
#     if(a>b):
#         print("C, A e B")
#     else:
#         print("C, B e A")
# else:
#     print("Não pode ter valores iguais")

"""
Construa um programa que mostre menu exatamente como o exemplo abaixo e
implemente as funções necessárias:
== Menu de Opções ==
1. Somar 2 números
2. Potência Y de um número X (xy)
3. Raiz quadrada de X
== Opção escolhida:
"""

# print("""
# ======== Menu de Opções ========
# 1. Somar 2 números
# 2. Potência Y de um número X
# 3. Raiz quadrada de X
# """)
#
# x = float(input("Digite o valor de X: "))
# y = float(input("Digite o valor de Y: "))
#
# opcao = int(input("================ Opção escolhida: "))
#
# soma = x + y
# potencia = x ** y
# raiz = x**(1/2)
#
# if(opcao == 1):
#     print("Você escolheu 'Somar 2 números'")
#     print("A resposta é igual {}".format(soma))
# elif(opcao == 2):
#     print("Você escolheu 'Potência Y de um número X '")
#     print("A resposta é igual {}".format(potencia))
# elif(opcao == 3):
#     print("Você escolheu 'Raiz quadrada de X'")
#     print("A resposta é igual {}".format(raiz))
# else:
#     print("Não existe essa opção")

"""
Construa um programa para determinar se o indivíduo está com um peso favorável.
Essa situação é determinada através do IMC (Índice de Massa Corporal), que é
definida como sendo a relação entre o peso e o quadrado da altura do indivíduo.
Ou seja: IMC = peso/altura² e a situação do peso é determinada pela tabela
abaixo:
"""

# peso = float(input("Qual é seu peso?\n"))
# altura = float(input("Qual é sua altura em metros?\n"))
#
# imc = peso/(altura**2)
#
# if(imc<18.5):
#     print("Baixo peso!")
# elif(imc>18.5 and imc<24.9):
#     print("Peso normal!")
# elif(imc>25 and imc<29.9):
#     print("Pré-obesidade!")
# elif(imc>30 and imc <34.9):
#     print("Obesidade Grau I")
# elif(imc>35.5 and imd<39.9):
#     print("Obesidade Grau II")
# elif(imc>40):
#     print("Obesidade Grau III")
# else:
#     print("Ouve algum erro nas informações!")

"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e o contrataram para desenvolver o programa que vai calcular
os reajustes. Faça um programa que recebe o salário de um colaborador e calcule
o reajuste segundo o seguinte critério baseado no salário atual:
- até R$ 710,00 (incluindo): aumento de 20%
- entre R$ 710,00 e R$ 1.000,00: aumento de 15%
- entre R$ 1.000,00 e R$ 2.500,00: aumento de 10%
- de R$ 2.500,00 em diante: aumento de 5%
Após o aumento ser realizado, informe na tela:
- salário antes do reajuste;
- percentual de aumento aplicado;
- valor do aumento;
- novo salário, após o aumento.
"""

salario = int(input("Qual é seu salário?\n"))

if(salario<=710):
    aumento = (salario * 0.2)
    ajuste = salario + aumento
    print("Seu salário era {}.\n Teve um percentual de aumento de {}, ou seja, {}.\n Seu novo salário é {}".format(salario, "0.2", aumento, ajuste))


elif(salario>710 and salario<1000):
    aumento = (salario * 0.15)
    ajuste = salario + aumento
    print("Seu salário era {}.\n Teve um percentual de aumento de {}, ou seja, {}.\n Seu novo salário é {}".format(salario, "0.2", aumento, ajuste))

elif(salario>1000 and salario<2500):
    aumento = (salario * 0.10)
    ajuste = salario + aumento
    print("Seu salário era {}.\n teve um percentual de aumento de {}, ou seja, {}.\n Seu novo salário é {}".format(salario, "0.2", aumento, ajuste))

elif(salrio>2500):
    aumento = (salario * 0.05)
    ajuste = salario + aumento
    print("Seu salário era {}.\n teve um percentual de aumento de {}, ou seja, {}.\n Seu novo salário é {}".format(salario, "0.2", aumento, ajuste))

else:
    print("Alguma informação esta errada!")
