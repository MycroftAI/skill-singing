# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.


import random
from os.path import dirname, join

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.skills.audioservice import AudioService
from mycroft.audio import wait_while_speaking

class SingingSkill(MycroftSkill):
    def __init__(self):
        super(SingingSkill, self).__init__(name="SingingSkill")
        self.process = None
        self.play_list = {
            0: join(dirname(__file__), "popey-favourite.mp3"),
            1: join(dirname(__file__), "popey-jackson.mp3"),
            2: join(dirname(__file__), "popey-jerusalem.mp3"),
            3: join(dirname(__file__), "popey-lose-yourself.mp3"),
            4: join(dirname(__file__), "popey-lovemetender.mp3"),
            5: join(dirname(__file__), "popey-rocketman.mp3"),
        }

    def initialize(self):
        self.audioservice = AudioService(self.bus)
        self.add_event("mycroft.sing", self.sing, False)

    def sing(self, message):
        self.audioservice.play(self.play_list[3])

    @intent_handler(IntentBuilder('').require('Sing'))
    def handle_sing(self, message):
        path = random.choice(self.play_list)
        try:
            self.speak_dialog('singing')
            wait_while_speaking()
            self.audioservice.play(path)
        except Exception as e:
            self.log.error("Error: {0}".format(e))


def create_skill():
    return SingingSkill()
