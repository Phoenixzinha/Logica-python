num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação que você deseja realizar (+, -, *, /): ")

if operacao == "+":
  resultado = num1 + num2
elif operacao == "-":
  resultado = num1 - num2
elif operacao == "*":
 resultado = num1 * num2
elif operacao == "/":
  resultado = num1 / num2
else:
  print("Operação inválida!")

if resultado % 2 == 0:
  print(f"O resultado da operção escolhida é: {resultado} e o resultado é par!")
else:
  print(f"O resultado da operção escolhida é: {resultado} e o resultado é ímpar!")

if resultado > 0:
  print("O resultado é positivo!")
else:
  print("O resultado é negativo!")

if resultado % 1 == 0:
  print("O resultado é um número inteiro!")
else:
  print("O resultado é um número decimal!")