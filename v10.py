# Import necessary libraries
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

# Define the GUI class
class GUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Projectile Motion Calculator")
        self.window.geometry("1000x750")

        # Create the main frame
        self.main_frame = tk.Frame(self.window, padx=20, pady=20)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Title and instructions
        self.hello = tk.Label(self.main_frame, text="Projectile Motion Calculator", font=("Arial", 16, "bold"))
        self.hello.grid(row=0, column=0, pady=10, columnspan=4)

        self.instructions = tk.Label(self.main_frame, text="Enter the initial velocity, angle, and gravity settings.", font=("Arial", 12))
        self.instructions.grid(row=1, column=0, pady=10, columnspan=4)

        # Velocity input
        self.velocity_label = tk.Label(self.main_frame, text="Enter Velocity (m/s):")
        self.velocity_label.grid(row=2, column=0, pady=5)
        self.entry_velocity = tk.Entry(self.main_frame, width=10)
        self.entry_velocity.grid(row=3, column=0, pady=5)

        # Angle input
        self.angle_label = tk.Label(self.main_frame, text="Enter Angle (0-90 degrees):")
        self.angle_label.grid(row=2, column=1, pady=5)
        self.entry_angle = tk.Entry(self.main_frame, width=10)
        self.entry_angle.grid(row=3, column=1, pady=5)

        # Gravity selection
        self.gravity_option_label = tk.Label(self.main_frame, text="Select Gravity:")
        self.gravity_option_label.grid(row=2, column=2, pady=5)

        self.gravity_choice = tk.StringVar(value="Earth")
        self.gravity_dropdown = tk.OptionMenu(self.main_frame, self.gravity_choice, "Earth", "Moon", "Mars", "Custom", command=self.handle_gravity_choice)
        self.gravity_dropdown.grid(row=3, column=2, pady=5)

        # Custom gravity input (only shown if "Custom" is selected)
        self.custom_gravity_label = tk.Label(self.main_frame, text="Enter Custom Gravity (m/s²):")
        self.entry_gravity = tk.Entry(self.main_frame, width=10)

        # Calculate and Clear buttons
        self.calculate_button = tk.Button(self.main_frame, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=4, column=0, pady=10)

        self.clear_button = tk.Button(self.main_frame, text="Clear", command=self.clear)
        self.clear_button.grid(row=4, column=1, pady=10)

        # Result display frame
        self.result_frame = tk.LabelFrame(self.main_frame, text="Results", padx=10, pady=10, font=("Arial", 12, "bold"), bd=2, relief="groove")
        self.result_frame.grid(row=5, column=0, columnspan=4, pady=20)

        # Labels for showing output values
        self.time_label = tk.Label(self.result_frame, text="Time of Flight: ", anchor='w', font=("Arial", 11))
        self.time_label.pack(fill='x', pady=2)

        self.max_height_label = tk.Label(self.result_frame, text="Maximum Height: ", anchor='w', font=("Arial", 11))
        self.max_height_label.pack(fill='x', pady=2)

        self.range_label = tk.Label(self.result_frame, text="Range: ", anchor='w', font=("Arial", 11))
        self.range_label.pack(fill='x', pady=2)

        # Info label for using matplotlib graph controls
        self.graph_info_label = tk.Label(
            self.main_frame,
            text="🖱 Graph Controls: Use the tools in the bottom left to interact:\n"
                 " - Pan tool:\n"
                 "   Click and drag to pan\n"
                 "   Right click and drag to zoom",
            font=("Arial", 10),
            justify="left",
            fg="gray"
        )
        self.graph_info_label.grid(row=6, column=0, columnspan=4, sticky="w")

    # Show/hide custom gravity input based on selection
    def handle_gravity_choice(self, selection):
        if selection == "Custom":
            self.custom_gravity_label.grid(row=2, column=3, pady=5)
            self.entry_gravity.grid(row=3, column=3, pady=5)
        else:
            self.custom_gravity_label.grid_forget()
            self.entry_gravity.grid_forget()

    # Clear all input and output fields
    def clear(self):
        self.entry_velocity.delete(0, tk.END)
        self.entry_angle.delete(0, tk.END)
        self.entry_gravity.delete(0, tk.END)
        self.gravity_choice.set("Earth")
        self.handle_gravity_choice("Earth")
        self.time_label.config(text="Time of Flight: ")
        self.max_height_label.config(text="Maximum Height: ")
        self.range_label.config(text="Range: ")

    # Calculate trajectory and show results
    def calculate(self):
        try:
            velocity = float(self.entry_velocity.get())
            angle = float(self.entry_angle.get())

            # Input validation
            if velocity <= 0:
                messagebox.showerror("Input Error", "Velocity must be greater than 0.")
                return

            if not (0 <= angle <= 90):
                messagebox.showerror("Input Error", "Angle must be between 0 and 90 degrees.")
                return

            gravity_option = self.gravity_choice.get()

            # Set gravity based on selection
            if gravity_option == "Earth":
                gravity = 9.81
            elif gravity_option == "Moon":
                gravity = 1.62
            elif gravity_option == "Mars":
                gravity = 3.71
            elif gravity_option == "Custom":
                try:
                    gravity = float(self.entry_gravity.get())
                    if gravity <= 0:
                        messagebox.showerror("Input Error", "Gravity must be greater than 0.")
                        return
                except ValueError:
                    messagebox.showerror("Input Error", "Enter a valid number for custom gravity.")
                    return
            else:
                gravity = 9.81  # default fallback

            # Plot trajectory and show results
            self.plot_trajectory(velocity, angle, gravity)

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values for velocity and angle")

    # Plot trajectory using matplotlib
    def plot_trajectory(self, velocity, angle, g):
        theta = np.radians(angle)

        # Calculate physics values
        time_of_flight = (2 * velocity * np.sin(theta)) / g
        max_height = (velocity**2 * np.sin(theta)**2) / (2 * g)
        range_x = (velocity**2 * np.sin(2 * theta)) / g

        # Generate time steps and coordinates
        t = np.linspace(0, time_of_flight, num=100)
        x = velocity * np.cos(theta) * t
        y = velocity * np.sin(theta) * t - (0.5 * g * t**2)

        # Set fixed axes limits for the graph
        x_max_fixed = 1000
        y_max_fixed = 300

        # Plot the graph
        plt.figure(figsize=(8, 5))
        plt.plot(x, y, label="Projectile Path", color="blue")
        plt.xlim(0, x_max_fixed)
        plt.ylim(0, y_max_fixed)
        plt.xlabel("Distance (m)")
        plt.ylabel("Height (m)")
        plt.title("Projectile Motion Trajectory")
        plt.legend()
        plt.grid(True)

        # Update results on the GUI
        self.time_label.config(text=f"Time of Flight: {time_of_flight:.2f} s")
        self.max_height_label.config(text=f"Maximum Height: {max_height:.2f} m")
        self.range_label.config(text=f"Range: {range_x:.2f} m")

        # Show the plot
        plt.show()


# Create the window and start the app
window = tk.Tk()
app = GUI(window)
window.mainloop()
