import openpyxl
from collections import deque

def read_excel_matrix(file_path):
    wb = openpyxl.load_workbook('Поле игры.xlsx')
    sheet = wb.active
    matrix = []
    for row in sheet.iter_rows(values_only=True):
        matrix.append(list(row))
    #print("\nНачальная матрица:")
    #for row in matrix:
        #print(row)
    return matrix

def wave_algorithm(matrix, start, end):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    wave_matrix = [[-1 for _ in range(cols)] for _ in range(rows)]
    wave_matrix[start[0]][start[1]] = 0
    queue = deque([start])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if matrix[nx][ny] == 0 and wave_matrix[nx][ny] == -1:
                    wave_matrix[nx][ny] = wave_matrix[x][y] + 1
                    queue.append((nx, ny))
                    if (nx, ny) == end:
                        queue = deque()
                        break

    #print("\nВолновая матрица:")
    #for row in wave_matrix:
        #print(" ".join(f"{val:3}" if val != -1 else " -1" for val in row))
    #print()

    if wave_matrix[end[0]][end[1]] == -1:
        return None

    path = []
    current = end
    path.append(current)

    while current != start:
        x, y = current
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if wave_matrix[nx][ny] == wave_matrix[x][y] - 1:
                    current = (nx, ny)
                    path.append(current)
                    break

    path.reverse()
    return path

excel_file = "Поле игры.xlsx"
print("Начальная точка")
start_point = (int(input('Введите номер строки: ')) - 1, int(input('Введите номер столбца: ')) - 1)
print("Конечная точка")
end_point = (int(input('Введите номер строки: ')) - 1, int(input('Введите номер столбца: ')) - 1)
#print(start_point, end_point)

matrix = read_excel_matrix(excel_file)
path = wave_algorithm(matrix, start_point, end_point)

print("Кратчайший путь найден. Длина пути:", len(path) - 1)
print("Координаты пути:", path)

if None:
    print("Путь не найден. Возможно, он заблокирован.")