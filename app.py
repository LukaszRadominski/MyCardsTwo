from flask import render_template, Flask

app = Flask(__name__)

@app.route('/mypage/me')
def warehouse():
    return render_template("card_name.html")

@app.route('/mypage/contact')  
def new_element():
    return render_template("card_contact.html")