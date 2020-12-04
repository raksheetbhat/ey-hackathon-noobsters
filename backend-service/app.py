import json

from flask import Flask
app = Flask(__name__)

data = [{

        "job_id": 1,
        "job_name": "BCG Analysis",
        "start_date": "2020-11-25",
        "end_date": "",
        "goal": "competitive_analysis",
        "data_sources": ["twitter","website","news","youtube"],
        "domain": "supply chain",
        "company_name": "BCG",
        "company_url": "www.bcg.com",
        "status": "submitted"
    }, {
        "job_id": 2,
        "job_name": "Trends in Supply chain",
        "start_date": "2020-11-25",
        "end_date": "",
        "goal": "emerging_trends",
        "data_sources": ["twitter","search","news","youtube"],
        "domain": "Blockchain",
        "status": "submitted"
    }
]


@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'


@app.route('/fetch_new_tasks')
def new_tasks():
    return json.dumps(data)


@app.route('/put_new_tasks')
def update_tasks():
    return json.dumps(data)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')


#Import the flask module
# from flask import Flask

# #Create a Flask constructor. It takes name of the current module as the argument
# app = Flask(__name__)

# #Create a route decorator to tell the application, which URL should be called for the #described function and define the function

# @app.route('/')
# def tutorialspoint():
# return "Welcome to TutorialsPoint"

# #Create the main driver function
# if __name__ == '__main__':
# #call the run method
# app.run(debug=True,host='0.0.0.0')