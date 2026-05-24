import customtkinter as ctk
from random import choice
import config as cfg

class GreetingsPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color = cfg.FRM_COLOR)
        self.controller = controller

        label_data = [
            ('Приветствую!', cfg.TXT_COLOR_1),
            ('Это игра "Викторина"', cfg.TXT_COLOR_2),
            ('Сыграем?', cfg.TXT_COLOR_1)
        ]

        for idx, (text, color) in enumerate (label_data):
            label = ctk.CTkLabel(
                self,
                text = text,
                font = ('Constantia', 27),
                text_color = color
            )
            label.place(relx = 0.5, rely = 0.3 + (0.15 * idx), anchor = 'c')

        button_data = [
            ('Не сейчас', self.controller.to_end),
            ('Давай!', lambda: self.controller.switch_to('RulesPage'))
        ]

        for idx, (text, command) in enumerate (button_data):
            button = ctk.CTkButton(
                self,
                **cfg.BTN_PARAMS,
                text = text,
                command = command
            )
            button.place(relx = 0.35 + (idx * 0.3), rely = 0.8, anchor = 'c')

class RulesPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color = cfg.FRM_COLOR)
        self.controller = controller

        label_data = [
            ('Правила очень просты:', cfg.TXT_COLOR_1),
            ('Я задам тебе несколько вопросов', cfg.TXT_COLOR_2),
            ('на самые разные темы', cfg.TXT_COLOR_1),
            ('а тебе нужно выбрать правильный ответ', cfg.TXT_COLOR_2),
            ('за каждый из которых', cfg.TXT_COLOR_1),
            ('тебе начисляется балл', cfg.TXT_COLOR_2),
            ('По итогу: считаем баллы', cfg.TXT_COLOR_1),
            ('Начнём?', cfg.TXT_COLOR_2)
        ]

        for idx, (text, color) in enumerate (label_data):
            label = ctk.CTkLabel(
                self,
                text = text,
                font = ('Constantia', 27),
                text_color = color
            )
            label.place(relx = 0.5, rely = 0.05 + (idx * 0.1), anchor = 'c')

        button_data = [
            ('Не сейчас', self.controller.to_end),
            ('Погнали', self.controller.create_game)
        ]

        for idx, (text, command) in enumerate (button_data):
            button = ctk.CTkButton (
                self,
                **cfg.BTN_PARAMS,
                text = text,
                command = command
            )
            button.place(relx = 0.35 + (idx * 0.3), rely = 0.9, anchor = 'c')

class QuizPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color = cfg.FRM_COLOR)
        self.controller = controller

        self.setup_variables()
        self.setup_ui()


    def setup_variables(self):
        self.index = 0
        self.boxes = []
        self.user_answers = []


    def setup_ui(self):
        self.question_frame = ctk.CTkFrame(
            self, fg_color = cfg.FRM_COLOR
        )
        self.question_frame.place(
            relx = 0, rely = 0.2,
            relwidth = 1.0, relheight = 0.3
        )

        self.box_frame = ctk.CTkFrame(self, fg_color = cfg.FRM_COLOR)
        self.box_frame.place(relx = 0, rely = 0.5, relwidth = 1.0, relheight = 0.3)

        self.x = ctk.IntVar(value = 0)

        for i in range (3):
            box = ctk.CTkRadioButton(
                self.box_frame,
                **cfg.BOX_PARAMS,
                variable = self.x,
                value = i
            )
            box.pack(pady = 10, anchor='c')
            self.boxes.append(box)

        self.question_label = ctk.CTkLabel(
            self.question_frame,
            text = '',
            font = ('Constantia', 27),
            text_color = cfg.TXT_COLOR_1
        )
        self.question_label.pack(pady = 10, fill = 'y', expand = True, anchor='c')

        self.labels = {}

        label_data = [
            ('step_label', cfg.TXT_COLOR_1, 0.25, 0.1),
            ('score_label', cfg.TXT_COLOR_2, 0.7, 0.1),
            ('comment_label', cfg.TXT_COLOR_1, 0.5, 0.9)
        ]

        for name, color, relx, rely in label_data:
            label = ctk.CTkLabel(
                self,
                text = '',
                font = ('Constantia', 27),
                text_color = color
            )
            label.place(relx = relx, rely = rely, anchor = 'c')
            self.labels[name] = label

        self.buttons = {}

        button_data = [
            ('back_button', 'Назад', self.go_back),
            ('go_button', 'Далее', self.give_feedback)
        ]

        for name, text, command in button_data:
            button = ctk.CTkButton(
                self,
                **cfg.BTN_PARAMS,
                text = text,
                command = command
            )
            self.buttons[name] = button

    def give_feedback(self):

        self.user_answers.append(self.x.get())

        box_params_1 = {
            "border_color": cfg.BTN_COLOR_1,
            "fg_color": cfg.BTN_COLOR_1,
            "border_width_unchecked": 5
        }

        box_params_2 = {
            "border_color": cfg.BTN_COLOR_4,
            "fg_color": cfg.BTN_COLOR_4,
            "border_width_unchecked": 5
        }

        for i in self.boxes:
            i.configure(state = 'disabled')
            if i.cget('value') == self.q['answer']:
                i.configure(**box_params_1)
            elif i.cget('value') == self.x.get():
                i.configure(**box_params_2)

        self.buttons['back_button'].place_forget()
        self.buttons['go_button'].place_forget()

        if self.x.get() == self.q['answer']:
            self.controller.score += 1
            score_text = f'Твои баллы: {self.controller.score}'
            comment_text_1 = f'{choice(cfg.RIGHT_COMMENTS)} {self.r}'
            self.labels['score_label'].configure(text = score_text)
            self.labels['comment_label'].configure(text = comment_text_1)
        else:
            comment_text_2 = f'{choice(cfg.WRONG_COMMENTS)} {self.r}'
            self.labels['comment_label'].configure(text = comment_text_2)

        self.after(3000, self.next_question)

    def go_forward(self):
        self.index += 1
        self.refresh_page()

    def go_back(self):
        if self.index == 0:
            self.controller.switch_to('RulesPage')
        elif self.index > 0:
            self.index -= 1
            self.refresh_page()

    def next_question(self):
        self.index += 1
        if self.index < len(cfg.QUESTIONS):
            self.refresh_page()
        else:
            self.controller.switch_to('FinalPage')

    def refresh_page(self):
        self.q = cfg.QUESTIONS[self.index]
        self.r = self.q['options'][self.q['answer']]
        is_answered = self.index < len(self.user_answers)

        if is_answered:
            current_value = self.user_answers[self.index]
            new_command = self.go_forward
        else:
            current_value = -1
            new_command = self.give_feedback
        self.x.set(current_value)
        self.buttons['go_button'].configure(command = new_command)

        for idx, btn in enumerate(self.boxes):
            if is_answered and idx == self.q['answer']:
                color, width = cfg.BTN_COLOR_1, 5
            elif is_answered and idx == current_value:
                color, width = cfg.BTN_COLOR_4, 5
            else:
                color, width = cfg.BTN_COLOR_2, 1

            btn.configure(
                state = 'disabled' if is_answered else 'normal',
                text = self.q['options'][idx],
                fg_color = color,
                border_color = color,
                border_width_unchecked = width
            )

        labels = self.labels
        buttons = self.buttons
        score_text = f'Твои баллы: {self.controller.score}'
        step_text = f'Вопрос номер: {self.index + 1}'

        back_coords = {"relx": 0.35, "rely": 0.9, "anchor": 'c'}
        go_coords = {"relx": 0.65, "rely": 0.9, "anchor": 'c'}

        labels['score_label'].configure(text = score_text)
        labels['step_label'].configure(text = step_text)
        self.question_label.configure(text = self.q['question'])
        labels['comment_label'].configure(text = '')
        buttons['back_button'].place(**back_coords)
        buttons['go_button'].place(**go_coords)

