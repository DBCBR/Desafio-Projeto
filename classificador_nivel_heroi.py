# Variável para armazenar o nível do herói
nome = str(input("Digite o nome do herói: "))

# Variável para armazenar a quantidade de xp do herói
xp = int(input("Digite a quantidade de xp do herói: "))

# Inicializa o nível como "imortal" por padrão
nivel = "imortal"

# Lista de limites de xp para cada nível
limites = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]

# Lista de níveis correspondentes de acordo com os limites de xp
niveis = ["ferro", "bronze", "prata", "ouro", "platina", "diamante", "mestre", "grandmaster", "challenger", "imortal"]

# Lógica para determinar o nível do herói com base na quantidade de xp
for i in range(len(limites)):
    if xp < limites[i]:
        nivel = niveis[i]
        break

# Saída do resultado   
print(f"O herói {nome} é do nível {nivel} com {xp} xp.")