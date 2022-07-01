FROM alpine

RUN apk update && \
    apk add python3 py3-pip curl && \
    pip3 install pyHoneygain

COPY honeygain-bot.py /bot/
COPY accounts.json /bot/accounts/

WORKDIR /bot

CMD ["python3","-u", "honeygain-bot.py"]
