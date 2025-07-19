#Base Image
FROM python:3.9

#WorkDir
WORKDIR /app

#Copy
COPY . /app

#Run
RUN pip install -r requirements.txt

#Port
EXPOSE 5000

#Command
CMD ["python","./app.py"]