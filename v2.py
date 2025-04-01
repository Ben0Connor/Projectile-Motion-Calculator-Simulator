import tkinter as tk

import tkinter as tk

class GUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Projectile Motion Calculator")
        self.window.geometry("900x750")

        self.main_frame = tk.Frame(self.window, padx=20, pady=20)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')  # Center the frame

        self.hello = tk.Label(self.main_frame, text="Projectile Motion Calculator", font=("Arial", 16, "bold"))
        self.hello.grid(row=0, column=0, pady=10, columnspan=2)

        self.instructions = tk.Label(self.main_frame, text="Enter the initial velocity and launch angle, then click 'Calculate'.", font=("Arial", 12))
        self.instructions.grid(row=1, column=0, pady=10, columnspan=2)

        self.velocity_label = tk.Label(self.main_frame, text="Enter Velocity (m/s):")
        self.velocity_label.grid(row=2, column=0, pady=5)

        self.entry_velocity = tk.Entry(self.main_frame, width=10)
        self.entry_velocity.grid(row=3, column=0, pady=5)

        self.angle_label = tk.Label(self.main_frame, text="Enter Angle (0-90 degrees):")
        self.angle_label.grid(row=2, column=1, pady=5)

        self.entry_angle = tk.Entry(self.main_frame, width=10)
        self.entry_angle.grid(row=3, column=1, pady=5)

        self.calculate_button = tk.Button(self.main_frame, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=4, column=0, pady=10)

        self.clear_button = tk.Button(self.main_frame, text="Clear", command=self.clear)
        self.clear_button.grid(row=4, column=1, pady=10)

    def clear(self):
        self.entry_velocity.delete(0, tk.END)
        self.entry_angle.delete(0, tk.END)

    def calculate(self):
        pass

window = tk.Tk()
app = GUI(window)
window.mainloop()