# Варіант 1 (Pure Python)
def analyze_matrix(matrix, name="Matrix"):
    print(f"--- {name} ---")
    
    print("Вхідна матриця:")
    for row in matrix:
        print("  " + "  ".join(f"{val:3}" for val in row))
    
    row_mins = [min(row) for row in matrix]
    alpha_lower = max(row_mins)
    
    maximin_strategies = [i + 1 for i, val in enumerate(row_mins) if val ==  alpha_lower]
    
    cols = list(zip(*matrix))
    col_maxs = [max(col) for col in cols]
    alpha_upper = min(col_maxs)
    
    minimax_strategies = [j + 1 for j, val in enumerate(col_maxs) if val == alpha_upper]
    
    print(f"Нижня ціна гри (максимін): {alpha_lower}")
    print(f"Верхня ціна гри (мінімакс): {alpha_upper}")
    print(f"Максимінна стратегія (Гравець 1): рядок {maximin_strategies}")
    print(f"Мінімаксна стратегія (Гравець 2): стовпець {minimax_strategies}")
    
    saddle_points = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == row_mins[i] and matrix[i][j] == col_maxs[j]:
                saddle_points.append((i + 1, j + 1)) 
    if alpha_lower == alpha_upper:
        print(f"Сідлові точки (рядок, стовпець): {saddle_points}")
        print(f"Чиста ціна гри: {alpha_lower}")
        print("Оптимальні розв'язки гри:")
        for pt in saddle_points:
            print(f" -> Гравець 1 обирає стратегію {pt[0]}, Гравець 2 обирає стратегію {pt[1]}")
        print("\n")
    else:
        print("Сідлових точок немає. Оптимальне рішення в чистих стратегіях відсутнє.\n")

# 1. Матриця з кількома сідловими точками
A1 = [
    [3, 3, 5, 4],
    [2, 2, -1, 4],
    [1, 0, -2, 3]
]
analyze_matrix(A1, "Матриця 1 (>1 сідлової точки)")

# 2. Матриця з однією сідловою точкою 
A2 = [
    [5, 0, 2, -1],
    [3, 2, 4, 1],
    [-2, -4, 0, -3]
]
analyze_matrix(A2, "Матриця 2 (1 сідлова точка)")

# 3. Матриця без сідлових точок
A3 = [
    [5, -2, 3, 0],
    [-1, 4, -3, 1],
    [0, 1, 2, -4]
]
analyze_matrix(A3, "Матриця 3 (без сідлових точок)")


# Варіант 2 (Numpy)
import numpy as np

def analyze_matrix_numpy(matrix, name="Matrix"):
    print(f"--- {name} (NumPy) ---")
    mat = np.array(matrix)

    print("Вхідна матриця:")
    print(mat)

    row_mins = np.min(mat, axis=1)
    col_maxs = np.max(mat, axis=0)
    
    alpha_lower = np.max(row_mins)
    alpha_upper = np.min(col_maxs)
    
    maximin_strategies = np.where(row_mins == alpha_lower)[0] + 1
    minimax_strategies = np.where(col_maxs == alpha_upper)[0] + 1
    
    print(f"Нижня ціна гри (максимін): {alpha_lower}")
    print(f"Верхня ціна гри (мінімакс): {alpha_upper}")
    print(f"Максимінна стратегія (Гравець 1): рядок {maximin_strategies.tolist()}")
    print(f"Мінімаксна стратегія (Гравець 2): стовпець {minimax_strategies.tolist()}")
    
    # Перевірка наявності сідлових точок
    if alpha_lower == alpha_upper:
        saddle_points = []
        for r in maximin_strategies:
            for c in minimax_strategies:
                if mat[r-1, c-1] == alpha_lower:
                    saddle_points.append((r, c))
                    
        print(f"Сідлові точки (рядок, стовпець): {saddle_points}")
        print(f"Чиста ціна гри: {alpha_lower}")
        print("Оптимальні розв'язки гри:")
        for pt in saddle_points:
            print(f" -> Гравець 1 обирає стратегію {pt[0]}, Гравець 2 обирає стратегію {pt[1]}")
        print("\n")
    else:
        print("Сідлових точок немає. Оптимальне рішення в чистих стратегіях відсутнє.\n")

# Масив матриць для перевірки
matrices = [
    ([[3, 3, 5, 4], [2, 2, -1, 4], [1, 0, -2, 3]], "Матриця 1 (>1 сідлової точки)"),
    ([[5, 0, 2, -1], [3, 2, 4, 1], [-2, -4, 0, -3]], "Матриця 2 (1 сідлова точка)"),
    ([[5, -2, 3, 0], [-1, 4, -3, 1], [0, 1, 2, -4]], "Матриця 3 (без сідлових точок)"),
]
for mat, name in matrices:
    analyze_matrix_numpy(mat, name)
