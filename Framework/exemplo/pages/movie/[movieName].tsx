import styles from '@/styles/movie.module.css'
import { getCookie } from 'cookies-next';
import { checkToken } from '@/services/tokenConfig';
import { useState, useEffect } from 'react';

export default function movie({ movieName }: any) {
    const [data, setData]: any = useState();
    // Formulário de avaliação
    const [formRating, setFormRating] = useState(
        {
            value: 0,
            comment: ''
        }
    );

    // Vincular o formulário com os inputs
    function handleFormEdit(event: any, field: string) {
        setFormRating({
            ...formRating,
            [field]: event.target.value
        });
    }

    // Criar a avaliação
    async function formSubmit(event: any) {
        event.preventDefault();

        try {
            const cookieAuth = getCookie('authorization');
            const tokenInfos = checkToken(cookieAuth);

            const response = await fetch(`/api/action/rating/create`, {
                method: 'POST',
                headers: { 'Content-type': 'application/json' },
                body: JSON.stringify(
                    {
                        value: Number(formRating.value),
                        comment: formRating.comment,
                        movieName: movieName,
                        username: tokenInfos.username
                    }
                )
            });

            const responseJson = await response.json();

            alert(responseJson.message);
        }
        catch (err) {
            console.log(err);
            alert(err);
        }
    }



    async function fetchData() {
        try {
            const response = await fetch(`/api/action/movie/find?name=` + movieName, {
                method: 'GET'
            })

            const responseJson = await response.json();

            setData(responseJson.data);

        }
        catch (err) {
            console.log(err);
        }
    }

    useEffect(() => {
        fetchData();

    }, [])

    return (
        <main id={styles.main} className='flex min-h-screen flex-col'>

            {
                data != undefined ?

                    <div className={styles.page}>
                        <div className={styles.movie}>
                            <img src={data.imageURL} className={styles.img} />

                            <div className={styles.movieInfos}>
                                <h2>{data.name}</h2>
                                <p>{data.releaseDate}</p>
                                <p>{data.description}</p>
                                <p>Generos</p>
                            </div>
                        </div>

                        <iframe className={styles.video} height="350"
                            src={'https://www.youtube.com/embed/' + data.videoURL}>
                        </iframe>


                        <form className={styles.formRating} onSubmit={formSubmit}>
                            <h2>Digite uma nota (0 a 5)</h2>
                            <input className={styles.value} type="number" onChange={(e) => { handleFormEdit(e, 'value') }} /><br />
                            <textarea className={styles.comment} placeholder='Digite um comentário' onChange={(e) => { handleFormEdit(e, 'comment') }} ></textarea><br />
                            <input className={styles.btnSubmit} type="submit" />
                        </form>

                        <div className={styles.comments}>
                            <div className={styles.commentCard}>
                                <div className={styles.commentInfos}>
                                    <label>Nome do usuário</label>
                                    <label className={styles.valueR}>(5) / 5 Recomendação</label>
                                </div>
                                <br />
                                <div className={styles.commentBox}>
                                    <label>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum</label>
                                </div>
                            </div>

                        </div>
                    </div>

                    :

                    <p>Erro 404. Não encontrado </p>

            }

        </main>
    );
}

export function getServerSideProps(context: any) {

    const { movieName } = context.query;

    return {
        props: { movieName }
    }

}