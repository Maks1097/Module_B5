def geep():
    print("Игра крестики-нолики")
    print("формат ввода: x y")
    print("x - номер строки")
    print("y - номер столбца")
geep()


ang = [[" "] * 3 for i in range(3)]


def show():
    print(f"  0 1 2")
    for i in range(3):
        row = " ".join(ang[i])
        print(f"{i} {row}")
show()


def ask():
    while True:
        cords = input("Ваш ход: ").split()

        if len(cords) != 2:
            print("Введите 2 координаты!")
            continue
        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа!")
            continue
        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапозона!")
            continue

        if ang[x][y] != " ":
            print("Клетка занята!")
            continue

        return x, y
ask()


def check_win():
    win_cords = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)),((0, 2), (1, 2), (2, 2)),
                 ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))]
    for cord in win_cords:

        a = cord[0]
        b = cord[1]
        c = cord[2]

        if ang[a[0]][a[1]] == ang[b[0]][b[1]] == ang[c[0]][c[1]] != " ":
            print(f"Победил {ang[a[0]][a[1]]}!")
            return True
    return False
check_win()


num = 0
while True:
    num += 1
    show()
    if num % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = ask()
    if num % 2 == 1:
        ang[x][y] = "X"
    else:
        ang[x][y] = "O"

    if check_win():
        break
    if num == 9:
        print("Ничья")
        break