import { NextApiRequest , NextApiResponse } from "next";
import { createUser } from "../../controller/UserController";

export default async ( req: NextApiRequest , res: NextApiResponse ) => {
    if ( req.method != 'POST' ) {
        return res.status(403).json( { message: 'Method not allowed' } );
    }

    const { name , username , password , confirmPassword , cpf } = req.body;

    // Verificar todos os dados do request.

    
    // Criar o usuário - Chamar controller
    const response:any = await createUser(username , password , confirmPassword , cpf , name);

    return res.status( response.status ).json( { message: response.message} );
}