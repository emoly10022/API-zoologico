
#testando criação de API
from flask import Flask 

app = Flask(__name__)

@app.route('/')
def zoologico():
    return "funcionou!!!!!!!!!!!!!!!!!!"


class Animal:
    def __init__(self, nome, especie, nivel_felicidade=50):
        self.nome = nome
        self.especie = especie
        self.nivel_felicidade = nivel_felicidade

    def alimentar(self):
        self.nivel_felicidade += 10

class Recinto:
    def __init__(self, nome):
        self.nome = nome
        self.animais = []

    def adicionar_animal(self, animal):
        if not self.animais or self.animais[0].especie == animal.especie:
            self.animais.append(animal)

    def cuidar_recinto(self):
        for animal in self.animais:
            animal.alimentar()

class Zoologico:
    def __init__(self):
        self.recintos = []
        self.visitantes = 0

    def criar_animal(self, nome, especie, nivel_felicidade=50):
        return Animal(nome, especie, nivel_felicidade)

    def criar_recinto(self, nome):
        recinto = Recinto(nome)
        self.recintos.append(recinto)
        return recinto

    def atrair_visitantes(self):
        felicidade_total = sum(animal.nivel_felicidade for recinto in self.recintos for animal in recinto.animais)
        visitantes = felicidade_total // 10  
        self.visitantes += visitantes
        return visitantes


if __name__ == '__main__':
    app.run(debug=True)
