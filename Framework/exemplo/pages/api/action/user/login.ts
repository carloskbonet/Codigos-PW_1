import { NextApiRequest , NextApiResponse } from "next";
import { login } from "../../controller/UserController";

export default async ( req: NextApiRequest , res: NextApiResponse ) => {
    if ( req.method != 'GET' ) {
        return res.status(403).json( { message: 'Method not allowed' } );
    }

    const { username , password } = req.body;

    // Verificar todos os dados do request.

    
    //Chamar controller
    const response = await login(username , password);

    return res.status( response.status ).json( response.message );

}