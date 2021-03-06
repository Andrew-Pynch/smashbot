import copy
import serial
import sys
import time
from struct import pack

from melee import enums, logger
from melee.console import Console

class ControllerState:
    """A snapshot of the state of a virtual controller"""

    def __init__(self):
        self.button = dict()
        #Boolean buttons
        self.button[enums.Button.BUTTON_A] = False
        self.button[enums.Button.BUTTON_B] = False
        self.button[enums.Button.BUTTON_X] = False
        self.button[enums.Button.BUTTON_Y] = False
        self.button[enums.Button.BUTTON_Z] = False
        self.button[enums.Button.BUTTON_L] = False
        self.button[enums.Button.BUTTON_R] = False
        self.button[enums.Button.BUTTON_START] = False
        self.button[enums.Button.BUTTON_D_UP] = False
        self.button[enums.Button.BUTTON_D_DOWN] = False
        self.button[enums.Button.BUTTON_D_LEFT] = False
        self.button[enums.Button.BUTTON_D_RIGHT] = False
        #Analog sticks
        self.main_stick = (.5, .5)
        self.c_stick = (.5, .5)
        #Analog shoulders
        self.l_shoulder = 0
        self.r_shoulder = 0

    def toBytes(self):
        """ Serialize the controller state into an 8 byte sequence that the Gamecube uses """
        buttons_total = 0x0080
        if self.button[enums.Button.BUTTON_A]:
            buttons_total += 0x0100
        if self.button[enums.Button.BUTTON_B]:
            buttons_total += 0x0200
        if self.button[enums.Button.BUTTON_X]:
            buttons_total += 0x0400
        if self.button[enums.Button.BUTTON_Y]:
            buttons_total += 0x0800
        if self.button[enums.Button.BUTTON_Z]:
            buttons_total += 0x1000
        if self.button[enums.Button.BUTTON_L]:
            buttons_total += 0x0002
        if self.button[enums.Button.BUTTON_R]:
            buttons_total += 0x0004

        buffer = pack(">H", buttons_total)

        # Convert from a float 0-1 to int 1-255
        val = pack(">B", (int((max(min(self.main_stick[0], 1), 0) * 254)) + 1))
        buffer += val
        val = pack(">B", (int((max(min(self.main_stick[1], 1), 0) * 254)) + 1))
        buffer += val
        val = pack(">B", (int((max(min(self.c_stick[0], 1), 0) * 254)) + 1))
        buffer += val
        val = pack(">B", (int((max(min(self.c_stick[1], 1), 0) * 254)) + 1))
        buffer += val

        # Convert from a float 0-1 to int 0-255
        #   The max/min thing just ensures the value is between 0 and 1
        val = pack(">B", int(max(min(self.l_shoulder, 1), 0) * 255))
        buffer += val
        val = pack(">B", int(max(min(self.r_shoulder, 1), 0) * 255))
        buffer += val
        return buffer

    def __str__(self):
        string = ""
        for val in self.button:
            string += str(val) + ": " + str(self.button[val])
            string += "\n"
        string += "MAIN_STICK: " + str(self.main_stick) + "\n"
        string += "C_STICK: " + str(self.c_stick) + "\n"
        string += "L_SHOULDER: " + str(self.l_shoulder) + "\n"
        string += "R_SHOULDER: " + str(self.r_shoulder) + "\n"
        return string

