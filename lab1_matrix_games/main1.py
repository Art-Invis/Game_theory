def analyze_matrix(matrix, name="Matrix"):
    print(f"--- {name} ---")
    
    row_mins = [min(row) for row in matrix]
    alpha_lower = max(row_mins)
    
    maximin_strategies = [i + 1 for i, val in enumerate(row_mins) if val == alpha_lower]
    
    cols = list(zip(*matrix))
    col_maxs = [max(col) for col in cols]
    alpha_upper = min(col_maxs)
    
    minimax_strategies = [j + 1 for j, val in enumerate(col_maxs) if val == alpha_upper]
    
    print(f"Нижня ціна гри (максимін): {alpha_lower}")
    print(f"Верхня ціна гри (мінімакс): {alpha_upper}")
    print(f"Максимінна стратегія (Гравець 1): рядок {maximin_strategies}")
    print(f"Мінімаксна стратегія (Гравець 2): стовпець {minimax_strategies}")
    
    # Пошук сідлових точок
    saddle_points = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == row_mins[i] and matrix[i][j] == col_maxs[j]:
                saddle_points.append((i + 1, j + 1))
                
    if alpha_lower == alpha_upper:
        print(f"Сідлові точки (рядок, стовпець): {saddle_points}")
        print(f"Чиста ціна гри: {alpha_lower}\n")
    else:
        print("Сідлових точок немає. Оптимальне рішення в чистих стратегіях відсутнє.\n")

# --- 1. Матриці з кількома сідловими точками ---
A1 = [
    [3, 3, 5, 4],
    [2, 2, -1, 4],
    [1, 0, -2, 3]
]
analyze_matrix(A1, "Матриця 1 (>1 сідлової точки)")

A2 = [
    [4, 1, 1, 2],
    [0, -3, -3, -1],
    [2, 1, 1, -2]
]
analyze_matrix(A2, "Матриця 2 (>1 сідлової точки)")

# --- 2. Матриці з однією сідловою точкою ---
A3 = [
    [5, 0, 2, -1],
    [3, 2, 4, 1],
    [-2, -4, 0, -3]
]
analyze_matrix(A3, "Матриця 3 (1 сідлова точка)")

A4 = [
    [0, 1, 2, 3],
    [-1, -2, -3, -4],
    [-2, 0, -1, 2]
]
analyze_matrix(A4, "Матриця 4 (1 сідлова точка)")

# --- 3. Матриці без сідлових точок ---
A5 = [
    [5, -2, 3, 0],
    [-1, 4, -3, 1],
    [0, 1, 2, -4]
]
analyze_matrix(A5, "Матриця 5 (без сідлових точок)")

A6 = [
    [4, 0, 1, 3],
    [-3, 5, -2, -1],
    [2, -4, 5, 2]
]
analyze_matrix(A6, "Матриця 6 (без сідлових точок)")
