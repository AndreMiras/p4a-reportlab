#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import kivy
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from reportlab.pdfgen import canvas

FILE_PATH = 'test.pdf'


class Controller(FloatLayout):

    label_text = StringProperty('Testing #1357')

    def save(self):
        c = canvas.Canvas(FILE_PATH)
        c.drawString(100, 100, 'Testing #1357')
        c.save()
        self.label_text = f'{FILE_PATH} saved'

    def delete(self):
        try:
            os.remove(FILE_PATH)
            self.label_text = f'{FILE_PATH} deleted'
        except FileNotFoundError:
            self.label_text = 'Deleted'
            self.label_text = f'{FILE_PATH} does not exist'

    def info(self):
        exists = os.path.exists(FILE_PATH)
        self.label_text = f'{FILE_PATH} exists: {exists}'


class ControllerApp(App):

    def build(self):
        return Controller()


if __name__ == '__main__':
    ControllerApp().run()
