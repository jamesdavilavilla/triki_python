import tkinter as tk
from tkinter import messagebox

#variables del juego
player = 'X'
game_over = False


#funcion para verificar el ganador

def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '':
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return True
    return False

def button_click(row,col):
    global player, game_over
    if buttons[row][col]['text'] == '' and not game_over:
        buttons[row][col]['text'] = player
        buttons[row][col]['bg'] = 'lightblue' if player == 'X' else 'lightgreen'
        if check_winner():
            messagebox.showinfo("Ganador", f"¡El jugador {player} ha ganado!")
            game_over = True
        elif all(button['text'] != '' for row in buttons for button in row):
            messagebox.showinfo("Empate", "¡El juego ha terminado en empate!")
            game_over = True
        else:
            player = 'O' if player == 'X' else 'X'

def reset_game():
    global player, game_over
    player = 'X'
    game_over = False
    for row in buttons:
        for button in row:
            button['text'] = ''
            button['bg'] = 'SystemButtonFace'

# Crear la ventana principal
root = tk.Tk()
root.title("Juego triki")
root.geometry("400x450")
root.configure(bg='lightgray')
frame = tk.Frame(root, bg='lightgray')
frame.place(relx=0.5, rely=0.5, anchor='center')

buttons = [[tk.Button(frame, text='', font=('Arial', 24), width=5, height=2,
                      command=lambda r=i, c=j: button_click(r, c)) for j in range(3)] for i in range(3)]


for row in range(3):
    for col in range(3):
        buttons[row][col].grid(row=row, column=col, padx=5, pady=5 )

reset_button = tk.Button(root, text='Reiniciar Juego', font=('Arial', 16), command=reset_game)
reset_button.place(relx=0.5, rely=0.9, anchor='center')
root.mainloop()