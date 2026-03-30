import tkinter as tk
from tkinter import messagebox
import random

win = tk.Tk()
win.title("Tic Tac Toe - Single Player")
win.geometry("300x330")

current_player = "X"
board = [""] * 9
buttons = []

def check_winner(b):
    combos = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b2,c in combos:
        if b[a] == b[b2] == b[c] != "":
            return b[a]
    if "" not in b:
        return "Tie"
    return None

# Simple AI using win/block logic
def computer_move():
    global board, current_player

    # 1. Try to win
    for i in range(9):
        if board[i] == "":
            temp = board[:]
            temp[i] = "O"
            if check_winner(temp) == "O":
                make_move(i, "O")
                return

    # 2. Block player from winning
    for i in range(9):
        if board[i] == "":
            temp = board[:]
            temp[i] = "X"
            if check_winner(temp) == "X":
                make_move(i, "O")
                return

    # 3. Else pick random free cell
    free = [i for i in range(9) if board[i] == ""]
    if free:
        make_move(random.choice(free), "O")

def make_move(i, player):
    global current_player

    if board[i] == "":
        board[i] = player
        buttons[i].config(text=player)

        winner = check_winner(board)
        if winner:
            if winner == "Tie":
                messagebox.showinfo("Result", "It's a Tie!")
            else:
                messagebox.showinfo("Winner", f"{winner} wins!")
            reset_board()
            return

        current_player = "X" if player == "O" else "O"

        # If it's computer's turn, let it move
        if current_player == "O":
            win.after(300, computer_move)  # small delay for realism

def on_click(i):
    if current_player == "X":
        make_move(i, "X")

def reset_board():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for btn in buttons:
        btn.config(text="")

# Create UI buttons
for i in range(9):
    btn = tk.Button(win, text="", font=("Arial", 24), width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

reset_btn = tk.Button(win, text="Reset", font=("Arial", 14),
                      command=reset_board)
reset_btn.grid(row=3, column=0, columnspan=3, sticky="nsew")

win.mainloop()
