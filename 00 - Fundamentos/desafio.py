Menu = """
 ----Bem vindo ao banco Python----
 ----Nesse banco você pode mais-----

[d] - depositar
[s] - sacar
[e] - extrato
[q] - sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(Menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0 :
           saldo += valor
           extrato += f"Depósito: R$ {valor:.2f}"
          

        else:
           print("Operação falhou! O valor informado é inválido.")

if opcao == "s":
        if numero_saques >= LIMITE_SAQUES:  # Check for exceeded withdrawals first
            print("Operação não deu certo, você atingiu o limite de saques.") 
        else:
            valor = float(input("Informe o valor do saque: "))
            exedeu_saldo = valor > saldo
            exedeu_limite = valor > limite

        if exedeu_saldo:
           print("Operação falhou! Você não tem saldo suficiente.")

        elif exedeu_limite:
           print("Operação não deu certo, o valor do saque excede o limite.")

        elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"  
                numero_saques += 1

        else:
                print("Operação falhou! O valor informado é inválido.")

    
    if opcao == "e":
       print("\=========== Extrato ============")
       print("Não foram realizadas movimentações." if not extrato else extrato)
       print(f"\nSaldo: R$ {saldo:.2f}")
       print("==================================")

    if opcao == "q":
       break

    else:
       print("Operação inválida, por favor selecione novamente a operação desejada.")

