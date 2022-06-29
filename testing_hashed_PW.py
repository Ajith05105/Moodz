import pymysql
import bcrypt

def login( username, password):  # ! Add comments
    # DB connection
    conn = pymysql.connect(host='localhost', port=3306,
                           user='root', passwd='Ajith@05', db='pythongui')
    cur = conn.cursor()
    cur.execute(
        "SELECT `password` FROM register WHERE `username`=%s", (username))
    result = cur.fetchone()
    #
    # Password checking
    if result is None:
        print("Incorrect username")

    elif result is not None and bcrypt.checkpw(bytes(password, 'utf-8'), bytes(result[0], 'utf-8')):
        print("logged in")

    else:
        print("incorrect password")

login('Ajith@05','Ajith@05')
