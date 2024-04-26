nome = str('');
sobrenome = str('');
nome_completo = str('');

print("\nO algoritmo concatenará o nome do usuário.");

sobrenome = input("Digite o seu sobrenome: ");
nome = input("Digite o seu nome: ");

nome_completo = nome + " " + sobrenome;

print(f'\nOlá {nome_completo}, seja bem vindo!!\n');
