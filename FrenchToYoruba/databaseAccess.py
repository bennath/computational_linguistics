import sqlite3
import os

class DatabaseAccess:
    #conn = sqlite3.connect('french2Yor.db')

    def getWords(self):
        #BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        #db_path = os.path.join(BASE_DIR,"french2Yor.")
        conn = sqlite3.connect('french2Yor.db')
        #cursor = conn.execute("SHOW TABLES")
        cursor = conn.execute("SELECT French, Yoruba, pos  FROM frey")
        wordPos = {}
        wordMean = {}
        for row in cursor:
            wordPos[str(row[0]).lower()] = str(row[2])
            wordMean[str(row[0]).lower()] = str(row[1])
        print("Operation done successfully!!")
        conn.close()
        return wordMean,wordPos

    def addNewWord(self,word,meaning,pos,username,password):
        conn = sqlite3.connect('french2Yor.db')
        #cursor=conn.execute("show tables")
        cursor= conn.execute("SELECT user,pass FROM admin")
        usernameandpass = {}
        print(cursor)

        for row in cursor:
            usernameandpass[row[0]] = str(row[1])
        print(usernameandpass)
        if (usernameandpass[username] == password):
            conn.execute("INSERT INTO frey(French, Yoruba, pos) VALUES (?,?,?)",(word,meaning,pos))
            print(word+" inserted successfully!!!")
        else:
            raise NotAnAdmin("Not an Admin")
        conn.commit()
        conn.close()

class NotAnAdmin(RuntimeError):
    def __init__(self,arg):
        self.args = arg






if __name__ == '__main__':
    data = DatabaseAccess()
    print(data.getWords())
