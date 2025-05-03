import tkinter as tk
from tkinter import ttk, messagebox

def calculate_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())
        interest_type = interest_type_var.get()

        if interest_type == "Simple":
            interest = (principal * rate * time) / 100
        else:  # Compound
            interest = principal * ((1 + rate / 100) ** time) - principal

        total_amount = principal + interest

        result_label.config(text=f"Interest: ₹{interest:.2f}\nTotal Amount: ₹{total_amount:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# ----------------- GUI Setup -----------------
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("400x350")
root.resizable(False, False)

# Title
ttk.Label(root, text="📈 Interest Calculator", font=("Arial", 16)).pack(pady=10)

# Input Fields
frame = ttk.Frame(root)
frame.pack(pady=10)

ttk.Label(frame, text="Principal Amount (₹):").grid(row=0, column=0, sticky="w")
principal_entry = ttk.Entry(frame, width=30)
principal_entry.grid(row=0, column=1)

ttk.Label(frame, text="Interest Rate (%):").grid(row=1, column=0, sticky="w")
rate_entry = ttk.Entry(frame, width=30)
rate_entry.grid(row=1, column=1)

ttk.Label(frame, text="Time (years):").grid(row=2, column=0, sticky="w")
time_entry = ttk.Entry(frame, width=30)
time_entry.grid(row=2, column=1)

# Interest Type
interest_type_var = tk.StringVar(value="Simple")
ttk.Label(root, text="Choose Interest Type:").pack()
ttk.Radiobutton(root, text="Simple Interest", variable=interest_type_var, value="Simple").pack()
ttk.Radiobutton(root, text="Compound Interest", variable=interest_type_var, value="Compound").pack()

# Calculate Button
ttk.Button(root, text="Calculate", command=calculate_interest).pack(pady=10)

# Result Label
result_label = ttk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run App
root.mainloop()
