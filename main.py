from flask import Flask, render_template, request, session, redirect
from backend_check.constants import Constants as cts
from backend_check.check_input_errors import user_input_errors
from backend_check.operations import save_info_db


app = Flask(__name__)


@app.route('/')
def captive_portal():
    # print session request
    # session["client_ip"] = request.args.get('client_ip')
    # session["client_mac"] = request.args.get('client_mac')
    # session["grant_url"] = request.args.get('base_grant_url')
    # session["Node_mac"] = request.args.get('node_mac')
    # session["user_continue_url"] = request.args.get('user_continue_url')
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

    if request.form.get("continue") == "continue":
        redirect_url = 'https://www.google.com'
        return redirect(redirect_url, code=302)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
