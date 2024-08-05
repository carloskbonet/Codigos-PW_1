import { getCookie } from "cookies-next";
import { checkToken } from "@/services/tokenConfig";
import styles from '@/styles/home.module.css'

export default function Home() {
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
        </div>

      </div>
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