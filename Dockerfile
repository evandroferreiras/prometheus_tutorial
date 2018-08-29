FROM python:3.4-alpine
ADD ./app /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "main.py"]

