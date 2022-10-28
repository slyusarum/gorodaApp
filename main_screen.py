from tkinter import *

def create_start_game_frame():
    start_frame.place(relx=0.01,rely = 0.01, relwidth = 0.98, relheight = 0.98)
    main_title_start.pack(side = TOP, padx=1, pady=1)
    start_button.pack(side = BOTTOM, pady = 10)

    

window = Tk()
window.title('Города')
window.geometry('640x400')

start_frame = Frame(window,bg='gray')
end_frame = Frame(window,bg='gray')
main_frame = Frame(window,bg='gray')
main_title_end = Label(start_frame, text='Игра города', bg='gray', font=32)
main_title_start = Label(start_frame, text='Игра города', bg='gray', font=32)
main_title_main = Label(main_frame, text='Игра города', bg='gray', font=32)
town_title = Label(main_frame, text='', font=32)
letter_title = Label(main_frame, text='', font=32)
end_title = Label(end_frame, text ='', font=46 )
reboot_button = Button(end_frame, text="Попробовать снова", command = reboot_button_click)
enter_button = Button(main_frame, text="Ввести ответ", command = enter_button_click)
start_button = Button(start_frame, text="Начать Игру", command = start_button_click)
lose_button = Button(main_frame, text="Сдаться", command = auto_lose)
entry_space = Entry(main_frame,width = 20, font=32, justify = 'center')

create_start_game_frame()








window.mainloop()