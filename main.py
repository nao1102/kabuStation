from attestation.generateToken import generateToken
from infomation.board import board

token=generateToken()
sonyBoard=board(1, 6758, token())

print(token())

print(sonyBoard("BisCategory"))