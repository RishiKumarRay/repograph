FROM python

WORKDIR /Repograph

COPY . .

RUN pip3 install flask 

EXPOSE 5000

ENTRYPOINT ["./docker-entrypoint.sh"]