from flask import Blueprint,render_template
from .forms import formulartest
from .views import blueprint
@blueprint.route('/vypis_jahn', methods=['GET'])
def Vypis_jahn():
        pole=[[0,1],
              [2,3],
              [0,30]]
        pole[0][1]=pole[0][1]+1
        return render_template("public/vypis_jahn.tmpl",data =pole)

@blueprint.route('/vypis_jahn/form', methods=['GET', 'POST'])
def formularjahntest():
    form = formulartest()
    if form.validate_on_submit():
        return str(form.a.data * form.b.data)
    return render_template("public/formularjahntest.tmpl", form = form)