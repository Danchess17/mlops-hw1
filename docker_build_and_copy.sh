#!/bin/bash
set -e

echo "=========================================="
echo "Сборка Docker образа и копирование wheel (scikit-build)"
echo "=========================================="

echo -e "\n[1/4] Сборка Docker образа..."
docker build -t cholesky-module-scikit .

echo -e "\n[2/4] Проверка wheel файла в контейнере..."
WHEEL_FILE=$(docker run --rm cholesky-module-scikit sh -c "ls dist/*.whl" | head -1 | xargs -n1 basename)
if [ -z "$WHEEL_FILE" ]; then
    echo "Wheel файл не найден в контейнере!"
    exit 1
fi
echo "Найден wheel: $WHEEL_FILE"

echo -e "\n[3/4] Копирование wheel файла на хост..."
mkdir -p dist
CONTAINER_ID=$(docker create cholesky-module-scikit)
docker cp $CONTAINER_ID:/app/dist/$WHEEL_FILE ./dist/
docker rm $CONTAINER_ID

echo "Wheel скопирован: dist/$WHEEL_FILE"

echo -e "\n[4/4] Запуск тестов в контейнере..."
docker run --rm cholesky-module-scikit

