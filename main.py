import customtkinter as ctk
from random import choice
import config as cfg
from functools import partial


class StaticPages(ctk.CTkFrame):
    def __init__(self, master, controller, page_name):
        super().__init__(master, fg_color=cfg.COLOR_DARK)

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
                command=partial(
                    controller.handle_info,
                    page_name,
                    info
                ),
                **cfg.BTN_PARAMS
            )
            button.place(relx=relx, rely=rely, anchor='c')

class QuizPage(ctk.CTkFrame):
    def __init__(self, master, controller, page_name=None):
        super().__init__(master, fg_color=cfg.COLOR_DARK)
        self.controller = controller

        self.frames = {}
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
            self.frames[name] = frame

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

        self.question_label = ctk.CTkLabel(
            self.frames['question_frame'],
            font=cfg.FONT_MEDIUM,
            text_color=cfg.COLOR_LIME
        )
        self.question_label.pack(
            pady=10, fill='y',
            expand=True, anchor='c'
        )

        self.boxes = []
        self.choice_var = ctk.StringVar(value='0')
        for widget in range(3):
            box = ctk.CTkRadioButton(
                self.frames['answer_frame'],
                variable = self.choice_var,
                **cfg.BOX_PARAMS,
            )
            box.pack(pady = 10, anchor='c')
            self.boxes.append(box)

        self.buttons = []
        button_data = cfg.QUIZ_PAGE_DATA['buttons']
        for text, info, relx, rely in button_data:
            button = ctk.CTkButton(
                self,
                text=text,
                command=partial(
                    self.controller.handle_info,
                    'QuizGame',
                    'info'
                ),
                **cfg.BTN_PARAMS
            )
            button.place(relx=relx, rely=rely, anchor='c')
            self.buttons.append(button)


class MessagePage(ctk.CTkFrame):
    def __init__(self, master, controller, page_name=None):
        super().__init__(master, fg_color=cfg.COLOR_DARK)

        self.message_lbl = ctk.CTkLabel(
            self,
            text='',
            text_color=cfg.COLOR_LIME,
            font=cfg.FONT_LARGE
        )
        self.message_lbl.place(relx=0.5, rely=0.5, anchor='c')

    def change_message(self, stage):
        self.message_lbl.configure(
            text=choice(cfg.DELAY_MESSAGES[stage])
        )


class MainLogic:
    def __init__(self):
        self.index = 0


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Моя Викторина')
        self.geometry('600x500+800+450')
        self.resizable(False, False)
        self.attributes('-alpha', 0.9)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill = 'both', expand = True)

        self.pages = {}
        self.current_frame = None
        page_types = [
            ('GreetingsPage', StaticPages),
            ('RulesPage', StaticPages),
            ('QuizPage', QuizPage),
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
            ('RulesPage', 'start'):     self.start_app
        }

        if method := router.get((page, info)):
            return method()
        self.transfer_data(page, info)

    def transfer_data(self, page, info):
        self.switch_to('QuizPage')


    def exit_app(self):
        self.pages["MessagePage"].change_message('farewell')
        self.switch_to("MessagePage")
        self.after(3000, self.destroy)

    def start_app(self):
        self.pages["MessagePage"].change_message('loading')
        self.switch_to("MessagePage")
        self.after(3000, lambda: self.switch_to("QuizPage"))


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()