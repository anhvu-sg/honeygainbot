FROM alpine

RUN apk update && \
    apk add --no-cache python3 py3-pip && \
    pip3 install pyHoneygain schedule && \
    rm -rf /var/cache/apk/*

COPY honeygain-bot.py /bot/
COPY accounts.json /bot/accounts/

WORKDIR /bot

CMD ["python3","-u", "honeygain-bot.py"]
