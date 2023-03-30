FROM python:3.11

# SET workdir
WORKDIR /core

COPY . /core

# install requirements
RUN pip install --no-cache-dir -r requirements.txt

# get environment variables from .env
ENV $(cat .env | xargs)

# expose on port 5000
EXPOSE 5000

# python app.py
CMD [ "python", "app.py" ]