# Classificador de Nível de Herói

## Descrição

Este projeto consiste em dois programas simples em Python que classificam o nível de um herói com base na quantidade de experiência (XP) ou no saldo de partidas ranqueadas (vitórias - derrotas). O objetivo é praticar conceitos básicos de programação, utilizando apenas variáveis, operadores, laços de repetição, estruturas de decisão e funções, conforme as restrições do desafio proposto pela DIO.

## Funcionalidades

- Solicita ao usuário o nome do herói.
- Solicita ao usuário a quantidade de XP **ou** a quantidade de vitórias e derrotas do herói.
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

## Lógica Utilizada

- Para classificação por XP, o programa utiliza uma lista de limites de XP e uma lista correspondente de níveis. Um laço de repetição percorre os limites e, ao encontrar o intervalo correto, define o nível do herói. Caso o XP seja maior que todos os limites, o nível padrão é "imortal".
- Para classificação por saldo de partidas, o programa calcula o saldo (vitórias - derrotas) e utiliza a mesma lógica de limites para definir o nível.

## Exemplo de Uso

### Classificação por XP

```
Digite o nome do herói: David
Digite a quantidade de xp do herói: 3500
O herói David é do nível ouro com 3500 xp.
```

### Classificação por Saldo de Partidas

```
Digite o nome do herói: Ana
Digite a quantidade de vitórias do herói: 25
Digite a quantidade de derrotas do herói: 5
O herói Ana tem saldo de 20 e está no nível bronze.
```

## Código Principal - Classificação por XP

```python
nome = input("Digite o nome do herói: ")
xp = int(input("Digite a quantidade de xp do herói: "))

limites = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
niveis = ["ferro", "bronze", "prata", "ouro", "platina", "diamante", "mestre", "grandmaster", "challenger", "imortal"]

nivel = niveis[-1]  # valor padrão: "imortal"

for i in range(len(limites)):
    if xp < limites[i]:
        nivel = niveis[i]
        break

print(f"O herói {nome} é do nível {nivel} com {xp} xp.")
```

## Código Principal - Classificação por Saldo de Partidas

```python
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