yearsOld = [12 , 19 , 23 , 17 , 19 , 29 , 41 , 36 , 19 , 23];
positions = [];
inputNumber = int(0);
count = int(0);

print('Digite uma idade para descobrir quantas vezes a mesma se repete no vetor.');

inputNumber = int(input('Digite: '));

# Processamento

for i in range(0 , len(yearsOld)):
    # Contagem da idade
    if ( yearsOld[i] == inputNumber ):
        count = count + 1;
        positions.append(i);


# Output

print(f'\nA idade {inputNumber} apareceu {count} vezes no vetor.');
print(f'Vetor: {yearsOld}');
print(f'Valor encontrado nas posições: {positions}');