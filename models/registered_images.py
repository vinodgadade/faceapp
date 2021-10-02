from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class RegisteredImagesModel(db.Model):
    __tablename__ = 'registered_images'

    id = db.Column(db.Integer, primary_key=True)
    mspin = db.Column(db.Integer(), nullable=False, index=True)
    path = db.Column(db.String(), nullable=False)
    added_date = db.Column(db.DateTime(), nullable=False)

    def __init__(self, mspin, path, added_date):
        self.mspin = mspin
        self.path = path
        self.added_date = added_date

    def __repr__(self):
        return f"<RegisteredImages {self.name}>"
