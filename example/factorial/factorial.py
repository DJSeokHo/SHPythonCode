# _*_ coding: utf-8 _*_
# @Time : 2022/08/17 1:25 PM
# @Author : Coding with cat
# @File : factorial
# @Project : SHPythonCode
import random
import time
from collections import Counter

from framewrok.utility.log_utility import ILog


class User:
    name: str
    missions: [str]
    receive_missions: [str]

    def __init__(self, name, mission_total_count):
        self.name = name

        # 미션 초기화
        self.missions = list()
        for m in range(0, mission_total_count):
            self.missions.append(f"mission{m}")

    def receive(self, mission_to_do_count):

        self.receive_missions = list()

        mission: str
        for n in range(0, mission_to_do_count):
            mission = random.choice(self.missions)
            self.missions.remove(mission)  # 해당 사용자 이미 수행한 미션을 다시 나타날 수 없음
            self.receive_missions.append(mission)


def example_for_repeatability(mission_total_count, mission_to_do_count, user_count,
                              with_log: bool = True) -> float:
    """
    계산 방법
    :param with_log:
    :param mission_total_count: 미션 창고 총 미션수
    :param mission_to_do_count: 수행할 미션 수
    :param user_count: 사용자 수
    :return: 여러명 사용자 같은 미션 받는 확률 (중복율)
    """

    # noise
    time.sleep(random.choice([0.001, 0.002, 0.003, 0.004, 0.005]))

    user_list: [User] = list()

    # 사용자 및 미션 초기화
    user: User
    for u in range(0, user_count):
        user = User(
            name=f'user{u}',
            mission_total_count=mission_total_count
        )
        user.receive(mission_to_do_count)
        user_list.append(
            user
        )

    if with_log:
        for user in user_list:
            ILog.debug(__file__, f'{user.name} {user.receive_missions}')

    if with_log:
        ILog.debug(__file__, "모든 사용자 의 미션:")
    all_users_total_missions = list()
    for user in user_list:
        all_users_total_missions.extend(user.receive_missions)
    if with_log:
        ILog.debug(__file__, f'{all_users_total_missions}')

    all_users_total_missions_count = Counter(all_users_total_missions)

    avg_repeat_ratio: float = 0
    total_repeat_ratio: float = 0
    repeat_count: float = 0
    for key, value in all_users_total_missions_count.items():
        if with_log:
            ILog.debug(__file__, f'{key} - {value}')

        if value > 1:
            repeat_count = repeat_count + 1
            # temp_repeat = float(value) / float(len(all_users_total_missions))
            temp_repeat = float(value) / float(user_count)
            total_repeat_ratio = total_repeat_ratio + temp_repeat
            if with_log:
                ILog.debug(__file__, '%.20f' % temp_repeat)

    if repeat_count == 0:
        total_repeat_ratio = float(0)
    else:
        avg_repeat_ratio = total_repeat_ratio / repeat_count

    if with_log:
        ILog.debug(__file__, "total repeat ratio is %.20f" % total_repeat_ratio)
        ILog.debug(__file__, "repeat avg ratio is %.20f" % avg_repeat_ratio)

    return avg_repeat_ratio


if __name__ == '__main__':

    # user = User('user 1', 10)
    # user.receive(3)

    # example_for_repeatability(100, 5, 100)
    # example_for_repeatability(20, 3, 10)
    # example_for_repeatability(10, 2, 2)

    _mission_total_count = 1000
    _mission_to_do_count = 5
    _user_count = 10000

    example_for_repeatability(_mission_total_count, _mission_to_do_count, _user_count)
    ILog.debug(__file__, '==================================')

    run_time = 100

    result: float = 0.0

    for i in range(0, run_time):
        ILog.debug(__file__, f'run time {i}')
        result = result + example_for_repeatability(
            _mission_total_count, _mission_to_do_count, _user_count, with_log=False
        )

    result = result / float(run_time)
    ILog.debug(
        __file__,
        '%d times repeat is %.30f  ~~~~~~ %.20f' % (run_time, result, result * 100) + ' %'
    )
