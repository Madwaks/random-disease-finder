FROM python:3.7

RUN mkdir /home/dev && mkdir /home/dev/code
WORKDIR /home/dev/code

COPY . .
RUN pip install --upgrade pip 

RUN pip install -r /home/dev/code/app/requirements.txt

CMD ["python", "app/Front/front.py"]