import random
import PySimpleGUI as sg

class MagicNumberGame:
    def __init__(self):
        self.number_range = range(1, 6)
        self.magic_number = random.choice(self.number_range)
        self.attempts = 0

        self.layout = [
            [sg.Text("Вгадай число!", font=("Helvetica", 16))],
            [sg.Text("Введіть число від 1 до 5: ")],
            [sg.InputText(key="user_guess")],
            [sg.Text("", size=(20, 2), key="output_text")],
            [sg.Button("Вгадати"), sg.Button("Вийти")]
        ]

        self.window = sg.Window("Гра Вгадай число", self.layout)

    def is_valid_guess(self, user_guess):
        try:
            user_guess = int(user_guess)
            return 1 <= user_guess <= 5
        except ValueError:
            return False

    def update_output_text(self, text):
        self.window["output_text"].update(text)

    def play_game(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED or event == "Вийти":
                break

            if event == "Вгадати":
                user_guess = values["user_guess"]

                if not self.is_valid_guess(user_guess):
                    self.update_output_text("Напишіть число в межах від 1 до 5.")
                    continue

                user_guess = int(user_guess)
                self.attempts += 1

                if user_guess < self.magic_number:
                    self.update_output_text("Число більше.")
                elif user_guess > self.magic_number:
                    self.update_output_text("Число менше.")
                else:
                    self.update_output_text(f"Ви вгадали число {self.magic_number} за {self.attempts} спроб.")
                    self.window["Вгадати"].update(disabled=True)

    def close_window(self):
        self.window.close()

def main():
    game = MagicNumberGame()
    game.play_game()
    game.close_window()

if __name__ == "__main__":
    main()