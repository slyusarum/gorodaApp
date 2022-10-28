import json
import random


class Game:
    current_letter = str
    answer_state = bool
    towns = []
    player_win = bool
    bad_chars = ['й', 'ы', 'ь']
    used_towns = []

    def __init__(self):
        self.player_turn = bool(random.randint(0, 1))
        self.end_game_state = False
        self.player_win = False
        self.current_letter = ""
        self.towns = self.get_list_of_towns()["towns"]
        self.towns = set(self.towns)
        self.towns = list(self.towns)
        self.original_towns = self.get_list_of_towns()["towns"]
        self.original_towns = set(self.towns)
        self.original_towns = list(self.towns)

    def check_repeat(self, answer):
        if answer in self.get_used_towns():
            print("Такой город уже был!")
            return False
        else:
            return True

    def set_player_win(self):
        self.player_win = True

    def get_player_win(self):
        if (self.player_win):
            return True
        else:
            return False

    def check_town(self, answer):
        if answer in self.get_towns():
            return True
        else:
            print(self.get_towns())
            print("Такого города не существует")
            return False

    def answer_rebuild(self,answer):
        if (len(answer.split()) > 1):
            buff = answer
            answer = ""
            for name in buff.split():
                if answer != "":
                    answer += " "
                answer += name.capitalize()
        else:
            answer = answer.capitalize()
        return (answer)

    def pull_answer(self, answer):
        answer = self.answer_rebuild(answer)
        if self.analyse_answer(answer):
            self.make_turn(answer)
            return True
        else:
            return False

    def analyse_answer(self, answer):
        state = False
        if type(answer) not in [str]:
            print("Название города должно состоять из букв!")
            return state
        if self.check_repeat(answer):
            if self.check_town(answer):
                if self.check_first_letter(answer):
                    if self.check_last_letter(answer):
                        self.set_current_letter(answer[-1])
                    else:
                        self.set_current_letter(answer[-2])
                    state = True
        return state

    def check_first_letter(self, answer):
        if answer.startswith(self.get_current_letter()):
            return True
        else:
            print("Выбран неверный город")
            return False

    def bot_choose_town(self):
        bot_towns = []
        if self.get_current_letter() == '':
            bot_answer = self.towns[random.randint(0, len(self.towns)-1)]
            self.analyse_answer(bot_answer)
            return bot_answer
        else:
            for town in self.towns:
                if town[0] == self.get_current_letter():
                    bot_towns.append(town)
            if not bot_towns:
                print("Бот не может найти ответ")
                return ""
            bot_answer = bot_towns[random.randint(0, len(bot_towns) - 1)]
        if (not bot_answer in self.get_used_towns()):
            self.analyse_answer(bot_answer)
            del bot_towns
            self.make_turn(bot_answer)
            return bot_answer

    def make_turn(self, answer):
        self.pull_info_in_used_towns(answer)
        self.remove_from_towns(answer)
        return True

    def print_info(self):
        print(self.used_towns)
        print(self.towns)

    def check_in_original_towns(self, answer):
        if (answer in self.original_towns):
            return True
        else:
            return False

    def game_reload(self):
        self.player_win = False
        self.current_letter = ''
        self.towns = []
        for i in self.original_towns:
            self.towns.append(i)
        self.used_towns = []

    def set_current_letter(self, letter):
        self.current_letter = letter.upper()

    def set_end_game_state(self):
        self.end_game_state = True

    def pull_info_in_used_towns(self, town):
        self.used_towns.append(town)

    def remove_from_towns(self, town):
        self.towns.remove(town)

    def set_player_turn(self, argument):
        self.player_turn = argument

    def get_player_turn(self):
        return self.player_turn

    def get_end_game_state(self):
        return self.end_game_state

    def get_current_letter(self):
        return self.current_letter

    def get_used_towns(self):
        return self.used_towns

    def get_towns(self):
        return self.towns

    def get_bad_chars(self):
        return self.bad_chars

    @staticmethod
    def get_list_of_towns():
        target_filename = "towns.txt"
        with open(target_filename, "r", encoding='utf-8') as file:
            text = file.read()
            data = json.loads(text)
        return data

    def check_last_letter(self, answer):  # Проверяем последнюю букву
        if answer[-1] in self.get_bad_chars():
            return False
        else:
            return True