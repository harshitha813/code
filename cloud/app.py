from flask import Flask, render_template, request,session

app = Flask(__name__)
app.secret_key ='a'
def showall():
    sql= "SELECT * from LOGIN"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The username is : ",  dictionary["USERNAME"])
        print("The Password is : ",  dictionary["PASSWORD"])
        dictionary = ibm_db.fetch_both(stmt)
        
def getdetails(username,password):
    sql= "select * from LOGIN where username='{}' and password='{}'".format(username,password)
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
       print("The username is : ",  dictionary["USERNAME"])
        print("The Password is : ",  dictionary["PASSWORD"])
        dictionary = ibm_db.fetch_both(stmt)
        
def insertdb(conn,username,password):
    sql= "INSERT into USER VALUES('{}','{}','{}','{}','{}','{}','{}')".format(username,password)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))
    
    
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud","PORT": 32286 SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=nmb64903;PWD=PGE9ynL5hzFRvf7i",'','')
print(conn)
print("connection successful...")

@app.route('/')
def index():
    return render_template('registration.html')

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        
        #inp=[name,email,contact,address,role,branch,password]
        insertdb(conn,email,password)
        return render_template('login.html')
        

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['pwd']
        sql= "select * from USER where username='{}' and password='{}'".format(username,password)
        stmt = ibm_db.exec_immediate(conn, sql)
        userdetails = ibm_db.fetch_both(stmt)
        print(userdetails)
        if userdetails:
            session['register'] =userdetails["EMAIL"]
            return render_template('userprofile.html',username=userdetails["USERNAME"],password=userdetails["PASSWORD"])
        else:
            msg = "Incorrect Username id or Password"
            return render_template("login.html", msg=msg)
    return render_template('login.html')


if __name__ =='__main__':
    app.run( debug = True)
