FROM python:3.8
WORKDIR /app

COPY . .

RUN apt-get update
RUN apt-get install pip -y
RUN apt-get install nosetests -y
RUN pip install -r 'requirements.txt'
    
CMD ["python", "main.py"]

EXPOSE 3000
