FROM python:latest

WORKDIR /app/src

# COPY requirements.txt ./
COPY main.py ./

# RUN pip installation --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]