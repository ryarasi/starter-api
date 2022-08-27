FROM python:3.8-slim

COPY ./requirements.txt /requirements.txt
COPY ./start.sh /start.sh
RUN chmod +x /start.sh
# create root directory for our project in the container
RUN mkdir /api
# COPY ./scripts /scripts
WORKDIR /api

# Copy the current directory contents into the container at /shuddhi
ADD . /api/

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /requirements.txt

CMD ["./start.sh"]

