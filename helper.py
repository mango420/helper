# Copyright (C) 2024  mango420

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

from openai import OpenAI
import pyperclip
from pynput import keyboard
import tkinter as tk

key = 'sk-xxxxxxxxxx'
client = OpenAI(api_key=key)

gpt_sys = {
    'role': 'system',
    'content': '''
    You are a Cisco Specialist in networking protocols and configurations, particularly with OSPF. 
    As part of the team, you're expected to answer detailed questions related to OSPF configurations, troubleshooting, and optimization strategies. 
    Your expertise also covers understanding the nuances of OSPF areas, route summarization, and the impact of OSPF on network performance.
      Please prepare to provide explanations, commands, and best practices that ensure optimal OSPF deployment and maintenance. 
      You might get multiple choice, questions with only one answer, questions with more than one answers or questions where to input things. 
      Read the questions carefully and answer accordingly and as detailed as possible. 
      If you have a multiple choice question, please answer with the letter of the correct answer and the answer. 
      It is possible that more than one answer is correct (read the question carefully). 
      If you have a question that is not multiple choice, please answer with the answer.
        If it says "kurz" or "short" or something like that then answer short! If only a word is asked only answer with the word!
        If nothing specified about the lenght try to answer short!
    '''
}

def ask_question(key):
    input_text = pyperclip.paste()

    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        max_tokens=300,
        temperature=0,
        n=1,
        stop=None,
        messages= [
            gpt_sys,
            {
                'role': 'user',
                'content': input_text
            },
        ],
        )

    answer = response.choices[0].message.content

    print(answer)
    pyperclip.copy(answer)

def on_key_pressed(key):
    if key == keyboard.Key.f10:
        ask_question(key)
    elif key == keyboard.Key.f8:
        renew_client()
    elif key == keyboard.Key.f7:
        show_clipboard()

def renew_client():
    client = OpenAI(api_key=key)
    print('Client renewed')

def show_clipboard():
    print(pyperclip.paste())
    window = tk.Tk()
    tk.Label(window, text=pyperclip.paste()).pack()
    window.mainloop()

with keyboard.Listener(on_press=on_key_pressed) as listener:
    listener.join()