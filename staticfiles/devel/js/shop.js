const openPopupButton = document.getElementById("open_popup");
const closePopupButton = document.getElementById("closePopup");
const popup = document.getElementById("popup");
const popupBody = document.getElementById("popup_body");

// Функция для открытия попапа
function openPopup() {
    popup.style.display = 'block'; // Сначала показываем
    setTimeout(() => popup.classList.add('show'), 10); // Задержка для плавного эффекта
}

// Функция для закрытия попапа
function closePopup() {
    popup.classList.remove('show');
    setTimeout(() => popup.style.display = 'none', 500); // Скрываем после анимации
}

// Добавляем обработчик событий
openPopupButton.addEventListener("click", openPopup);
closePopupButton.addEventListener("click", closePopup);

// Закрытие попапа при клике вне его содержимого
window.addEventListener("click", function(event) {
    if (event.target === popupBody) {
        closePopup();
    }
});
