import json


def write_data(data, task_id, type, source):
    with open('/opt/airflow/data/'+str(task_id)+'/'+type+'/'+source+'.json', 'w+') as file:
        data = json.dumps(data)
        file.write(data)