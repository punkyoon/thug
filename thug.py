import re
import random

from slacker import Slacker


class Thug:
    def __init__(self, TOKEN, TRIG):
        # Init slack bot config
        self.slack = Slacker(TOKEN)
        self.response = self.slack.rtm.start()
        self.endpoint = self.response.body['url']
        self.thug_name = TRIG

        # Init message count
        self._count = 0
        self._food_count = 0

        self.food_keyword = re.compile('순대')
        self.action_keyword = re.compile('밥먹자')

    def catch_message(self, ch, user, msg):
        cmd = msg
        msg = msg.split(' ')

        self._count += 1
        if self._count % 40 == 0 and '<@{}>'.format(self.thug_name) != msg[0]:
            self._count = 0

            option_msg = [
                '수다쟁이', '그만 떠들어!', '안물',
                '어쩌라고', '노-잼', '방구나 먹어라'
            ]
            picked_msg = random.choice(option_msg)
            self.slack.chat.post_message(
                ch,
                '{msg} <@{user}>'.format(user=user, msg=picked_msg),
                as_user=True
            )

            return


        if '<@{}>'.format(self.thug_name) == msg[0]:
            option_msg = [
                '왜', '왜 ㅡㅡ', '왜불러', '어쩔', '데헷 >_<',
                '뿌직!', '뿌우웅=3', '반사', '무지개반사', '뭠마'
            ]
            picked_msg = random.choice(option_msg)
            self.slack.chat.post_message(ch, picked_msg, as_user=True)

        _food = False
        # Find 순대
        if len(self.food_keyword.findall(cmd)) > 0:
            _food = True

        if _food and user != self.thug_name:
            self._food_count += 1
            option_msg = [
                '지금 순대라고 하셨나요? 쿰척쿰척',
                '순대의 칼로리는 1인분에 500kcal입니다^^ 쿰척쿰척',
                '순대?! 쿰-척',
                '그동안 순대를 {} 번 언급하셨군요! ^^'.format(self._food_count)
            ]
            picked_msg = random.choice(option_msg)
            self.slack.chat.post_message(ch, picked_msg, as_user=True)

        # Find 밥타령
        _bob = False
        if len(self.action_keyword.findall(cmd)) > 0:
            option_msg = [
                '또 밥타령이냐?! <@{}>'.format(user)
            ]
            picked_msg = random.choice(option_msg)
            self.slack.chat.post_message(ch, picked_msg, as_user=True)
