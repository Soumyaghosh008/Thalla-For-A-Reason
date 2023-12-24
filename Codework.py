import tkinter as tk
from tkinter import messagebox
import pygame
def play_bgm(mp3):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.play()
def calculate_sum():
    try:
        input_text = entry.get()
        values = [1 if char.isalpha() else int(char) for char in input_text]
        total_sum = sum(values)
        if total_sum == 7:
            play_bgm("thalla.mp3")
          # Show "Thalla For A Reason" popup (optional)
            messagebox.showinfo("Thalla For A Reason", "Sum is equal to 7!")
        else:
            play_bgm("moye.mp3")
          # Show "Moye Moye" popup (optional)
            messagebox.showinfo("Moye Moye", "Sum is not equal to 7!")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values or alphabetic characters.")
app = tk.Tk()
app.title("Your Thalla Checker")
entry = tk.Entry(app,width=50, font=('Arial', 14))
entry.pack(pady=20)
button = tk.Button(app, text="Check Sum", command=calculate_sum, font=('Arial', 14))
button.pack()
app.mainloop()
