import turtle

import pandas

screen = turtle.Screen()
screen.title("US States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()

game_is_on = True
states_count = len(states_data)
guessed_states = []
while game_is_on:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{states_count} States guessed",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        df = pandas.DataFrame(missing_states)
        df.to_csv("missed_states.csv")
        break
    if answer_state in all_states:
        state_data = states_data[states_data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        guessed_states.append(answer_state)


screen.exitonclick()



# Get State Coordinates based on the image
# def get_mouse_click_point(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_point)
# turtle.mainloop()

