class Disciplina:
    def __init__(self, nome , professor):
        self.nome = nome
        self.professor = professor

        #Temporário
        python = Disciplina("python", "Russi")
        print(python.professor)