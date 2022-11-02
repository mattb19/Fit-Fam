from Database import db
from flask_login import UserMixin
from app import login

# REMINDER: IF NEED COLUMN IN CHRONOLOGICAL ORDER (SUCH AS POSTS TABLE) MAKE SURE index=TRUE FOR THE NECESSARY COLUMN

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(62), unique=True, nullable=False)
    nickname = db.Column(db.String(50))
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<User {self.firstName} {self.lastName}>'


class SecurityQuestions(db.Model):
    __tablename__ = 'SecurityQuestions'
    userId = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)
    Question1 = db.Column(db.String(20), nullable=False)
    Answer1 = db.Column(db.String(255), nullable=False)
    Question2 = db.Column(db.String(20), nullable=False)
    Answer2 = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<{self.Question1}: {self.Answer1}, {self.Question2}: {self.Answer2}>'

class Groups(db.Model):
    __tablename__ = 'Groups'
    groupId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    groupName = db.Column(db.String(20), nullable=False)
    groupOwner = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)

class GroupMembers(db.Model):
    __tablename__ = 'GroupMembers'
    group = db.Column(db.Integer, db.ForeignKey('Groups.groupId'), nullable=False)
    member = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)