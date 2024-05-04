from tkinter import *
import threading

countdown_started = False  # Flag to track whether the countdown has started or not
correct_word_count = 0  # Variable to store the total number of deleted words
wrong_word_count = 0


def handle_key_press(event):
    global countdown_started

    if event.keysym == 'space':
        match_text = typing_text.get(1.0, "end-1c")
        typing_text.delete('1.0', END)

        global correct_word_count, wrong_word_count

        if match_text in text_type:
            correct_word_count += 1
        else:
            wrong_word_count += 1

    elif not countdown_started:  # Start countdown only if it hasn't started yet
        threading.Thread(target=count_time).start()
        countdown_started = True  # Set the flag to True when countdown starts


def count_time(i=60):
    if i > -1:
        timer_text.config(text=f"{i} Second")
        window.after(1000, count_time, i - 1)  # Call count_time function after 1000 milliseconds (1 second)
    else:
        typing_text.config(state="disabled")  # Disable the typing_text box
        timer_text.config(text=f"Your Typing Speed is {correct_word_count} words per minutes. You misspelled "
                               f"{wrong_word_count} words", fg='red', font=(FONT_NAME, 20, "bold"))


FONT_NAME = 'Courier'
text_type = ("Typing speed is a valuable skill in today's digital age. Whether you're a student taking notes in class, "
             "an employee drafting emails, or a writer composing articles, being able to type quickly and accurately "
             "can significantly improve productivity. By honing your typing skills, you can save time and reduce "
             "errors, allowing you to focus more on the content you're creating. Typing speed tests are a great way "
             "to track your progress and identify areas for improvement. Practice regularly, and you'll soon find "
             "yourself typing with speed and precision. In the fast-paced world we live in, typing speed can be the "
             "difference between keeping up and falling behind. Whether you're engaged in online communication, "
             "coding, or data entry, the ability to type swiftly and efficiently is a valuable asset. Improving your "
             "typing speed not only enhances your productivity but also boosts your confidence in handling digital "
             "tasks. With practice and perseverance, you can increase your words-per-minute (WPM) rate and tackle "
             "challenges with ease. Take the time to practice regularly, and you'll soon find yourself typing "
             "effortlessly and achieving your goals faster than ever before.")

window = Tk()
window.title('Typing Speed Test')
window.config(padx=20, pady=20, bg='#987dbd')

Label(text='Typing speed Test', bg='#987dbd', fg='white', font=(FONT_NAME, 35, 'bold'), anchor="nw").grid(column=1,
                                                                                                          row=0)
timer_text = Label(text="00 Second", bg='#987dbd', fg='white', font=(FONT_NAME, 35, "bold"), anchor="nw")
timer_text.grid(column=1, row=1)

display_words = Text(width=50, height=10, bg='#401e6e', fg="white", highlightthickness=2, font=("Arial", 24))
display_words.grid(columnspan=3, row=2)
display_words.insert(INSERT, text_type)
display_words.config(state="disabled")

typing_text = Text(pady=5, width=20, height=1, bg='black', fg="white", highlightthickness=4, font=("Arial", 16))
typing_text.grid(column=1, row=3)
typing_text.bind("<Key>", handle_key_press)  # Bind handle_key_press function to any key press event

window.mainloop()
