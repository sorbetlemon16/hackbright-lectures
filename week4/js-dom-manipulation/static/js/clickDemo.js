button = document.querySelector('button');

button.addEventListener('click', () => {
    catImage = document.querySelector('#cat');
    if (catImage.style.display === 'none') {
        catImage.style.display = '';
    }
    else {
        catImage.style.display = 'none';
    }
});