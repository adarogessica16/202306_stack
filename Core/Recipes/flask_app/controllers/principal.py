from flask import render_template, flash, redirect, session
from flask_app import app
from flask_app.models.recipe import Recipe


@app.route('/')
def inicio():
    if 'user' not in session:
        flash("No iniciaste sesion!", "error")
        return redirect("/login")
    recipes= Recipe.get_all()
    return render_template("inicio.html", recipes=recipes)