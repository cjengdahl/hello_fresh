FROM python:3.8-slim-buster
WORKDIR /app
RUN pip3 install flask==2.0.2
COPY . .
ENV FLASK_APP=hello_fresh
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=3000"]