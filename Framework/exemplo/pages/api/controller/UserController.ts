import { createUserModel , findUserModelByCPF, findUserModelByUsername, findUserModelLogin } from "../model/user";
import { generateToken } from '@/services/tokenConfig';

export async function createUser(_username:string , _password:string , _confirmPassword:string , _cpf:string , _name = "") {
    // Realizar verificações em atributos Únicos das tabelas.
    // Verificar se os valores já estão cadastrados no banco de dados
    try {
        if( _password != _confirmPassword ) {
            return { status: 400 , message: 'Passwords dont match' };
        }

        //Verificar username e cpf
        const userByCPF = await findUserModelByCPF(_cpf);

        if ( userByCPF != undefined ) {
            return { status: 403 , message: "CPF already registered" };
        }

        const userByUsername = await findUserModelByUsername(_username);

        if ( userByUsername != undefined ) {
            return { status: 403 , message: 'Username already registered' };
        }

        const response = await createUserModel( _name , _username , _password , _cpf );

        return { status: 201 , message: 'User registered' , data: response };

    }
    catch(err) {
        return { status: 500 , message: 'Something went wrong' };
    }
}



export async function login(_username: string , _password: string) {
    try {

        const userLogin = await findUserModelLogin(_username , _password);

        if ( userLogin == undefined ) {
            return { status: 404, message: 'Incorrect username or password' }
        }
        else {
            const _token = generateToken(_username); 

            return { status: 200, message: 'Logged In', token: _token };
        }

    }
    catch(err) {
        return { status: 500 , message: 'Something went wrong' };
    }
}