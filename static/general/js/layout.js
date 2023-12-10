//для окна элементов
const openBurger = document.getElementById('nav_menu');
const menu = document.getElementById('nav_items');
//для окна регистрации
const openLogin = document.getElementById("icon_of_login");
const Login =document.getElementById('nav_login');

const body = document.getElementById('body');

openBurger.addEventListener('click', function(e){
    e.preventDefault();
    openBurger.classList.toggle('active');
    menu.classList.toggle('active');
    body.classList.toggle('lock');
    openBurger.close('')
})



openLogin.addEventListener('click', function(e){
    e.preventDefault();
    Login.classList.toggle('active');
    body.classList.toggle('lock');
    openLogin.classList.toggle('active');

})