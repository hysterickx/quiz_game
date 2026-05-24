# My Quiz Game (Моя Викторина)

A modern, desktop-based quiz application built with Python using Object-Oriented Programming (OOP) principles and a sleek CustomTkinter graphical user interface. 

The application welcomes users, explains the rules, and presents multiple-choice trivia questions across various topics. At the end, it displays the user's final score and allows them to restart or exit.

<img width="452" height="398" alt="image" src="https://github.com/user-attachments/assets/a827c346-8856-4dc0-a8dd-6cfec8cd792d" />


## ✨ Features

* **Modern Dark GUI:** Built using `customtkinter` for a responsive, modern interface.
* **OOP Architecture:** Clean, modular structure using a controller-page workflow to switch between views efficiently.
* **Dynamic Navigation:** Multi-page flows including Welcome, Rules, Active Quiz, and Final Results pages.
* **Visual Score Tracking:** Real-time updates showing the current question number and accumulated points.

## 🛠️ Tech Stack

* **Language:** Python 3.8+
* **GUI Framework:** CustomTkinter
* **Design Pattern:** Object-Oriented Programming (OOP) with centralized configuration management.

## 📦 Project Structure

```text
├── main.py          # Application controller and main entry point
├── pages/           # Module containing GUI page classes (GreetingsPage, RulesPage, QuizPage, etc.)
├── config.py        # Centralized styling variables, parameters, and colors
└── README.md        # Project documentation
```

## 🚀 Getting Started

Follow these steps to set up and run the game locally.

### Prerequisites

Ensure you have Python installed on your system. You will also need to install `customtkinter`:

```bash
pip install customtkinter
```

### Installation & Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd quiz-game
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```

## 🎮 How to Play

1. **Welcome Screen:** Click **"Давай!"** (Let's go!) to proceed or **"Не сейчас"** (Not now) to exit.
2. **Rules Screen:** Read through the quiz rules before beginning.
3. **Quiz Interface:** Read the question and choose one of the three available radio buttons. Click **"Далее"** (Next) to advance.
4. **Results:** View your final score, then click to replay or exit.

---
Developed with ❤️ using Python and CustomTkinter.
