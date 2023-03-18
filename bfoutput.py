"""

Класс для красивого вывода в консоль

"""


class BfOutput:

    @staticmethod
    def print_tables(a: list[tuple]):
        for i in range(len(a)):
            print(f" {i + 1}. {a[i][0]}")

    @staticmethod
    def get_list_of_sizes(a: list[tuple]):
        if len(a) == 0:
            return []

        size = [0 for i in range(len(a[0]))]
        for i in a:
            for j in range(len(i)):
                size[j] = max(size[j], len(str(i[j])))

        for i in range(len(size)):
            size[i] += 2

        return size

    @staticmethod
    def print_begining(a: list[int]):
        for i in a:
            print('+', end='')
            print('-' * i, end='')
        print('+')

    @staticmethod
    def print_empty_row(a: list[int]):
        for i in a:
            print('|', end='')
            print(' ' * i, end='')
        print('|')

    @staticmethod
    def get_element(a: str, size: int):
        ans = [' ' for i in range(size)]
        for i in range(len(a)):
            ans[1 + i] = a[i]
        return ''.join(ans)

    @staticmethod
    def print_row(a: tuple, size: list[int]):
        ans = []
        for i in range(len(a)):
            ans += '|'
            ans += BfOutput.get_element(str(a[i]), size[i])
        ans += '|'
        print(''.join(ans))

    @staticmethod
    def print_table(a: list[tuple]):
        if len(a) == 0:
            return

        size = BfOutput.get_list_of_sizes(a)
        BfOutput.print_begining(size)
        BfOutput.print_row(a[0], size)
        BfOutput.print_begining(size)

        for i in range(1, min(100, len(a))):
            BfOutput.print_row(a[i], size)
        if len(a) > 100:
            print('...')
        if len(a) == 1:
            BfOutput.print_empty_row(size)

        BfOutput.print_begining(size)

