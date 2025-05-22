# Classificador de Nível de Herói

## Descrição

Este projeto consiste em um programa interativo em Python que permite:
- Classificar o nível de um herói com base na quantidade de experiência (XP) **ou** no saldo de partidas ranqueadas (vitórias - derrotas).
- Criar diferentes tipos de heróis e simular ataques de acordo com o tipo escolhido.

O objetivo é praticar conceitos básicos de programação, utilizando apenas variáveis, operadores, laços de repetição, estruturas de decisão e funções, conforme as restrições do desafio proposto pela DIO.

## Funcionalidades

- Menu interativo para o usuário escolher a ação desejada.
- Solicita ao usuário o nome do herói.
- Solicita ao usuário a quantidade de XP **ou** a quantidade de vitórias e derrotas do herói.
- Validação de entradas numéricas (XP, vitórias, derrotas, idade).
- Validação do tipo de herói, aceitando apenas: mago, guerreiro, arqueiro, ladrao, paladino.
- Classifica o herói em um dos seguintes níveis:
  - Ferro
  - Bronze
  - Prata
  - Ouro
  - Platina
  - Diamante
  - Mestre
  - Grandmaster
  - Challenger
  - Imortal
- Exibe o resultado da classificação na tela.
- Permite criar heróis com nome, idade e tipo.
- Permite simular ataques de acordo com o tipo do herói.
- Permite realizar várias operações até o usuário decidir encerrar.

## Lógica Utilizada

- Para classificação por XP, o programa utiliza uma lista de limites de XP e uma lista correspondente de níveis. Um laço de repetição percorre os limites e, ao encontrar o intervalo correto, define o nível do herói. Caso o XP seja maior que todos os limites, o nível padrão é "imortal".
- Para classificação por saldo de partidas, o programa calcula o saldo (vitórias - derrotas) e utiliza a mesma lógica de limites para definir o nível.
- Para a classe de herói, o tipo define o ataque realizado, utilizando um dicionário para determinar a arma ou magia usada.
- Todas as entradas numéricas são validadas para garantir que o usuário digite apenas números inteiros.
- O tipo do herói é validado para evitar erros de digitação.

## Exemplo de Uso

### Menu Interativo

```
Escolha uma opção:
1 - Classificar herói por XP
2 - Classificar herói por saldo de partidas
3 - Criar herói e simular ataque
Opção: 1
Digite o nome do herói: David
Digite a quantidade de xp do herói: 3500
O herói David é do nível ouro com 3500 xp.
```

```
Escolha uma opção:
1 - Classificar herói por XP
2 - Classificar herói por saldo de partidas
3 - Criar herói e simular ataque
Opção: 2
Digite o nome do herói: Ana
Digite a quantidade de vitórias do herói: 25
Digite a quantidade de derrotas do herói: 5
O herói Ana tem saldo de 20 e está no nível bronze.
```

```
Escolha uma opção:
1 - Classificar herói por XP
2 - Classificar herói por saldo de partidas
3 - Criar herói e simular ataque
Opção: 3
Digite o nome do herói: Gandalf
Digite a idade do herói: 2000
Digite o tipo do herói ['mago', 'guerreiro', 'arqueiro', 'ladrao', 'paladino']: mago
O mago atacou com magia
```

## Código Principal

```python
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
```

## Regras do Desafio

- Utilizar apenas variáveis, operadores, laços de repetição, estruturas de decisão e funções.
- Não utilizar bibliotecas externas ou recursos além dos permitidos.
- O programa deve solicitar os dados ao usuário.
- A classificação deve ser feita conforme os intervalos definidos.
- Exibir o resultado da classificação na tela de forma clara.
- Manter o código simples e de fácil compreensão.

## Autor

Projeto desenvolvido por David Barcellos Cardoso para o desafio da DIO.