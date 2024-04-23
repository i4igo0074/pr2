#!/bin/bash


echo "Введите имя папки: "
read foldername


mkdir "$foldername"


echo "Это тестовый файл." > "$foldername/test.txt"

echo "Папка $foldername и файл test.txt созданы."
