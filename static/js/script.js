// Highlight selected option dynamically
document.addEventListener('DOMContentLoaded', () => {
    const labels = document.querySelectorAll('label');

    labels.forEach(label => {
        const radio = label.querySelector('input[type="radio"]');
        radio.addEventListener('change', () => {
            const groupName = radio.name;
            document.querySelectorAll(`input[name="${groupName}"]`).forEach(r => {
                r.parentElement.classList.remove('selected');
            });
            if(radio.checked) {
                label.classList.add('selected');
            }
        });
    });
});
