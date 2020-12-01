FROM python:3

RUN apt-get update -y && \
 apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

CMD [ "python3", "app.py" ]

# FROM python:3
# RUN apk update
# RUN apk add −y pip3 build−essential
# COPY . .
# RUN pip3 install −r requirements.txt
# ENTRYPOINT ["python3"]
# CMD ["app.py"]

# FROM python:3-onbuild
# RUN pip install --upgrade pip 
# COPY . /usr/src/app
# CMD ["python3", "app.py"]

#FROM python:3.7
#
#RUN mkdir /backend-service
#
#WORKDIR /backend-service
#
#COPY requirements.txt /backend-service/requirements.txt
#
#RUN pip install --upgrade pip && \
#    pip install -r requirements.txt
#
#COPY . .
#
#CMD ["python3", "app.py"]