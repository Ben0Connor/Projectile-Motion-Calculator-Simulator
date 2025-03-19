import tkinter as tk

window = tk.Tk()
window.title("Projectile Motion Calculator")
window.geometry("900x750")

hello = tk.Label(text="Projectile Motion Calculator")
hello.pack()

entryangle = tk.Entry()
entryangle.insert(0,"Enter Angle Here . . .")
entryangle.pack()

clearbutton = tk.Button(text="Calculate")
clearbutton.pack()

tk.mainloop()