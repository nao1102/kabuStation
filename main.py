import kabuStationApi as kabuApi
import sys

def main():
    sys.dont_write_bytecode = True
    token = kabuApi.generateToken()
    sonyBoard = kabuApi.board(1, 6758, token())
    margin = kabuApi.marginpremium(9433, token())


    print(token())

    print(sonyBoard(""))

    print(margin(""))


if __name__ == "__main__":
    main()