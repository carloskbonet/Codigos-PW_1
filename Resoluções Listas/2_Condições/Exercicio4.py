birthYear = int(0);
yearsOld = int(0);
current_year = int(0);
next_el_year = int(0);
year_verification = int(0);

print('O algoritmo irá verificar se o usuário poderá votar na próxima eleição.');

birthYear = int(input('Digite seu ano de nascimento: '));
current_year = int(input('Digite o ano atual: '));

# Processamento
yearsOld = current_year - birthYear;

print(f'\nNo ano {current_year} o usuário tem {yearsOld} anos');

year_verification = current_year % 5;

if ( year_verification == 0 ):
    print(f'O ano de {current_year} É um ano de eleição.');

    if ( yearsOld < 16 ):
        print('NÃO pode votar.');
    else:
        print('PODE votar.');

else:
    print(f'O ano de {current_year} NÃO É um ano de eleição.');

    next_el_year = current_year - year_verification;

    print(f'A última eleição foi no ano de {next_el_year}');

    next_el_year = next_el_year + 5;

    print(f'A próxima eleição será no ano de {next_el_year}');

    yearsOld = next_el_year - birthYear;

    print(f'Em {next_el_year} o usuário terá {yearsOld} anos');

    if ( yearsOld < 16 ):
        print('NÃO poderá votar.');
    else:
        print('PODE votar na próxima eleição.');
