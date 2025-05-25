document.addEventListener("DOMContentLoaded", function() {
    const rectangles = document.querySelectorAll(".eventsRectangle");

    rectangles.forEach(rect => {
        rect.addEventListener("click", function() {
            // Убираем класс 'active' у всех прямоугольников
            rectangles.forEach(r => r.classList.remove("active"));
            
            // Добавляем 'active' только к нажатому
            this.classList.add("active");
        });
    });
});

function showEventDetails(element, eventName) {
    const allRectangles = document.querySelectorAll('.eventsRectangle');

    // Закрываем все открытые элементы
    allRectangles.forEach(rect => {
        rect.classList.remove('active');
        rect.querySelector('.event-details').style.display = 'none';
    });

    // Открываем текущий
    element.classList.add('active');
    const details = element.querySelector('.event-details');
    details.style.display = 'block';

}