get_bin = lambda x, n: format(x, "b").zfill(n)


class Item:
    def __init__(self, size, value):
        self.size = size
        self.value = value


items = [
    Item(9, 13),
    Item(5, 4),
    Item(3, 11),
    Item(4, 7),
    Item(1, 9),
]
knapsack_size = 14

if __name__ == "__main__":
    best_selection = "0" * len(items)
    best_value = 0
    for base in range(2 ** len(items) - 1, -1, -1):
        selection = get_bin(base, len(items))
        size = 0
        value = 0
        for index, i in enumerate(selection):
            if i == "1":
                size += items[index].size
                value += items[index].value

        if size < knapsack_size and value >= best_value:
            best_value = value
            best_selection = selection
    print(f"Решение = {best_selection}, стоимость = {best_value}")
