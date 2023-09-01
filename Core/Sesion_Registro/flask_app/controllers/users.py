from flask_app import app
from flask import render_template,redirect,request,flash, session
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) 



@app.route("/login")
def login():
    return render_template("form.html")

#Para el registro
@app.route('/procesar_registro',methods=['POST'])
def procesar():
    print(request.form)
    errores= User.validar(request.form)
    if len(errores) > 0:
        for error in errores:
            flash(error, "error")
        return redirect("/login")
    
    if request.form["password"] != request.form["confirmar_password"]:
        flash("las contraseñas no son iguales", "error")
        return redirect("/login")
    
    password_hash= bcrypt.generate_password_hash(request.form['password'])
    print(password_hash)

    #Guardar los datos
    data={
        "name": request.form['name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password":password_hash
    }
    user_id= User.save(data)
    flash("Usuario registrado correctamente", "success")
    return redirect("/login")

#Para el login
@app.route('/procesar_login', methods=["POST"])
def procesar_login():
    print(request.form)

    user  = User.get_by_email(request.form['email'])
    if not user:
        flash("El correo o la contraseña no es válida", "error")
        return redirect("/login")
    #Verificar la contraseña
    resultado = bcrypt.check_password_hash(user.password, request.form['password'])

    if resultado:
        session['user'] = {
            'id': user.id,
            'name': user.name,
            'last_name': user.last_name,
            'email': user.email
        }
        return redirect("/")

    flash("La contraseña o el correo no es válido", "error")
    return redirect("/login")

#El logout

@app.route('/salir')
def salir():
    session.clear()
    return redirect("/login")

