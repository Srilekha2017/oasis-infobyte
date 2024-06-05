import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import json
import os

class BMI_Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("BMI Calculator")
        self.master.geometry("300x300")

        self.user_data = {}
        self.load_data()

        self.label_weight = tk.Label(master, text="Weight (kg):")
        self.label_weight.pack()
        self.entry_weight = tk.Entry(master)
        self.entry_weight.pack()

        self.label_height = tk.Label(master, text="Height (m):")
        self.label_height.pack()
        self.entry_height = tk.Entry(master)
        self.entry_height.pack()

        self.calculate_button = tk.Button(master, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.pack()

    def calculate_bmi(self):
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())
            bmi = weight / (height ** 2)
            bmi_category = self.get_bmi_category(bmi)
            messagebox.showinfo("BMI Result", f"Your BMI is {bmi:.2f} ({bmi_category})")
            self.save_data(weight, height, bmi)
            self.plot_bmi_trend()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid weight and height.")

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def save_data(self, weight, height, bmi):
        self.user_data["weight"] = weight
        self.user_data["height"] = height
        self.user_data["bmi"] = bmi

        with open("user_data.json", "w") as f:
            json.dump(self.user_data, f)

    def load_data(self):
        if os.path.exists("user_data.json"):
            with open("user_data.json", "r") as f:
                self.user_data = json.load(f)

    def plot_bmi_trend(self):
        weights = []
        bmis = []

        if os.path.exists("user_data.json"):
            with open("user_data.json", "r") as f:
                user_data = json.load(f)
                weights.append(user_data["weight"])
                bmis.append(user_data["bmi"])

        plt.plot(weights, bmis, marker='o')
        plt.xlabel('Weight (kg)')
        plt.ylabel('BMI')
        plt.title('BMI Trend')
        plt.grid(True)
        plt.show()

def main():
    root = tk.Tk()
    app = BMI_Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
