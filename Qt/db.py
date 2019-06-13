import sqlite3

class DBHandler:
    def __init__(self,DBName="db.sqlite"):
        self.connect = sqlite3.connect(DBName)

    def setup(self):
        self.connect.execute('CREATE TABLE users ('
                             'name text'
                             ',phone integer'
                             ',id integer primary key autoincrement'
                             ',password text)')

        self.connect.execute('create table locations ('
                             'id integer primary key autoincrement '
                             ',user_id'
                             ',lat integer'
                             ',lon integer)')
    def insertUser(selfself,name,phone,username,password):
        insertIn = 'insert into users(name ,phone,username,password) values (?,?,?,?)'
        val = (name,phone,username,password)
        selfself.connect.execute(insertIn,val)
        selfself.connect.commit()

    def insertLoc(self,user_id,lat,lon):
        insertIn = 'insert into locations (user_id,lat,lon)'
        val = (user_id,lat,lon)
        self.connect.execute(insertIn,val)
        self.connect.commit()

    def find_ID(self,userName,password):
        insertIn = 'select id from users where(userName,password) = (?,?)'
        val = (userName,password)
        cursor = self.connect.cursor()
        cursor.execute(insertIn,val)
        output = cursor.fetchone()
        return output

    def readUser(self,user_ID):
        insertIn = 'select name,phone , username , password from users where id = (?)'
        val = (user_ID,)
        cursor = self.connect.cursor()
        cursor.execute(insertIn,val)