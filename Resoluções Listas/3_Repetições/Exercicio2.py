start = int(0);
end = int(0);
verify = float(0);

print('Digite 2 intervalos. O algoritmo mostrará os números impares dentro deles.');

start = int(input('Início: '));
end = int(input('Fim: '));

for number in range(start , end , 1):
    
    verify = number % 2;

    if ( verify != 0 ):
        print(number);