import { createUserModel , findUserModelByCPF, findUserModelByUsername } from "../model/user";

export async function createUser(_username:string , _password:string , _confirmPassword:string , _cpf:string , _name = "") {
    // Realizar verificações em atributos Únicos das tabelas.
    // Verificar se os valores já estão cadastrados no banco de dados
    try {
        if( _password != _confirmPassword ) {
            return { message: 'Passwords dont match' };
        }

        //Verificar username e cpf
        const userByCPF = await findUserModelByCPF(_cpf);

        if ( userByCPF != undefined ) {
            return { message: "CPF already registered" };
        }

        const userByUsername = await findUserModelByUsername(_username);

        if ( userByUsername != undefined ) {
            return { message: 'Username already registered' };
        }

        const response = await createUserModel( _name , _username , _password , _cpf );

        return response;

    }
    catch(err) {
        return { message: 'Something went wrong' };
    }
}