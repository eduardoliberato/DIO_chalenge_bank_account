# operations you need to implement: deposit, withdrawal, statement

saldo = 1500.0  #  Using float to allow decimal values
numero_saque = 0
limite = 0

while True:
    objeto = int(input(
        """
----    Bem vindo ao banco do futuro!!! ----
        
        Escolha a operação: 
        (1) Saque
        (2) Depósito
        (3) Extrato
        (4) Finalizar
    
    """
    ))

    if objeto == 1:
        valor = float(input("Digite o valor do saque: "))
        if valor > 500:
            print("O limite máximo por saque é de R$500,00")
        elif valor > saldo:
            print("Saldo indisponível")
        elif valor < 500:            
            saldo -= valor
            numero_saque += 1
            print(f"Saque de {valor:.2f} realizado. \nSaldo disponível após o saque: {saldo:.2f}")
            if numero_saque > 2:
                print("Limite de 3 saques diarios já atingido")
                break

    elif objeto == 2:
        valor = float(input("Digite o valor do depósito: "))
        saldo += valor
        print(f"Novo saldo após o depósito: {saldo:.2f}")

    elif objeto == 3:
        print(f"Saldo atual: R${saldo:.2f}")

    elif objeto == 4:
        print("Finalizado o atendimento")
        break  # Encerra o loop

    else:
        print("Opção indisponível")
