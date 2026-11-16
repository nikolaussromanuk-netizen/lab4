MAX_CELLS = 7
POINTS = 25

items = {
    'r': {'survival': 25, 'cells': 3},   # Винтовка
    'p': {'survival': 15, 'cells': 2},   # Пистолет
    'a': {'survival': 15, 'cells': 2},   # Боекомплект
    'm': {'survival': 20, 'cells': 2},   # Аптечка
    #'i': {'survival': 5,  'cells': 1},   # Ингалятор
    'k': {'survival': 15, 'cells': 1},   # Нож
    'x': {'survival': 20, 'cells': 3},   # Топор
    't': {'survival': 25, 'cells': 1},   # Оберег
    'f': {'survival': 15, 'cells': 1},   # Фляжка
    'd': {'survival': 10, 'cells': 1},   # Антидот
    's': {'survival': 20, 'cells': 2},   # Еда
    'c': {'survival': 20, 'cells': 2},   # Арбалет
}


def gen_table_memo(items, cells=MAX_CELLS):
    table = [[0 for _ in range(cells)] for _ in range(len(items.keys()))]
    for row, item in enumerate(items.values()):
        price = item['survival']
        cell = item['cells']

        for col, cells_curr in enumerate(range(1, cells + 1)):
            if row == 0:
                if cell > cells_curr:
                    table[row][col] = 0
                else:
                    table[row][col] = price
                continue
            
            prev_price = table[row - 1][col]

            if cells_curr - cell > 0:
                res_price = price + table[row - 1][col - cell]


            elif cells_curr - cell == 0:
                res_price = price


            else:
                res_price = 0

            table[row][col] = max(prev_price, res_price)

    return table


def find_result(table):
    pass


if __name__ == "__main__":
    table = gen_table_memo(items)