import pyautogui as pg
import pygetwindow as gw
import time
import webbrowser
def focus_browser_window(title_substring="ChatGPT"):
    windows = gw.getWindowsWithTitle(title_substring)
    if not windows:
        print(f"No window found with title containing '{title_substring}'")
        return False
    window = windows[0]
    window.activate()
    time.sleep(1)
    return True
def send_message(message):
    # Tab to input box
    for _ in range(7):
        pg.press('tab')
        time.sleep(0.1)
    pg.write(message, interval=0.05)
    pg.press('enter')
    print(f"Sent: {message}")
    time.sleep(50)  # Wait for ChatGPT to respond
def open_chatgpt_and_learn(prompts):
    webbrowser.open('https://chat.openai.com/')
    time.sleep(2)  # Wait longer for browser to load
    if not focus_browser_window("ChatGPT"):
        print("Failed to find ChatGPT window. Exiting.")
        return
    for prompt in prompts:
        send_message(prompt)
# List of prompts to learn automation
learning_prompts = [
    "Explain what automation is and how it is used in programming.",
    "Give me the examples of automation in a particular programming language?",
    "Teach me GUI automation with Python using pyautogui.",
    "I would like you to help me create a automation script.",
    "How do I use Selenium for browser automation?",
    "I would like a demo automating a specific website.",
    "I would like you to deep dive into waiting strategies, interacting with elements, and handling popups.",
    "What are the differences between GUI automation and browser automation?",
    "Can you give me a small project idea for automation?",
    "I also want you to execute the above project and explain the code line by line."
]
# Run
open_chatgpt_and_learn(learning_prompts)