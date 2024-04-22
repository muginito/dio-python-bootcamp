from functools import reduce

saldo = 0
LIMITE_SAQUES = 3
n_saques = 0
extrato = []

def saca(valor):
    global n_saques
    global extrato
    global saldo
    if n_saques == LIMITE_SAQUES:
        return "Limite diário de saque"
    elif valor > 500:
        return "Limite máximo de R$ 500,00 por saque"
    elif saldo < valor:
        return "Saldo insuficiente."
    saldo -= valor
    extrato.append(f"- R$ {valor:.2f}\n")
    n_saques += 1
    return "Saque concluído."

def deposita(valor):
    global n_saques
    global extrato
    global saldo
    if valor < 0:
        return "Valor inválido"
    saldo += valor
    extrato.append(f"+ R$ {valor:.2f}\n")
    return "Depósito concluído."

def mostra_extrato():
    global n_saques
    global extrato
    global saldo
    total_extrato = reduce(lambda x, y: x + y, extrato)
    return total_extrato + f"\nTotal: R$ {saldo:.2f}"

def menu():
    return int(input((f"\n{"MENU".center(20, "=")}\n\n1 - Depósito\n\n2 - Saque\n\n3 - Extrato\n\n0 - Sair\n\n")))


if __name__ == "__main__":
    while True:
        opt = menu()

        if opt == 0:
            print("Encerrando sistema.\n")
            break

        if opt == 1:
            valor = float(input((f"{"Depósito".center(20,"=")}\n\nInsira o valor para depósito: ")))
            print(deposita(valor))
            continue
        
        if opt == 2:
            valor = float(input(f"{"Saque".center(20,"=")}\n\nInsira o valor para saque: "))
            print(saca(valor))
            continue
        
        if opt == 3:
            print(f"{"Extrato".center(20,"=")}\n\n{mostra_extrato()}")
            continue

        else:
            print("Valor inválido. Insira um valor correto.\n")
