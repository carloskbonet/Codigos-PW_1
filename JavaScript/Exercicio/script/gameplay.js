
const parameter = new URLSearchParams(window.location.search);
const dif = parameter.get('dif');
// Variáveis do HTML
const difField = document.getElementById('dif');
const result = document.getElementById('result');
var inputNumber = document.getElementById('inputNumber');
const triesField = document.getElementById('tries');
const tipsField = document.getElementById('tips');
// Variáveis do Jogo
let sortedNumber = 0;
let tries = 4;
let tips = 2;
// Variáveis para fazer a dica
let maxSorted = 0;
let sortedNumberTip = 0;
let tipText = document.getElementById('tipText');

triesField.textContent = tries;
tipsField.textContent = tips;


switch(dif){
    case 'easy':
        difField.textContent = 'Dificuldade escolhida: Fácil';
        sortedNumber = Math.floor(Math.random() * 30) + 1;
        maxSorted = 30;
        break;
    case 'med':
        difField.textContent = 'Dificuldade escolhida: Médio';
        sortedNumber = Math.floor(Math.random() * 60) + 1;
        maxSorted = 60;
        break;
    case 'hard':
        difField.textContent = 'Dificuldade escolhida: Difícil';
        sortedNumber = Math.floor(Math.random() * 90) + 1;
        maxSorted = 90;
        break;
    default:
        difField.textContent = 'Não encontramos a dificuldade'
        break;
}

console.log(sortedNumber);

async function exit() {
    await sleep(3000);
    window.location.replace('./home.html');
}

function sleep (time) {
    return new Promise((resolve) => setTimeout(resolve, time));
}


function gameplay() {
    let number = parseInt(inputNumber.value);
    inputNumber.value = null;

    if ( number == sortedNumber ) {
        result.textContent = 'Uau, eu não estava esperando por essa!! HAHAHA você realmente acertou!!!!!!! Meus parabéns Vencedor.';

        return exit();
    }
    else {
        if ( tries > 0 ) {
            tries = tries -1;

            triesField.textContent = tries;

            result.textContent = 'Buuuuuuh não foi dessa vez !!! Você tem ' + tries + ' tentativas restantes';
        }
        
        if ( tries <= 0 ) {
            result.textContent = "GAME OVER";

            return exit();
        }
    }
}


function callTip() {
    if ( tips <= 0 ) {
        alert('Você não tem dicas restantes.');
        
        return;
    }
    else {
        tips = tips - 1;
        tipsField.textContent = tips;
    }

    sortedNumberTip = Math.floor(Math.random() * maxSorted) + 1;

    if ( sortedNumberTip > sortedNumber ) {
        // Falar que o número sorteado é MENOR que o número da dica
        tipText.textContent = `O número sorteado é MENOR que ${sortedNumberTip}`
    }
    if ( sortedNumberTip < sortedNumber ) {
        // Falar que o número sorteado é MAIOR que o número da dica
        tipText.textContent = `O número sorteado é MAIOR que ${sortedNumberTip}`
    }

    if ( sortedNumberTip == sortedNumber ) {
        // Escolher uma fala
        tipText.textContent = `Tente TUDO menos ${sortedNumberTip}`
    }
}