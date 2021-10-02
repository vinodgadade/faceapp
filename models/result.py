from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ResultModel(db.Model):
    __tablename__ = 'result'

    id = db.Column(db.Integer, primary_key=True)
    mspin = db.Column(db.Integer(), nullable=False, index= True)
    registered_img_id = db.Column(db.Integer, db.ForeignKey("registered_images.id", nullable=False))
    verified_path = db.Column(db.String(), nullable=False)
    result = db.Column(db.Boolean(), nullable=False)
    added_date = db.Column(db.DateTime(), nullable=False)

    def __init__(self, mspin, registered_img_id, verified_path, result, added_date):
        self.mspin = mspin
        self.registered_img_id = registered_img_id
        self.verified_path = verified_path
        self.result = result
        self.added_date = added_date

    def __repr__(self):
        return f"<Result {self.name}>"

