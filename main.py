from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, NumericProperty
from kivy.core.text import LabelBase
from functools import partial

Window.size = (350, 550)

class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign: StringProperty
    font_size = 17

class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign: StringProperty
    font_size = 17

class CCITChatBot(MDApp):
    scheduled_event = None  # Add this line to store the scheduled event
    responses = {
        "help": "Here is the list of the queries I am programmed to answer:\n1. What are the programs of CCIT? (Programs)\n2. Who developed you? (Developers)\n3. Tell me more about a specific program (BSCS, BSIT, BLIS, DCT)\n4. What are the admission requirements (Requirements)",
        "programs": "Here are the following programs of CCIT:\n1. Bachelor of Science in Computer Science (BSCS)\n2.  Bachelor of Science in Information Technology (BSIT)\n3. Bachelor of Library and Information Science (BLIS)\n4. Diploma in Computer Technology (DCT)\nIf you want to know a program even further, type the program code!",
        "hello": "Greetings! How can I help you today?",
        "hi": "Greetings! How can I help you today?",
        "bscs": "The BSCS Program prepares graduates to design and create algorithmically complex software and develop new and effective algorithms for solving computing problems.\nThe career prospects for this program are:\n\nPRIMARY JOB ROLES:\n- Software Engineer\n- Systems Software Developer\n- Research & Dev't Computing Professional\n- Applications Software Developer\n- Computer Programmer\n\nSECONDARY JOB ROLES:\n- System Analyst\n- Data Analyst\n- Quality Assurance Specialist\n- Software Support Specialist\n\nIf you want to know other programs, just type the program code!",
        "bsit": "The BSInfoTech Program prepares graduates to address user needs involving the selection, development, application, integration and management of computing within an organization.\nThe career prospects for this program are:\n\nPRIMARY JOB ROLES:\n- Web and Applications Developer\n- Junior Database Administrator\n- Systems Administrator\n- Network Engineer\n- Junior Information Security Admin\n- Systems Integration Personnel\n- IT Audit Assistant\n- Technical Support Specialist\n\nSECONDARY JOB ROLES\n- Systems Analyst\n- Quality Assurance Specialist\n- Computer Programmer\n\nIf you want to know other programs, just type the program code!",
        "blis": "The BLIS Program prepares graduates to apply information technology to basic library operations and functions. Moreover, they are trained to harness a range of bibliographical and online tools to support teaching, research, and other services.\nThe career prospects for the program are:\n\nREGISTERED LIBRARIAN (Passed the Librarian Licensure Examination):\n- Librarian\n- Abstractor\n-Archivist\n- Cataloger\n- Indexer\n-Records Manager\n\nBLIS GRADUATE:\n- Bibliographer\n- Copy Cataloger\n- Documentation Officer\n- Library Applications Developer\n- Library Assistant\n\nIf you want to know other programs, just type the program code!",
        "dct": "The Diploma in Computer Technology is a Two-Year Non-Degree Program that prepares graduates to perform computer systems servicing and management of computer networks.\nThe career prospects for this program are:\n- Computer Laboratory Technician\n- Management Information System (MIS) Personnel\n- Technical Assistant\n - Computer Programmer\n- Web Developer\n\nIf you want to know other programs, just type the program code!",
        "qualification": "Here are the admission requirements for the programs:\n1. Grade 12 General Weighted Average of at least 80% (for BSCS, BSIT, BLIS)\n2. Senior Highschool Graduate (for DCT)",
        "developers": "I was developed by the following students:\n- Allain Alonzo\n- Eric John Cruz\n- Marc Owen Esteban\n- Rafael Mendoza\n- Rembert Tambua",
        "tanginamo": "Aba! Aba! Tangina mo ring, gago ka! Nawa'y mababa ang grado na ibibigay sa'yo!"
    }

    def change_screen(self, name):
        screen_manager.current = name

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("Main.kv"))
        screen_manager.add_widget(Builder.load_file("Chats.kv"))
        return screen_manager

    def get_response(self, command_label):
        value = command_label.text.lower()
        return self.responses.get(value, 'I am unable to respond to the query. Please check the spelling or type "Help" for the list of queries I am programmed to answer.')

    def response(self, command_label, *args):
        response_text = self.get_response(command_label)
        screen_manager.get_screen('chats').chat_list.add_widget(Response(text=response_text, size_hint_x=.75))

    def send(self):
        if screen_manager.get_screen('chats').text_input != "":
            value = screen_manager.get_screen('chats').text_input.text
            if len(value) < 6:
                size = .22
                halign = "left"
            elif len(value) < 11:
                size = .32
                halign = "left"
            elif len(value) < 16:
                size = .45
                halign = "left"
            elif len(value) < 21:
                size = .58
                halign = "left"
            elif len(value) < 26:
                size = .71
                halign = "left"
            else:
                size = .77
                halign = "left"
            command_label = Command(text=value, size_hint_x=size, halign=halign)
            screen_manager.get_screen('chats').chat_list.add_widget(command_label)
            self.scheduled_event = Clock.schedule_once(partial(self.response, command_label), 2)
            screen_manager.get_screen('chats').text_input.text = ""  # Clear the text_input

if __name__ == '__main__':
    CCITChatBot().run()
