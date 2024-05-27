
const parameter = new URLSearchParams(window.location.search);
const dif = parameter.get('dif');

const difField = document.getElementById('dif');

switch(dif){
    case 'easy':
        difField.textContent = 'Dificuldade escolhida: Fácil';
        break;
    case 'med':
        difField.textContent = 'Dificuldade escolhida: Médio';
        break;
    case 'hard':
        difField.textContent = 'Dificuldade escolhida: Difícil';
        break;
    default:
        difField.textContent = 'Não encontramos a dificuldade'
        break;
}

function exit() {
    window.location.replace('./home.html');
}