from turtle import Turtle, Screen
from statedisplay import StateDisplay

screen = Screen()
screen.colormode(255)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

country_turtle = Turtle()
country_turtle.shape(image)
state_display = StateDisplay()

score = 0
states_guessed = []
while len(states_guessed) < 50:
    answer_state = screen.textinput(title=f"Guess the State: {len(states_guessed)}/50", prompt="Can you name another "
                                                                                               "state? \n If you'd like"
                                                                                               " to exit, type 'Exit."
                                                                                               "'").title()
    if answer_state == "Exit":
        break
    elif state_display.state_initializer(answer_state):
        states_guessed.append(answer_state)
    else:
        print("boo >:c")

study_guide(states_guessed)