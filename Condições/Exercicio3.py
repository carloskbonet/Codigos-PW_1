nota_1 = int(0);
nota_2 = int(0);
nota_3 = int(0);
nota_4 = int(0);
nota_final = float(0);

print("O algoritmo verificará se o aluno está APROVADO ou REPROVADO.\n");

nota_1 = float(input("1° Bimestre: "));
nota_2 = float(input("2° Bimestre: "));
nota_3 = float(input("3° Bimestre: "));
nota_4 = float(input("4° Bimestre: "));

# Processamento

nota_final = (nota_1 + nota_2 + nota_3 + nota_4) / 4;

print(f'\nNota Final: {nota_final}\n');

if ( nota_final >= 7 ):
    print("\nO aluno está APROVADO.\n");
else:
    print("\nO aluno está REPROVADO.\n");
