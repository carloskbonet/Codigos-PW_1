
numeros = [11 , 5 , 3 , 5 , 9 , 10];

print(f'Vetor inicial: {numeros}');

numeros.append(81);
numeros.append(35);

print(f'Vetor com append: {numeros}');

numeros.pop();
numeros.remove(5)

print(f'Vetor atualizado: {numeros}');

print(f'Menor valor do vetor: { min(numeros) }');
print(f'Maior valor do vetor: { max(numeros) }');

print(f'Vetor não ordenado: {numeros}');
numeros.sort();
print(f'Vetor ordenado: {numeros}');