import numpy as np

ITEMS = [
    ["Нож", "н", 1, 15],
    ["Оберег", "о", 1, 25],
    ["Фляжка", "ф", 1, 15],
    ["Аптечка", "а", 2, 20],
    ["Боекомплект", "б", 2, 15],
    ["Пистолет", "п", 2, 15],
    ["Еда", "к", 2, 20],
    ["Арбалет", "р", 2, 20],
    ["Винтовка", "в", 3, 25],
    ["Топор", "т", 3, 20]
]

MANDATORY_ITEMS = [
    ["Ингалятор", "и", 1, 5],
    ["Антидот", "д", 1, 10]
]

N = len(ITEMS)
TOTAL_VALUE = sum([ITEMS[i][3] for i in range(len(ITEMS))])
INF = np.inf


def solve(dp, cells): 
    for item_id in range(N + 1):
        for space in range(cells + 1):
            if item_id == 0 or space == 0:
                dp[item_id][space] = 0
            elif ITEMS[item_id - 1][2] <= space:
                dp[item_id][space] = max(
                    ITEMS[item_id - 1][3] + dp[item_id - 1][space - ITEMS[item_id - 1][2]],
                    dp[item_id - 1][space]
                )
            else:
                dp[item_id][space] = dp[item_id - 1][space]
    
    return dp[item_id][cells]


def getItems(dp, space, result):
    included_items = []
    for item_id in range(N, 0, -1):
        if result <= 0:
           return included_items
        if result == dp[item_id - 1][space]:
           continue
        else:
           included_items.append(ITEMS[item_id - 1])
           result -= ITEMS[item_id - 1][3]
           space -= ITEMS[item_id - 1][2]
    return included_items


def print_matrix(size, items, extra):
    if extra: items.append(MANDATORY_ITEMS[extra])
    matrix = [["" for _ in range(size[1])] for _ in range(size[0])]
    for i in range(size[0]):
        for j in range(items[i][2]):
            matrix[i][j] = items[i][1]
    items = items[size[0]:]
    for j in range(size[1] - 1, -1, -1):
        for i in range(size[0] - 1, -1, -1):
            if(not len(items)): break
            if matrix[i][j] == "":
                for k in range(i, i + items[i][2]):
                    matrix[k][j] = items[0][1]
                items = items[1:]
    print(np.matrix(matrix))


def main():
    sick = int(input("""
Any sickness?
Нет (0)
Астма (1)
Заражение (2)
"""))
    survival_points = int(input("Survival points: ")) 
    cells_x = int(input("Cells x: "))
    cells_y = int(input("Cells y: "))
    cells = cells_x * cells_y
	
    if sick == 1:
        survival_points += MANDATORY_ITEMS[sick - 1][3] - MANDATORY_ITEMS[sick][3]
        cells -= MANDATORY_ITEMS[sick - 1][2]
    elif sick == 2:
        survival_points += MANDATORY_ITEMS[sick - 1][3] - MANDATORY_ITEMS[sick - 2][3]
        cells -= MANDATORY_ITEMS[sick - 1][2]
    else:
        survival_points -= MANDATORY_ITEMS[sick][3] - MANDATORY_ITEMS[sick + 1][3]
	
    dp = np.zeros((N + 1, cells + 1), dtype=int)
    result = solve(dp, cells)
    included_items = getItems(dp, cells, result)
    final_survival_points = result * 2 - TOTAL_VALUE + survival_points
    if final_survival_points > 0:
        print("\nSurvive with:", final_survival_points)
        print_matrix((cells_x, cells_y), included_items, sick - 1)
    else:
        print("\nDoes not survive")
    return

if __name__ == "__main__":
    main()

