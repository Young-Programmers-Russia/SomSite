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



const regBtn = document.querySelector(".nav-2");
const logBtn = document.querySelector(".nav-l");
const regF = document.querySelector(".registration_form");
const logF = document.querySelector(".login_form");
const closeBtnL = document.querySelector(".close_btnL");
const closeBtnR = document.querySelector(".close_btnR");
const shadow = document.querySelector(".l_close");

const registration = document.querySelector(".reg");
const login = document.querySelector(".log")


regBtn.addEventListener("click", ()=>{
  regF.classList.toggle("registration_form-open");
  shadow.classList.add("l_open");
});

logBtn.addEventListener("click", ()=>{
  logF.classList.toggle("login_form-open");
  shadow.classList.add("l_open");
});

closeBtnL.addEventListener("click", ()=>{
  logF.classList.remove("login_form-open");
  shadow.classList.remove("l_open");

});

closeBtnR.addEventListener("click", ()=>{
  regF.classList.remove("registration_form-open");
  shadow.classList.remove("l_open");
});

registration.addEventListener("click", ()=>{
  logF.classList.remove("login_form-open");
  regF.classList.add("registration_form-open");
})

login.addEventListener("click", ()=>{
  regF.classList.remove("registration_form-open");
  logF.classList.add("login_form-open");
})

