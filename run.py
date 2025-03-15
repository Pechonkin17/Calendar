from flask import Flask
from routes import subject_bp, lab_bp, semester_bp
from base import create_db, drop_db

app = Flask(__name__)
app.register_blueprint(subject_bp)
app.register_blueprint(lab_bp)
app.register_blueprint(semester_bp)


#create_db()


if __name__ == "__main__":
    app.run(debug=True)