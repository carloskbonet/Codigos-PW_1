gender = str("");
height = float(0);
weight = float(0);
imc = float(0);
inputMenu = int(0);

print(f'O algoritmo calculará o IMC do usuário. Favor digitar os dados solicitados.');

while (True):
    print('\nDigite 1 para F (Feminino)');
    print('Digite 2 para M (Masculino)');
    inputMenu = int(input('Digite: '));

    if (inputMenu < 1 or inputMenu > 2):
        print('Digite apenas números presentes no menu.');

    if (inputMenu == 1):
        gender = 'F';
        break;
    if (inputMenu == 2):
        gender = 'M';
        break;

weight = float(input('Peso (Utilize notação com ponto, ex: 70.5): '));
height = float(input('Altura (Ex: 1.80): '));

imc = weight / (height ** 2);

print(f'\nIMC do usuário: {round(imc, 2)}');

if ( gender == 'M' ):
    if (imc < 18.5):
        print('Abaixo do peso.');
    if (imc >= 18.5 and imc < 25):
        print('Peso Normal');
    if (imc >= 25 and imc < 30):
        print('Acima do peso');
    if (imc >= 30):
        print('Obeso');

if ( gender == 'F' ):
    if (imc < 17):
        print('Abaixo do peso.');
    if (imc >= 17 and imc < 23):
        print('Peso Normal');
    if (imc >= 23 and imc < 27):
        print('Acima do peso');
    if (imc >= 27):
        print('Obeso');
