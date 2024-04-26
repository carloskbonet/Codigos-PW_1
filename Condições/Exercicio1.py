x = int(0);

print("O algoritmo verificará se o número digitado é positivo, negativo ou zero.\n");

x = int(input("Digite um número: "));

# Processamento

if ( x == 0 ):
    print("O número digitado é ZERO.");
    exit();

if ( x > 0 ):
    print("O número digitado é POSITIVO.");
    exit();
else:
    print("O número digitado é NEGATIVO.");
    exit();
