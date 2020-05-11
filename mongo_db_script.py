import pymongo
from pymongo import MongoClient
from fastapi import FastAPI

cluster = MongoClient("mongodb+srv://user_avito:<***>@cluster0-ftcef.\
                        mongodb.net/test?retryWrites=true&w=majority")
db = cluster['secret']
collection = db['secret']

app = FastAPI()


@app.post("/generate")
async def generate(secret:str,secret_key:str):
    """Generate your secret
    input:
    secret-type:string, some text which will you need save
    key-type:string, codeword"""
    post = {'key':secret_key,'secret':secret}
    collection.insert_one(post)
    results = collection.find({'key': secret_key})
    for result in results:
        collection.create_index(result['key'],expireAfterSeconds=259200)
    return post['key']

@app.get("/secrets/{secret_key}")
async def get_secret(secret_key):
    """Return your text
    input:
    secret_key:string"""
    results = collection.find({'key':secret_key})
    for result in results:
        return result['secret']

