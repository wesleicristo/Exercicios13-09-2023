nomeCliente = input("Digite o nome do cliente: ")
diasLocacao = int(input("Digite quantidade de dias locados: "))
valorLocacao = float(180.00)
while diasLocacao <= 0 :
    diasLocacao = int(input("Digite um valor válido: "))

print(f"O cliente {nomeCliente} deve R${diasLocacao * valorLocacao:.2f} na locação referente a {diasLocacao} dias da locação.")