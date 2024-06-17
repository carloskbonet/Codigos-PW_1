import styles from '@/styles/register.module.css';
import Head from 'next/head';

export default function registerPage() {

    return (
        <main className='flex min-h-screen flex-col'>
            <Head>
                <title>Cadastro</title>
            </Head>

            <div className={styles.container}>
                
                <input type="text"/>
                <br /><br />
                <input type="password" />
                <br /><br />
                <input type="email" />

            </div>

        </main>
    );
} 