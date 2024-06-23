import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random


def load_image(file_path, size):
    img = Image.open(file_path)
    img = img.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)


def determine_winner(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    result = ''
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = 'You win!'
    else:
        result = 'You lose!'
    
    messagebox.showinfo("Result", f"You chose {user_choice}.\nComputer chose {computer_choice}.\n{result}")


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("800x600")


bg_image = Image.open("img21.jpeg.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=bg_image.width, height=bg_image.height)
canvas.pack(fill="both", expand=True)


canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)


label = tk.Label(root, text="Choose your move:", font=("Arial", 16), bg="#f0f0f0")
label_window = canvas.create_window(400, 50, window=label)


rock_img = load_image('thumb.png', (100, 100))
paper_img = load_image('paper.png', (100, 100))
scissors_img = load_image('scissor.png', (100, 100))


frame = tk.Frame(root, bg="#9b59b6")
frame_window = canvas.create_window(400, 200, window=frame)

rock_btn = tk.Button(frame, image=rock_img, command=lambda: determine_winner('rock'))
rock_btn.grid(row=0, column=0, padx=20)

paper_btn = tk.Button(frame, image=paper_img, command=lambda: determine_winner('paper'))
paper_btn.grid(row=0, column=1, padx=20)

scissors_btn = tk.Button(frame, image=scissors_img, command=lambda: determine_winner('scissors'))
scissors_btn.grid(row=0, column=2, padx=20)


root.mainloop()
