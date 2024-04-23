#!/bin/bash

while true; do
    echo "Загрузка процессора:"
    top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1"%"}'
    echo "Использование памяти:"
    free -m | awk 'NR==2{printf "%.2f%%\n", $3*100/$2}'
    echo "Использование дискового пространства:"
    df -h | grep "/dev/" | awk '{print $5}'
    sleep 5
done
