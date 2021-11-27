#!/bin/python3




class TicTacToe:
    def __init__(self):
        self.board = [
                ["", "", ""],
                ["", "", ""],
                ["", "", ""],
                ]
        self.players = ["  🔴  ","  🔵  "]

    def add(self, row, column, player):
        player = self.players[player]
        self.board[row][column] = player



    def check_row(self):
        board = self.board
        players = self.players
        for row in board:
            for player in players:
                if "".join(row) == player*3:
                    return player

    def check_col(self):
        board = self.board
        players = self.players
        for column in range(2):
            col_string = ""
            for row in board:
                col_string += row[column]
            for player in players:
                if col_string == player*3:
                    return player



    
    def check_dia(self):
        pass

    def check_win(self):
        if self.check_row() != None:return self.check_row()
        elif self.check_col() != None:return self.check_col()
        elif self.check_dia() != None:return self.check_dia()

    def show(self):
        board = str(self.board)
        board = board.replace(" ","").replace("''"," ⚪ ").replace("],","]\n\n").replace("[","").replace("]","").replace(",","").replace("'","")
        print(board)



def main():
    game = TicTacToe()
    players = game.players
    player = players[0]
    while True:
        if player == players[0]:player = players[1]
        elif player == players[1]:player = players[0]


        game.show()
        i = input(f"\n{player}: ").split(",")
        row = int(i[0])
        col = int(i[1])
        game.add(row-1, col-1, players.index(player))
        print("\n\n")
        if game.check_win()!=None:print(game.check_win());exit()

        








if __name__=="__main__":
    main()
