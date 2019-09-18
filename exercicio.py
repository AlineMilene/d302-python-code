idade = int(input("Digite sua idade: "))

if idade >= 21 and idade <= 65:
    salario = float(input("Digite o seu salario: "))
    emprestimo = float(input("Digite o valor desejado de empréstimo: "))
    if emprestimo < 10*salario:
        print("Empréstimo aprovado!")
    else:
        print ("Empréstimo superior ao permitido pelo seu salário!n")
else:
    print("Idade inválida para empréstimo")