import pygame
import pi_servo_hat

# Initialize Pygame and the joystick
pygame.init()
pygame.joystick.init()

# Attempt to setup the joystick
try:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
except pygame.error:
    raise ValueError("Joystick not found")

# Initialize the PiServoHat
servo_hat = PiServoHat()
servo_hat.restart()  # Restart the servo hat to clear register

# Helper function to map joystick values to servo angles
def map_value(x, in_min, in_max, out_min, out_max):
    """ Maps a value from one range to another. """
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

# Main loop
try:
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Read joystick axes and map them to servo angles
        x_axis = joystick.get_axis(0)  # Assume axis 0 for x-axis
        y_axis = joystick.get_axis(1)  # Assume axis 1 for y-axis
        
        # Map joystick value (typically -1.0 to 1.0) to servo angle (0 to 180)
        x_servo = map_value(x_axis, -1.0, 1.0, 0, 180)
        y_servo = map_value(y_axis, -1.0, 1.0, 0, 180)

        # Set servos
        servo_hat.move_servo_position(0, x_servo)
        servo_hat.move_servo_position(1, y_servo)
finally:
    pygame.quit()