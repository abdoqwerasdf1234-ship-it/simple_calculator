import tkinter as tk

# 1. إعداد النافذة
root = tk.Tk()
root.title("حاسبتي الاحترافية")
root.geometry("320x450")
root.configure(bg="#1e1e1e")

# 2. شاشة العرض
entry = tk.Entry(root, font=("Arial", 28), bg="#252526", fg="white", borderwidth=0, justify="right")
entry.pack(pady=20, padx=10, fill="x")

# 3. دالات العمليات
def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(key))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "خطأ")

# 4. إطار الأزرار
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(expand=True, fill="both")

# قائمة الأزرار
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 0
col_val = 0

for btn_text in buttons:
    # تحديد دالة كل زر
    if btn_text == "=":
        action = calculate
        bg_color = "#28a745" # أخضر
    elif btn_text == "C":
        action = clear
        bg_color = "#dc3545" # أحمر
    else:
        action = lambda x=btn_text: press(x)
        bg_color = "#3c3c3c" # رمادي للأرقام

    btn = tk.Button(frame, text=btn_text, font=("Arial", 16, "bold"),
                    bg=bg_color, fg="white", borderwidth=0,
                    command=action, width=5, height=2)
    
    btn.grid(row=row_val, column=col_val, sticky="nsew", padx=2, pady=2)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# جعل الأزرار تتمدد لتملأ المساحة
for i in range(4):
    frame.grid_columnconfigure(i, weight=1)
for i in range(4):
    frame.grid_rowconfigure(i, weight=1)

root.mainloop()