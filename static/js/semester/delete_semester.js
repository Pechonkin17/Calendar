function confirmDelete_semester(semesterId) {
    if (confirm("Ви дійсно хочете видалити цей семестер?")) {
        fetch(`/semester/delete/${semesterId}`, {
            method: 'DELETE',
        })
            .then(response => {
                if (response.ok) {
                    alert('Семестер успішно видалено');
                    window.location.reload();
                } else {
                    alert('Помилка при видаленні семестру');
                }
            })
            .catch(error => {
                console.error('Помилка:', error);
            });
    }
}