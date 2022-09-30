from dojos_flask_app.models.dojo_model import Dojo
from dojos_flask_app import app
from flask import render_template, redirect, request

@app.route('/')
def root():
    return "redirect()"

@app.route("/dojos")
def dojos():
    all_dojos=Dojo.all_dojos()
    return render_template('dojos.html', all_dojos=all_dojos)

@app.route('/created',methods=['POST'])
def created():
    Dojo.created(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {
        "id": dojo_id
    }
    dojo = Dojo.get_dojo(data)
    print(f'show_dojo. dojo: {dojo}')
    ninjas_in_dojo = Dojo.get_ninjas_in_dojo(data)
    print(f'show_dojo. ninjas_in_dojo: {ninjas_in_dojo}')
    return render_template('show.html', dojo=dojo, ninjas_in_dojo=ninjas_in_dojo)

