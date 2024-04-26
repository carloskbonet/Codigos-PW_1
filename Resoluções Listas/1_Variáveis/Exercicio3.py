raio = float(0);
area = float(0);
PI = float(3.14);

print('O algoritmo calculará a área do círculo a partir do raio digitado.');

raio = float(input('Digite: '));

# Processamento

area = PI * ( pow(raio , 2) );

# Output

print(f'Resultado: {area}');