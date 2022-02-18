from flask import Flask, render_template, request
from backend_check.constants import Constants as cts
from backend_check.check_input_errors import user_input_errors
from backend_check.operations import save_info_db


app = Flask(__name__)


@app.route('/')
def captive_portal():
    ent_name = cts.COMPANY_NAME
    return render_template("captive_portal.html", title=ent_name)


@app.route('/confirmation', methods=["POST"])
def confirmation():
    ent_name = cts.COMPANY_NAME
    cts.NAME = request.form.get("first_name")
    cts.LASTNAME = request.form.get("last_name")
    cts.EMAIL = request.form.get("email")
    cts.MOVIL = request.form.get("movil")

    error = user_input_errors(cts.NAME, cts.LASTNAME, cts.EMAIL, cts.MOVIL)
    if error:
        return render_template("captive_portal.html", title=ent_name, first_name=cts.NAME, last_name=cts.LASTNAME, email=cts.EMAIL, movil=cts.MOVIL, error=error)
    else:
        return render_template("confirmation.html", title=ent_name, first_name=cts.NAME, last_name=cts.LASTNAME, email=cts.EMAIL, movil=cts.MOVIL)


@app.route('/welcome', methods=["POST"])
def welcome():
    if request.form.get("return") == 'return':
        return render_template("captive_portal.html", title=cts.COMPANY_NAME, first_name=cts.NAME, last_name=cts.LASTNAME, email=cts.EMAIL, movil=cts.MOVIL)
    if request.form.get("access") == 'access':
        save_info_db(cts.NAME, cts.LASTNAME, cts.EMAIL, cts.MOVIL)
        return render_template("welcome.html", title=cts.COMPANY_NAME, first_name=cts.NAME)


if __name__ == '__main__':
    app.run()
