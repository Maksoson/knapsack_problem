class Item:
    def __init__(self, size, value):
        self.size = size
        self.value = value

# Решение = 01011111, стоимость = 44

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
    K = knapsack_size
    n = len(items)
    F = [[0] * (K + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for k in range(1, K + 1):
            if k >= items[i - 1].size:
                F[i][k] = max(
                    F[i - 1][k], F[i - 1][k - items[i - 1].size] + items[i - 1].value
                )
            else:
                F[i][k] = F[i - 1][k]

    selection = ""
    k = K
    for i in range(n, 0, -1):
        if F[i][k] != F[i - 1][k]:
            selection = "1" + selection
            k -= items[i - 1].size
        else:
            selection = "0" + selection
    print(f"Решение = {selection}, стоимость = {F[n][K]}")
