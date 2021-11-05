from application import app, db
from application.models import Task

@app.route('/add/<checkComplete>/<newTask>')
def add(checkComplete, newTask):
    new_task = Task(complete=checkComplete , task=newTask)
    db.session.add(new_task)
    db.session.commit()
    return f"Added {new_task.task} Currently {new_task.complete}"

@app.route('/')
@app.route('/read')
def read():
    all_task = Task.query.all()
    task_string = ""
    for task in all_task:
        task_string += "<br>" + str(task.id) + " " + task.complete + " " + task.task
    return f"the tasks are: <br> <strong>ID</strong> <strong>progress</strong> <strong>task</strong>{task_string}"

@app.route('/update/<int:idnum>/<descript>')
def update(idnum, descript):
    task_change = Task.query.get(idnum)
    task_change.task = descript
    db.session.commit()
    return f"changed task {idnum} into {task_change.task}"

@app.route('/delete/<int:idnum>')
def delete(idnum):
    delete_task = Task.query.filter_by(id = idnum).delete()
    db.session.commit()
    return "Deleted task"