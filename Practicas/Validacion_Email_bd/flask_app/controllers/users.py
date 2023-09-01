from flask_app import app
from flask import render_template,redirect,request,flash
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template("form.html")


@app.route('/process', methods=['POST'])
def process():
    if not User.validar(request.form):
        return redirect('/')
    User.save(request.form)
    flash("Email Añadido", "success")
    return redirect('/result')


@app.route("/result")
def result():
    users= User.get_all()
    return render_template("info.html", users=users)

@app.route('/user/delete/<int:id>')
def delete(id):
    data ={
        'id': id
    }
    User.delete(data)
    flash("Email borrado", "success")
    return redirect('/result')