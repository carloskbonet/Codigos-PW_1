
# Variáveis
valor_total = float(0);
desconto_porcentagem = int(0);
valor_desconto = float(0);
valor_final = float(0);

print("\nO algoritmo calculará o valor de desconto na compra.");

# Input
valor_total = float(input("Digite o valor total: "));
desconto_porcentagem = int(input("Digite a porcentagem de desconto (0 a 100): "));

# Processamento
#valor_desconto = (valor_total * desconto_porcentagem) / 100;

valor_desconto = valor_total * (desconto_porcentagem / 100);
valor_final = valor_total - valor_desconto;

print(f'O valor de desconto da compra é: {valor_desconto} R$');
print(f'O valor da compra é: {valor_final} R$');