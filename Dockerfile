FROM python:3.12.3-alpine3.19
COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "src.main:application"]
