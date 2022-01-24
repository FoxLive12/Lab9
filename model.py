from app import db
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    address = db.Column(db.String(200), nullable=False)
    telephone = db.Column(db.String(200), nullable=False)
    passw = db.Column(db.String(250), nullable=False)
    type_user = db.Column(db.Integer, db.ForeignKey('type.id'))

    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<Users {}>'.format(self.name)

class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, unique=True)
    users_id = db.relationship("Users", backref='type', uselist=False)

    def __init__(self, *args, **kwargs):
        super(Type, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<Type {}>'.format(self.title)


class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    img_name = db.Column(db.String(200), nullable=False)
    уmployee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    application_id = db.relationship("Application", backref='type', uselist=False)

    def __init__(self, *args, **kwargs):
        super(Services, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<Services {}>'.format(self.name)

class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    telephone = db.Column(db.String(200), nullable=False)

    services = db.relationship("Services")
    application = db.relationship("Application")

    def __init__(self, *args, **kwargs):
        super(Services, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<Services {}>'.format(self.name)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(200), nullable=False)
    user_telephone = db.Column(db.String(200), nullable=False)
    user_adress = db.Column(db.String(200), nullable=False)
    vehicle_model = db.Column(db.String(200), nullable=False)
    problem_description = db.Column(db.String(200), nullable=False)
    master_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    vehicle_type = db.Column(db.Integer, db.ForeignKey('services.id'))

    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<Application {}>'.format(self.vehicle_type)