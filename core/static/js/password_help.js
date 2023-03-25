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


