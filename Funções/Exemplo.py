# Variáveis
number_1 = int(0);
number_2 = int(0);
number_3 = int(0);

# Funções
def media( n1:int , n2:int , n3:int ):
    result = float(0);

    result = ( n1 + n2 + n3 ) / 3;

    print(f'Média: {result}');

# Explicação
print("O algoritmo fará o cálculo da média de 3 números.");

# Inputs
number_1 = int(input("Digite: "));
number_2 = int(input("Digite: "));
number_3 = int(input("Digite: "));

# Processamento 

print("\nFunção em execução...\n");

media(8,16,10);
#media(number_1 , number_2 , number_3);

#media( 3, 6, 9 );
#media(10, 19, 24);
#media(1, 14, 7);