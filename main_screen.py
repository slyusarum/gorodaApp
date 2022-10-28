from tkinter import *


def auto_lose():
    create_endgame_frame()


def reboot_button_click():
    game_session.game_reload()
    main_frame.place_forget()
    end_frame.place_forget()
    create_main_game_frame()
    set_start_labels()


def enter_button_click():
    temp = entry_space.get()
    if game_session.pull_answer(temp):
        entry_space.delete(0, END)
        new_entry = game_session.bot_choose_town()
        if (new_entry == ""):
            game_session.set_player_win()
            create_endgame_frame()
        else:
            town_title.configure(text="Опоннент ответил: " + new_entry)
            letter_title.configure(text="Вам на " + game_session.get_current_letter())
    else:
        if (game_session.check_in_original_towns(temp)):
            if not game_session.check_first_letter(temp):
                town_title.configure(text='Выбран неверный город')
            else:
                town_title.configure(text='Такой город уже был')
        town_title.configure(text='Ошибка ввода')


def start_button_click():
    create_main_game_frame()


def set_start_labels():
    if (game_session.get_player_turn()):
        new_entry = game_session.bot_choose_town()
        town_title.configure(text="Опоннент начинает: " + new_entry)
        letter_title.configure(text="Вам на " + game_session.get_current_letter())
    else:
        town_title.configure(text="Вы начинаете: ")
        letter_title.configure(text="Выбирайте любой город ")


def create_main_game_frame():
    start_frame.place_forget()
    end_frame.place_forget()
    main_frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
    main_title_main.pack(anchor='n', padx=1, pady=1)
    set_start_labels()
    town_title.pack(anchor='n')
    letter_title.pack(anchor='n')
    lose_button.pack(side=BOTTOM, anchor='center', pady=10)
    enter_button.pack(side=BOTTOM, anchor='center', pady=10)
    entry_space.focus()
    entry_space.pack(side=BOTTOM)


def create_start_game_frame():
    start_frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
    main_title_start.pack(side=TOP, padx=1, pady=1)
    start_button.pack(side=BOTTOM, pady=10)


def create_endgame_frame():
    start_frame.place_forget()
    main_frame.place_forget()
    end_frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
    if (not game_session.get_player_win()):
        state_text = 'Вы проиграли'
    else:
        state_text = 'Вы победили'

    end_title.configure(text=state_text)
    end_title.pack(anchor='center')
    reboot_button.pack(side=BOTTOM, anchor='center', pady=10)


game_session = Game()
window = Tk()
window.title('Города')
window.geometry('640x400')

start_frame = Frame(window, bg='gray')
end_frame = Frame(window, bg='gray')
main_frame = Frame(window, bg='gray')
main_title_end = Label(start_frame, text='Игра города', bg='gray', font=32)
main_title_start = Label(start_frame, text='Игра города', bg='gray', font=32)
main_title_main = Label(main_frame, text='Игра города', bg='gray', font=32)
town_title = Label(main_frame, text='', font=32)
letter_title = Label(main_frame, text='', font=32)
end_title = Label(end_frame, text='', font=46)
reboot_button = Button(end_frame, text="Попробовать снова", command=reboot_button_click)
enter_button = Button(main_frame, text="Ввести ответ", command=enter_button_click)
start_button = Button(start_frame, text="Начать Игру", command=start_button_click)
lose_button = Button(main_frame, text="Сдаться", command=auto_lose)
entry_space = Entry(main_frame, width=20, font=32, justify='center')

create_start_game_frame()

window.mainloop()