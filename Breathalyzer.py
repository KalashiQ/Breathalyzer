import tkinter as tk
from tkinter import ttk


def calculate_alcohol_blood_level(volume_ml, alcohol_percentage, weight_kg, gender):
    pure_alcohol_g = volume_ml * alcohol_percentage / 100 * 0.789

    if gender == "мужской":
        distribution_coefficient = 0.7
    else:
        distribution_coefficient = 0.6

    blood_alcohol_level = pure_alcohol_g / (weight_kg * distribution_coefficient)
    return blood_alcohol_level

def time_to_sober_up(blood_alcohol_level, gender):
    if gender == "мужской":
        elimination_rate = 0.15
    else:
        elimination_rate = 0.12

    sober_time = blood_alcohol_level / elimination_rate
    return sober_time

def calculate():
    try:
        gender = gender_var.get()
        weight = float(weight_entry.get())
        volume = float(volume_entry.get())
        alcohol = float(alcohol_entry.get())

        if weight <= 0 or volume <= 0 or alcohol <= 0 or alcohol > 100:
            result_label.config(text="Ошибка: Проверьте введенные данные!")
            return

        bal = calculate_alcohol_blood_level(volume, alcohol, weight, gender)
        time = time_to_sober_up(bal, gender)

        result_label.config(
            text=(
                f"Уровень алкоголя в крови: {bal:.2f} промилле\n"
                f"Время до трезвости: {time:.2f} часов"
            )
        )
    except ValueError:
        result_label.config(text="Ошибка: Проверьте введенные данные!")


root = tk.Tk()
root.title("Алкотестер")
root.geometry("500x450")
root.configure(bg="#F0F0F0")  # Легкий серый фон


title_label = tk.Label(root, text="Виртуальный Алкотестер", font=("Helvetica", 18, "bold"), anchor="center", bg="#F0F0F0", fg="#37474F")
title_label.pack(pady=20)


gender_label = tk.Label(root, text="Выберите ваш пол:", bg="#F0F0F0", fg="#37474F", font=("Helvetica", 12))
gender_label.pack(anchor="w", padx=20)

gender_var = tk.StringVar(value="мужской")
gender_frame = tk.Frame(root, bg="#F0F0F0")
gender_frame.pack(anchor="w", padx=20)
male_button = tk.Radiobutton(gender_frame, text="Мужской", variable=gender_var, value="мужской", bg="#F0F0F0", fg="#37474F", font=("Helvetica", 11))
female_button = tk.Radiobutton(gender_frame, text="Женский", variable=gender_var, value="женский", bg="#F0F0F0", fg="#37474F", font=("Helvetica", 11))
male_button.grid(row=0, column=0, padx=5)
female_button.grid(row=0, column=1, padx=5)


weight_label = tk.Label(root, text="Ваш вес (в кг):", bg="#F0F0F0", fg="#37474F", font=("Helvetica", 12))
weight_label.pack(anchor="w", padx=20)
weight_entry = tk.Entry(root)
weight_entry.pack(fill="x", padx=20, pady=5)

volume_label = tk.Label(root, text="Объем алкоголя (в мл):", bg="#F0F0F0", fg="#37474F", font=("Helvetica", 12))
volume_label.pack(anchor="w", padx=20)
volume_entry = tk.Entry(root)
volume_entry.pack(fill="x", padx=20, pady=5)

alcohol_label = tk.Label(root, text="Процент алкоголя (%):", bg="#F0F0F0", fg="#37474F", font=("Helvetica", 12))
alcohol_label.pack(anchor="w", padx=20)
alcohol_entry = tk.Entry(root)
alcohol_entry.pack(fill="x", padx=20, pady=5)


calculate_button = tk.Button(root, text="Рассчитать", command=calculate, bg="#FF6F61", fg="black", font=("Helvetica", 12, "bold"), padx=10, pady=5)
calculate_button.pack(pady=10)


result_label = tk.Label(root, text="", font=("Helvetica", 14, "italic"), background="#F0F0F0", fg='black')
result_label.pack(pady=20)


root.mainloop()