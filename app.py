from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import *
from time import gmtime, strftime
from wtform_fields import *

# engine = create_engine('sqlite:///todo.db')
# Base.metadata.create_all(engine)
#
# DBSession = sessionmaker(bind=engine)
# session = DBSession()

app = Flask(__name__)
app.secret_key="sdfdsuperfdlkngflkjnlkbgirlsdessexyasspussyfucfgfgfhhyah!!!!!dfghhm;glhjkhjl,.jk"
app.config['WTF_CSRF_SECRET_KEY'] = "b'f\xfa\x8b{X\x8b\x9eM\x83l\x19\xad\x84\x08\xaa"

app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/login')
def login_form():
    reg_form = RegistartionForm()
    if reg_form.validate_on_submit():
        return redirect(url_for('show_tasks'))
        
    return render_template('log.html', form=reg_form)

@app.route('/')
@app.route('/tasks')
def show_tasks():
    tasks = Task.query.filter_by(done=False).all()
    return render_template('task.html', tasks=tasks)



@app.route('/completedTasks')
def show_completed():
    tasks = Task.query.filter_by(done=True).all()
    return render_template('completed.html', tasks=tasks)



@app.route('/addTask', methods=['POST'])
def addTask():
    if request.form['name']:
        newTask = Task(name=request.form['name'])
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
