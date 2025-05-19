def calcular_saldo(vitorias, derrotas):
    return vitorias - derrotas

def classificar_nivel(saldo):
    limites = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    niveis = ["ferro", "bronze", "prata", "ouro", "platina", "diamante", "mestre", "grandmaster", "challenger", "imortal"]
    nivel = niveis[-1]  # valor padrão: "imortal"
    for i in range(len(limites)):
        if saldo < limites[i]:
            nivel = niveis[i]
            break
    return nivel

def main():
    nome = input("Digite o nome do herói: ")
    vitorias = int(input("Digite a quantidade de vitórias do herói: "))
    derrotas = int(input("Digite a quantidade de derrotas do herói: "))
    saldo = calcular_saldo(vitorias, derrotas)
    nivel = classificar_nivel(saldo)
    print(f"O herói {nome} tem saldo de {saldo} e está no nível {nivel}.")

if __name__ == "__main__":
    main()
