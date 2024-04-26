
# Declaração de Variáveis.
altura = float(0);
largura = float(0);
resultado = float(0);

# Explicação do algoritmo.
print("\nO algoritmo calculará a área do retângulo \na partir dos dados informados.");

# Input ( Entrada de Dados )
altura = float(input("Altura: "));
largura = float(input("Largura: "));

# Processamento ( Instruções Lógicas )

if ( altura == largura ) :
    # Reposta SIM
    print("\nOs dados inseridos não remetem a um retângulo. A figura formada é um quadrado, portanto a área não será calculada.");
    exit();
else :
    # Resposta NÃO
    resultado = altura * largura;

# Output ( Saída de Dados )
print(f"\nA área do retângulo é : {resultado}\n");
