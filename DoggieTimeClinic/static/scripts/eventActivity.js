document.addEventListener("DOMContentLoaded", function() {
    const rectangles = document.querySelectorAll(".eventsRectangle");

    rectangles.forEach(rect => {
        rect.addEventListener("click", function() {
            // ������� ����� 'active' � ���� ���������������
            rectangles.forEach(r => r.classList.remove("active"));
            
            // ��������� 'active' ������ � ��������
            this.classList.add("active");
        });
    });
});

function showEventDetails(element, eventName) {
    const allRectangles = document.querySelectorAll('.eventsRectangle');

    // ��������� ��� �������� ��������
    allRectangles.forEach(rect => {
        rect.classList.remove('active');
        rect.querySelector('.event-details').style.display = 'none';
    });

    // ��������� �������
    element.classList.add('active');
    const details = element.querySelector('.event-details');
    details.style.display = 'block';

}