import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time
import threading
from playsound import playsound

def play_sound():
    try:
        playsound("ding.mp3")
    except:
        print("🔇 فشل تشغيل الصوت")

def alert(msg):
    messagebox.showinfo("🚨 تنبيه", msg)
    threading.Thread(target=play_sound).start()

def start_timer(study_min, break_min, total_minutes):
    def run():
        sessions = total_minutes // (study_min + break_min)
        for session in range(sessions):
            update_status(f"🧠 دراسة {study_min} دقيقة")
            countdown(study_min * 60)
            alert("خلصت الدراسة! خذ بريك ☕")

            update_status(f"😌 بريك {break_min} دقيقة")
            countdown(break_min * 60)
            alert("خلص البريك! يلا نكمل 💪")

        update_status("🎉 خلصت كل الجلسات! فخور فيك 👏")
        alert("انتهى كل شيء! ✨")

    threading.Thread(target=run).start()

def countdown(seconds):
    progress["maximum"] = seconds
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_display.config(text=f"{mins:02d}:{secs:02d}")
        progress["value"] = progress["maximum"] - seconds
        time.sleep(1)
        seconds -= 1
    timer_display.config(text="00:00")
    progress["value"] = 0

def update_status(text):
    status_label.config(text=text)

def on_start():
    try:
        study_total = int(study_hours.get()) * 60 + int(study_minutes.get())
        break_total = int(break_hours.get()) * 60 + int(break_minutes.get())
        total_hours = float(total_time_entry.get())
        total_minutes = int(total_hours * 60)
        start_timer(study_total, break_total, total_minutes)
    except ValueError:
        messagebox.showwarning("⚠️ خطأ", "تأكد أنك اخترت القيم بشكل صحيح")

# === واجهة البرنامج ===
root = tk.Tk()
root.title("📚 منبه الدراسة الذكي")
root.geometry("420x500")
root.configure(bg="white")
root.resizable(False, False)

font_main = ("Helvetica", 14)
font_big = ("Helvetica", 36, "bold")

# ===== إعداد الوقت الكلي =====
tk.Label(root, text="⏱️ كم ساعة تبي تذاكر؟", font=font_main, bg="white", fg="black").pack(pady=5)
total_time_entry = tk.Entry(root, font=font_main, justify="center", width=10)
total_time_entry.insert(0, "2")
total_time_entry.pack(pady=5)

# ===== اختيار وقت الدراسة =====
tk.Label(root, text="✏️ وقت الجلسة الدراسية:", font=font_main, bg="white", fg="black").pack(pady=5)
frame_study = tk.Frame(root, bg="white")
frame_study.pack()

study_hours = tk.StringVar(value="0")
study_minutes = tk.StringVar(value="25")

tk.OptionMenu(frame_study, study_hours, *[str(i) for i in range(13)]).pack(side="left", padx=5)
tk.Label(frame_study, text="ساعات", bg="white").pack(side="left")

tk.OptionMenu(frame_study, study_minutes, *[str(i) for i in range(60)]).pack(side="left", padx=5)
tk.Label(frame_study, text="دقايق", bg="white").pack(side="left")

# ===== اختيار وقت البريك =====
tk.Label(root, text="☕ وقت البريك:", font=font_main, bg="white", fg="black").pack(pady=5)
frame_break = tk.Frame(root, bg="white")
frame_break.pack()

break_hours = tk.StringVar(value="0")
break_minutes = tk.StringVar(value="5")

tk.OptionMenu(frame_break, break_hours, *[str(i) for i in range(13)]).pack(side="left", padx=5)
tk.Label(frame_break, text="ساعات", bg="white").pack(side="left")

tk.OptionMenu(frame_break, break_minutes, *[str(i) for i in range(60)]).pack(side="left", padx=5)
tk.Label(frame_break, text="دقايق", bg="white").pack(side="left")

# ===== زر البدء =====
start_btn = tk.Button(root, text="🚀 ابدأ", font=font_main, bg="#4CAF50", fg="white", command=on_start)
start_btn.pack(pady=15)

# ===== المؤقت و شريط التقدم =====
tk.Label(root, text="⏰", font=("Helvetica", 30), bg="white").pack()

timer_display = tk.Label(root, text="00:00", font=font_big, fg="#0077CC", bg="white")
timer_display.pack(pady=5)

progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=10)

status_label = tk.Label(root, text="", font=("Helvetica", 12), fg="gray", bg="white")
status_label.pack(pady=5)

root.mainloop()
