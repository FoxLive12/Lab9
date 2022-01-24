from os import name
from flask.helpers import flash, url_for
from werkzeug.utils import redirect
from app import app, login_manager, admin
from model import *
from adminModel import AdminView
from flask_admin.contrib.sqlamodel import ModelView
from flask import render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, current_user, logout_user

admin.add_view(AdminView(Users, db.session))
admin.add_view(AdminView(Services, db.session))
admin.add_view(AdminView(Employees, db.session))
admin.add_view(AdminView(Type, db.session))
admin.add_view(AdminView(Application, db.session))

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


@app.route('/', methods=["POST", "GET"])
def index():
    service = Services.query.all()
    service_name_list = []
    service_img_list = []
    for i in service:
        service_name_list.append(i.name)
        service_img_list.append(i.img_name)

    if request.method == 'POST':
        if request.form['check_login'] == 'registration':
            name = request.form['name']
            email = request.form['email']
            address = request.form['address']
            telephone = request.form['telephone']
            pssw = generate_password_hash(request.form['pssw'])
            if name == "" or  email == "" or address == "" or telephone == "" or pssw == "":
                flash("Вы заполнили не все поля")
            else:
                user = Users.query.filter_by(email=request.form['email']).first()
                if user is None:
                    user = Users(name = name, email = email, address = address, telephone = telephone, passw = pssw, type_user=2)
                    db.session.add(user)
                    db.session.commit()
                    return redirect('/#popup')
                else:
                    flash("Пользователь с таким email уже зарегистрирован")
        if request.form['check_login'] == 'login':
            email = request.form['login_email']
            pssw = request.form['login_pssw']
            if email and pssw:
                user = Users.query.filter_by(email=email).first()
                if check_password_hash(user.passw, pssw):
                    rm = True if request.form.get('remember') else False
                    login_user(user, remember = rm)
                    return redirect('/#nav')
                    
    return render_template('base.html', current_user=current_user, menu_list = service_name_list, img_list = service_img_list)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/applications', methods=["POST", "GET"])
@login_required
def applications():
    service = Services.query.all()
    service_name_list = []
    for i in service:
        service_name_list.append(i.name)
    
    masters = Employees.query.all()
    master_name_list = []
    for i in masters:
        master_name_list.append(i.name)

    if request.method == 'POST':
        user_name = current_user.name
        user_telephone = current_user.telephone
        user_address = current_user.address
        vehicle_type = str(request.form.get('service_list'))
        id_vehicle_type = Services.query.filter_by(name=vehicle_type).first()
        a = Employees.query.filter(Employees.services.contains(id_vehicle_type)).all()
        print(a.id)

    
        vehicle_model = request.form['model']
        problem_description = request.form['problem']

        application = Application(user_name = user_name, user_telephone = user_telephone, user_adress = user_address, 
            vehicle_model = vehicle_model, problem_description = problem_description, vehicle_type=int(id_vehicle_type.id))
        db.session.add(application)
        db.session.commit()

    return render_template('applications.html', service_list = service_name_list, masters_list = master_name_list)