from pynput import keyboard
import threading
import time
import sys
import os

isEnd = False


def on_press(key):
    print(key)
    if key == keyboard.Key.ctrl_r:
        os._exit(1)


def listen_key():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def start():
    t3 = threading.Thread(target=listen_key)
    t3.start()


if __name__ == '__main__':
    t3 = threading.Thread(target=listen_key)
    t3.start()
