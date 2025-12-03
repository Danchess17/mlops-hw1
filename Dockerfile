FROM python:3.10-slim

WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    ninja-build \
    && rm -rf /var/lib/apt/lists/*

# Копируем файлы проекта
COPY . .

# Очищаем старые сборки (если есть)
RUN rm -rf dist/ build/ *.egg-info/ 2>/dev/null || true

# Устанавливаем зависимости Python
RUN pip install build pybind11 scikit-build-core

# Собираем wheel
RUN python -m build --wheel

# Устанавливаем наш пакет (только что собранный для Python 3.10)
RUN sh -c 'pip install dist/cholesky_module-0.1.0-cp310*.whl'

# Устанавливаем зависимости для тестов
RUN pip install numpy

# Запускаем тесты
CMD ["python", "test_cholesky.py"]

