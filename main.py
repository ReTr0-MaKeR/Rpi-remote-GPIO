from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from gpiozero import LED
from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory

class Function(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.value = True

    def connect(self):

        ip = self.ids.ip.text
        print(ip)
        factory = PiGPIOFactory(host = str(ip), port=8888)
        self.servo = AngularServo(27, min_angle=-90, max_angle=90, pin_factory=factory)
        self.led = LED(17, pin_factory=factory)
        print("Established")

    def on_led(self):
        self.led.on()
    def off_led(self):
        self.led.off()
    def go_max(self):
        self.servo.angle = 90
    def go_min(self):
        self.servo.angle = -90

class Main(MDApp):
    def build(self):
        Builder.load_file("layout.kv")
        return Function()
Main().run()

