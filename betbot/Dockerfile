FROM python:3
ENV DISCORD_TOKEN=$DISCORD_TOKEN
COPY . /app
RUN pip install -r /app/requirements.txt
CMD python /app/src/bot.py
