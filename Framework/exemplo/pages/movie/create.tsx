import Head from "next/head";
import styles from "@/styles/createMovie.module.css"
import { useState } from "react";

export default function createMovie() {
    const [ formData , setFormData ] = useState(
        {
            name : '',
            releaseDate : '',
            imageURL : '',
            videoURL : '',
            description : ''
        }
    );

    function handleFormEdit(event:any , field:string) {
        setFormData({
            ...formData,
            [field] : event.target.value
        });
    }

    async function formSubmit(event:any) {
        event.preventDefault();
        try {

        }
        catch (err) {
            console.log(err);
        }
    }

    return (
        <main className='flex min-h-screen flex-col'>
            <Head>
                <title>Cadastro de Filmes</title>
            </Head>

            <div>
                <form className={styles.formContainer}>

                    <input className={styles.input} type="text" placeholder="Nome" onChange={(event) => {handleFormEdit(event , 'name')}} />
                    <div className={styles.boxInput}>
                        <p>Data de lançamento</p>
                        <input className={styles.input} type="date" onChange={(event) => {handleFormEdit(event , 'releaseDate')}}/>
                    </div>
                    <div className={styles.boxInput}>
                        <p>Imagem</p>
                        <input className={styles.input} type="file" />
                    </div>
                    <br />
                    <input type="text" placeholder="Link para um video (Youtube) do filme" onChange={(event) => {handleFormEdit(event , 'videoURL')}} />
                    <br />
                    <textarea className={styles.input} placeholder="Descrição do filme" onChange={(event) => {handleFormEdit(event , 'description')}} />
                    <br />

                    <input type="submit" className={styles.sendBtn} />
                </form>
            </div>

        </main>
    );

}