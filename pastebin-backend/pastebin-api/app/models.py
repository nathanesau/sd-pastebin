from app import db

from datetime import datetime

# should correspond to DDL definition
class Pastes(db.Model):
    shortlink = db.Column(db.String(7), primary_key=True, nullable=False)
    expiration_length_in_minutes = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    paste_path = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Pastes {}>'.format(self.shortlink)
