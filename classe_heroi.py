class Heroi():
    def __init__ (self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "arqueiro":
            ataque = "arco e flecha"
        elif self.tipo == "ladrao":
            ataque = "facas"
        elif self.tipo == "paladino":
            ataque = "maça"
        else:
            return "Tipo de herói inválido"
        print(f"O {self.tipo} atacou com {ataque}")
    
heroi1 = Heroi("Gandalf", 2000, "mago")
heroi2 = Heroi("Aragorn", 87, "guerreiro")
heroi3 = Heroi("Legolas", 1000, "arqueiro")
heroi4 = Heroi("Frodo", 50, "ladrao")
heroi5 = Heroi("Gimli", 139, "paladino")

heroi1.atacar()
heroi2.atacar()
heroi3.atacar()
heroi4.atacar()
heroi5.atacar()
