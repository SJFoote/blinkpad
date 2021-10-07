from flask import Flask, render_template, request, redirect, jsonify
from flask.helpers import url_for
from flask_pymongo import PyMongo
import json
from bson import json_util
from flask_cors import CORS

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
CORS(app)

app.config["MONGO_URI"] = "mongodb+srv://admin:drm8c5DszR7bipP@cluster0.akrc2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongo = PyMongo(app)

accessUsers = mongo.db.users

@app.route("/", methods=['GET','PUT'])          # The "@" decorator associates this route with the function immediately following
def index():
    # context = accessUsers.find()
    context = accessUsers.find_one({},{'_id': 0, 'Likes': 1})

    # return jsonify({
    #     'data' : context
    # })
    return render_template('index.html', likes=context)


# @app.route("/", methods=['PUT'])
# def update():
#     # update = accessUsers.update_one({"_id": request.}, {"$set": {'Likes': ""}})
        
#     return jsonify()

@app.route("/likes", methods=['GET', 'PUT'])
def likes():
    bun1 = accessUsers.find_one({"id":1})
    usrID1 = bun1['_id']
    bun2 = accessUsers.find_one({"id":2})
    usrID2 = bun2['_id']
    bun3 = accessUsers.find_one({"id":3})
    usrID3 = bun3['_id']
    bun4 = accessUsers.find_one({"id":4})
    usrID4 = bun4['_id']

    if request.method == "PUT":
        bun1 = request.get_json()
        bun2 = request.get_json()
        bun3 = request.get_json()
        bun4 = request.get_json()
        # print(bun1)
        # print(bun2)
        if bun1:
            if bun1 != None or bun1 != "":
                result = accessUsers.update_one(
                    {'_id': usrID1},
                    {
                            "$set":{
                                    "Likes": bun1
                                    },
                            "$currentDate":{"lastModified":True}
                            }
                    )
            return print("Data updated with id",result)
        if bun2:
            if bun2 != None or bun2 != "":
                result2 = accessUsers.update_one(
                {'_id': usrID2},
                {
                        "$set":{
                                "Likes": bun2
                                },
                        "$currentDate":{"lastModified":True}
                        }
                )
            return print("Data updated with id",result2)
        if bun3:
            if bun3 != None or bun3 != "":
                result3 = accessUsers.update_one(
                {'_id': usrID3},
                {
                        "$set":{
                                "Likes": bun3
                                },
                        "$currentDate":{"lastModified":True}
                        }
                )
            return print("Data updated with id",result3)
        if bun4:
            if bun4 != None or bun4 != "":
                result4 = accessUsers.update_one(
                {'_id': usrID4},
                {
                        "$set":{
                                "Likes": bun4
                                },
                        "$currentDate":{"lastModified":True}
                        }
                )
            return print("Data updated with id",result4)

    else:
        return render_template('index.html', bun1=bun1, bun2=bun2, bun3=bun3, bun4=bun4)
    
# @app.route("/create")
# def create():
#     new_bun_1 = {"id" : 1, "name" : "Wicket", "likes" : 0}
#     new_bun_2 = {"id" : 2, "name" : "Chewie", "likes" : 0}
#     new_bun_3 = {"id" : 3, "name" : "Ghost", "likes" : 0}
#     new_bun_4 = {"id" : 4, "name" : "Pinto", "likes" : 0}
#     new_bun_5 = {"id" : 4, "name" : "Bungie", "likes" : 0}
#     new_buns = [new_bun_1, new_bun_2, new_bun_3, new_bun_4, new_bun_5,]
#     accessUsers.insert_many(new_buns)
#     # for i in range(1, 5, 1):
#     #     print(new_buns[i]["Name"] + "has" + ["Likes"], "Created Successfully")
#     return redirect("/")



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
