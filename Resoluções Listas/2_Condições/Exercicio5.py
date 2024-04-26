name = str("");
gender = str("");
c_state = str("");
m_time = int(0);
inputMenu = int(0);

print(f'Iremos apresentar um formulário ao usuário. Favor preencher corretamente.');

name = input('Nome: ');

print('\nDigite 1 para F (Feminino)');
print('Digite 2 para M (Masculino)');
inputMenu = int(input('Digite: '));

if (inputMenu == 1):
    gender = 'F';
if (inputMenu == 2):
    gender = 'M';

if (gender == 'F'):
    print('\nDigite 1 para Casada');
    print('Digite 2 para Solteira');

    inputMenu = int(input('Digite: '));

    if (inputMenu == 1):
        c_state = 'Casada';
    if (inputMenu == 2):
        c_state = 'Solteira';
if (gender == 'M'):
    print('\nDigite 1 para Casado');
    print('Digite 2 para Solteiro');

    inputMenu = int(input('Digite: '));

    if (inputMenu == 1):
        c_state = 'Casado';
    if (inputMenu == 2):
        c_state = 'Solteiro';

print(f'\nDados Cadastrados:');
print(f'Nome: {name} / Sexo: {gender} / Estado Civil: {c_state}');

if (c_state == 'Casado' or c_state == 'Casada'):
    m_time = input(f'Digite a quantos anos você está {c_state}: ');