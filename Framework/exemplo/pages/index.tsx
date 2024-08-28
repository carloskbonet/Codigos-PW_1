import { getCookie } from "cookies-next";
import { checkToken } from "@/services/tokenConfig";
import styles from '@/styles/home.module.css'
import { useState, useEffect } from "react";

export default function Home() {
  // Constante para armazenar os filmes
  const [data, setData]: any = useState(undefined);

  // Função para receber os dados dos filmes
  async function fetchData() {
    try {
      const response = await fetch(`/api/action/movie/select`, {
        method: 'GET',
      })

      const responseJson = await response.json();

      console.log(responseJson.data);
      setData(responseJson.data);

    }
    catch (err) {
      console.log(err);
    }
  }


  useEffect(() => {

    fetchData();

  }, [])




  return (
    <main id={styles.main} className='flex min-h-screen flex-col'>
      <nav className={styles.navBar}>
        <img className={styles.icon} src="/pipoca.png" alt="" />
        <input className={styles.searchBar} type="text" />
        <button className={styles.logoutBtn}>Logout</button>
      </nav>

      <div className={styles.mainContainer}>

        <div className={styles.leftContainer}>
        </div>



        <div className={styles.rightContainer}>

          {data != undefined && data instanceof Array ?

            data.map(movie => (

              <div className={styles.card}>
                <img src="/card.jfif" alt="" className={styles.cardImg} />
                <div className={styles.cardInfos}>
                  <h2>{movie.name}</h2>
                  <p>{movie.releaseDate}</p>
                  <p>Generos</p>
                </div>
              </div>

            ))

            :

            <p>No movies found</p>

          }



        </div>


      </div>
    </main>
  );
}

export function getServerSideProps({ req, res }: any) {
  try {
    // Procura o cookie no navegador e armazena o valor do token
    const token = getCookie('authorization', { req, res });

    // Se o cookie não existir, vamos lançar um erro
    if (!token) {
      throw new Error('Invalid Token');
    }

    // Verifica se o token é verdadeiro
    checkToken(token);

    // Se o token for verdadeiro, o usuário pode se manter na página
    return {
      props: {}
    }

  }
  catch (err) {
    // Caso o token não exista ou seja inválido, a função executará o código abaixo
    // Envia o usuário para a página de login
    return {
      redirect: {
        permanent: false,
        destination: '/user/login',
      },
      props: {}
    }
  }
}