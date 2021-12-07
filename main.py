from flask import Flask,redirect,request
from flask.helpers import url_for
from flask.templating import render_template
from flask.wrappers import Request
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask_mail import Mail, Message



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' #4 /'dan sonra kodu indirdiğiniz yerin içerisinde olan DB path'i girilecektir.
db = SQLAlchemy(app)

@app.route('/')
def index():

    infos = adres.query.all()
    return render_template('index.html', infos = infos)

@app.route('/ormAdd')
def ormAdd():

    infos = adres.query.all()
    return render_template('ormAdd.html', infos = infos)

@app.route('/add', methods= ["POST"])
def addInformation():
    id        = request.form.get("id")
    name      = request.form.get("name")
    surname   = request.form.get("surname")
    addr      = request.form.get("addr")
    city      = request.form.get("city")
    town      = request.form.get("town")
    c_code    = request.form.get("c_code")

    newInfo = adres(id=id, name = name, surname=surname, addr=addr,city=city,town=town,c_code=c_code)
    db.session.add(newInfo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/ormlist')
def ormlist():
   infos = adres.query.all()
   return render_template("ormList.html", infos = infos)

conn = sqlite3.connect('adresdata.db')
print ("Opened Database succesfully")

#conn.execute('CREATE TABLE nonOrm (id INTEGER , name TEXT, surname TEXT, addr TEXT, city TEXT, town TEXT, cCode INTEGER)')
print ("Tabled created succesfully")
conn.close()

@app.route('/enternew')
def new_inf():
    return render_template('non.html')

@app.route('/non', methods= ["POST","GET"])
def non_orm():
   if request.method == 'POST':
      try:
         id = request.form['id']
         name = request.form['name']
         surname = request.form['surname']
         addr = request.form['addr']
         city = request.form['city']
         town = request.form['town']
         cCode = request.form['cCode']

         
         with sqlite3.connect("adresdata.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO nonOrm (id,name,surname,addr,city,town,cCode) VALUES (?,?,?,?,?,?,?)",(id,name,surname,addr,city,town,cCode) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         conn.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/nonlist')
def list():
   con = sqlite3.connect("adresdata.db")
   con.row_factory = sqlite3.Row
   
   cur = con.cursor()
   cur.execute("select * from nonOrm")
   
   rows = cur.fetchall(); 
   return render_template("list.html",rows = rows)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '' #Tırnakların arasına E-mail adresinizi girmeniz gerekmektedir.
app.config['MAIL_PASSWORD'] = '' #Tırnakların arasına Password'unuzu girmeniz gerekmektedir.
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
#Mail yollamanız için döküman üzerindeki mail gönderme bölümünü okuyup, gerekenleri yapmanız gerekmektedir.

mail = Mail(app)
@app.route('/mail-gonder')
def mailgonder():
    try:
        msg = Message("Merhaba Şelale Park",
          sender="", #Tırnakların arasına Mail'i gönderecek E-mail adresini girmeniz gerekmektedir.
          recipients=[""]) # Tırnakların arasına göndereceğiniz mail adresini girmeniz gerekmektedir.
        msg.body = "Merhaba!\nSG pls"           
        mail.send(msg)
        return 'Mail başarıyla gönderildi!'
    except Exception as e:
        return(str(e))


class adres(db.Model):
   id      = db.Column('id', db.Integer, primary_key = True)
   name    = db.Column(db.String(100))
   surname = db.Column(db.String(50))  
   addr    = db.Column(db.String(200))
   city    = db.Column(db.String(25))
   town    = db.Column(db.String(25))
   c_code  = db.Column(db.Integer)




if __name__ == "__main__":
    app.run(debug=True)