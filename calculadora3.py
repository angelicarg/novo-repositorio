outra_conta = "SIM"

while outra_conta == "SIM":
  
  print("SELECIONE A OPERAÇÃO DESEJADA")
  print("+ para Adição")
  print("- para Subtração")
  print("* para Multiplicação")
  print("/ para Divisão")
  print("0 para sair")

  
  operador = input("\nQual operação você deseja realizar? ")

   #+
  if operador == "+":
    valor1 = float(input("\nDigite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    soma = valor1 + valor2
    print("\nA soma entre",valor1,"e",valor2,"é:",soma,"\n")
    print("*"*33,"\n")
    outra_conta = input("Gostaria de fazer outra operação? ").upper()
    print("*"*33,"\n")

  #-
  if operador == "-":
    valor1 = float(input("\nDigite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    diminuir = valor1 - valor2
    print("\nA subtração entre",valor1,"e",valor2,"é:",diminuir,"\n")
    print("*"*33,"\n")
    outra_conta = input("Gostaria de fazer outra operação? ").upper()
    print("*"*33,"\n")

  #*
  if operador == "*":
    valor1 = float(input("\nDigite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    multiplicar = valor1 * valor2
    print("\nA multiplicação entre",valor1,"e",valor2,"é:",multiplicar,"\n")
    print("*"*33,"\n")
    outra_conta = input("Gostaria de fazer outra operação? ").upper()
    print("*"*33,"\n")

  #/
  if operador == "/":
    valor1 = float(input("\nDigite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    while valor2 == 0:                  #Garantindo que d2 não seja zero!!
      print("O segundo valor não pode ser zero!")
      valor2 = float(input("\nDigite o segundo valor (diferente de zero): "))
    dividir = valor1 / valor2
    print("\nA divisão entre",valor1,"e",valor2,"é:",dividir,"\n")
    print("*"*33,"\n")
    outra_conta = input("Gostaria de fazer outra operação? ").upper()
    print("*"*33,"\n")

  #0
  if operador == "0":
    print("Programa encerrado")
    break