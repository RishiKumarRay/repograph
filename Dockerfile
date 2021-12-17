FROM python

WORKDIR /Repograph

COPY . .

RUN pip3 install flask && chmod +x docker-entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["./docker-entrypoint.sh"]