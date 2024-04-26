# Variáveis
numero = int(0);
restoDivisao = int(0);

# Explicação
print("O algoritmo verificará se o número digitado é PAR ou IMPAR.\n");

# Inputs
numero = int(input("Digite: "));

# Processamento

restoDivisao = numero % 2;

if ( restoDivisao > 0 ):
    print("O número digitado é IMPAR.");
else:
    print("O número digitado é PAR.");