import text2emotion as te
import tkinter as tk
from tkinter import font
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')

class EmotionApp():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('700x700')
        self.root.title("🧠 Emotion Analyzer")
        self.root.configure(bg="#f0f4f7")
        self.setup_ui()

    def setup_ui(self):
        header = tk.Label(self.root, text="Emotion Analyzer", font=("Helvetica", 20, "bold"), bg="#f0f4f7", fg="#333")
        header.pack(pady=20)

        self.label = tk.Label(self.root, text="Enter your text below:", font=("Helvetica", 12), bg="#f0f4f7")
        self.label.pack(pady=5)

        self.entry = tk.Text(self.root, height=6, width=60, font=("Helvetica", 11))
        self.entry.pack(pady=10)

        self.button = tk.Button(self.root, text="🔍 Analyze Emotions", command=self.analyze_emotion, bg="#4caf50", fg="white", font=("Helvetica", 12, "bold"))
        self.button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 11), bg="#f0f4f7", wraplength=600, justify="left")
        self.result_label.pack(pady=10)

        self.canvas_frame = tk.Frame(self.root, bg="#f0f4f7")
        self.canvas_frame.pack(pady=10)

        footer = tk.Label(self.root, text="Made by ItsIzabela", font=("Helvetica", 9), bg="#f0f4f7", fg="#777")
        footer.pack(side="bottom", pady=10)

        self.canvas = None 

    def analyze_emotion(self):
        text = self.entry.get("1.0", tk.END).strip()

        if not text:
            self.result_label.config(text="⚠️ Please enter some text first!")
            return

        try:
            emotions = te.get_emotion(text) 
            self.result_label.config(text=f"🔎 Emotion Analysis Result:\n{emotions}")
            print(emotions)
            self.show_chart(emotions)
        except Exception as e:
            self.result_label.config(text=f"❌ Error: {e}")

    def show_chart(self, emotions):
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(5, 3))
        emotion_names = list(emotions.keys())
        emotion_values = list(emotions.values())

        ax.bar(emotion_names, emotion_values, color="#4caf50")
        ax.set_ylim(0, 1)
        ax.set_title("Emotion Distribution", fontsize=14, weight="bold")
        ax.set_ylabel("Intensity")

        self.canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    def run(self):
        self.root.mainloop()

app = EmotionApp()
app.run()
