import datetime

nome = input("Digite seu nome: ")
anoNasc = int(input("Digite seu ano de nascimento: "))

while anoNasc >= datetime.date.today().year :
    anoNasc = int(input("Digite um ano menor que o atual: "))

print(f"{nome} você possui {datetime.date.today().year - anoNasc} anos de idade.")