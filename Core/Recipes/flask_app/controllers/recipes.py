from flask_app import app
from flask import render_template,redirect,request,flash
from flask_app.models.recipe import Recipe
from flask_app.models.user import User
@app.route('/recipes')
def index():
    return render_template('recipe_form.html')

@app.route('/process_add_recipe',methods=['POST'])
def new_recipe():
    print(request.form)
    errores=Recipe.validar_Recipe(request.form)
    if len(errores) > 0:
        for error in errores:
            flash(error, "error")
        return redirect("/recipes")
    Recipe.add_recipe(request.form)
    flash("Recipe added successfully!", "success")
    return redirect('/')


@app.route('/recipe/<int:id>')
def show_recipe(id):
    recipe= Recipe.get_recipe(id)
    print("Recibo esto",recipe)
    user= User.get(id)
    return render_template('recipe_show.html',user=user, recipe=recipe)

@app.route('/recipe/edit/<int:id>')
def edit(id):
    recipe = Recipe.get_recipe(id)
    return render_template("update.html", recipe=recipe)

@app.route('/recipe/update', methods=['POST'])
def update_user():
    data = {
        "id": request.form['id'],
        "name": request.form["name"],
        "description": request.form["description"],
        "instruction": request.form["instruction"],
        "time_preparation":request.form['time_preparation'],
        "made":request.form['made']

    }
    errores = Recipe.validar_Recipe(data) 
    if len(errores) > 0:
        for error in errores:
            flash(error, "error")
        return redirect('/')

    Recipe.update(data) 
    flash("Recipe updated successfully!", "success")
    return redirect('/')


@app.route('/recipe/delete/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    Recipe.delete(data)
    flash("Deleted recipe!!", "info")
    return redirect('/')

