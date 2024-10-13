function confirmDelete_subject(subjectId) {
    if (confirm("Ви дійсно хочете видалити цей предмет?")) {
        fetch(`/subjects/delete/${subjectId}`, {
            method: 'DELETE'
        })
            .then(response => {
                if (response.ok) {
                    alert('Предмет успішно видалено');
                    window.location.reload();
                } else {
                    alert('Помилка при видаленні предмету');
                }
            })
            .catch(error => {
                console.error('Помилка:', error);
            });
    }
}