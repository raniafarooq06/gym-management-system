from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
 return render_template('home.html')
@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")
@app.route('/membership')
def membership():
 return render_template('membership.html')
@app.route('/services')
def services():
 return render_template('services.html')
@app.route('/gallery')
def gallery():
 return render_template('gallery.html')
@app.route('/contactus')
def contactus():
 return render_template('contactus.html')
@app.route('/login')
def login():
 return render_template('login.html')
@app.route('/registration')
def registration():
 return render_template('registration.html')
if __name__ == '__main__':
 app.run(debug=True)
