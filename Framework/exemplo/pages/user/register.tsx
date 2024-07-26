import styles from '@/styles/register.module.css';
import Head from 'next/head';
import { useState } from 'react';

export default function registerPage() {

    // Formulário a ser enviado para o servidor
    const [ formData , setFormData ] = useState(
        {
            name : "",
            username : "",
            password : "",
            confirmPassword : "",
            cpf : ""
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

        console.log(formData);

        try {
            const response = await fetch(`/api/action/user/create` , {
                method: 'POST',
                headers: { 'Content-type':'application/json' },
                body: JSON.stringify(formData)
            });
            
            const responseJson = await response.json();

            alert(`${response.status} \n${responseJson}`);


        }
        catch(err) {
            console.log(err);
        }
    }


    return (
        <main id={styles.main} className='flex min-h-screen flex-col'>
            <Head>
                <title>Cadastro</title>
            </Head>

            <form className={styles.container} onSubmit={formSubmit}>
                <div id={styles.infos}>
                    <img src='/icone.png' alt="" />
                    <h2>Crie sua conta</h2>
                </div>

                <div id={styles.accountForm}>
                    <input className={styles.input} type="text" placeholder='Nome' onChange={(event) => { handleFormEdit(event , 'name') }} />
                    <br /><br />
                    <input className={styles.input} type="text" placeholder='Nome de Usuário' onChange={(event) => { handleFormEdit(event , 'username') }} />
                    <br /><br />
                    <input className={styles.input} type="text" placeholder='CPF' onChange={(event) => { handleFormEdit(event , 'cpf') }} />
                    <br /><br />
                    <input className={styles.input} type="password" placeholder='Senha' onChange={(event) => { handleFormEdit(event , 'password') }} />
                    <br /><br />
                    <input className={styles.input} type="password" placeholder='Confirmar Senha' onChange={(event) => { handleFormEdit(event , 'confirmPassword') }} />
                    <br /><br />
                    

                    <br />
                    <input id={styles.submitBtn} type="submit" value='Enviar' />
                </div>

            </form>

        </main>
    );
}