class Controller:
    """Utility class that manages virtual controller state and button presses"""

    def __init__(self, console, port, serial_device="/dev/ttyACM0"):
        self._is_dolphin = console.is_dolphin
        if self._is_dolphin:
            self.pipe_path = console.get_dolphin_pipes_path(port)
            self.pipe = None
        else:
            try:
                self.tastm32 = serial.Serial(serial_device, 115200, timeout=None, rtscts=True)
            except serial.serialutil.SerialException:
                print("TAStm32 was not ready. It might be booting up. " +
                      "Wait a few seconds and try again")
                sys.exit(-1)

        self.prev = ControllerState()
        self.current = ControllerState()
        self.logger = console.logger

    def connect(self):
        """Connect the controller to the console """
        if self._is_dolphin:
            self.pipe = open(self.pipe_path, "w")
            return True
        else:
            # Remove any extra garbage that might have accumulated in the buffer
            self.tastm32.reset_input_buffer()

            # Send reset command
            self.tastm32.write(b'R')
            cmd = self.tastm32.read(2)
            if cmd != b'\x01R':
                # TODO Better error handling logic here
                print("ERROR: TAStm32 did not reset properly. Try power cycling it.")
                return False
            # Set to gamecube mode
            self.tastm32.write(b'SAG\x80\x00')
            cmd = self.tastm32.read(2)
            self.tastm32.reset_input_buffer()
            if cmd != b'\x01S':
                # TODO Better error handling logic here
                print("ERROR: TAStm32 did not set to GCN mode. Try power cycling it.")
                return False
            return True

    def disconnect(self):
        """Disconnects the controller from the console """
        if self._is_dolphin:
            if self.pipe:
                self.pipe.close()
                self.pipe = None
        else:
            # TODO: Tear down connection to TAStm32
            self.tastm32.close()
            pass

    def simple_press(self, x, y, button):
        """Here is a simpler representation of a button press, in case
            you don't want to bother with the tedium of manually doing everything.
            It isn't capable of doing everything the normal controller press functions
            can, but probably covers most scenarios.
            Notably, a difference here is that doing a button press releases all
            other buttons pressed previously.
            Don't call this function twice in the same frame
                x = 0 (left) to 1 (right) on the main stick
                y = 0 (down) to 1 (up) on the main stick
                button = the button to press. Enter None for no button"""
        if self._is_dolphin:
            if not self.pipe:
                return
            #Tilt the main stick
            self.tilt_analog(enums.Button.BUTTON_MAIN, x, y)
            #Release the shoulders
            self.press_shoulder(enums.Button.BUTTON_L, 0)
            self.press_shoulder(enums.Button.BUTTON_R, 0)
            #Press the right button
            for item in enums.Button:
                #Don't do anything for the main or c-stick
                if item == enums.Button.BUTTON_MAIN:
                    continue
                if item == enums.Button.BUTTON_C:
                    continue
                #Press our button, release all others
                if item == button:
                    self.press_button(item)
                else:
                    self.release_button(item)
        else:
            # TODO Tastm32 button presses
            pass

    def press_button(self, button):
        """ Press a single button

        If already pressed, this has no effect
        """
        self.current.button[button] = True
        if self._is_dolphin:
            if not self.pipe:
                return
            command = "PRESS " + str(button.value) + "\n"
            if self.logger:
                self.logger.log("Buttons Pressed", command, concat=True)
            self.pipe.write(command)

    def release_button(self, button):
        """ Unpress a single button

        If already released, this has no effect
        """
        self.current.button[button] = False
        if self._is_dolphin:
            if not self.pipe:
                return
            command = "RELEASE " + str(button.value) + "\n"
            if self.logger:
                self.logger.log("Buttons Pressed", command, concat=True)
            self.pipe.write(command)

    def press_shoulder(self, button, amount):
        """ Press the analog shoulder buttons to a given amount

        button - Button enum. Has to be L or R
        amount - Float between 0 (not pressed at all) and 1 (Fully pressed in)

        Note that the 'digital' button press of L or R are handled separately
            as normal button presses. Pressing the shoulder all the way in
            will not cause the digital button to press
        """
        if button == enums.Button.BUTTON_L:
            self.current.l_shoulder = amount
        elif button == enums.Button.BUTTON_R:
            self.current.r_shoulder = amount
        if self._is_dolphin:
            if not self.pipe:
                return
            command = "SET " + str(button.value) + " " + str(amount) + "\n"
            if self.logger:
                self.logger.log("Buttons Pressed", command, concat=True)
            self.pipe.write(command)

    def tilt_analog(self, button, x, y):
        """ Tilt one of the analog sticks to a given (x,y) value

        button - Button enum. Must be main stick or C stick
        x - Float between 0 (left) and 1 (right)
        y - Float between 0 (down) and 1 (up)
        """
        if button == enums.Button.BUTTON_MAIN:
            self.current.main_stick = (x, y)
        else:
            self.current.c_stick = (x, y)
        if self._is_dolphin:
            if not self.pipe:
                return
            command = "SET " + str(button.value) + " " + str(x) + " " + str(y) + "\n"
            if self.logger:
                self.logger.log("Buttons Pressed", command, concat=True)
            self.pipe.write(command)

    def empty_input(self):
        """ Helper function to reset the controller to a resting state

        All buttons are released, all sticks set to 0.5
        """
        #Set the internal state back to neutral
        self.current.button[enums.Button.BUTTON_A] = False
        self.current.button[enums.Button.BUTTON_B] = False
        self.current.button[enums.Button.BUTTON_X] = False
        self.current.button[enums.Button.BUTTON_Y] = False
        self.current.button[enums.Button.BUTTON_Z] = False
        self.current.button[enums.Button.BUTTON_L] = False
        self.current.button[enums.Button.BUTTON_R] = False
        self.current.button[enums.Button.BUTTON_START] = False
        self.current.button[enums.Button.BUTTON_D_UP] = False
        self.current.button[enums.Button.BUTTON_D_DOWN] = False
        self.current.button[enums.Button.BUTTON_D_LEFT] = False
        self.current.button[enums.Button.BUTTON_D_RIGHT] = False
        self.current.main_stick = (.5, .5)
        self.current.c_stick = (.5, .5)
        self.current.l_shoulder = 0
        self.current.r_shoulder = 0
        if self._is_dolphin:
            if not self.pipe:
                return
            command = "RELEASE A" + "\n"
            command += "RELEASE B" + "\n"
            command += "RELEASE X" + "\n"
            command += "RELEASE Y" + "\n"
            command += "RELEASE Z" + "\n"
            command += "RELEASE L" + "\n"
            command += "RELEASE R" + "\n"
            command += "RELEASE START" + "\n"
            command += "RELEASE D_UP" + "\n"
            command += "RELEASE D_DOWN" + "\n"
            command += "RELEASE D_LEFT" + "\n"
            command += "RELEASE D_RIGHT" + "\n"
            command += "SET MAIN .5 .5" + "\n"
            command += "SET C .5 .5" + "\n"
            command += "SET L 0" + "\n"
            command += "SET R 0" + "\n"
            #Send the presses to dolphin
            self.pipe.write(command)
            if self.logger:
                self.logger.log("Buttons Pressed", "Empty Input", concat=True)

    def flush(self):
        """ Actually send the button presses to the console

        Up until this point, any buttons you 'press' are just queued in a pipe.
        It doesn't get sent to the console until you flush
        """
        if self._is_dolphin:
            if not self.pipe:
                return
            self.pipe.flush()
            # Move the current controller state into the previous one
            self.prev = copy.copy(self.current)
        else:
            # Command for "send single controller poll" is 'A'
            # Serialize controller state into bytes and send
            self.tastm32.write(b'A' + self.current.toBytes())
            start = time.time()
            cmd = self.tastm32.read(1)

            if cmd != b'A':
                print("Got error response: ", bytes(cmd))
