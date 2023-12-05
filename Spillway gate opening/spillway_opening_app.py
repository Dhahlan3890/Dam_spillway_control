import tkinter as tk
from tkinter import ttk, messagebox
from spillway_opening_function import control_gates

heights = [0.0, 0.0]

class GatePositions:
    def __init__(self, master):
        self.master = master
        self.master.title("Prediction App")
        self.master.iconbitmap("icon.ico") 

        # Add a logo and company name
        self.logo = tk.PhotoImage(file="mahaweli-authority.png")  # Replace with the actual path to your logo image
        self.slogan_label = ttk.Label(master, text="An efficient way to control gates", font=('Arial', 10, 'italic'))
        self.logo_label = ttk.Label(master, image=self.logo)
        
        # Create and set up widgets
        self.label_height = ttk.Label(master, text="Height:")
        self.entry_height = ttk.Entry(master)
        self.status_button = ttk.Button(master, text="Gate Status", command=self.get_status)

        # Layout
        self.logo_label.grid(row=0, column=0, columnspan=2, pady=10)
        self.slogan_label.grid(row=1, column=0, columnspan=2, pady=0, padx=10)
        self.label_height.grid(row=2, column=0, padx=10, pady=10)
        self.entry_height.grid(row=2, column=1, padx=10, pady=10)
        self.status_button.grid(row=4, column=0, columnspan=2, pady=10)
        
    def get_status(self):
        try:
            height_value = float(self.entry_height.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric value for Height.")
            return
        
        heights = [0.0, 0.0]
        heights.append(height_value)
        

        try:
            gate_status = control_gates(heights)
            messagebox.showinfo("Prediction", f"The spillway will be \n{gate_status}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Add code to load and train your machine learning model
    
    # Create the main application window
    root = tk.Tk()
    app = GatePositions(root)
    root.mainloop()
