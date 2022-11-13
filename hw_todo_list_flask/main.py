from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='template')


@app.route("/")
def main():
    return render_template('main.html')


@app.route("/login/")
def login():
    return render_template('login.html')


@app.route("/detail/")
def detail():
    task_name = request.form.get('task_name')
    task_description = request.form.get('task_descr')
    return render_template('todo_detail.html', task_description=task_description, task_name=task_name)


@app.route("/todo_add/", methods=['POST', 'GET'])
def todo_add():
    task_name = request.form.get('task_name')
    task_description = request.form.get('task_descr')
    return render_template('main.html', task_description=task_description, task_name=task_name)
