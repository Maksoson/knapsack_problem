class Item:
    def __init__(self, size, value):
        self.size = size
        self.value = value

items = [
    Item(5, 3),

    Item(1, 2),

    Item(6, 9),

    Item(4, 7),
    Item(2, 5),
    Item(3, 11),
    Item(2, 5),
    Item(2, 14),
]

knapsack_size = 14

if __name__ == "__main__":
    sorted_items = sorted(items, key=lambda x: x.value / x.size, reverse=True)
    rel_value = [i.value / i.size for i in sorted_items]
    selected = []
    value = 0
    for index, i in enumerate(rel_value):
        item = sorted_items[index]
        if item.size <= knapsack_size:
            knapsack_size -= item.size
            value += item.value
            selected.append(items.index(item))

    selection = ""
    for i in range(len(items)):
        if i in selected:
            selection += "1"
        else:
            selection += "0"
    print(f"Решение = {selection}, стоимость = {value}")
