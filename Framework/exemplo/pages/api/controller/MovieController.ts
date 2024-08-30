import { createMovieModel , findMovieModelByName, selectMoviesModel } from "../model/movie";

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

export async function selectMovies() {
    try {
        const movies = await selectMoviesModel();

        return { status: 200 , message: 'Select movies', data: movies }
    }
    catch (err) {
        return { status: 500 , message: 'Something went wrong' };
    }
}


export async function findMovieByName(_name:string) {
    try {
        const movieByName = await findMovieModelByName(_name);

        if ( movieByName == undefined ) {
            return { status: 404, message: 'Movie not found' };
        }
        else {
            return { status: 200, message: 'Movie found', data: movieByName };
        }
        
    }
    catch (err) {
        return { status: 500 , message: 'Something went wrong' };
    }
}