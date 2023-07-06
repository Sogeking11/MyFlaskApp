import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine
from pymongo import MongoClient

app = Flask(__name__)


myclient = MongoClient('mongodb://localhost:27017/',         
                username='root',
                password='root',
                authSource='admin')
mydb = myclient["coucou"]
mycol = mydb["collection"]

values = list(mycol.find())
print(values)
My_dict = {
    v['_id']:{
        'name':v['name'],
        'email':v['email']
        } for v in values
    }
print(My_dict)
db = MongoEngine()
db.init_app(app)


class User():
    name = db.StringField()
    email = db.StringField()
    def to_json(self):
        return My_dict

@app.route('/', methods=['GET'])
def query_records():
    name = x['name']
    user = User.objects(name=name).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(user.to_json())

@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(x)
    user = User(name=record['name'],
                email=record['email'])
    user.save()
    return jsonify(user.to_json())

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(x)
    user = User.objects(name=record['name']).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.update(email=record['email'])
    return jsonify(user.to_json())

@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    user = User.objects(name=record['name']).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.delete()
    return jsonify(user.to_json())

if __name__ == "__main__":
    app.run(debug=True)