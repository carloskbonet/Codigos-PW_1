fahrenheit = float(0);
celsius = float(0);

print('O algoritmo converterá a temperatura digitava em °F para °C');

fahrenheit = float(input('Digite: '));

# Processamento

celsius = ( fahrenheit - 32 ) / 1.8;

# Output

print(f'\nTemperatura em °C : {celsius}°')
