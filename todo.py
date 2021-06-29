from flask import Flask,render_template,redirect,url_for
from flask.globals import request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import RequestURITooLarge

app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\SQLite\\todo.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\\polis odası\\YAŞAR\\AAA Kodlama\\Kodlama\\Flask\\TODOApp\\todo.db'

db=SQLAlchemy(app)

@app.route("/")
def index():
    todos=Todo.query.all()
    return render_template("index.html",todos=todos)

@app.route("/add",methods=["POST"])
def AddTodo():
    title=request.form.get("title")
    newTodo=Todo(title=title,complete=False)
    db.session.add(newTodo)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/complete/<string:id>")
def completeTodo(id):
    todo=Todo.query.filter_by(id=id).first()
    todo.complete=not todo.complete
    db.session.commit()
    
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def todoDelete(id):
    todo=Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for("index"))


class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(80))
    complete=db.Column(db.Boolean)


if __name__=="__main__":
    db.create_all()
    app.run(debug=True)


