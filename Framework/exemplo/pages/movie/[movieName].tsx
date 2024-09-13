import styles from '@/styles/movie.module.css'
import { getCookie } from 'cookies-next';
import { checkToken } from '@/services/tokenConfig';
import { useState, useEffect } from 'react';
import { useRouter } from 'next/router';

export default function movie({ movieName }: any) {
    const [data, setData]: any = useState();

    const router = useRouter();

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
            router.reload();
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

                            <div className={styles.star_rating}>

                                <input className={styles.radio_hide} type="radio" id='star_5' name='stars' value='5' onChange={(e) => { handleFormEdit(e, 'value') }} />
                                <label className={styles.radio_star} htmlFor='star_5' ></label>

                                <input className={styles.radio_hide} type="radio" id='star_4' name='stars' value='4' onChange={(e) => { handleFormEdit(e, 'value') }} />
                                <label className={styles.radio_star} htmlFor='star_4' ></label>

                                <input className={styles.radio_hide} type="radio" id='star_3' name='stars' value='3' onChange={(e) => { handleFormEdit(e, 'value') }} />
                                <label className={styles.radio_star} htmlFor='star_3' ></label>

                                <input className={styles.radio_hide} type="radio" id='star_2' name='stars' value='2' onChange={(e) => { handleFormEdit(e, 'value') }} />
                                <label className={styles.radio_star} htmlFor='star_2' ></label>

                                <input className={styles.radio_hide} type="radio" id='star_1' name='stars' value='1' onChange={(e) => { handleFormEdit(e, 'value') }} />
                                <label className={styles.radio_star} htmlFor='star_1' ></label>


                            </div>
                            <textarea className={styles.comment} placeholder='Digite um comentário' onChange={(e) => { handleFormEdit(e, 'comment') }} ></textarea><br />
                            <input className={styles.btnSubmit} type="submit" />
                        </form>

                        <div className={styles.comments}>
                            <h1 className={styles.commentTitle}>Comentários</h1>
                            {
                                data.ratings.map((rating: any) => (
                                    <div className={styles.commentCard}>
                                        <div className={styles.commentInfos}>
                                            <label>{rating.user.username}</label>
                                            <label className={styles.valueR}>({rating.value}) / 5 Recomendação</label>
                                        </div>
                                        <br />
                                        <div className={styles.commentBox}>
                                            <label>{rating.comment}</label>
                                        </div>
                                    </div>

                                ))
                            }
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