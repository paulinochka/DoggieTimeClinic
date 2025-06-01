document.addEventListener("DOMContentLoaded", function () {
    const rectangles = document.querySelectorAll(".partnerRectangle");

    rectangles.forEach(rect => {
        rect.addEventListener("click", function () {
            rectangles.forEach(r => {
                if (r !== this) {
                    r.classList.remove("active");
                }
            });

            this.classList.toggle("active");
            if (this.classList.contains('active')) {
                const detailedView = this.querySelector('.partnerDetailedView');
                this.style.height = `${detailedView.scrollHeight + 40}px`;
                this.style.width = `${detailedView.scrollWidth + 40}px`;
            } else {
                this.style.height = '';
                this.style.width = '';
            }
        });
    });
});