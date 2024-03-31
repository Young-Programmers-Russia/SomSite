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



document.addEventListener("DOMContentLoaded", function () {
  const backToTop = document.getElementById("up_image");

  // Показать/скрыть кнопку при прокрутке страницы
  window.addEventListener("scroll", function () {
    if (window.pageYOffset > 300) {
      backToTop.style.display = "block";
    } else {
      backToTop.style.display = "none";
    }
  });

  // Плавная прокрутка при клике на кнопку
  backToTop.addEventListener("click", function (event) {
    event.preventDefault();
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
});