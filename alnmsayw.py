import tkinter as tk
from PIL import Image, ImageTk
import math

def main():
    root = tk.Tk()
    root.title("الرسام النمساوي")

    
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    
    for angle in range(0, 360, 10):
        x = 200 + 150 * math.cos(math.radians(angle))
        y = 200 + 150 * math.sin(math.radians(angle))
        canvas.create_oval(x-2, y-2, x+2, y+2, fill="gray")

    
    image = Image.open("moon_image.jpg")  
    photo = ImageTk.PhotoImage(image)
    image_id = canvas.create_image(200, 200, image=photo)

    
    text = """
████╗░░░████████████╗
████║░░░████████████║
████║░░░████╔═══════╝
████║░░░████║░░░░░░░░
████████████████████╗
████████████████████║
╚═══════████╔═══████║
░░░░░░░░████║░░░████║
████████████║░░░████║
████████████║░░░████║
╚═══════════╝░░░╚═══╝
"""
    label = canvas.create_text(200, 200, text=text, font=("Arial", 12))

    
    move_text_under_dots(canvas, label, 200, 200)

    root.mainloop()

def move_text_under_dots(canvas, text_id, x, y):
    angle = 0
    while True:
        x_offset = 150 * math.cos(math.radians(angle))
        y_offset = 150 * math.sin(math.radians(angle))
        canvas.coords(text_id, x+x_offset, y+y_offset)
        angle += 1
        if angle >= 360:
            angle = 0
        canvas.update()
        canvas.after(10)

if __name__ == "__main__":
    main()
