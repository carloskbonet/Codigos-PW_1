
nota_1 = float(0);
nota_2 = float(0);
nota_3 = float(0);
resultado = float(0);

print("O algoritmo calculará a média dos 3 números digitados.\n");

nota_1 = float(input("Digite a primeira Nota: "));
nota_2 = float(input("Digite a segunda Nota: "));
nota_3 = float(input("Digite a terceira Nota: "));

resultado = (nota_1 + nota_2 + nota_3) / 3;

print(f"\nA média dos números digitados é: {resultado}\n");