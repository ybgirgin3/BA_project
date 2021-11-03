from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

class HelloWorld(Resource):
    def get(self):
        return {"HelloWorld"}

api.add_resource(HelloWorld, "/helloworld")


if __name__ == '__main__':
    app.run(debug=True)
    
