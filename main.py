from attestation.generateToken import generateToken
from infomation.board import board
from infomation.marginpremium import marginpremium

token = generateToken()
sonyBoard = board(1, 6758, token())
margin = marginpremium(9433, token())


print(token())

print(sonyBoard(""))

print(margin(""))
