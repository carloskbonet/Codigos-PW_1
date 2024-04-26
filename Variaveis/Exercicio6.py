# Declaração de Variáveis
valor_principal = float(0);
taxa_juros = float(0);
meses = int(0);
valor_de_juros = float(0);
valor_final = float(0);


# Explicação do Algoritmo
print("\nO banco central está oferecendo rendimento para sua conta.\nDigite as informações abaixo.");


# Entrada de Dados
valor_principal = float(input("Digite o valor atual da sua conta: "));
taxa_juros = float(input("Digite quantos %/ sua conta vai render por mês: "));
meses = int(input("Em quantos meses deseja fazer a simulação?\nDigite: "));


# Processamento
valor_de_juros = (valor_principal * (taxa_juros / 100)) * meses;
valor_final = valor_de_juros + valor_principal;

# Saída de Dados
print(f'\nO rendimento da sua conta no período de {meses} meses foi de {valor_de_juros} R$');
print(f'O montante final da conta é de {valor_final} R$');
