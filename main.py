from kivy.lang import Builder
from kivymd.app import MDApp
from datetime import datetime
from core.physics.ftrt_core import calculate_demo_ftrt

KV = '''
MDScreen:
    MDLabel:
        id: label
        text: "FTRT Mobile"
        halign: "center"

    MDRaisedButton:
        text: "CALCULAR"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        on_release: app.run_ftrt()
'''

class FTRTApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def run_ftrt(self):
        value = calculate_demo_ftrt()
        print("FTRT:", value)

FTRTApp().run()
