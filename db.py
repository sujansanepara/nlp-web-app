import json
import os

class Database:

    def __init__(self):
        if not os.path.exists("db.json"):
            with open("db.json","w") as f:
                json.dump({},f)

    def insert(self,name,email,password):

        with open('db.json','r') as rf:
            database = json.load(rf)

        if email in database:
            return 0
        else:
            database[email] = [name,password]
            with open('db.json','w') as wf:
                json.dump(database,wf)
            return 1

    def search(self,email,password):

        with open('db.json','r') as rf:
            database = json.load(rf)
            if email in database:
                if database[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0



# d=Database()
# d.add_data('sujan','sujan@gmail.com',"1234")