const openPopUp = document.getElementById('open_pop_up');
const closePopUp = document.getElementById('pop_up_close');
const popUp = document.getElementById('pop_up');

openPopUp.addEvenListener('click', function(e){
    e.preventDefault();
    popUp.classList.add('active');
})

closePopUp.addEvenListener('click', function(e) {
    popUp.classList.remove('active');

})