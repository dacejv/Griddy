FROM python:3

WORKDIR /app/scrappy
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
RUN chmod 0644 main.py
RUN apt-get update
RUN apt-get -y install cron
RUN crontab -l | { cat; echo "* 1 * * 4 main.py"; } | crontab -

CMD cron
CMD [ "python3", "./main.py" ]


