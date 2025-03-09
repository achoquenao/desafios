import random
aluno0=(input("Digite o nome do aluno 0:	 "))
aluno1=(input("Digite o nome do aluno 1:	 "))
aluno2=(input("Digite o nome do aluno 2:	 "))
aluno3=(input("Digite o nome do aluno 3:	 "))
lista=[aluno0,aluno1,aluno2,aluno3]
random.shuffle(lista)
print(lista)


