import turtle
import pandas

FONT = "Canbera", 8, "normal"

screen = turtle.Screen()
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()

guess = turtle.Turtle()
guess.penup()
guess.hideturtle()

data = pandas.read_csv("50_states.csv")
states = data["state"]
# print(states)

correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # missing_states = []
        # for state in states:
        #     if state not in correct_guesses:
        #         missing_states.append(state)
        missing_states = [state for state in states if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    for state in states:
        if answer_state == state:
            correct_guesses.append(answer_state)
            state_info = data[data.state == state]
            x_cor = int(state_info["x"])
            y_cor = int(state_info["y"])
            guess.goto(x=x_cor, y=y_cor)
            guess.write(f"{answer_state}", align="center", font=FONT)




# this is used in order to get x and y coordinates of states in image
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

# screen.exitonclick()