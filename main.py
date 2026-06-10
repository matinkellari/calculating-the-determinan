def menu(choose = input("Please choose one:\n1. 2*2 Matris\n2. 3*3 Matris\nc. Cancel\nyour choice:")):
    return choose


def format_2(board = "[[{}  {}]\n[{}  {}]] "):
    matris = "ABCD"
    table = (f"\nNow we calculate the determinan of 2*2 matris. 2*2 matris:\n{board.format(*matris)}")
    return table


def format_3(board = "[[{}  {}  {}]\n[{}  {}  {}]\n[{}  {}  {}]] "):
    matris = "ABCDEFGHI"
    table = (f"\nNow we calculate the determinan of 3*3 matris. 3*3 matris:\n{board.format(*matris)}")
    return table


def get_numbers_2(count=1):
    numbers = []
    for prompt in range(65, 65+count):
        while True:
            number = input(f"enter the number in front of each letter\n{chr(prompt)}:")
            if number.isdigit():
                numbers.append(int(number))
                break
            else:
                print("Error: please enter number")
    return numbers


def get_numbers_3(count=1):
    numbers = []
    for prompt in range(65, 65+count):
        while True:
            number = input(f"enter the number in front of each letter\n{chr(prompt)}:")
            if number.isdigit():
                numbers.append(int(number))
                break
            else:
                print("Error: please enter number")
    return numbers


def determinan_2(matris: list[int]):
    determinan = (matris[0] * matris[3] - matris[1] * matris[2])
    return determinan


def determinan_3(matris: list[int]):
    determinan = (
        matris[0] * matris[4] * matris[8] 
        + matris[3] * matris[7] * matris[2] 
        + matris[1] * matris[5] * matris[6] 
        - matris[2] * matris[4] * matris[6]
        + matris[1] * matris[3] * matris[8]
        + matris[5] * matris[7] * matris[0]
        )
    return determinan


def users_matris_2(parts, board = "[[{}  {}]\n[{}  {}]] "):
    form = (f"{parts[0]}{parts[1]}{parts[2]}{parts[3]}")
    matris = board.format(*form)
    return matris


def users_matris_3(parts, board = "[[{}  {}  {}]\n[{}  {}  {}]\n[{}  {}  {}]] "):
    form = (f"{parts[0]}{parts[1]}{parts[2]}{parts[3]}{parts[4]}{parts[5]}{parts[6]}{parts[7]}{parts[8]}")
    matris = board.format(*form)
    return matris


def main():
    menue = menu()
    print(menue)
    while True:
        match menue:
            case "1":
                board = format_2()
                print(board)
                matris = get_numbers_2(4)
                its_matris = users_matris_2(matris)
                print(f"\nyour matris:\n{its_matris}")
                result = determinan_2(matris)
                print(f"\ndeterminan : {result}")
                break
            case "2":
                board = format_3()
                print(board)
                matris = get_numbers_3(9)
                its_matris = users_matris_3(matris)
                print(f"\nyour matris:\n{its_matris}")
                result = determinan_3(matris)
                print(f"\ndeterminan : {result}")
                break
            case "c":
                break
            case _:
                print("Error: please choose a number in menu.")


if __name__ == "__main__":
    main()