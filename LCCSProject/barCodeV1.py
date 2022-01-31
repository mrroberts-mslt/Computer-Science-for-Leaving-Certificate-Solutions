runningTime = 0
output = 0

def on_button_pressed_a():
    global runningTime, output
    runningTime = 0
    basic.show_number(Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.LEFT))
    basic.pause(1000)
    basic.show_number(Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.RIGHT))
    Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 40)
    basic.pause(2000)
    Kitronik_Move_Motor.stop()
    output = runningTime / 1000
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(runningTime)
    if output < 3000:
        basic.show_string("Milk")
    else:
        basic.show_string("Jam")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global runningTime
    while Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.LEFT) < 100 or Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.RIGHT) < 100:
        runningTime += input.running_time()
basic.forever(on_forever)
