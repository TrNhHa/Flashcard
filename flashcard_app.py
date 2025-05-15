
import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
import random

DATA_FILE = "data.json"

# Load & Save
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Thêm flashcard
def add_flashcard():
    question = simpledialog.askstring("Thêm flashcard", "Câu hỏi:")
    if not question:
        return
    answer = simpledialog.askstring("Thêm flashcard", "Đáp án:")
    if not answer:
        return
    flashcards.append({"question": question, "answer": answer})
    save_data(flashcards)
    messagebox.showinfo("✔️", "Đã thêm flashcard!")

# Hiển thị ngẫu nhiên
def show_random_flashcard():
    if not flashcards:
        messagebox.showinfo("⚠️", "Chưa có flashcard nào.")
        return
    global current_card
    current_card = random.choice(flashcards)
    question_label.config(text=f"❓ {current_card['question']}")
    answer_label.config(text="(Nhấn 'Hiện đáp án')")
    show_answer_btn.config(state="normal")

# Hiện đáp án
def show_answer():
    if current_card:
        answer_label.config(text=f"💡 {current_card['answer']}")

# Giao diện chính
flashcards = load_data()
current_card = None

root = tk.Tk()
root.title("🧠 Flashcard học tập")
root.geometry("400x300")

question_label = tk.Label(root, text="Nhấn 'Ôn bài' để bắt đầu", font=("Arial", 14, "bold"), wraplength=380)
question_label.pack(pady=20)

answer_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
answer_label.pack(pady=10)

show_answer_btn = tk.Button(root, text="Hiện đáp án", command=show_answer, state="disabled")
show_answer_btn.pack(pady=5)

tk.Button(root, text="📖 Ôn bài (ngẫu nhiên)", command=show_random_flashcard).pack(pady=5)
tk.Button(root, text="➕ Thêm flashcard", command=add_flashcard).pack(pady=5)
tk.Button(root, text="❌ Thoát", command=root.quit).pack(pady=10)

root.mainloop()
