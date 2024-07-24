import styles from '@/styles/login.module.css';
import Head from 'next/head';

export default function loginPage() {

    return (
        <main className='flex min-h-screen flex-col'>
            <Head>
                <title>Login</title>
            </Head>

            <form className={styles.container}>

                <input type="text" placeholder='Nome de usuário' />
                <input type="password" placeholder='Senha' />

                <input type="submit" value="Login" />

            </form>

        </main>
    );
}