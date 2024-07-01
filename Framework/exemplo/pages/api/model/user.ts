import { prisma } from "@/db";

// Create
export async function createUserModel(_name:string , _username:string, _password: string, _cpf:string) {

    const user = await prisma.user.create({
        data: {
            name: _name,
            username: _username,
            password: _password,
            cpf: _cpf
        }
    });


    return user;
}


export async function findUserModelByCPF (_cpf : string) {

    const user = await prisma.user.findUnique({
        where: {
            cpf : _cpf
        }
    });

    return user;
}

export async function findUserModelByUsername (_username : string) {

    const user = await prisma.user.findUnique({
        where: {
            username : _username
        }
    });

    return user;
}