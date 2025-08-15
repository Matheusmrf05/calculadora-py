'''fazer uma calculadora'''
from time import sleep

simb = ("+", "-", "*", "/")
n1 = int(input("Digite um número: "))

print(n1)
for i in simb:
    print(i, end = " ")

simbolo = str(input("Selecione a operação: "))

while True:
    n2 = 0
    while True:
        n2 = int(input("Digite um número: "))
        if simbolo == "+":
            n1 += n2
            print(n1) 
            break
        elif simbolo == "-":
            n1 -= n2
            print(n1)
            break
        elif simbolo == "*":
            n1 *= n2
            print(n1)
            break
        elif simbolo == "/":
            n1 /= n2 
            print(n1)
            break
    
    resp = str(input("Quer continuar? ")).strip().upper()[0]
    simbolo = str(input("Selecione a operação: "))
    while resp not in "SN":
        print("Error! Responda com S ou N")
        break
    if resp == "N":
        print("Finalizando...")
        sleep(1)
        break
