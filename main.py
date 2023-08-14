import tkinter as tk
from tkinter import messagebox
questions = [
    {
        'question': 'Which type of plastic is most harmful to marine life?',
        'answer': 'Single use plastics'
    },
    {
        'question': 'What percentage of marine pollution is caused by plastic?',
        'answer': '80%'
    },
    {
        'question': 'How long does it take for a plastic bottle to decompose?',
        'answer': '450 years'
    },

    {
        'question': 'What is the colour of most plastic bags commonly found in oceans?',
        'answer': 'White'
    },

    {
        'question': 'What is the main source of plastic pollution in waterways?',
        'answer': 'Land-based activities'
    },
]

score = 0

def show_question(index):
    question_label.config(text=questions[index]['question'], fg="blue")
    submit_button.config(command=lambda: check_answer(index))

def check_answer(index):
    user_answer = answer_entry.get().strip()
    correct_answer = questions[index]['answer']
    global score

    if user_answer.lower() == correct_answer.lower():
        messagebox.showinfo('Result', 'Correct answer!')
        score = score + 1
    else:
        messagebox.showerror('Result', f'Incorrect answer. The correct answer is: {correct_answer}')

    answer_entry.delete(0, tk.END)

    # Move to the next question or show final message
    if index < len(questions) - 1:
        show_question(index + 1)
    else:
        messagebox.showinfo('Quiz Completed', 'Congratulations! You completed the quiz.')
        messagebox.showinfo('Score', f'{score}/{index + 1} correct')
        root.destroy()

# Create the main GUI window
root = tk.Tk()
root.title('Plastic Pollution Quiz')

question_label = tk.Label(root, text='', wraplength=300, bg='white')
question_label.pack(pady=20,)

answer_entry = tk.Entry(root, width=30)
answer_entry.pack(pady=10)

submit_button = tk.Button(root, text='Submit', command=lambda: check_answer(0))
submit_button.pack(pady=10)

# Start the quiz by showing the first question
show_question(0)


# Run the main event loop
root.mainloop()
