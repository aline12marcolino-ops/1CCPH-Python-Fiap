class Disciplina:
    def __init__(self, nome , professor):
        self.nome = nome
        self.professor = professor
    def exibir_disciplina(self):
        print(f"Disciplina: {self.nome} | Professor: {self.professor}")

    #Temporário
#python = Disciplina("python", "Russi")
#python.exibir_infos()
#print(python.professor)