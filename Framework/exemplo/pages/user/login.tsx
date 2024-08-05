import styles from '@/styles/login.module.css';
import Head from 'next/head';
import Link from 'next/link';
import { useState } from 'react';

export default function loginPage() {
    
    const [ formData , setFormData ] = useState(
        {
            username: '',
            password: ''
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
            const response = await fetch(`/api/action/user/login` , {
                method: 'POST',
                headers: {'Content-type' : 'application/json'},
                body: JSON.stringify(formData)
            });

            const responseJson = await response.json();

            alert(`${response.status}\n${responseJson.message}\n${responseJson.token}`);

        }
        catch(err) {
            console.log(err);
        }
    }

    return (
        <main id={styles.main} className='flex min-h-screen flex-col'>
            <Head>
                <title>Login</title>
            </Head>

            <form className={styles.container} onSubmit={formSubmit}>
                <div id={styles.infos}>
                    <img src='/pipoca.png' alt="" />
                    
                </div>

                <div id={styles.accountForm}>
                    <h2>Inicie uma Sessão</h2><br />
                    <input className={styles.input} type="text" placeholder='Nome de usuário' onChange={(event) => {handleFormEdit(event , 'username')}} /><br />
                    <input className={styles.input} type="password" placeholder='Senha' onChange={(event) => {handleFormEdit(event , 'password')}} />

                    <br /><br />
                    <input id={styles.submitBtn} type="submit" value="Login" />
                    <Link href={`/user/register`}>Criar uma conta</Link>
                </div>

            </form>

        </main>
    );
}