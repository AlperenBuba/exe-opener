import os
import sys
import json
import subprocess
import importlib
import threading

try:
    import tkinter as tk
    from tkinter import filedialog, messagebox
except ImportError:
    subprocess.check_call(["sudo", "apt", "install", "-y", "python3-tk"])
    import tkinter as tk
    from tkinter import filedialog, messagebox

import shutil

try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
    HAS_DND = True
except ImportError:
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "tkinterdnd2"])
        from tkinterdnd2 import DND_FILES, TkinterDnD
        HAS_DND = True
    except:
        HAS_DND = False

CONFIG_DIR = os.path.expanduser("~/.config/exe-opener")
RECENT_FILE = os.path.join(CONFIG_DIR, "recent.json")


def load_recent():
    try:
        with open(RECENT_FILE) as f:
            return json.load(f)
    except:
        return []


def save_recent(path):
    recent = load_recent()
    if path in recent:
        recent.remove(path)
    recent.insert(0, path)
    recent = recent[:10]
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(RECENT_FILE, "w") as f:
        json.dump(recent, f)


def check_and_install_wine():
    if shutil.which("wine"):
        return True
    temp = tk.Tk()
    temp.withdraw()
    ret = messagebox.askyesno(
        "Wine Kurulumu",
        "Wine sisteminizde bulunamadı. Kurmak ister misiniz?"
    )
    if not ret:
        temp.destroy()
        return False
    try:
        subprocess.run(["sudo", "apt", "install", "-y", "wine"], check=True)
    except subprocess.CalledProcessError:
        messagebox.showerror("Hata", "Wine kurulumu başarısız oldu.")
        temp.destroy()
        return False
    temp.destroy()
    return True


if not check_and_install_wine():
    sys.exit(1)


if HAS_DND:
    root = TkinterDnD.Tk()
else:
    root = tk.Tk()

root.title("EXE Opener - Wine Launcher")
W, H = 420, 200
root.geometry(f"{W}x{H}")
root.update_idletasks()
x = (root.winfo_screenwidth() - W) // 2
y = (root.winfo_screenheight() - H) // 2
root.geometry(f"{W}x{H}+{x}+{y}")
root.resizable(False, False)

if HAS_DND:
    root.drop_target_register(DND_FILES)
    root.dnd_bind("<<Drop>>", lambda e: entry_var.set(e.data.strip("{}")))

center = tk.Frame(root)
center.pack(expand=True, pady=(20, 0))

entry_frame = tk.Frame(center)
entry_frame.pack()

entry_var = tk.StringVar()
entry = tk.Entry(entry_frame, textvariable=entry_var, width=35)
entry.pack(side=tk.LEFT, padx=(0, 5))


def select_file():
    path = filedialog.askopenfilename(
        initialdir=os.path.expanduser("~"),
        filetypes=[("EXE files", "*.exe")]
    )
    if path:
        entry_var.set(path)


btn_dots = tk.Button(entry_frame, text="...", command=select_file, width=3)
btn_dots.pack(side=tk.LEFT, padx=(0, 2))


def show_recent_menu(btn):
    recent = load_recent()
    if not recent:
        return
    menu = tk.Menu(btn, tearoff=0)
    for path in recent:
        menu.add_command(label=path, command=lambda p=path: entry_var.set(p))
    menu.tk_popup(btn.winfo_rootx(), btn.winfo_rooty() + btn.winfo_height())


btn_recent = tk.Button(entry_frame, text="▼", command=lambda: show_recent_menu(btn_recent), width=2)
btn_recent.pack(side=tk.LEFT)


def append_log(line):
    log_text.config(state="normal")
    log_text.insert("end", line)
    log_text.see("end")
    log_text.config(state="disabled")


def save_log():
    content = log_text.get("1.0", "end-1c")
    if not content.strip():
        return
    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("Log files", "*.log"), ("All files", "*.*")]
    )
    if path:
        with open(path, "w") as f:
            f.write(content)


def open_exe():
    path = entry_var.get().strip()
    if not path:
        messagebox.showwarning("Uyarı", "Lütfen bir EXE dosyası seçin.")
        return
    save_recent(path)
    log_text.config(state="normal")
    log_text.delete("1.0", "end")
    log_text.config(state="disabled")
    append_log(f"Çalıştırılıyor: wine {path}\n")

    def run():
        proc = subprocess.Popen(
            ["wine", path],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        for line in proc.stdout:
            root.after(0, append_log, line)

    threading.Thread(target=run, daemon=True).start()


btn_open = tk.Button(center, text="Aç", command=open_exe, width=12)
btn_open.pack(pady=(15, 0))

log_visible = False


def toggle_log():
    global log_visible
    if log_visible:
        log_frame.pack_forget()
        root.geometry("420x200")
        btn_log_toggle.config(text="▼")
    else:
        log_frame.pack(in_=root, fill="both", expand=True, pady=(0, 0))
        root.geometry("420x380")
        btn_log_toggle.config(text="▲")
    log_visible = not log_visible


bottom_bar = tk.Frame(root)
bottom_bar.pack(side=tk.BOTTOM, anchor=tk.W, fill=tk.X)

btn_log_toggle = tk.Button(bottom_bar, text="▼", command=toggle_log, width=3, relief=tk.FLAT)
btn_log_toggle.pack(side=tk.LEFT, padx=4, pady=2)

log_frame = tk.Frame(root)
log_text_frame = tk.Frame(log_frame)
log_text_frame.pack(fill="both", expand=True)
log_text = tk.Text(
    log_text_frame, bg="black", fg="white", height=10,
    font=("Consolas", 9), state="disabled"
)
scrollbar = tk.Scrollbar(log_text_frame, orient="vertical", command=log_text.yview)
log_text.configure(yscrollcommand=scrollbar.set)
log_text.pack(side=tk.LEFT, fill="both", expand=True)
scrollbar.pack(side=tk.RIGHT, fill="y")

log_btn_frame = tk.Frame(log_frame)
log_btn_frame.pack(fill=tk.X, padx=4, pady=4)
btn_save_log = tk.Button(log_btn_frame, text="Kaydet", command=save_log, width=10)
btn_save_log.pack(side=tk.RIGHT)

root.mainloop()
