from pymongo import MongoClient


CONNECTION_STRING = "mongodb+srv://v911-dev:DNGAdPz8OENi9HIR69bXQIaPs9ciWXEVU7n8G0uby9MxN59ZzOF3u52Z0paWhgJB6u0GVbN2gwNHZNONGSCcRQ@develop-qa-cluster.jm1lw.mongodb.net/v911-dev-db?retryWrites=true&w=majority&directConnection=false"

def get_database(table:str = 'users'):
    # Is by default retriving to users table
    # Create a connection using MongoClient.
   client = MongoClient(CONNECTION_STRING)
   return client['v911-dev-db'][table]


def is_administrator(user_id:dict = None):
    # get "user_id" from browser local storage and search that from the mongodb databse
    # get  user data from the db using the "user_id"
    # get the is_adin flag fromt he user data
    user_data = get_database().find_one({'sub':user_id['Username']})
    is_admin = bool(user_data['is_admin'])
    return is_admin