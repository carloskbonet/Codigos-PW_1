import styles from '@/styles/register.module.css';
import Head from 'next/head';

export default function registerPage() {

    return (
        <main id={styles.main} className='flex min-h-screen flex-col'>
            <Head>
                <title>Cadastro</title>
            </Head>

            <form className={styles.container}>
                <div id={styles.infos}>
                    <img src='/icone.png' alt="" />
                    <h2>Crie sua conta</h2>
                </div>

                <div id={styles.accountForm}>
                    <input className={styles.input} type="text" placeholder='Nome' />
                    <br /><br />
                    <input className={styles.input} type="password" placeholder='Senha' />
                    <br /><br />
                    <input className={styles.input} type="password" placeholder='Confirmar Senha' />
                    <br /><br />
                    <input className={styles.input} type="email" placeholder='Email' />

                    <br />
                    <input id={styles.submitBtn} type="submit" value='Enviar' />
                </div>

            </form>

        </main>
    );
}