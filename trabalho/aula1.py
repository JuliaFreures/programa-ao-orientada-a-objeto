#Exercicio 1
nome = input("Digite seu nome:")
num1 = int(input("Digite sua dade:"))
num2 = float(input("Digite sua altura em metros:"))
print(f"Seu nome é {nome}, você tem {num1} anos e sua altura é {num2}")

#Exercicio 2
nome = input("Digite seu nome:")
num1 = int(input("Digite um número inteiro:"))
num2 = float(input("Digite um número decimal:"))
resultado = num1 + num2
if resultado >= 10:
    print(f"Seu nome é {nome} e a soma dos seus números é {resultado}")
else:
    print(f"{resultado / 2}")
 
