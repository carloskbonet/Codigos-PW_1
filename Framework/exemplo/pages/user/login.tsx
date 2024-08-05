import styles from '@/styles/login.module.css';
import Head from 'next/head';
import Link from 'next/link';
import { useState } from 'react';
import { setCookie, getCookie } from 'cookies-next';
import { checkToken } from '@/services/tokenConfig';
import { useRouter } from 'next/router';

export default function loginPage() {
    const router = useRouter();

    // Criação do formulário
    const [ formData , setFormData ] = useState(
        {
            username: '',
            password: ''
        }
    );

    // Função para conectar o formulário aos inputs
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

            setCookie('authorization' , responseJson.token);

            if ( response.status != 200 ) {
                alert(`${responseJson.message}`);
            }
            else {
                router.push(`/`);
            }

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

