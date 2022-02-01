"""

This detects difference between sensors and increments time var. needs adjusting e.g pause and light change val

"""

def on_button_pressed_a():
    basic.pause(1000)
    Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 30)
    basic.pause(3000)
    Kitronik_Move_Motor.stop()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.pause(1000)
    basic.show_number(time)
    if time <= 10:
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        # . . . #
        """)
    elif time <= 20:
        basic.show_leds("""
            # # # # #
                        # . . . #
                        # . . . #
                        # . . . #
                        # # # # #
        """)
    else:
        basic.show_leds("""
            # # . # #
                        . # # # .
                        # . . . #
                        . # . # .
                        . . # . .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

lightChange = 0
rightLightSensor = 0
leftLightSensor = 0
time = 0
time = 0

def on_forever():
    global leftLightSensor, rightLightSensor, lightChange, time
    basic.show_number(time)
    leftLightSensor = Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.LEFT)
    basic.pause(200)
    rightLightSensor = Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.RIGHT)
    lightChange = leftLightSensor - rightLightSensor
    if lightChange > 5:
        time = time + 1
basic.forever(on_forever)
