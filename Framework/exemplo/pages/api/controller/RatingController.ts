import { findMovieModelByName } from "../model/movie";
import { createRatingModel , findRatingUser , updateRating } from "../model/rating";
import { findUserModelByUsername } from "../model/user";

export async function createRating(_value:number , _username:string , _movieName:string , _comment = "") {
    try {
        const userByUsername = await findUserModelByUsername(_username);

        if ( userByUsername == undefined ) {
            return { status: 404, message: 'User not found' };
        }

        const movieByName = await findMovieModelByName(_movieName);

        if ( movieByName == undefined ) {
            return { status: 404, message: 'Movie not found' };
        }
        
        // Verificar se o usuário já possui uma avaliação nesse filme
        const ratingByUser = await findRatingUser(userByUsername.id , movieByName.id);

        if ( ratingByUser != undefined ) {
            const updating = await updateRating(ratingByUser.id , _value , _comment);


            return { status: 200, message: 'Rating updated' , data:updating };
        }

        // Após as verificações, criar a avaliação
        const response = await createRatingModel(_value , _comment , userByUsername.id , movieByName.id);

        return { status: 200, message: 'Rating created', data: response };
    
    }
    catch (err) {
        return { status: 500 , message: 'Something went wrong' };
    }
}