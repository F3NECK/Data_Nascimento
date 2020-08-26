"calculo da data de nascimento do individuo"

"entrada"
nome = input("ensira seu nome de usuario: ")
senha = input("para sua segurança ensira sua senha: ")
datanasc = int(input("Qual seu ano de Nascimento? "))
idade = 2020 - datanasc
dias = idade * 365
"saida"
print("a idade de", nome, "é", idade ,"com isso ele viveu", dias ,"dias")
