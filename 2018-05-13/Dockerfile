FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y samba

RUN sed -i -e '$ a \
        [public]\n \
        path = /home/public \n \
        browseable = yes \n \
        writable = yes \n \
        guest ok = yes \n \
    ' /etc/samba/smb.conf && \
    mkdir /home/public

CMD [ "bash", "-c", "nmbd -D && smbd -F </dev/null"]
