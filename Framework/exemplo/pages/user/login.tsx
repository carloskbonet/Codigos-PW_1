import styles from '@/styles/login.module.css';
import Head from 'next/head';
import Link from 'next/link';

export default function loginPage() {

    return (
        <main id={styles.main} className='flex min-h-screen flex-col'>
            <Head>
                <title>Login</title>
            </Head>

            <form className={styles.container}>
                <div id={styles.infos}>
                    <img src='/pipoca.png' alt="" />
                    
                </div>

                <div id={styles.accountForm}>
                    <h2>Inicie uma Sessão</h2><br />
                    <input className={styles.input} type="text" placeholder='Nome de usuário' /><br />
                    <input className={styles.input} type="password" placeholder='Senha' />

                    <br /><br />
                    <input id={styles.submitBtn} type="submit" value="Login" />
                    <Link href={`/user/register`}>Criar uma conta</Link>
                </div>

            </form>

        </main>
    );
}