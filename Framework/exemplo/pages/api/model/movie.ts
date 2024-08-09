import { prisma } from "@/db";

export async function createMovieModel(_name:string , _releaseDate:string, _imageURL:string , _description:string) {

    const movie = await prisma.movie.create(
        {
            data: {
                name: _name ,
                releaseDate: _releaseDate ,
                imageURL: _imageURL ,
                description : _description
            }
        }
    );

    return movie;
}


export async function findMovieModelByName(_name: string) {

    const movie = await prisma.movie.findUnique(
        {
            where: {
                name: _name
            }
        }
    );

    return movie;
}