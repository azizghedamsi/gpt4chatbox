import openai
import os
import tkinter as tk
from tkinter import ttk

OPENAI_API_KEY = "API"
openai.api_key = OPENAI_API_KEY

def ask_gpt4(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = response.choices[0].text.strip()
    return message

def send_message(event=None):
    user_input = user_text.get()
    if user_input:
        chat_history.configure(state="normal")
        chat_history.insert(tk.END, f"You: {user_input}\n")
        user_text.set("")
        prompt = f"User: {user_input}\nAI:"
        response = ask_gpt4(prompt)
        chat_history.insert(tk.END, f"AI: {response}\n")
        chat_history.configure(state="disabled")
        chat_history.yview(tk.END)

root = tk.Tk()
root.title("GPT-4 Chatbot")

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

chat_history = tk.Text(main_frame, wrap=tk.WORD, state="disabled", width=50, height=15)
chat_history.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=chat_history.yview)
scrollbar.grid(row=0, column=2, sticky=(tk.N, tk.S))

chat_history["yscrollcommand"] = scrollbar.set

user_text = tk.StringVar()
entry_field = ttk.Entry(main_frame, textvariable=user_text, width=40)
entry_field.grid(row=1, column=0, sticky=(tk.W, tk.E))

send_button = ttk.Button(main_frame, text="Send", command=send_message)
send_button.grid(row=1, column=1, sticky=(tk.W, tk.E))

entry_field.bind("<Return>", send_message)

main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(0, weight=1)

entry_field.focus_set()

root.mainloop()
