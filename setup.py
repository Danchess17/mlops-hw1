from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        "cholesky_module",
        ["src/bindings.cpp", "src/cholesky.cpp"],
        include_dirs=["src"],
        cxx_std=17,
    ),
]

setup(
    name="cholesky_module",
    version="0.1.0",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
)