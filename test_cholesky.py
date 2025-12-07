import numpy as np

from cholesky_module import cholesky_decomposition
print("Модуль успешно импортирован!")


def test_cholesky(A, test_name):
    print(f"Тест: {test_name}")
    print("Матрица A:")
    print(np.array(A))
    
    L_custom = cholesky_decomposition(A)
    L_numpy = np.linalg.cholesky(A)
    
    print("\nРезультат нашей реализации:")
    print(np.array(L_custom))
    
    print("\nРезультат NumPy:")
    print(L_numpy)
    
    error = np.max(np.abs(np.array(L_custom) - L_numpy))
    print(f"\nМаксимальная разница: {error}")
    
    if error < 1e-10:
        print("ТЕСТ ПРОЙДЕН!")
        return True
    else:
        print("ТЕСТ НЕ ПРОЙДЕН!")
        return False


if __name__ == "__main__":
    print("Тестирование разложения Холецкого")
    
    results = []

    A1 = [[4]]
    results.append(test_cholesky(A1, "Матрица 1x1"))
    
    A2 = [[4, 2], 
          [2, 5]]
    results.append(test_cholesky(A2, "Матрица 2x2"))
    
    A3 = [[4, 12, -16],
          [12, 37, -43], 
          [-16, -43, 98]]
    results.append(test_cholesky(A3, "Матрица 3x3"))
    
    A4 = [[25, 15, -5, 0],
          [15, 18, 0, 0],
          [-5, 0, 11, 0],
          [0, 0, 0, 9]]
    results.append(test_cholesky(A4, "Матрица 4x4"))
    
    A5 = [[25, 15, -5, 0, 0],
          [15, 18, 0, 0, 0],
          [-5, 0, 11, 0, 0],
          [0, 0, 0, 9, 0],
          [0, 0, 0, 0, 16]]
    results.append(test_cholesky(A5, "Матрица 5x5"))

    A6 = [[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]]
    results.append(test_cholesky(A6, "Единичная матрица 3x3"))
    
    A7 = [[9, 0, 0],
          [0, 16, 0],
          [0, 0, 25]]
    results.append(test_cholesky(A7, "Диагональная матрица 3x3"))
    
    A8 = [[6, 3, 1],
           [3, 5, 2],
           [1, 2, 4]]
    results.append(test_cholesky(A8, "Плотная матрица 3x3"))

    A9 = [[10, 4, 2, 1],
          [4, 8, 3, 2],
          [2, 3, 7, 1],
          [1, 2, 1, 6]]
    results.append(test_cholesky(A9, "Плотная матрица 4x4"))
    
    A10 = [[16, 8, 4, 2, 1],
          [8, 15, 6, 3, 2],
          [4, 6, 14, 5, 3],
          [2, 3, 5, 13, 4],
          [1, 2, 3, 4, 12]]
    results.append(test_cholesky(A10, "Плотная матрица 5x5"))
    
    print("ИТОГИ ТЕСТИРОВАНИЯ:")
    print(f"Пройдено тестов: {sum(results)}/{len(results)}")
    

