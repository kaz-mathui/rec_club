from typing import Dict


def knapsack(target: int, items: Dict) -> int:
    """
    Return the total value of a subset of items that has the maximum value
    within the target constraint. Each item be used only once.
    O(target * len(items)) time and space complexity.
    """
    wt = []
    val = []
    for k, v in items.items():
        wt.append(k)
        val.append(v)
    length = len(items)
    table = [[0] * (target + 1) for x in range(length + 1)]
    for i in range(1, length + 1):
        for j in range(1, target + 1):
            curr = val[i - 1]
            if wt[i - 1] <= j:
                table[i][j] = max(curr + table[i - 1]
                                  [j - wt[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]
    return table[length][target]


weight_to_value = {5: 60, 3: 50, 4: 70, 2: 30}
print(knapsack(5, weight_to_value))  # 80
print(knapsack(10, weight_to_value))  # 150
