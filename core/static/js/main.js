// Mobile nav
mobileNavBtn = document.getElementById('mobileNavBtn');
mobileNav = document.getElementById('mobileNav');

function openNav() {
    mobileNav.classList.toggle('mobile__nav-active');
}

mobileNavBtn.addEventListener('click', openNav);

// password helper

password = document.getElementById('password');
passwordConfirmation = document.getElementById('password-confirmation');

passwordNumbers = document.getElementById('password-numbers');
passwordCharacters = document.getElementById('password-characters');
passwordSpecialCharacters = document.getElementById('password-special');
passwordLower = document.getElementById('password-lower');
passwordUpper = document.getElementById('password-upper');

function passwordIncludesNumbers() {
    if (password.value.match(/[0-9]/)) {
        return true;
    } else {
        return false;
    }
}

function passwordMoreThanMinCharacters() {
    if (password.value.length >= 12) {
        return true;
    } else {
        return false;
    }
}

function passwordIncludesSpecialCharacters() {
    if(password.value.match(/[!@#$%^&*£]/)) {
        return true;
    } else {
        return false;
    }
}

function passwordIncludesLower() {
    isLower = new RegExp('[a-z]');
    if (password.value.match(isLower)) {
        return true;
    } else {
        return false;
    }
}


function passwordIncludesUpper(){
    isUpper = new RegExp('[A-Z]');
    if (password.value.match(isUpper)) {
        return true;
    } else {
        return false;
    }
}
password.addEventListener('input', function () {
    if (passwordMoreThanMinCharacters()) {
        passwordCharacters.style.color = 'green';
    } else {
        passwordCharacters.style.color ='rgb(167, 0, 0)';
    }
    if(passwordIncludesNumbers()) {
        passwordNumbers.style.color = 'green';
    } else {
        passwordNumbers.style.color ='rgb(167, 0, 0)';
    }
    if(passwordIncludesSpecialCharacters()) {
        passwordSpecialCharacters.style.color = 'green';
    } else {
        passwordSpecialCharacters.style.color ='rgb(167, 0, 0)';
    }
    if(passwordIncludesLower()) {
        passwordLower.style.color = 'green';
    } else {
        passwordLower.style.color ='rgb(167, 0, 0)';
    }
    if(passwordIncludesUpper()) {
        passwordUpper.style.color = 'green';
    } else {
        passwordUpper.style.color ='rgb(167, 0, 0)';
    }
})


passwordConfirmation.addEventListener('input', function () {
    if (password.value == passwordConfirmation.value) {
        passwordConfirmation.style.border = '3px solid green';
        password.style.border = '3px solid green';
    } else {
        passwordConfirmation.style.border ='3px solid rgb(167, 0, 0)';
        password.style.border ='3px solid rgb(167, 0, 0)';
    }
})



// INPUT AUTOCOMPLETE

let words = [
    'Rock',
    'Metal',
    'Pop',
    'Jazz',
    'Classical',
    'Hip Hop',
    'Dance',
    'Punk'
];

// sorts the list of words in alphabetical order
words.sort();

// grabbing the input and the suggestion span from the DOM
let input = document.getElementById('genre_input');
let suggestion = document.getElementById('suggestion');

// immediately after the window laods, this callback function is executed
window.onload = () => {
    input.value = '';
    clearSuggestion();
}

const clearSuggestion = () => {
    suggestion.innerHTML = '';
};

const caseCheck = word => {
    // make word into array of characters
    word = word.split('');
    let inputText = input.value;

    for(let i in inputText) {
        if (inputText[i] == word[i]){
            continue;
        } else if (inputText[i].toUpperCase() == word[i]){
            word.splice(i, 1, word[i].toLowerCase());
        } else {
            word.splice(i, 1, word[i].toUpperCase());
        }
    }
    return word.join('');
};



input.addEventListener('input', (e) => {
    clearSuggestion();
    let regex = new RegExp('^' + input.value, 'i');
    
    for (let i in words) {
        if(regex.test(words[i]) && input.value != '') {
            words[i] = caseCheck(words[i]);
            suggestion.innerHTML = words[i].toLowerCase();
            break;
        }
    }
})

// complete autocomplete on enter key
input.addEventListener('keydown', (e) => {
    if(e.key === 'Enter' && suggestion.innerText != ''){
        e.preventDefault();
        input.value = suggestion.innerText;
        clearSuggestion();
        document.getElementById('submit_genre').removeAttribute('disabled');
    }
})
