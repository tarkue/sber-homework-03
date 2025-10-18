FROM python:3.9


WORKDIR /server-app


COPY ./requirements.txt /server-app/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /server-app/requirements.txt


COPY ./ /server-app/


CMD ["python", "main.py"]