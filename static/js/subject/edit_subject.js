function submitForm() {
    const form = document.getElementById('edit-form');
    const formData = new FormData(form);

    fetch(window.location.href, {
        method: 'PATCH',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            return response.json()
        } else {
            throw new Error('Помилка при оновленні');
        }
    })
    .then(data => {
        console.log(data.message);
        window.location.href = "/subjects";
    })
    .catch(error => {
        alert('Сталася помилка при оновленні: ' + error.message);
    });
}
