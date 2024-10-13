function submitForm_lab() {
    const form = document.getElementById('edit-form-lab');
    const formData = new FormData(form);

    const subjectId = document.getElementById('subject_id').value;

    fetch(window.location.href, {
        method: 'PATCH',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Помилка при оновленні');
        }
    })
    .then(data => {
        console.log(data.message);
        window.location.href = `/labs/${subjectId}`;
    })
    .catch(error => {
        alert('Сталася помилка при оновленні: ' + error.message);
    });
}
