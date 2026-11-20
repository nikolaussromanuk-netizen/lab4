MAX_CELLS = 8
POINTS = 25

items = {
    'r': {'survival': 25, 'cells': 3},   # Винтовка
    'p': {'survival': 15, 'cells': 2},   # Пистолет
    'a': {'survival': 15, 'cells': 2},   # Боекомплект
    'm': {'survival': 20, 'cells': 2},   # Аптечка
    'i': {'survival': 5,  'cells': 1},   # Ингалятор
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


def re_table(table, items, start_points, max_cells):
    names = list(items.keys())
    n = len(names)
    ans = []
    score = start_points

    w = max_cells - 1
    for i in range(n-1, 0, -1):
        name = names[i]
        item = items[name]
        survival = item['survival']
        cells = item['cells']

        if cells <= w + 1 and table[i][w] != table[i - 1][w]:
            ans.append(name)
            score += survival
            w -= cells
        else:
            score -= survival

    return ans, score


def output(items, ans):
    temp = []
    for i in ans:
        #print(f"{i} : {items[i]['cells']}")
        temp.append([items[i]['cells'], i])
    
    temp = sorted(temp)[::-1]
    w = 4

    inv = []
    row = []

    for count, item in temp:
        if w - count >= 0:
            w -= count
            for _ in range(count):
                row.append(item)
        else:
            w = 4
            w -= count
            inv.append(row)
            row = [item for _ in range(count)]

    inv.append(row)

    for a in inv:
        for b in range(len(a)):
            print(f"[{a[b]}]", end="")
            if b < len(a) - 1:
                print(',', end="")
            else:
                print()


def solve(cells=MAX_CELLS):
    global items

    temp = items['d']

    cells -= items['d']['cells']
    del items['d']

    table = gen_table_memo(items, cells)

    ans, score = re_table(table, items, POINTS, cells)

    ans.append('d')
    items['d'] = temp

    print(score)
    output(items, ans)


if __name__ == "__main__":
    solve()