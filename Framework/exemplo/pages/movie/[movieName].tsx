import styles from '@/styles/movie.module.css'

export default function movie( { movieName }:any ) {
    return (
        <main id={styles.main} className='flex min-h-screen flex-col'>
            
            <div className={styles.page}>
                <div className={styles.movie}>
                    <img src="/card.jfif" className={styles.img} />

                    <div className={styles.movieInfos}>
                        <h2>Nome do Filme</h2>
                        <p>Data de Lançamento</p>
                        <p>Descrição</p>
                        <p>Generos</p>
                    </div>
                </div>

                <iframe className={styles.video} height="350" 
                src='https://www.youtube.com/embed/laNiRXqh82Q'>
                </iframe>
            </div>

        </main>
    );
}

export function getServerSideProps( context:any ) {

    const { movieName } = context.query;

    return {
        props: { movieName }
    }

}