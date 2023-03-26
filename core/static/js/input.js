// INPUT AUTOCOMPLETE

words = []

dom_genres = document.getElementsByClassName('genre__search-link')

for (let i = 0; i < dom_genres.length; i++) {
    words.push(dom_genres[i].innerHTML)
}


console.log(words)

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
