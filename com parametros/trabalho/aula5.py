#Exercicio 1 
n = int(input("Digite um número inteiro:")) 
def verifica(n):
    try:
        
        if n < 0:
            return "Número inválido"
        if n % 2 == 0 and n % 3 == 0:
            return "Par e multiplo de 3"
        
        elif n % 2 != 0 and n % 5 == 0:
            return "ímpar e multiplo de 5"
        
        elif n % 2 == 0 and n % 3 != 0 and n % 5 != 0:
            return "Par e não multiplo de 3 e 5"
        
        elif n % 2 != 0 and n % 5 != 0:
            return "ímpar e não multiplo de 5"
        
     
    except ValueError:
        return "Valor inválido"  
    
print(verifica(n))
#exercicio 2
def maior_de_tres(a, b, c):
    
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
        
    if a == b and a > c:
            return "Há uma repetição entre os maiores valores"
    elif b == c and b > a:
            return "Há uma repetição entre os maiores valores"
    elif c == a and c > b:
            return "Há uma repetição entre os maiores valores"
        
try: 
    a = float(input("Digite um número:"))
    b = float(input("Digite outro número:"))
    c = float(input("Digite outro número:"))
    print(maior_de_tres(a, b, c))
except ValueError:
    print("Valor inválido")

#Exercicio 3
def classifica_imc(peso, altura):
        
        imc = peso / (altura ** 2)
        if imc < 18.5:
            return "Abaixo do peso"
        elif imc < 24.9:
             return "Peso ideal"
        elif imc < 29.9:
             return "Sobrepeso"
        elif imc < 34.9:
             return "Obesidade grau 1"
        else:
             return "Obesidade grau 2 ou mais-atenção!"
try:
     peso = float(input("Digite seu peso:"))
     altura = float(input("Digite sua altura:"))
     print(classifica_imc(peso, altura))
except ValueError:
     print("Valor inválido")

#Exrcicio 4
def contador_reverso(inicio):
     if inicio < 0:
          return "Número inválido"
     
     while inicio >= 0:
          print(inicio)
          inicio -= 1
try:
     inicio = int(input("digite um número:"))
     contador_reverso(inicio)
except ValueError:
     print("Valor inválido")

#Exercicio 5
def tentando_ate_negativo():
     soma = 0
     quantidade = 0
     while True:
          try:
            num = float(input("Digite um número:"))
            if num < 0:
                print("Número negativo")
                break
            soma += num
            quantidade += 1
          except ValueError:
               print("Inválido, tente novamente")
     if quantidade == 0:
        print("Nenhum número positivo.")
     else:
        media = soma / quantidade
        print(f"A média dos números positivos digitados é: {media:.2f}")       
tentando_ate_negativo()


#Exercicio 6 
def tabuada(n):
     print(f"Tabuada de {n}:")
     for i in range(1, 11):
          print(f"{n} x {i} = {n*i}")

try:
    n = float(input("Digite um número:"))
    tabuada(n)
except ValueError:
     print("Valor inválido")  

#Exercicio 7 
def calculadora(a, b, operacao):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        return a / b
    else:
        return "Operação inválida"
try:
     a = float(input("Digite o primeiro número:"))
     b = float(input("Digite o segundo número:"))
     operacao = input("Digite a operação (+, -, *, /):")  
     resultado = calculadora(a, b, operacao)
     print(f"Resultado: {resultado}")
except ValueError:
     print("Valor inválido")

#Exercicio 8
def verifica_primo(num):
    if num < 2:
         return "Número inválido"
    divisor = 2
    while divisor * divisor <= num:
         if num % divisor == 0:
              return "Não é primo"
         divisor += 1
    return "Primo"
try: 
     num = int(input("Digite um número:"))
     if verifica_primo(num):
          print(f"{num}: {verifica_primo(num)}")
except ValueError:
     print("Valor inválido")
         

