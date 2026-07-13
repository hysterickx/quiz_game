import customtkinter as ctk
from random import choice
import config as cfg
from functools import partial


class StaticPages(ctk.CTkFrame):
    def __init__(self, master, controller, page_name):
        super().__init__(master, fg_color=cfg.COLOR_DARK)

        self.controller = controller
        self.page_name = page_name
        page_config = cfg.STATIC_PAGES_DATA[page_name]

        label_data = page_config['labels']
        for text, color, font, relx, rely in label_data:
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=font
            )
            label.place(relx=relx, rely=rely, anchor='c')

        button_data = page_config['buttons']
        for text, info, relx, rely in button_data:
            button = ctk.CTkButton(
                self,
                text=text,
                command=partial(self.send_info, info),
                **cfg.BTN_PARAMS
            )
            button.place(relx=relx, rely=rely, anchor='c')

    def send_info(self, info):
        self.controller.handle_info(
            self.page_name, info
        )


class QuizPage(ctk.CTkFrame):
    def __init__(self, master, controller, page_name=None):
        super().__init__(master, fg_color=cfg.COLOR_DARK)
        self.controller = controller

        frames = {}
        frame_data = cfg.QUIZ_PAGE_DATA['frames']
        for name, color, relx, rely, relwidth, relheight in frame_data:
            frame = ctk.CTkFrame(
                self,
                fg_color=color
            )
            frame.place(
                relx=relx, rely=rely,
                relwidth=relwidth, relheight=relheight
            )
            frames[name] = frame

        self.labels = {}
        label_data = cfg.QUIZ_PAGE_DATA['labels']
        for name, color, font, relx, rely in label_data:
            label = ctk.CTkLabel(
                self,
                font=font,
                text_color=color
            )
            label.place(relx=relx, rely=rely, anchor='c')
            self.labels[name] = label

        self.question_lbl = ctk.CTkLabel(
            frames['question_frm'],
            font=cfg.FONT_LARGE,
            text_color=cfg.COLOR_LIME
        )
        self.question_lbl.pack(
            pady=10, fill='y',
            expand=True, anchor='c'
        )

        self.boxes = []
        self.choice_var = ctk.IntVar(value=0)
        for widget in range(3):
            box = ctk.CTkRadioButton(
                frames['answer_frm'],
                variable = self.choice_var,
                value=widget,
                **cfg.BOX_PARAMS,
            )
            box.pack(pady = 10, anchor='c')
            self.boxes.append(box)

        self.button = ctk.CTkButton(
            self,
            text='Далее',
            command=self.send_info,
            **cfg.BTN_PARAMS
        )

    def send_info(self):
        self.controller.handle_info(
            'QuizPage', self.choice_var.get()
        )

    def show_feedback(self, status, index):
        self.button.place_forget()

        part = cfg.GAME_DATA[index-1]
        answer = part['answers'][part['right_answer']]
        self.labels['comment_lbl'].configure(
            text=f'{choice(cfg.GAME_MESSAGES[status])} {answer}'
        )

        for box in self.boxes:
            box.configure(state='disabled')

        wrong_box = self.boxes[self.choice_var.get()]
        wrong_box.configure(
            border_color=cfg.COLOR_RED,
            fg_color=cfg.COLOR_RED,
            border_width_unchecked=5
        )
        right_box = self.boxes[part['right_answer']]
        right_box.configure(
            border_color=cfg.COLOR_LIME,
            fg_color=cfg.COLOR_LIME,
            border_width_unchecked=5
        )

    def show_next_question(self, index, score):
        self.labels['step_lbl'].configure(
            text=f'Вопрос номер: {index+1}'
        )
        self.labels['score_lbl'].configure(
            text=f'Твои баллы: {score}'
        )
        self.question_lbl.configure(
            text=cfg.GAME_DATA[index]['question']
        )
        self.labels['comment_lbl'].configure(text='')
        answers_list = cfg.GAME_DATA[index]['answers']
        for idx, box in enumerate(self.boxes):
            box.configure(
                text=answers_list[idx],
                state='normal',
                **cfg.BOX_PARAMS
            )
        self.choice_var.set(0)
        self.button.place(relx=0.5, rely=0.9, anchor='c')


