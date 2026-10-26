import customtkinter as ctk
import json

with open("Starttaps.json", "r") as f:
        start = json.load(f)

# Налаштування вікна
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("Пошук у базі даних")
app.geometry("400x300")

# --- ОСЬ ТУТ ПИШИ СВОЮ ЛОГІКУ ---
def search_company():

    query = entry.get().strip().lower()

    if not query:
        result_label.configure(text="Введіть текст для пошуку!", text_color="yellow")
        return

    found_startpus = []

    for item in start:
        if query in item["name"].lower():
            found_startpus.append(item["name"])
    if found_startpus:
        joined_names = ", ".join(found_startpus)
        result_label.configure(text=f"Знайдено: {joined_names}", text_color="green")
    else:
        result_label.configure(text="Не знайдено", text_color="red")
        
    print(found_startpus)
# --------------------------------

# Елементи інтерфейсу
title_label = ctk.CTkLabel(app, text="Пошук стартапів Ycombinator", font=("Arial", 18, "bold"))
title_label.pack(pady=20)

entry = ctk.CTkEntry(app, placeholder_text="Введіть назву стартапа...", width=250)
entry.pack(pady=10)

search_button = ctk.CTkButton(app, text="Шукати", command=search_company)
search_button.pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
result_label.pack(pady=20)

app.mainloop()
