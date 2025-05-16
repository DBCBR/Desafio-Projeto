# Classificador de Nível de Herói

## Descrição

Este projeto consiste em um programa simples em Python que classifica o nível de um herói com base na quantidade de experiência (XP) informada pelo usuário. O objetivo é praticar conceitos básicos de programação, utilizando apenas variáveis, operadores, laços de repetição e estruturas de decisão, conforme as restrições do desafio proposto pela DIO.

## Funcionalidades

- Solicita ao usuário o nome do herói.
- Solicita ao usuário a quantidade de XP do herói.
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

O programa utiliza uma lista de limites de XP e uma lista correspondente de níveis. Um laço de repetição percorre os limites e, ao encontrar o intervalo correto, define o nível do herói. Caso o XP seja maior que todos os limites, o nível padrão é "imortal".

## Exemplo de Uso

```
Digite o nome do herói: David
Digite a quantidade de xp do herói: 3500
O herói David é do nível ouro com 3500 xp.
```

## Código Principal

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

## Regras do Desafio

- O programa deve solicitar o nome e a quantidade de XP do herói ao usuário.
- A classificação deve ser feita conforme os intervalos de XP definidos.
- Exibir o resultado da classificação na tela de forma clara.
- Manter o código simples e de fácil compreensão.

## Autor

Projeto desenvolvido por David Barcellos Cardoso para o desafio da DIO.