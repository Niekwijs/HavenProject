from flask import Flask
import mysql.connector
from flask_cors import CORS ##############

app = Flask(__name__)
cors = CORS(app)  ################


@app.route("/schip_aanmaken/<schipnaam>/<bootlengte>")
def hello_world(schipnaam, bootlengte):
    mydb = mysql.connector.connect(
    host="localhost",  #port erbij indien mac
    user="root",
    password="",
    database="havendb"
    )
    mycursor = mydb.cursor()
    print("hoi2")
    sql = "INSERT INTO sschip (naam, lengte) VALUES (%s, %s)"
    val = (schipnaam, bootlengte) 
    mycursor.execute(sql, val)

    mydb.commit()
    return "<p>Hello, World!</p>"


@app.route("/toon_alle_schepen")
def toon_alle_schepen():
    mydb = mysql.connector.connect(
    host="localhost",  #port erbij indien mac
    user="root",
    password="",
    database="havendb"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM sschip")

    myresult = mycursor.fetchall()
    print(myresult)
    keys = [i[0] for i in mycursor.description]

    data = [
        dict(zip(keys, row)) for row in myresult
    ]
    return data