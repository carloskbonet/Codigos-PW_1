import { createMovieModel , findMovieModelByName } from "../model/movie";

export async function createMovieC(_name:string , _releaseDate:string , _imgURL = "" , _videoURL = "",  _description = "") {
    try {
        // Verificar atributos ÚNICOS

        const movieByName = await findMovieModelByName(_name);

        if ( movieByName != undefined ) {
            return { status: 403 , message: 'Name already registered' };
        }

        const response = await createMovieModel(_name , _releaseDate , _imgURL , _videoURL, _description);

        return { status: 201 , message: 'Movie created' , data: response };

    }
    catch (err) {
        return { status: 500 , message: 'Something went wrong' };
    }
}

