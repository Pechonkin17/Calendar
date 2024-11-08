function submitForm_subject() {
    const form = document.getElementById('edit-form-subject');
    const formData = new FormData(form);

    const semesterId = document.getElementById('semester_id').value;

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
        window.location.href = `/subjects/${semesterId}`;
    })
    .catch(error => {
        alert('Сталася помилка при оновленні: ' + error.message);
    });
}
