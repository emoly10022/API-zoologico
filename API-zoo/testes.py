#proprio do python para rodar os testes
import unittest
from animais import Animal, Recinto, Zoologico 


class TestAnimal(unittest.TestCase):
    def test_alimentar(self):
        animal = Animal("Leão", "Felino", 40)
        animal.alimentar()
        self.assertEqual(animal.nivel_felicidade, 50)

class TestRecinto(unittest.TestCase):
    def test_adicionar_animal(self):
        recinto = Recinto("Savana")
        animal1 = Animal("Zebra", "Herbívoro")
        animal2 = Animal("Leão", "Felino")
        recinto.adicionar_animal(animal1)
        self.assertIn(animal1, recinto.animais)
        recinto.adicionar_animal(animal2)
        self.assertNotIn(animal2, recinto.animais) 

    def test_cuidar_recinto(self):
        recinto = Recinto("Floresta")
        animal1 = Animal("Tigre", "Felino", 60)
        animal2 = Animal("Leopardo", "Felino", 70)
        recinto.adicionar_animal(animal1)
        recinto.adicionar_animal(animal2)
        recinto.cuidar_recinto()
        self.assertEqual(animal1.nivel_felicidade, 70)
        self.assertEqual(animal2.nivel_felicidade, 80)

class TestZoologico(unittest.TestCase):
    def test_criar_animal(self):
        zoo = Zoologico()
        animal = zoo.criar_animal("Elefante", "Herbívoro")
        self.assertEqual(animal.nome, "Elefante")
        self.assertEqual(animal.especie, "Herbívoro")

    def test_criar_recinto(self):
        zoo = Zoologico()
        recinto = zoo.criar_recinto("Savana")
        self.assertEqual(recinto.nome, "Savana")

    def test_atrair_visitantes(self):
        zoo = Zoologico()
        recinto1 = Recinto("Floresta")
        recinto2 = Recinto("Savana")
        animal1 = Animal("Zebra", "Herbívoro", 40)
        animal2 = Animal("Leão", "Felino", 60)
        recinto1.adicionar_animal(animal1)
        recinto2.adicionar_animal(animal2)
        zoo.recintos.extend([recinto1, recinto2])
        visitantes = zoo.atrair_visitantes()
        self.assertEqual(visitantes, 10)  

#importante para rodar os testes diretamente ao rodar o script 
if __name__ == '__main__':
    unittest.main()
