const openBurger = document.getElementById('nav_menu');
const body = document.getElementById('body');
const menu = document.getElementById('nav_items');

openBurger.addEventListener('click', function(e){
    e.preventDefault();
    menu.classList.toggle('active');
    body.classList.toggle('lock');
})

openBurger.addEventListener('click', function(e){
    e.preventDefault();
    openBurger.classList.toggle('active');
})