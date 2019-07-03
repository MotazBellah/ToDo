from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import *
from time import gmtime, strftime
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from flask import session as login_session
from wtform_fields import *


app = Flask(__name__)
app.secret_key="sdfdsuperfdlkngflkjnlkbgirlsdessexyasspussyfucfgfgfhhyah!!!!!dfghhm;glhjkhjl,.jk"
app.config['WTF_CSRF_SECRET_KEY'] = "b'f\xfa\x8b{X\x8b\x9eM\x83l\x19\xad\x84\x08\xaa"

app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# configure flask_login
login = LoginManager(app)
login.init_app(app)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
@app.route('/register', methods=['GET', 'POST'])
def login_form():
    reg_form = RegistartionForm()
    if reg_form.validate_on_submit():
        # return redirect(url_for('show_tasks'))
        username = reg_form.username.data
        email = reg_form.email.data
        password = reg_form.password.data
        hashed_pswd = pbkdf2_sha256.hash(password)
        # Add user to DB
        user = User(username=username, email=email, password=hashed_pswd)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('log.html', form=reg_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    # Allow login if validation success
    if login_form.validate_on_submit():
        user_object = User.query.filter_by(email=login_form.email.data).first()
        login_user(user_object)
        login_session['user_id'] = user_object.id
        return redirect(url_for('show_tasks'))

    return render_template("login.html", form=login_form)


@app.route('/logout')
def logout():
    logout_user()
    del login_session['user_id']
    return redirect(url_for('login_form'))



@app.route('/tasks')
def show_tasks():
    user_id = login_session['user_id']
    tasks = Task.query.filter_by(done=False).filter_by(user_id=user_id).all()
    return render_template('task.html', tasks=tasks)



@app.route('/completedTasks')
def show_completed():
    if not current_user.is_authenticated:
        return redirect(url_for('login_form'))

    tasks = Task.query.filter_by(done=True).all()
    return render_template('completed.html', tasks=tasks)



@app.route('/addTask', methods=['POST'])
def addTask():
    if request.form['name']:
        newTask = Task(name=request.form['name'], user_id=login_session['user_id'])
        db.session.add(newTask)
        db.session.commit()

    return redirect(url_for('show_tasks'))


@app.route('/delete/<task_name>')
def deleteTask(task_name):
    task = Task.query.filter_by(name=task_name).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('show_tasks'))


@app.route('/edit', methods=['POST'])
def editTask():
    task = Task.query.filter_by(name=request.form['id']).first()
    task.name = request.form['name']
    db.session.add(task)
    db.session.commit()

    return jsonify({'result': 'success'})


@app.route('/complete', methods=['POST'])
def completeTask():
    task = session.query(Task).filter_by(name=request.form['id']).first()
    task.done = True
    session.add(task)
    session.commit()

    return jsonify({'result': 'success'})




if __name__ == '__main__':
    # app.secret_key = 'super_secret_key'
    # app.debug = True
    # app.run(host = '0.0.0.0', port = 8000)
    app.run(debug=True)
