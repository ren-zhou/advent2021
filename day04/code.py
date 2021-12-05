with open("data.txt") as f:
    data = f.read().split("\n\n")


nums = data[0].split(",")
boards = list(map(lambda s: s.split(), data[1:]))
def mark(board, num):
    try:
        board[board.index(num)] = '0'
    except:
        pass

def check(board):
   cols = [''.join(board[i::5]) for i in range(5)]
   rows = [''.join(board[i:i+5]) for i in range(0,25,5)]
   return '0'*5 in (cols + rows)



def time_of_win(board):
    for i, num in enumerate(nums):
        mark(board, num)
        if check(board):
            return i, sum([int(n) for n in board])*int(num)



# == crunched: 330 2-in-1 == 
import re
c,*b=open("data.txt").read().split("\n\n")
r=range
def t(b):
 i=0
 for n in c.split(","):
  b=re.sub(rf"\b{n}\b",z:=".01",b);d=b.split()
  if z*5 in[''.join(s) for s in[d[i::5] for i in r(5)]+[d[i:i+5] for i in r(0,25,5)]]:return i,int(sum(map(float,d)))*int(n)
  i+=1
print([e[1] for e in sorted(map(t,b))[::len(b)-1]])


