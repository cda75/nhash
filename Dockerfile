FROM alpine:latest

RUN apk add --update git python py-pip rrdtool rrdcollect py-rrd tzdata lighttpd \
    && pip install requests \
    && rm -rf /var/cache/apk/* \
    && cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime

WORKDIR /usr/local
RUN git clone https://github.com/cda75/nhash 
#RUN touch crontab.tmp \
    && echo '*/1 * * * * /usr/bin/python /usr/local/nhash/nhash.py > /dev/null' > crontab.tmp \
    && crontab crontab.tmp \
    && rm -rf crontab.tmp

RUN echo "It works!!" > /var/www/localhost/htdocs/index.html
RUN mkdir -p /etc/lighttpd/lighttpd.conf.d/ && \
    touch /etc/lighttpd/lighttpd.conf.d/empty && \
    echo 'include_shell "cat /etc/lighttpd/lighttpd.conf.d/*"' >> /etc/lighttpd/lighttpd.conf

RUN chown -R lighttpd:www-data /var/www
RUN chmod -R 750 /var/www
EXPOSE 80

CMD [ "/usr/sbin/lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf" ]

