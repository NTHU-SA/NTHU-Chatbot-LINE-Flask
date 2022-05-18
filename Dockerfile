FROM python:3.7-buster

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt
ENV GINIP=${GINIP}

EXPOSE 5000

COPY . .

# CMD ["python", "run.py"]
CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]