class FinalPage(ctk.CTkFrame):
    def __init__(self, master, controller, page_name=None):
        super().__init__(master, fg_color=cfg.COLOR_DARK)

        self.controller = controller

        self.labels = {}
        label_data = cfg.FINAL_PAGE_DATA['labels']
        for name, text, color, font, relx, rely in label_data:
            label = ctk.CTkLabel(
                self,
                text=text,
                font=font,
                text_color=color
            )
            label.place(relx=relx, rely=rely, anchor='c')
            self.labels[name] = label

        button_data = cfg.FINAL_PAGE_DATA['buttons']
        for text, info, relx, rely in button_data:
            button = ctk.CTkButton(
                self,
                text=text,
                command=partial(self.send_info, info),
                **cfg.BTN_PARAMS
            )
            button.place(relx=relx, rely=rely, anchor='c')

    def send_info(self, info):
        self.controller.handle_info(
            'FinalPage', info
        )

    def change_message(self, score):
        self.labels['score_lbl'].configure(
            text=f'Ты набрал {score} баллов из 5!'
        )


class MessagePage(ctk.CTkFrame):
    def __init__(self, master, controller, page_name=None):
        super().__init__(master, fg_color=cfg.COLOR_DARK)

        self.message_lbl = ctk.CTkLabel(
            self,
            text='',
            text_color=cfg.COLOR_LIME,
            font=cfg.FONT_LARGE
        )
        self.message_lbl.place(
            relx=0.5, rely=0.5, anchor='c'
        )

    def change_message(self, stage):
        self.message_lbl.configure(
            text=choice(cfg.DELAY_MESSAGES[stage])
        )


class MainLogic:
    def __init__(self):
        self.index = 0
        self.score = 0

    def give_data(self, user_choice):
        part = cfg.GAME_DATA[self.index]
        right_answer = part['right_answer']
        if user_choice == right_answer:
            status = 'right'
            self.score += 1
        else:
            status = 'wrong'
        self.index += 1
        return status, self.index, self.score

    def update_variables(self):
        self.index = 0
        self.score = 0
        return self.index, self.score


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Моя Викторина')
        self.geometry('600x500+800+450')
        self.resizable(False, False)
        self.attributes('-alpha', 0.9)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(
            fill = 'both', expand = True
        )
        self.logic = MainLogic()

        self.pages = {}
        self.current_frame = None
        page_types = [
            ('GreetingsPage', StaticPages),
            ('RulesPage', StaticPages),
            ('QuizPage', QuizPage),
            ('FinalPage', FinalPage),
            ('MessagePage', MessagePage)
        ]

        for page_name, page_class in page_types:
            self.pages[page_name] = page_class(
                self.main_frame,
                self,
                page_name
            )
        self.switch_to("GreetingsPage")

    def switch_to(self, page_name):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.pages[page_name]
        self.current_frame.pack(fill="both", expand=True)

    def handle_info(self, page, info):
        go_to_rules = partial(self.switch_to, 'RulesPage')

        router = {
            ('GreetingsPage', 'exit'):  self.exit_app,
            ('GreetingsPage', 'next'):  go_to_rules,
            ('RulesPage', 'exit'):      self.exit_app,
            ('RulesPage', 'start'):     self.start_app,
            ('FinalPage', 'exit'):      self.exit_app,
            ('FinalPage', 'start'):     self.start_app
        }

        if method := router.get((page, info)):
            return method()
        self.transfer_data(info)

    def transfer_data(self, info):
        status, index, score  = self.logic.give_data(info)
        q_page = self.pages['QuizPage']
        if index == len(cfg.GAME_DATA):
            q_page.show_feedback(status, index)
            self.pages['FinalPage'].change_message(score)
            self.after(
                3000,
                lambda: self.switch_to('FinalPage')
            )
        else:
            q_page.show_feedback(status, index)
            self.after(
                3000,
                lambda: q_page.show_next_question(index, score)
            )

    def exit_app(self):
        self.pages["MessagePage"].change_message('farewell')
        self.switch_to("MessagePage")
        self.after(3000, self.destroy)

    def start_app(self):
        self.pages["MessagePage"].change_message('loading')
        self.switch_to("MessagePage")
        index, score = self.logic.update_variables()
        self.pages['QuizPage'].show_next_question(index, score)
        self.after(3000, lambda: self.switch_to("QuizPage"))


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()