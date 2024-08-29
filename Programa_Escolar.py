import time

Nota_1 = float(input('Digite a primeira Nota do Aluno: '))
Nota_2 = float(input('Digite a segunda Nota do Aluno: '))

def Media (Nota_1, Nota_2):
    return (Nota_1 + Nota_2) / 2

media = Media(Nota_1, Nota_2)

print('---------------------------------------')
time.sleep(1)

if  media == 10:
    print("O aluno está aprovado com distinção!!")
elif media >= 7:
    print("O aluno está aprovado!")
else: 
    print('O aluno está reprovado...')
