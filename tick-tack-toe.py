def printBoard(board):
    print(board['top-L'], '|', board['top-M'] + '|', board['top-R'])
    print('--+--+--')
    print(board['middle-L'], '|', board['middle-M'] + '|', board['middle-R'])
    print('--+--+--')
    print(board['bottom-L'], '|', board['bottom-M'] + '|', board['bottom-R'])

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'middle-L': ' ', 'middle-M': ' ', 'middle-R': ' ',
            'bottom-L': ' ', 'bottom-M': ' ', 'bottom-R': ' '}

printBoard(theBoard)

