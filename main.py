from tkinter import Tk, Button, Label, Frame
import random

def next_turn(row, col):
    global player

    if buttons[row][col]['text'] == "" and not check_winner():
        # Place the player's mark on the button
        buttons[row][col]['text'] = player
        
        if check_winner():  # Check if there's a winner
            label.config(text=f"{player} wins!")
        elif empty_spaces() == False:  # Check if it's a tie
            label.config(text="Tie.")
        else:  # If the game is still ongoing, switch player
            player = players[1] if player == players[0] else players[0]
            label.config(text=f"{player}'s turn")

def check_winner():
    # Check rows, columns, and diagonals for a winner
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            highlight_winner(row, 0, row, 1, row, 2)
            return True
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            highlight_winner(0, col, 1, col, 2, col)
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        highlight_winner(0, 0, 1, 1, 2, 2)
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        highlight_winner(0, 2, 1, 1, 2, 0)
        return True
    return False

def highlight_winner(r1, c1, r2, c2, r3, c3):
    buttons[r1][c1].config(background='green')
    buttons[r2][c2].config(bg='green')
    buttons[r3][c3].config(bg='green')

def empty_spaces():
    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] == "":
                return True
    return False

def new_game():
    global player
    player = random.choice(players)
    label.config(text=f"{player}'s turn")

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text = "", bg = "red")

window = Tk()
window.title("Tic-Tac-Toe")

players = ["X", "O"]
player = random.choice(players)

label = Label(text = f"{player}'s turn", font=('consolas', 40))
label.pack(side = "top")

reset_button = Button(text = "Restart", font = ('consolas', 20), command = new_game)
reset_button.pack(side = "top")

frame = Frame(window)
frame.pack()

buttons = [[None,None,None],
           [None,None,None],
           [None,None,None]]

for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text = "", font=('consolas', 40), width = 5, height = 2,
                                   command = lambda row=row, col=col: next_turn(row,col))
        buttons[row][col].grid(row=row, column=col)


window.mainloop()
