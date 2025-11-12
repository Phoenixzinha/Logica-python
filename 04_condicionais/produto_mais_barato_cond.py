# Utilizando estruturas condicionais

valor_ano1 = float(input("Digite o valor do carro no primeiro ano: "))
valor_ano2 = float(input("Digite o valor do carro no segundo ano: "))
valor_ano3 = float(input("Digite o valor do carro no terceiro ano: "))

if valor_ano1 >= valor_ano2 and valor_ano1 >= valor_ano3:
    valor_mais_alto = valor_ano1
elif valor_ano2 >= valor_ano1 and valor_ano2 >= valor_ano3:
    valor_mais_alto = valor_ano2
else:
    valor_mais_alto = valor_ano3

if valor_ano1 <= valor_ano2 and valor_ano1 <= valor_ano3:
    valor_mais_baixo = valor_ano1
elif valor_ano2 <= valor_ano1 and valor_ano2 <= valor_ano3:
    valor_mais_baixo = valor_ano2
else:
    valor_mais_baixo = valor_ano3

print(f"O valor mais alto é: {valor_mais_alto}")
print(f"O valor mais baixo é: {valor_mais_baixo}")