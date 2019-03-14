from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]

def check_point(x,y):
    if x[0] in range(y[0],y[0]+y[2]) and x[1] in range(y[1],y[1]+y[3]):
        return True
    else:
        return False


def get_shapes():
    return shapes


def generate_quiz():
    return [
                choice(['GREEN','YELLOW','RED','BLUE']),
                choice(['#4CAF50','#FFD600','#C62828','#3F51B5']),
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):

    user_check= [x,y]
    print(user_check)
    print(quiz_type)
    check_answer = None
    if quiz_type == 0:
        for shape in shapes:
            if text == shape['text'].upper():
                if check_point(user_check,shape['rect']):
                    check_answer = True
                else:
                    check_answer = False

    elif quiz_type == 1:
        for shape in shapes:
            if color == shape['color']:
                if check_point(user_check,shape['rect']):
                    check_answer = True
                else:
                    check_answer = False
    return check_answer
