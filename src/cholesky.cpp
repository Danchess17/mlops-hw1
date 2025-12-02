#include "cholesky.h"
#include <vector>
#include <cmath>
#include <stdexcept>

std::vector<std::vector<double>> cholesky_decomposition(const std::vector<std::vector<double>>& A) {
    int n = A.size();
    
    if (n == 0 || A[0].size() != n) {
        throw std::invalid_argument("Matrix must be square");
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (std::abs(A[i][j] - A[j][i]) > 1e-10) {
                throw std::invalid_argument("Matrix must be symmetric");
            }
        }
    }
    
    std::vector<std::vector<double>> L(n, std::vector<double>(n, 0.0));
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            double sum = 0.0;
            
            if (j == i) {
                for (int k = 0; k < j; k++) {
                    sum += L[j][k] * L[j][k];
                }
                if (A[j][j] - sum <= 0) {
                    throw std::invalid_argument("Matrix must be positive definite");
                }
                L[j][j] = std::sqrt(A[j][j] - sum);
            } else {
                for (int k = 0; k < j; k++) {
                    sum += L[i][k] * L[j][k];
                }
                L[i][j] = (A[i][j] - sum) / L[j][j];
            }
        }
    }
    
    return L;
}
