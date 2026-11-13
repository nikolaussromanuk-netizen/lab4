MAX_CELLS = 4

items = {
    'a': {'price': 700, 'cells': 3},
    'b': {'price': 300, 'cells': 1},
    'c': {'price': 500, 'cells': 2},
    'd': {'price': 550, 'cells': 2}
}


def gen_table_memo(items, cells=MAX_CELLS):
    table = [[0 for _ in range(cells)] for _ in range(len(items.keys()))]
    for row, item in enumerate(items.values()):
        price = item['price']
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

    print(table)



if __name__ == "__main__":
    gen_table_memo(items)