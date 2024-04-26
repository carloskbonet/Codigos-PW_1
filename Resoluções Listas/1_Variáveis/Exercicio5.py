yearsOld = int(0);
months = int(0);
days = int(0);
hours = int(0);

print('O algoritmo converterá a idade digitada em : Meses, Dias e Horas');

yearsOld = int(input('Qual a sua idade? '));

# Processamento

days = yearsOld * 365;
months = yearsOld * 12;
hours = days * 24;


print(f'\nValor em Anos: {yearsOld}');
print(f'Meses: {months}');
print(f'Dias: {days}');
print(f'Horas: {hours}');
