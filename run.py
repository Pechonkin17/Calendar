from flask import Flask
from routes import index_bp, subject_bp, lab_bp
from base import create_db, drop_db

app = Flask(__name__)

app.register_blueprint(index_bp)
app.register_blueprint(subject_bp)
app.register_blueprint(lab_bp)

create_db()

if __name__ == "__main__":
    app.run(debug=True)


# TODO 1. оновлення/видалення лаби 2. відображення всіх предметів на головній сторінці 3. кнопка 'адмін' для активації оновлення/видалення предмети/лаби 4. добавити html+css