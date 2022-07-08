import pandas
from turtle import Turtle

STATE_DATA = pandas.read_csv("50_states.csv")
STATES = STATE_DATA.state.to_list()


def study_guide(states_guessed):
    states = []
    x = []
    y = []

    for state_ in STATES:
        if state_ not in states_guessed:
            states.append((STATE_DATA[STATE_DATA.state == state_]).state.item())
            x.append(int(STATE_DATA[STATE_DATA.state == state_].x))
            y.append(int(STATE_DATA[STATE_DATA.state == state_].y))

    study_list = {"state": states, "x": x, "y": y}
    study_list_data_frame = pandas.DataFrame(study_list)
    study_list_data_frame.to_csv("StudyList.csv")


class StateDisplay:
    def __init__(self):
        self.states_on_board = []

    def state_initializer(self, user_answer):
        if user_answer in STATES:
            self.get_state_turtle(user_answer)
            return True
        else:
            return False

    @staticmethod
    def get_state_turtle(correct_answer):
        new_state_data = STATE_DATA[STATE_DATA.state == correct_answer]
        new_state_name = Turtle()
        new_state_name.hideturtle()
        new_state_name.penup()
        new_state_name.color(0, 0, 0)
        new_state_name.goto(int(new_state_data.x), int(new_state_data.y))
        new_state_name.write(new_state_data.state.item(), align="center")
