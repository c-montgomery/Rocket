import asyncio
from pynput import keyboard

#allow input to manipulate sim
class Control:
    def __init__(self):
        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )

    def on_press(self, key):
        try:
            print('Alphanumeric key {0} pressed'.format(key.char))
        except AttributeError:
            print('Special key {0} pressed'.format(key))

    def on_release(self, key):
        print('{0} released'.format(key))
        if key == keyboard.Key.esc:
            # Stop listener
            asyncio.get_event_loop().stop()

    def start_listener(self):
        asyncio.ensure_future(self.listen())
        asyncio.get_event_loop().run_forever()

    async def listen(self):
        
        self.listener.start()
        await asyncio.Future()

    def stop_listener(self):
        self.listener.stop()

