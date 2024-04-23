#!/bin/bash

echo "Введите имя файла: "
read filename

cp "$filename" ./copied_file.txt

mv "$filename" ./moved_file.txt

echo "Файл $filename скопирован и перемещен."
