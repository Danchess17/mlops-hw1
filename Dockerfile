FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    ninja-build \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN rm -rf dist/ build/ *.egg-info/ 2>/dev/null || true

RUN pip install build pybind11 scikit-build-core

RUN python -m build --wheel

RUN sh -c 'pip install dist/cholesky_module-0.1.0-cp310*.whl'

RUN pip install numpy pytest

CMD ["pytest", "test_cholesky.py", "-v"]

