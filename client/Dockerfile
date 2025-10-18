FROM python:3.9


WORKDIR /client-app


COPY ./requirements.txt /client-app/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /client-app/requirements.txt


COPY ./ /client-app/


CMD ["python", "main.py"]