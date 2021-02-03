from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open('users.json') as f:
    users = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}


# Initialize the database

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/selllist', methods=['GET', 'PUT']) 
def selllist():
    if request.method == 'PUT':
        userfound = False
        data = request.json
        for user in users:
            if(user['username'] == data['username']):
                userfound = True
                if(user['password'] == data['password']):
                    # return jsonify('good password')
                    user['selllist'] = data['selllist']
                    return jsonify(data['selllist'])
                    break
                else:
                    return jsonify('bad password')
                    break
        if(not userfound):
            return jsonify('user not found')
    if request.method == 'GET':
        data = request.json
        for user in users:
            if(user['username'] == data['username']):
                userfound = True
                return jsonify(user['selllist'])
                break
        if(not userfound):
            return jsonify('user not found')


@app.route('/buylist', methods=['GET', 'PUT']) 
def buylist():
    if request.method == 'PUT':
        userfound = False
        data = request.json
        for user in users:
            if(user['username'] == data['username']):
                userfound = True
                if(user['password'] == data['password']):
                    # return jsonify('good password')
                    user['buylist'] = data['buylist']
                    return jsonify(data['buylist'])
                    break
                else:
                    return jsonify('bad password')
                    break
        if(not userfound):
            return jsonify('user not found')
    if request.method == 'GET':
        data = request.json
        for user in users:
            if(user['username'] == data['username']):
                userfound = True
                return jsonify(user['buylist'])
                break
        if(not userfound):
            return jsonify('user not found')


@app.route('/executebuyorder', methods=['POST']) 
def buylist():
    if request.method == 'POST':
        userfound = False
        data = request.json
        for user in users:
            if(user['username'] == data['username']):
                userfound = True
                if(user['password'] == data['password']):
                    # return jsonify('good password')
                    user['buylist'] = data['buylist']
                    return jsonify(data['buylist'])
                    break
                else:
                    return jsonify('bad password')
                    break
        if(not userfound):
            return jsonify('user not found')


@app.route('/senditems', methods=['POST']) 
def senditems():
    if request.method == 'POST':
        userfound = False
        data = request.json
        for user in users:
            if(user['username'] == data['username']):
                userfound = True
                if(user['password'] == data['password']):
                    # return jsonify('good password')
                    user['buylist'] = data['buylist']
                    return jsonify(data['buylist'])
                    break
                else:
                    return jsonify('bad password')
                    break
        if(not userfound):
            return jsonify('user not found')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
