
import tkinter as tk
from tkinter import messagebox

import matplotlib.pyplot as plt
import numpy as np


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
        try:
            velocity = float(self.entry_velocity.get())
            angle = float(self.entry_angle.get())

            if velocity <= 0:
                messagebox.showerror("Input Error", "Velocity must be greater than 0.")
                return

            if not (0 <= angle <= 90):
                messagebox.showerror("Input Error", "Angle must be between 0 and 90 degrees.")
                return

            print(f"Valid input: Velocity = {velocity}, Angle = {angle}")

            self.plot_trajectory(velocity, angle)

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values for velocity and angle")

    def plot_trajectory(self, velocity, angle):
        g = 9.81
        theta = np.radians(angle)

        time_of_flight = (2 * velocity * np.sin(theta)) / g
        max_height = (velocity**2 * np.sin(theta)**2) / (2 * g)
        range_x = (velocity**2 * np.sin(2 * theta)) / g  # Horizontal range

        t = np.linspace(0, time_of_flight, num=100)

        x = velocity * np.cos(theta) * t
        y = velocity * np.sin(theta) * t - (0.5 * g * t**2)

        x_max_fixed = 200
        y_max_fixed = 50

        plt.figure(figsize=(8, 5))
        plt.plot(x, y, label="Projectile Path", color="blue")

        plt.xlim(0, x_max_fixed)
        plt.ylim(0, y_max_fixed)

        plt.xticks(np.arange(0, x_max_fixed + 1, 50))
        plt.yticks(np.arange(0, y_max_fixed + 1, 10))

        plt.xlabel("Distance (m)")
        plt.ylabel("Height (m)")
        plt.title("Projectile Motion Trajectory")
        plt.legend()
        plt.grid(True)

        plt.show()
window = tk.Tk()
app = GUI(window)
window.mainloop()