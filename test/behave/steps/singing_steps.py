# Copyright 2020 Mycroft AI Inc.
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

from mycroft.audio import wait_while_speaking

from test.integrationtests.voight_kampff import emit_utterance, wait_for_dialog


@given('mycroft is singing')
def given_news_playing(context):
    emit_utterance(context.bus, "sing a song")
    wait_for_dialog(context.bus, ['singing'])
    wait_while_speaking()
    time.sleep(3)
    context.bus.clear_messages()


@given('mycroft is not singing')
def given_nothing_playing(context):
    emit_utterance(context.bus, "stop playback")
    time.sleep(5)
    context.bus.clear_messages()


@then('mycroft should sing')
def then_playback_start(context):
    cnt = 0
    while context.bus.get_messages('mycroft.audio.service.play') == []:
        if cnt > 20:
            assert False, 'Mycroft didn\'t start singing :('
            break
        time.sleep(0.5)


@then('mycroft should stop singing')
def then_playback_stop(context):
    cnt = 0
    while context.bus.get_messages('mycroft.audio.service.stop') == []:
        if cnt > 20:
            assert False, 'Mycroft didn\'t stop singing'
            break
        else:
            cnt += 1
        time.sleep(0.5)
