# Emotion Analyzer

Emotion Analyzer is a desktop application built with Python that detects emotional tones in user-inputted text. It uses the `text2emotion` library to classify emotions and visualizes the results with a bar chart using `matplotlib`. The GUI is built with `tkinter`, making it lightweight and easy to run locally.

---

## 🚀 Features

- Enter text and detect emotions such as **Happy, Angry, Surprise, Sad, and Fear**.
- Displays emotion analysis results both as text and a visual bar chart.
- Simple and user-friendly interface.
- Cross-platform: works on Windows, macOS, and Linux.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/emotion-analyzer.git
cd emotion-analyzer
```

2. Install following libraries

``` bash
pip install text2emotion matplotlib nltk
python emotion_analyzer.py
```

## Dependencies
- Python 3.8 +
- Tkinter
- Text2emotion
- Matplotlib
- NLTK

## How it works

1. User inputs text into the GUI.

2. Text2Emotion analyzes the text and returns a dictionary of emotions with intensity values.

3. The result is displayed in the GUI and a bar chart is generated using Matplotlib.

## Author

Made by ItsIzabela

## License

This project is open-source and available under the MIT License.

