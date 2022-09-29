from crypt import methods
from dojos_flask_app.models.ninja_model import Ninja
from dojos_flask_app.models.dojo_model import Dojo
from dojos_flask_app import app
from flask import render_template, redirect, request 

@app.route('/ninjas')
def form_ninja():
    all_dojos = Dojo.all_dojos()
    return render_template('ninjas.html', all_dojos=all_dojos)


@app.route("/created_ninjas", methods=['POST'])
def created_ninja():
    print(request.form, "CONTIENE")
    id_ninja = Ninja.created_ninja(request.form)
    data={
        "id": id_ninja
    }
    a_ninja = Ninja.get_ninja(data)
    print(a_ninja, "CONTIENE")
    return redirect(f'/dojos/{a_ninja.dojo_id}')

@app.route('/')
def root():
    return render_template('login_reg.html')

