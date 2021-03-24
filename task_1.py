def task(array: str) -> int:
    return list(array).index('0')


def task1(array: str) -> int:
    return list(map(int, list(array))).index(0)


print(task("111111111111111111111111100000000"))
print(task1("111111111111111111111111100000000"))

#  Какова сложность вашего алгоритма?
#  Сложность O(N) - линейная зависимость
