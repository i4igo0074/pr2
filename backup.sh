#!/bin/bash

# Путь к исходному каталогу
source_dir="/home/islambek/programming"

# Путь к каталогу для резервных копий
backup_dir="/home/islambek/backupcopies"

# Проверяем, существует ли исходный каталог
if [ ! -d "$source_dir" ]; then
    echo "Исходный каталог '$source_dir' не существует."
    exit 1
fi

# Проверяем, существует ли каталог для резервных копий, и создаем его, если необходимо
if [ ! -d "$backup_dir" ]; then
    mkdir -p "$backup_dir"
    echo "Каталог для резервных копий '$backup_dir' создан."
fi

# Копируем все файлы из исходного каталога в каталог для резервных копий
cp -r "$source_dir"/* "$backup_dir"

echo "Резервное копирование завершено."
