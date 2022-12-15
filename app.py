from flask import Flask,jsonify,request  

# the constructor of this class Flask that we imported takes the name of the current module, stored in __name__ as an argument
#and the variable app is now a Flaskobject

app = Flask(__name__)

tasks = [
    {
        'Contact': "99876444456",
        'Name': 'Raju',
        'id': 1, 
        'done': False
    },
    {
        'Contact': "9876543222",
        'Name': 'Rahul',
        'id': 2, 
        'done': False
    }
]



#api to get data of tasks
@app.route("/")
def getTask():
    return jsonify({
       "data":tasks
    })

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })



 #to run 
if (__name__ == "__main__"):
    app.run(debug=True)
