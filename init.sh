#!/bin/sh
mkdir -p /usr/local/nhash
cp nhash.py /usr/local/nhash
echo "*/1 * * * * /usr/bin/python /usr/local/nhash/nhash.py > /dev/null" > /tmp/crontab.tmp
crontab /tmp/crontab.tmp
rm -f /tmp/crontab.tmp 
docker volume create --name=nhash-data
docker build -t nhash . 
docker run -itd -p 80:80 -v nhash-data:/usr/local/nhash --name nhash nhash
