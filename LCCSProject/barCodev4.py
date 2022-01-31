#this code works except it keeps counting after the buggy has stopped if the buggy stops on black
runningTime = 0
lightSensor = 0

def on_button_pressed_a():
    global runningTime
    runningTime = 0
    Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 30)
    basic.pause(3000)
    Kitronik_Move_Motor.stop()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(runningTime)
    if runningTime > 2:
        basic.show_string("Milk")
    else:
        basic.show_string("Jam")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global lightSensor, runningTime
    lightSensor = Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.LEFT)
    basic.show_number(runningTime)
    while lightSensor < 20:
        runningTime = runningTime + 1
        break
basic.forever(on_forever)
