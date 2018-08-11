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

    def catch_message(self, ch, user, msg):
        msg = msg.split(' ')

        self._count += 1
        if self._count % 40 == 0 and self.thug_name != msg[0]:
            self._count = 0

            option_msg = [
                '수다쟁이', '그만 떠들어!', '안물',
                '어쩌라고', '노-잼'
            ]
            picked_msg = random.choice(option_msg)
            this.slack.chat.post_message(
                ch,
                '{msg} <@{user}>'.format(user=user, msg=picked_msg),
                as_user=True
            )

            return


        if self.thug_name == msg[0]:
            option_msg = [
                '왜', '왜 ㅡㅡ', '왜불러', '어쩔', '데헷 >_<',
                '뿌직!', '뿌우웅=3', '반사', '무지개반사', '뭠마'
            ]
            picked_msg = random.choice(option_msg)
            self.slack.chat.post_message(ch, picked_msg, as_user=True)
