import Head from "next/head";
import styles from "@/styles/createMovie.module.css"

export default function createMovie() {

    return (
        <main className='flex min-h-screen flex-col'>
            <Head>
                <title>Cadastro de Filmes</title>
            </Head>

            <div>
                <form className={styles.formContainer}>

                    <input className={styles.input} type="text" placeholder="Nome" />
                    <div className={styles.boxInput}>
                        <p>Data de lançamento</p>
                        <input className={styles.input} type="date"/>
                    </div>
                    <div className={styles.boxInput}>
                        <p>Imagem</p>
                        <input type="file" />
                    </div>
                    <br />
                    <input className={styles.input} type="text" placeholder="Descrição do filme" />
                    <br />

                    <input type="submit" className={styles.sendBtn} />
                </form>
            </div>

        </main>
    );

}