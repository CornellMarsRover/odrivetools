import odrive
from odrive.enums import *
import time
import keyboard
import curses
import serial

try:
	usb = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
	usb.reset_input_buffer()
except:
	print("ERROR - Could not open serial port.")
	print("exit")
	exit()

SERIAL0 = "206534845748" #front wheels
SERIAL1 = "206A34A05748" #middle wheels
SERIAL2 = "206A349E5748" #back wheels

if __name__ == '__main__':
    
    print("Finding odrives")
    odrv0 = odrive.find_any(serial_number = SERIAL0)
    print("Odrive 0 found")

    # odrv1 = odrive.find_any(serial_number = SERIAL1)
    # print("Odrive 2 found")

    # odrv2 = odrive.find_any(serial_number = SERIAL2)
    # print("Odrive 3 found")
    
    odrv0.axis0.config.motor_type = MotorType.HIGH_CURRENT
    
    odrv0.axis0.config.motor.pole_pairs = 6
    
    odrv0.axis0.config.motor.torque_constant = 1
    
    odrv0.axis0.motor.config.current_lim        = 9
    odrv0.axis0.motor.config.current_lim_margin = 10
    
    # odrv0.axis0.config.motor.calibration_current = 4.5
    
    # odrv0.axis0.config.motor.resistance_calib_max_voltage
    
    # odrv0.axis0.config.enable_watchdog = True
    
    odrv0.axis0.requested_state = AxisState.MOTOR_CALIBRATION
    
    odrv0.axis0.config.can_node_id = 3
    # odrv0.axis1.config.can_node_id = 1
    odrv0.can.config.baud_rate = 250000
    odrv0.save_configuration()
    odrv0.reboot()

    # odrv0.save_configuration()