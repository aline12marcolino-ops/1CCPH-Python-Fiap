from aluno import Aluno
from disciplina import Disciplina

#Criar / Instanciar 1 Aluno
aluno1 = Aluno("Marcos", 454842, "Engenharia")

#Criar / Instanciar 2 disciplina
prompt_ia = Disciplina("Pompt IA", "Jorge")
sers = Disciplina("Soluções Renováveis", "André")

#Matricular o aluno nas disciplinas
aluno1.matricular(prompt_ia)
aluno1.matricular(sers)
#print(aluno1.displina[0].professor)

#Adicionas nota do aluno referentes ás disciplinas
aluno1.adicionar_nota(prompt_ia,10)
aluno1.adicionar_nota(prompt_ia,5)
aluno1.adicionar_nota(sers,7)
aluno1.adicionar_nota(sers,3)
#print(aluno1.notas_por_disciplina)

print(aluno1.calcular_nota(prompt_ia))
print(aluno1.calcular_media_geral())