import { NextApiRequest , NextApiResponse } from "next";
import { selectMovies } from "../../controller/MovieController";

export default async ( req: NextApiRequest , res: NextApiResponse ) => {
    if ( req.method != 'GET' ) {
        return res.status(403).json( { message: 'Method not allowed' } );
    }
    
    // Criar o usuário - Chamar controller
    const response = await selectMovies();

    return res.status( response.status ).json( { message: response.message , data: response.data} );
}