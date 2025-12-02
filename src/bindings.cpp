#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "cholesky.h"

namespace py = pybind11;

PYBIND11_MODULE(cholesky_module, m) {
    m.doc() = "Cholesky decomposition module";
    
    m.def("cholesky_decomposition", &cholesky_decomposition, 
          "Perform Cholesky decomposition of a symmetric positive definite matrix",
          py::arg("A"));
}