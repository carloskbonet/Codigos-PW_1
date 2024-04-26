nota_1 = float(0);
nota_2 = float(0);
nota_3 = float(0);
notaFinal = float(0);

print('O algoritmo calculará a média ponderada das notas digitadas.');
print('Ao total serão 3 notas, sendo a 1° com peso 2. A 2° com peso 3. E a 3° com peso 5.');
print('Cada nota será um valor de 0 a 10');

nota_1 = float(input('Nota 1 : '));
nota_2 = float(input('Nota 2 : '));
nota_3 = float(input('Nota 3 : '));


notaFinal = ( (nota_1 * 2) + (nota_2 * 3) + (nota_3 * 5) ) / 10;

print(f'\nNota Final: {notaFinal}');

if ( notaFinal >= 7 ):
    print('APROVADO.');
else:
    print('REPROVADO.');