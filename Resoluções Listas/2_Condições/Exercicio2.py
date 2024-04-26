a = int(0);
b = int(0);
c = int(0);

print('O algoritmo solicitará 3 números inteiros. Ao final, exibirá todos eles em ordem decrescente.');

a = int(input('Digite: '));
b = int(input('Digite: '));
c = int(input('Digite: '));


print();

if ( a > b and a > c  ):
    print(a);
    if ( b > c ):
        print(b);
        print(c);
    else:
        print(c);
        print(b);

if ( b > a and b > c ):
    print(b);
    if (a > c):
        print(a);
        print(c);
    else:
        print(c);
        print(a);
    
if ( c > a and c > b ):
    print(c);
    if (a > b):
        print(a);
        print(b);
    else:
        print(b);
        print(a);