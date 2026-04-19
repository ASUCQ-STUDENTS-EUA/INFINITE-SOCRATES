from __future__ import annotations

import tkinter as tk
from tkinter import ttk


def run_app() -> None:
    root = tk.Tk()
    root.title("Infinite Socrates")
    root.geometry("900x600")

    root.columnconfigure(0, weight=3)
    root.columnconfigure(1, weight=2)
    root.rowconfigure(0, weight=1)

    notebook_frame = ttk.Frame(root, padding=12)
    notebook_frame.grid(row=0, column=0, sticky="nsew")
    notebook_frame.columnconfigure(0, weight=1)
    notebook_frame.rowconfigure(1, weight=1)

    ttk.Label(
        notebook_frame,
        text="Notepad (placeholder)",
        font=("Arial", 14, "bold"),
    ).grid(row=0, column=0, sticky="w")

    notepad = tk.Text(notebook_frame, wrap="word")
    notepad.grid(row=1, column=0, sticky="nsew", pady=(8, 0))

    right_panel = ttk.Frame(root, padding=12)
    right_panel.grid(row=0, column=1, sticky="nsew")
    right_panel.columnconfigure(0, weight=1)
    right_panel.rowconfigure(1, weight=1)

    ttk.Label(
        right_panel,
        text="Socratic prompts (placeholder)",
        font=("Arial", 14, "bold"),
    ).grid(row=0, column=0, sticky="w")

    prompts = tk.Listbox(right_panel)
    prompts.grid(row=1, column=0, sticky="nsew", pady=(8, 0))

    for prompt in [
        "What do the variables represent here?",
        "What operation would isolate x?",
        "What assumptions are you making?",
    ]:
        prompts.insert(tk.END, prompt)

    root.mainloop()

