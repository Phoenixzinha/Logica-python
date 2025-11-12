quant_litros = float(input("Digite a quantidade de litros: "))
tipo_combustivel = input("Digite o tipo de combustível (E para etanol e D para diesel): ").upper()

if tipo_combustivel == "E":
  preco_litro = 1.70
  if quant_litros <= 15:
    desconto = 0.02
  else:
    desconto = 0.04
  valor_a_pagar = preco_litro * quant_litros * (1 - desconto)
  print(f"O valor a ser pago é: R$ {valor_a_pagar:.2f}")
elif tipo_combustivel == "D":
  preco_litro = 2.00
  if quant_litros <= 15:
    desconto = 0.03
  else:
    desconto = 0.05
  valor_a_pagar = preco_litro * quant_litros * (1 - desconto)
  print(f"O valor a ser pago é: R$ {valor_a_pagar:.2f}")
else:
  print("Tipo de combustível inválido!")