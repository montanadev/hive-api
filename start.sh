#!/bin/bash

cd /srv

# start the cups daemon
exec /usr/sbin/cupsd -f&

echo "waiting for cups to start"
while [ "$(nc -z 127.0.0.1 631; echo $?)" -gt 0 ] ; do
    echo "."
    sleep 0.01
done

# connect the printers
LOCAL_PRINTERS=$(lpinfo -v | grep 'DYMO' | awk '{print $2}')
for connection in $LOCAL_PRINTERS; do
    connection_name=$(echo $connection | cut -d '/' -f 4 | sed 's/\%20/\ /g; s/?.*//g')
    connection_name_nospace=$(echo $connection_name | sed 's/\ /_/g')
    connection_ppd=$(lpinfo -m | grep "$connection_name" | grep -ve '/' | head -n 1 | awk '{print $1}')
    lpadmin -p $connection_name_nospace -v $connection -P /usr/share/cups/model/$connection_ppd
    cupsenable $connection_name_nospace
    cupsaccept $connection_name_nospace
    lpoptions -d $connection_name_nospace
done

lpstat -d -t

# start the web app
poetry run gunicorn hive.wsgi:application --bind 0.0.0.0