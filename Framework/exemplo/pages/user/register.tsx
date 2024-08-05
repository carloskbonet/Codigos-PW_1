import styles from '@/styles/register.module.css';
import Head from 'next/head';
import Link from 'next/link';
import { useState } from 'react';
import { getCookie } from 'cookies-next';
import { checkToken } from '@/services/tokenConfig';
import { useRouter } from 'next/router';

export default function registerPage() {
    const router = useRouter();

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

        try {
            const response = await fetch(`/api/action/user/create` , {
                method: 'POST',
                headers: { 'Content-type':'application/json' },
                body: JSON.stringify(formData)
            });
            
            const responseJson = await response.json();

            alert(`${responseJson.message}`);

            if ( response.status == 201 ){
                router.push(`/user/login`);
            }
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
                    <img src='/pipoca.png' alt="" />
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
                    <div className={styles.btns}>
                        <Link className={styles.redirect} href={`/user/login`}>Já tenho uma conta</Link>
                        <input id={styles.submitBtn} type="submit" value='Enviar' />
                    </div>
                </div>

            </form>

        </main>
    );
}


export function getServerSideProps( {req , res}:any ) {
    try {
        // Procura o cookie no navegador e armazena o valor do token
        const token = getCookie('authorization' , {req , res});

        // Se o cookie não existir, vamos lançar um erro
        if ( !token ) {
            throw new Error('Invalid Token');
        }

        // Verifica se o token é verdadeiro
        checkToken(token);

        // Se o token for verdadeiro, envia o usuário para dentro do sistema
        return {
            redirect: {
                permanent: false,
                destination: '/',
            },
            props: {}
        }

    }
    catch (err) {
        // Caso o token não exista ou seja inválido, a função executará o código abaixo
        return {
            props: {}
        }
    }
}