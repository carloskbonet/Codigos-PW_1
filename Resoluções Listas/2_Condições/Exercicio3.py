passwordInput = str("");
PASSWORD = "very-very-long-password";

print('O algoritmo irá solicitar uma senha para liberar acesso ao sistema.');

passwordInput = input('Digite: ');

# Processamento

print();

if ( passwordInput == PASSWORD ):
    print('Logged In');
else:
    print('Not Authorized');