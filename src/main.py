# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       chaaranathb                                                  #
# 	Created:      2/2/2024, 9:39:50 PM                                         #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

#region VEXcode Generated Robot Configuration
from vex import *
import random

# Brain should be defined by default
brain=Brain()

# Robot configuration code
left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_6_1, True)
left_motor_b = Motor(Ports.PORT5, GearSetting.RATIO_6_1, True)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)
right_motor_a = Motor(Ports.PORT9, GearSetting.RATIO_6_1, False)
right_motor_b = Motor(Ports.PORT10, GearSetting.RATIO_6_1, False)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 295, 40, MM, 1)
bumper_a = Bumper(brain.three_wire_port.a)
controller_1 = Controller(PRIMARY)
catapult = Motor(Ports.PORT3, GearSetting.RATIO_36_1, False)
left_wing = Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)
right_wing = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")



# define variables used for controlling motors based on controller inputs
drivetrain_l_needs_to_be_stopped_controller_1 = False
drivetrain_r_needs_to_be_stopped_controller_1 = False

# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
    global drivetrain_l_needs_to_be_stopped_controller_1, drivetrain_r_needs_to_be_stopped_controller_1, remote_control_code_enabled
    # process the controller input every 20 milliseconds
    # update the motors based on the input values
    while True:
        if remote_control_code_enabled:

            # calculate the drivetrain motor velocities from the controller joystick axies
            # left = axis3
            # right = axis2
            drivetrain_left_side_speed = controller_1.axis3.position()
            drivetrain_right_side_speed = controller_1.axis2.position()

            # check if the value is inside of the deadband range
            if drivetrain_left_side_speed < 5 and drivetrain_left_side_speed > -5:
                # check if the left motor has already been stopped
                if drivetrain_l_needs_to_be_stopped_controller_1:
                    # stop the left drive motor
                    left_drive_smart.stop()
                    # tell the code that the left motor has been stopped
                    drivetrain_l_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the left motor next
                # time the input is in the deadband range
                drivetrain_l_needs_to_be_stopped_controller_1 = True
            # check if the value is inside of the deadband range
            if drivetrain_right_side_speed < 5 and drivetrain_right_side_speed > -5:
                # check if the right motor has already been stopped
                if drivetrain_r_needs_to_be_stopped_controller_1:
                    # stop the right drive motor
                    right_drive_smart.stop()
                    # tell the code that the right motor has been stopped
                    drivetrain_r_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the right motor next
                # time the input is in the deadband range
                drivetrain_r_needs_to_be_stopped_controller_1 = True

            # only tell the left drive motor to spin if the values are not in the deadband range
            if drivetrain_l_needs_to_be_stopped_controller_1:
                left_drive_smart.set_velocity(drivetrain_left_side_speed, PERCENT)
                left_drive_smart.spin(FORWARD)
            # only tell the right drive motor to spin if the values are not in the deadband range
            if drivetrain_r_needs_to_be_stopped_controller_1:
                right_drive_smart.set_velocity(drivetrain_right_side_speed, PERCENT)
                right_drive_smart.spin(FORWARD)
        # wait before repeating the process
        wait(20, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True

rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
#
# Project: VEXcode Project
# Author: VEX
# Created:
# Description: VEXcode V5 Python Project
#
# ------------------------------------------

# Library imports
from vex import *

# Begin project code

# Begin project code
def catapult_launch():
    catapult.set_velocity(35, PERCENT)
    catapult.spin(FORWARD)


def catapult_launch_hold():
    catapult.set_stopping(HOLD)
    while(controller_1.buttonR1.pressing()):
        print("catapulting")
        catapult.set_velocity(35, PERCENT)
        catapult.set_max_torque(100, PERCENT)
        catapult.spin(FORWARD)
        catapult.stop()

def catapult_reverse():
    catapult.set_stopping(HOLD)
    while(controller_1.buttonR2.pressing()):
        print("catapulting")
        catapult.set_velocity(20, PERCENT)
        catapult.set_max_torque(100, PERCENT)
        catapult.spin(REVERSE)
        catapult.stop()

def move_drive():
    drivetrain.drive(REVERSE)

def stop_drive():
    drivetrain.stop()

def wings_out():
    left_wing.spin_to_position(90, DEGREES, wait = False)
    right_wing.spin_to_position(90, DEGREES, wait = False)

def wings_in():
    left_wing.spin_to_position(0, DEGREES, wait=False)
    right_wing.spin_to_position(0, DEGREES, wait=False)

def turn_180():
    drivetrain.set_turn_velocity(100, PERCENT)
    drivetrain.turn_for(LEFT, 500, DEGREES)



def pre_autonomous():
    # actions to do when the program starts
    brain.screen.clear_screen()
    brain.screen.print("pre auton code")
    wait(1, SECONDS)

def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")

    # place automonous code here

    # Begin project code
    drivetrain.set_drive_velocity(70, PERCENT)
    catapult.set_velocity(30, PERCENT)
    drivetrain.set_stopping(BRAKE)
    catapult.set_stopping(HOLD)

    #brings catapult backwards
    while True:
        catapult_launch()

    #after the catapult launches (theoretically) moves the cart back to touch the bar again
    #bumper_a.released(move_drive)
    #bumper_a.pressed(stop_drive)



def user_control():
    left_wing.set_stopping(HOLD)
    right_wing.set_stopping(HOLD)
    left_wing.set_position(0, DEGREES)
    right_wing.set_position(0, DEGREES)
    left_wing.set_velocity(80, PERCENT)
    right_wing.set_velocity(80, PERCENT)
    brain.screen.clear_screen()
    catapult.set_velocity(25, PERCENT)
    catapult.set_max_torque(100, PERCENT)

    # place driver control in this while loop
    while True:
        catapult.set_velocity(25, PERCENT)
        catapult.set_max_torque(100, PERCENT)
        drivetrain.set_drive_velocity(60, PERCENT)
        controller_1.buttonR1.pressed(catapult_launch_hold)
        controller_1.buttonR2.pressed(catapult_reverse)
        controller_1.buttonX.pressed(wings_out)
        controller_1.buttonY.pressed(wings_in)
        controller_1.buttonA.pressed(turn_180)
        wait(20, MSEC)

# create competition instance
comp = Competition(user_control, autonomous)
pre_autonomous()
