import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Zodiac sign logic
def get_zodiac_sign(day, month):
    signs = [
        (20, "Capricorn", "♑️"), (19, "Aquarius", "♒️"), (20, "Pisces", "♓️"),
        (20, "Aries", "♈️"), (21, "Taurus", "♉️"), (21, "Gemini", "♊️"),
        (23, "Cancer", "♋️"), (23, "Leo", "♌️"), (23, "Virgo", "♍️"),
        (23, "Libra", "♎️"), (22, "Scorpio", "♏️"), (22, "Sagittarius", "♐️"),
        (31, "Capricorn", "♑️")
    ]
    if day <= signs[month - 1][0]:
        return signs[month - 1][1], signs[month - 1][2]
    else:
        return signs[month][1], signs[month][2]

# Age calculation logic
def calculate():
    dob_input = dob_entry.get()
    try:
        dob = datetime.strptime(dob_input, "%d-%m-%Y")
        today = datetime.today()

        y = today.year - dob.year
        m = today.month - dob.month
        d = today.day - dob.day

        if d < 0:
            m -= 1
            d += 30
        if m < 0:
            y -= 1
            m += 12

        zodiac, emoji = get_zodiac_sign(dob.day, dob.month)

        next_birthday = dob.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)
        days_left = (next_birthday - today).days

        result_age.config(text=f"🎉 {y} years, {m} months, {d} days")
        result_zodiac.config(text=f"🔮 Zodiac Sign: {zodiac} {emoji}")
        result_birthday.config(text=f"🎂 Next birthday in {days_left} days 🎈")

    except ValueError:
        messagebox.showerror("Invalid", "Please enter DOB in format DD-MM-YYYY")

# GUI Setup
root = tk.Tk()
root.title("✨ Age & Zodiac Calculator")
root.geometry("400x400")
root.configure(bg="#fef6ff")  # light lavender/pink background

# Card
card = tk.Frame(root, bg="white", bd=0, relief="ridge")
card.place(relx=0.5, rely=0.5, anchor="center", width=330, height=330)

tk.Label(card, text="🌟 Age & Zodiac", font=("Segoe UI Emoji", 18, "bold"),
         bg="white", fg="#7f5af0").pack(pady=(20, 10))

tk.Label(card, text="Enter DOB (DD-MM-YYYY)", font=("Segoe UI", 11),
         bg="white", fg="#2d2d2d").pack()

dob_entry = tk.Entry(card, font=("Segoe UI", 12), justify="center",
                     bd=1, relief="solid", width=22)
dob_entry.pack(pady=10)

tk.Button(card, text="Calculate", font=("Segoe UI", 12, "bold"), bg="#7f5af0",
          fg="white", activebackground="#a58df5", relief="flat", padx=12, pady=4,
          command=calculate).pack(pady=10)

result_age = tk.Label(card, text="", font=("Segoe UI Emoji", 11), bg="white", fg="#2d2d2d")
result_age.pack(pady=4)

result_zodiac = tk.Label(card, text="", font=("Segoe UI Emoji", 11), bg="white", fg="#2d2d2d")
result_zodiac.pack()

result_birthday = tk.Label(card, text="", font=("Segoe UI Emoji", 11), bg="white", fg="#2d2d2d")
result_birthday.pack()

root.mainloop()
