import screen_brightness_control as sbc

from pynput.keyboard import Listener, HotKey

brightness = False

def main():
    def on_activate():
        global brightness
        brightness = not brightness
        if brightness:
            sbc.set_brightness(100)
        else:
            sbc.set_brightness(0)

    def for_canonical(f):
        return lambda k: f(l.canonical(k))

    hotkey = HotKey(HotKey.parse('<ctrl>+<alt>+<up>'), on_activate)
    with Listener(
            on_press=for_canonical(hotkey.press),
            on_release=for_canonical(hotkey.release)) as l:
        l.join()

if __name__ == '__main__':
    main()