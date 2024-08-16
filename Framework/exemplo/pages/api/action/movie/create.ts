import { NextApiRequest , NextApiResponse } from "next";
import { createMovieC } from "../../controller/MovieController";

export default async ( req: NextApiRequest , res: NextApiResponse ) => {
    if ( req.method != 'POST' ) {
        return res.status(403).json( { message: 'Method not allowed' } );
    }

    const { name , releaseDate , imageURL, videoURL , description } = req.body;

    // Verificar todos os dados do request.

    
    // Criar o usuário - Chamar controller
    const response = await createMovieC(name , releaseDate , imageURL, videoURL , description);

    return res.status( response.status ).json( { message: response.message} );
}