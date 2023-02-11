import configparser

def main():
    token = generateToken()
    sonyBoard = board(1, 6758, token())
    margin = marginpremium(9433, token())


    print(token())

    print(sonyBoard(""))

    print(margin(""))


if __name__ == "__main__":
    main()