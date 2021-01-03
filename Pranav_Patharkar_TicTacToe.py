import random
import sys

print('Game Start!')
for i in range(0,2):
    print('     |     |   ')
    print('------------------')
print('     |     |   ')

dict1 = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
list1 = []
flag = 0
def player_move():
    global m
    m = int(input('Make your move:'))
    if m<1 or m>9 :
        global flag
        flag = 1
        print('Invalid move!')
    global list1
    for k in list1:
        if m == k:
                flag = 1
                print('Invalid move!')
                break
    else:
      dict1[m] = 'X'
      list1.append(m)

def CPU_move():
        c = random.randint(1,9)
        if dict1[c] == '':
            dict1[c] = 'O'
            list1.append(c)
            return 1
        else:
            return 5

def print_grid():
      for dict_key in range(1,3):
          if dict1[dict_key]== 'X' or dict1[dict_key]== 'O':
                print(' ',dict1[dict_key],' |',end='')
          else: print(' ',dict1[dict_key],' ','|',end='')
      print(' ',dict1[3])
      print('------------------')

      for dict_key in range(4,6):
          if dict1[dict_key]== 'X' or dict1[dict_key]== 'O':
                print(' ',dict1[dict_key],' |',end='')
          else: print(' ',dict1[dict_key],' ','|',end='')
      print(' ',dict1[6])
      print('------------------')

      for dict_key in range(7,9):
          if dict1[dict_key]== 'X' or dict1[dict_key]== 'O':
                print(' ',dict1[dict_key],' |',end='')
          else: print(' ',dict1[dict_key],' ','|',end='')
      print(' ',dict1[9])

def victory():
        won = 0
        if dict1[1] == dict1[2] == dict1[3] == 'X' or dict1[4] == dict1[5] == dict1[6] == 'X' or dict1[7] == dict1[8] == dict1[9] == 'X':
            print_grid()
            print('You Won !')
            won = 1
            return 1
        if dict1[1] == dict1[4] == dict1[7] == 'X' or dict1[2] == dict1[5] == dict1[8] == 'X' or dict1[3] == dict1[6] == dict1[9] == 'X':
            print_grid()
            print('You Won !')
            won = 1
            return 1
        if dict1[1] == dict1[5] == dict1[9] == 'X' or dict1[3] == dict1[5] == dict1[7] == 'X':
            print_grid()
            print('You Won !')
            won = 1
            return 1

        if dict1[1] == dict1[2] == dict1[3] == 'O' or dict1[4] == dict1[5] == dict1[6] == 'O' or dict1[7] == dict1[8] == dict1[9] == 'O':
            print('You Lost !')
            won = 1
            return 1
        if dict1[1] == dict1[4] == dict1[7] == 'O' or dict1[2] == dict1[5] == dict1[8] == 'O' or dict1[3] == dict1[6] == dict1[9] == 'O':
            print('You Lost !')
            won = 1
            return 1
        if dict1[1] == dict1[5] == dict1[9] == 'O' or dict1[3] == dict1[5] == dict1[7] == 'O':
            print('You Lost !')
            won = 1
            return 1
        if grid_not_full() != True and won == 0:
            print_grid()
            print('Draw !')
            return 1

def grid_not_full():
    for i in range(1,10):
        if dict1[i] == '':
            return True
        elif i == 9 and dict1[i] != '':
            return False
while grid_not_full() == True:
      player_move()
      if flag == 1: continue
      game_over = victory()
      if game_over == 1:
          break
      else:
          r =CPU_move()
          if r == 1:
              print_grid()
          elif r == 5:
              while True:
                  r = CPU_move()
                  if r != 5:
                      print_grid()
                      break
          game_over = victory()
          if game_over == 1:
              break