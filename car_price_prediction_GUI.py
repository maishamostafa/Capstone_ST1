import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

class CarPriceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Price Viewer")

        # Correct the path to where your dataset is located
        self.dataset = pd.read_csv("car_price_prediction.csv")

        # Create the main frame
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(pady=20)

        # Add buttons
        self.btn_final_price = ttk.Button(self.main_frame, text="1. Final Price", command=self.show_final_price)
        self.btn_final_price.pack(fill='x', expand=True)

        self.btn_show_data = ttk.Button(self.main_frame, text="2. Car Price Dataset", command=self.show_dataset)
        self.btn_show_data.pack(fill='x', expand=True)

        self.btn_exit = ttk.Button(self.main_frame, text="3. Exit", command=self.root.quit)
        self.btn_exit.pack(fill='x', expand=True)

    def show_final_price(self):
        # Display the 'Price' column as 'Final Price'
        try:
            final_price = self.dataset['Price']
            messagebox.showinfo("Final Price", str(final_price))
        except KeyError:
            messagebox.showerror("Error", "The 'Price' column does not exist in the dataset.")

    def show_dataset(self):
        # Display the dataset in a new window
        top = tk.Toplevel()
        top.title("Car Price Dataset")
        txt = tk.Text(top, wrap="none")
        txt.pack(fill="both", expand=True)

        # Use scrollbar
        scrollb_x = ttk.Scrollbar(top, orient="horizontal", command=txt.xview)
        scrollb_x.pack(fill="x", side="bottom")
        scrollb_y = ttk.Scrollbar(top, orient="vertical", command=txt.yview)
        scrollb_y.pack(fill="y", side="right")
        txt['xscrollcommand'] = scrollb_x.set
        txt['yscrollcommand'] = scrollb_y.set

        # Insert the data
        txt.insert("end", str(self.dataset))

# Create the main window and pass it to the CarPriceApp
root = tk.Tk()
app = CarPriceApp(root)
root.mainloop()