class MessagePage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color = cfg.FRM_COLOR)
        self.controller = controller

        self.label = ctk.CTkLabel (self, text = '',
        font = ('Constantia', 27), text_color = cfg.TXT_COLOR_1)
        self.label.place(relx = 0.5, rely = 0.5, anchor = 'c')

    def set_text(self, mode):
        if mode == 'loading':
            self.label.configure(text=choice(cfg.RPT_WORDS))
        else:
            self.label.configure(text=choice(cfg.FRW_WORDS))

class FinalPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color = cfg.FRM_COLOR)
        self.controller = controller

        self.score_label = ctk.CTkLabel (self, text = '',
        font = ('Constantia', 27), text_color = cfg.TXT_COLOR_1)
        self.score_label.place(relx = 0.5, rely = 0.35, anchor = 'c')

        repeat_label = ctk.CTkLabel (self, text = 'Хочешь сыграть снова?',
        font = ('Constantia', 27), text_color = cfg.TXT_COLOR_2)
        repeat_label.place(relx = 0.5, rely = 0.5, anchor = 'c')

        button_data = [
            ('Не сейчас', self.controller.to_end),
            ('Давай!', self.controller.create_game)
        ]

        for idx, (text, command) in enumerate (button_data):
            button = ctk.CTkButton(
                self,
                **cfg.BTN_PARAMS,
                text = text,
                command = command
            )
            button.place(relx = 0.35 + (idx * 0.3), rely = 0.75, anchor = 'c')

    def get_data(self, score):
        text = f'Ты набрал: {score} баллов из {len(cfg.QUESTIONS)}'
        self.score_label.configure(text = text)

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Моя Викторина')
        self.geometry ('600x500+800+450')
        self.resizable (False, False)
        self.attributes ('-alpha', 0.9)

        self.main = ctk.CTkFrame(self)
        self.main.pack(fill = 'both', expand = True)

        self.score = 0
        self.pages = {}
        self.current_frame = None

        for F in (GreetingsPage, RulesPage, QuizPage, MessagePage, FinalPage):
            page_name = F.__name__
            self.pages[page_name] = F(master = self.main, controller=self)

        self.switch_to("GreetingsPage")

    def switch_to(self, page_name):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.pages[page_name]
        if page_name == "FinalPage":
            self.pages['FinalPage'].get_data(self.score)
            self.pages["QuizPage"].user_answers = []
        self.current_frame.pack(fill="both", expand=True)

    def to_end(self):
        self.pages["MessagePage"].set_text('farewell')
        self.switch_to("MessagePage")
        self.after(3000, self.destroy)

    def create_game(self):
        quiz = self.pages["QuizPage"]
        if not quiz.user_answers:
            self.pages["MessagePage"].set_text('loading')
            self.switch_to("MessagePage")
            self.score = 0
            quiz.index = 0
            quiz.user_answers = []
            quiz.refresh_page()
            self.after(3000, lambda: self.switch_to("QuizPage"))
        else:
            self.switch_to("QuizPage")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

#testing
#testing