anos = int(0);
resultado = int(0);
DIAS_NO_ANO = int(365);

print ("O algoritmo converterá o valor digitado em anos para dias.\n");

anos = int(input("Digite quantos anos você tem: "));

resultado = anos * DIAS_NO_ANO;

print(f'\nO usuário tem {anos} anos // Convertendo para {resultado} dias');