#Exercicio 9
def par(num):
     return "Par" if num % 2 == 0 else "Ímpar" 

def fatorial(num):
    if num < 0:
         return "Número inválido"
    
    resultado = 1
    while num > 1:
         resultado *= num
         num -= 1
    return resultado
while True:
    print("Escolha uma opção:")
    print("1 - Verificar se o número é par")
    print("2 - Calcular fatorial")
    print("3 - Sair")
    
    try:
        opcao = int(input("Digite uma das opções: "))
    except ValueError:
        print("Valor inválido")
        continue
       
    if opcao == 1:
        try:
            num = int(input("Digite um número inteiro: "))
            print(f"{num} é {par(num)}")
        except ValueError:
            print("Valor inválido")

    elif opcao == 2:
        try:
            num = int(input("Digite um número inteiro: "))
            print(f"{num}! = {fatorial(num)}")
        except ValueError:
            print("Valor inválido")

    elif opcao == 3:
        print("Saindo...")
        break  

    else:
        print("Opção inválida! Escolha 1, 2 ou 3.")

#Exercicio 10
numeros = []  # Lista global para armazenar os números inseridos

def adicionar_numero():
    while True:
        try:
            num = int(input("Digite um número inteiro positivo: "))
            if num > 0:
                numeros.append(num)
                print(f"Número {num} adicionado com sucesso!")
                break
            else:
                print("Número inválido! Digite um número positivo maior que zero.")
        except ValueError:
            print("Valor inválido! Digite um número inteiro.")

def exibir_estatisticas():
    if not numeros:
        print("Nenhum número foi inserido ainda.")
        return

    total_numeros = len(numeros)
    soma_total = sum(numeros)
    media = soma_total / total_numeros
    maior = max(numeros)
    menor = min(numeros)

    print("\n===== Estatísticas =====")
    print(f"Quantidade de números: {total_numeros}")
    print(f"Soma total: {soma_total}")
    print(f"Média: {media:.2f}")
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
    print("========================")

def verificar_paridade_multiplos():
    if not numeros:
        print("Nenhum número foi inserido ainda.")
        return

    print("\n===== Paridade e Múltiplos =====")
    for num in numeros:
        paridade = "Par" if num % 2 == 0 else "Ímpar"
        multiplos = []
        if num % 3 == 0:
            multiplos.append("múltiplo de 3")
        if num % 5 == 0:
            multiplos.append("múltiplo de 5")
        
        descricao = f"Número {num}: {paridade}"
        if multiplos:
            descricao += ", " + " e ".join(multiplos)
        
        print(descricao)
    print("=================================")

def contagem_regressiva():
    if not numeros:
        print("Nenhum número foi inserido")
        return

    ultimo_numero = numeros[-1]
    if ultimo_numero > 0 and ultimo_numero % 2 == 0:
        print(f"\nContagem regressiva a partir de {ultimo_numero}:")
        while ultimo_numero >= 0:
            print(ultimo_numero, end=" ")
            ultimo_numero -= 2
        print("\nContagem finalizada!")
    else:
        print("Não é possível executar a contagem com este valor")

def menu():
    while True:
        print("\n====== MENU PRINCIPAL ======")
        print("[1] Adicionar número à lista")
        print("[2] Exibir estatísticas")
        print("[3] Verificar paridade e múltiplos")
        print("[4] Mostrar contagem regressiva do último número")
        print("[5] Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida! Digite um número entre 1 e 5.")
            continue

        if opcao == 1:
            adicionar_numero()
        elif opcao == 2:
            exibir_estatisticas()
        elif opcao == 3:
            verificar_paridade_multiplos()
        elif opcao == 4:
            contagem_regressiva()
        elif opcao == 5:
            print("Encerrando o programa... Até logo!")
            break
        else:
            print("Opção inválida! Escolha um número entre 1 e 5.")


menu()
       
            


                    



    
        
     
    
    
    
      

      
      