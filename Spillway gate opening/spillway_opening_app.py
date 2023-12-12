import tkinter as tk
from tkinter import ttk, messagebox
import cv2
from PIL import Image, ImageTk  # Make sure to install the Pillow library: pip install Pillow
from spillway_opening_function import control_gates

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
        self.status_button = ttk.Button(master, text="Gate Status", command=self.open_video)

        # Create a canvas for displaying video frames
        self.canvas = tk.Canvas(master)
        self.canvas.grid(row=3, column=0, columnspan=2, pady=10)

        # Layout
        self.logo_label.grid(row=0, column=0, columnspan=2, pady=10)
        self.slogan_label.grid(row=1, column=0, columnspan=2, pady=0, padx=10)
        self.label_height.grid(row=2, column=0, padx=10, pady=10)
        self.entry_height.grid(row=2, column=1, padx=10, pady=10)
        self.status_button.grid(row=4, column=0, columnspan=2, pady=10)

    def open_video(self):
        try:
            height_value = float(self.entry_height.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric value for Height.")
            return

        heights = [0.0, 0.0, height_value]  # Adjust the list for consistency

        try:
            gate_status = control_gates(heights)
            self.display_video(gate_status)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def display_video(self, gate_status):
        while gate_status.isOpened():
            ret, frame = gate_status.read()
            if ret:
                # Convert the frame from BGR to RGB
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Resize the frame to fit the canvas
                img = Image.fromarray(rgb_frame)
                img = img.resize((400, 300), Image.LANCZOS)

                # Convert the frame to PhotoImage
                tk_img = ImageTk.PhotoImage(img)

                # Update the canvas with the new frame
                self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)
                self.master.update_idletasks()

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break

        gate_status.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = GatePositions(root)
    root.mainloop()
