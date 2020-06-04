from flask import Flask,render_template,request,jsonify
from flask_restless import APIManager
import requests
import json
import yaml

from flask_mysqldb import MySQL

app = Flask(__name__)

#Configure db
db = yaml.load(open('db.y   aml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)
@app.route('/api/fetch-news',methods=['GET'])
def returnAll():
    response = requests.get("http://newsapi.org/v2/everything?q=bitcoin&from=2020-05-03&sortBy=publishedAt&apiKey=934c2ad2b0a24accb937481c14df9da6")

    if response.ok:
         userDetails = response.json()
        #  data = json.loads()
         print(userDetails)    
# def index():
    # if request.method == 'POST':
    #     #Fetch user Details
    #     userDetails = request.form
    #     name = userDetails['name']
    #     email = userDetails['email']
    #     cur = mysql.connection.cursor()
    #     cur.execute("INSERT INTO users(name, email) VALUES(%s,%s)",(name,email))
    #     mysql.connection.commit()
    #     cur.close()
    #     return 'success'
    # return render_template('index.html')

if __name__ == '__main__':
    app.run(debug= True)