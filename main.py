def classificar_nivel(valor, limites, niveis):
    """
    Classifica o nível do herói com base no valor informado (XP ou saldo).
    """
    nivel = niveis[-1]  # valor padrão: "imortal"
    for i in range(len(limites)):
        if valor < limites[i]:
            nivel = niveis[i]
            break
    return nivel

class Heroi:
    """
    Classe que representa um herói com nome, idade e tipo.
    """
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        """
        Exibe o ataque do herói de acordo com seu tipo.
        """
        ataques = {
            "mago": "magia",
            "guerreiro": "espada",
            "arqueiro": "arco e flecha",
            "ladrao": "facas",
            "paladino": "maça"
        }
        ataque = ataques.get(self.tipo)
        if ataque:
            print(f"O {self.tipo} atacou com {ataque}")
        else:
            print("Tipo de herói inválido.")

def menu():
    print("\nEscolha uma opção:")
    print("1 - Classificar herói por XP")
    print("2 - Classificar herói por saldo de partidas")
    print("3 - Criar herói e simular ataque")
    return input("Opção: ")

def ler_inteiro(mensagem):
    """
    Lê um valor inteiro do usuário, com validação.
    """
    while True:
        valor = input(mensagem)
        if valor.isdigit():
            return int(valor)
        print("Por favor, digite um número inteiro válido.")

def main():
    tipos_validos = ["mago", "guerreiro", "arqueiro", "ladrao", "paladino"]
    limites_xp = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
    niveis = ["ferro", "bronze", "prata", "ouro", "platina", "diamante", "mestre", "grandmaster", "challenger", "imortal"]
    limites_saldo = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    while True:
        escolha = menu()
        if escolha == "1":
            nome = input("Digite o nome do herói: ")
            xp = ler_inteiro("Digite a quantidade de xp do herói: ")
            nivel = classificar_nivel(xp, limites_xp, niveis)
            print(f"O herói {nome} é do nível {nivel} com {xp} xp.")
        elif escolha == "2":
            nome = input("Digite o nome do herói: ")
            vitorias = ler_inteiro("Digite a quantidade de vitórias do herói: ")
            derrotas = ler_inteiro("Digite a quantidade de derrotas do herói: ")
            saldo = vitorias - derrotas
            nivel = classificar_nivel(saldo, limites_saldo, niveis)
            print(f"O herói {nome} tem saldo de {saldo} e está no nível {nivel}.")
        elif escolha == "3":
            nome = input("Digite o nome do herói: ")
            idade = ler_inteiro("Digite a idade do herói: ")
            tipo = input(f"Digite o tipo do herói {tipos_validos}: ").lower()
            if tipo not in tipos_validos:
                print("Tipo de herói inválido. Tente novamente.")
                continue
            heroi = Heroi(nome, idade, tipo)
            heroi.atacar()
        else:
            print("Opção inválida.")

        continuar = input("Deseja realizar outra operação? (s/n): ").lower()
        if continuar != "s":
            print("Programa encerrado.")
            break

if __name__ == "__main__":
    main()