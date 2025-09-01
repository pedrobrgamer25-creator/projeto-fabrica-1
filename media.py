nome = (input("Insira o nome do aluno: "))
nota1 = float(input("Insira a nota do aluno: "))
nota2 = float(input("Insira a nota do aluno: "))
nota3 = float(input("Insira a nota do aluno: "))
nota4 = float(input("Insira a nota do aluno: "))

media = ( nota1 + nota2 + nota3 + nota4 ) / 4

if media > 7.0:
    print ("Aprovado(a)", media)
if media > 5.0 and media < 7.0:
    print ("Recuperação", media)
if media < 5.0:
    print ("Reprovado", media)