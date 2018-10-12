disciplinas = [
    [{"nome":"LTPI"},{"Joao": 2.5, "Maria": 8.9, "José": 6.7}],
    [{"nome": "Copiladores"},{"Joao": 6.2, "Maria": 10, "José": 2.1, "Mario:": 6.9}],
    [{"nome": "Tópicos Especiais"},{"Maria": 9.2, "José": 9.1, "Mario": 5.5, "Joao": 5}],
]
def notas (alunos):
    for i in range(0,3):
        try:
            print(disciplinas[i][0]["nome"])
            if (disciplinas[i][1][alunos] >= 10):
                print ("SS")
            elif (disciplinas[i][1][alunos] >= 6):
                print("MS")
            elif (disciplinas[i][1][alunos] >= 4):
                print("MM")
            elif (disciplinas[i][1][alunos] >= 2):
                print("MI")
            elif (disciplinas[i][1][alunos] >= 2):
                print("II")
        except:
            print("SR")
notas(str(input("De qual aluno você deseja obter informações?\n")))

def decaimento(x, meiaVida, atual):
    x = x / 2
    atual += meiaVida
    print(x)
    print(atual)
    if x < 0.1:
        quit()
    else:
        decaimento(x, meiaVida, atual)

decaimento(9000, 12, 2018)
