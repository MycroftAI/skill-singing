# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import time

from behave import given, then

from mycroft.messagebus import Message


@given('mycroft is singing')
def given_news_playing(context):
    context.bus.emit(Message('recognizer_loop:utterance',
                             data={'utterances': ['sing a song'],
                                   'lang': 'en-us',
                                   'session': '',
                                   'ident': time.time()},
                             context={'client_name': 'mycroft_listener'}))
    time.sleep(10)
    context.bus.clear_messages()


@given('mycroft is not singing')
def given_nothing_playing(context):
    context.bus.emit(Message('recognizer_loop:utterance',
                             data={'utterances': ['stop playback'],
                                   'lang': 'en-US',
                                   'session': '',
                                   'ident': time.time()},
                             context={'client_name': 'mycroft_listener'}))
    time.sleep(5)
    context.bus.clear_messages()


@then('mycroft should sing')
def then_playback_start(context):
    cnt = 0
    while context.bus.get_messages('mycroft.audio.service.play') == []:
        if cnt > 20:
            assert False
            break
        time.sleep(0.5)


@then('mycroft should stop singing')
def then_playback_stop(context):
    cnt = 0
    while context.bus.get_messages('mycroft.audio.service.stop') == []:
        if cnt > 20:
            assert False
            break
        else:
            cnt += 1
        time.sleep(0.5)
