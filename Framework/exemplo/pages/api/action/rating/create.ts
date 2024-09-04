import { NextApiRequest , NextApiResponse } from "next";
import { createRating } from "../../controller/RatingController";

export default async ( req: NextApiRequest , res: NextApiResponse ) => {
    if ( req.method != 'POST' ) {
        return res.status(403).json( { message: 'Method not allowed' } );
    }

    const { value , comment, username , movieName } = req.body;

    // Verificar todos os dados do request.
    
    // Criar a avaliação - Chamar controller
    const response = await createRating(value , username , movieName , comment);

    return res.status( response.status ).json( { message: response.message} );
}