function confirmDeleteLab(labId) {
    if (confirm("Ви дійсно хочете видалити цю лабораторну?")) {
        fetch(`/labs/delete/${labId}`, {
            method: 'DELETE'
        })
            .then(response => {
                if (response.ok) {
                    alert('Лабораторну успішно видалено');
                    window.location.reload();
                } else {
                    alert('Помилка при видаленні лабораторної');
                }
            })
            .catch(error => {
                console.error('Помилка:', error);
            });
    }
}
