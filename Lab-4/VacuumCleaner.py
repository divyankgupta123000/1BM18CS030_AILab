def clean(floor):
    for row in range(len(floor)):
#         print('Floor {} : '.format(row + 1))
        for col in range(len(floor[0])):
            print('[{}][{}] : {}'.format(row, col, floor[row][col]))
            if floor[row][col]:
                floor[row][col] = 0
                print_floor(floor)
                print('Cleaned ')
            else: print('Already Cleaned ')
            print()
        print()

def print_floor(floor): # row, col represent the current vacuum cleaner position
    for i in range(len(floor)):
        for j in range(len(floor[0])):
            print(floor[i][j], end = ' ')
        print()

def main():
    print("Enter no. of rows")
    m = int(input())
    print("Enter no.of columns")
    n = int(input())
    floor = []
    for i in range(0, m):
        a = list(map(int, input().split(" ")))
        floor.append(a)
    print()
    clean(floor)

main()

'''
Output

Enter no. of rows
3
Enter no.of columns
4

1 0 0 1
0 0 0 1
0 1 0 0
[0][0] : 1
0 0 0 1 
0 0 0 1 
0 1 0 0 
Cleaned 
[0][1] : 0
Already Cleaned 
[0][2] : 0
Already Cleaned 
[0][3] : 1
0 0 0 0 
0 0 0 1 
0 1 0 0 
Cleaned 
[1][0] : 0
Already Cleaned 
[1][1] : 0
Already Cleaned 
[1][2] : 0
Already Cleaned 
[1][3] : 1
0 0 0 0 
0 0 0 0 
0 1 0 0 
Cleaned 
[2][0] : 0
Already Cleaned 
[2][1] : 1
0 0 0 0 
0 0 0 0 
0 0 0 0 
Cleaned 
[2][2] : 0
Already Cleaned 
[2][3] : 0
Already Cleaned 
'''
