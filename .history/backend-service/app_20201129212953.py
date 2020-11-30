# From flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world:
#     return 'Hey, we have Flask in a Docker container!'


# if __name == '__main__':
#     app.run(debug=True, host='0.0.0.0')

#Import the flask module
from flask import Flask

#Create a Flask constructor. It takes name of the current module as the argument
app = Flask(__name__)

#Create a route decorator to tell the application, which URL should be called for the #described function and define the function

@app.route('/')
def tutorialspoint():
return "Welcome to TutorialsPoint"

#Create the main driver function
if __name__ == '__main__':
#call the run method
app.run(debug=True,host='0.0.0.0')