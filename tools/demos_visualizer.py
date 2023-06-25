#!/usr/bin/env python

import os
import argparse

from typing import List

from rlbench.action_modes.action_mode import MoveArmThenGripper
from rlbench.action_modes.arm_action_modes import JointVelocity
from rlbench.action_modes.gripper_action_modes import Discrete
from rlbench.environment import Environment
from rlbench.observation_config import ObservationConfig
from rlbench.utils import name_to_task_class


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--task",
        help="name of the task to visualize",
        type=str,
        default="reach_target",
    )
    parser.add_argument(
        "--demos",
        help="the number of demonstrations to run",
        type=int,
        default=2,
    )

    args = parser.parse_args()
    TASK_CLASS = name_to_task_class(args.task)
    NUM_DEMOS = args.demos

    obs_config = ObservationConfig()
    obs_config.set_all(True)

    env = Environment(
        action_mode=MoveArmThenGripper(
            arm_action_mode=JointVelocity(), gripper_action_mode=Discrete()),
        obs_config=ObservationConfig(),
        headless=False)
    env.launch()

    task = env.get_task(TASK_CLASS)
    demos = task.get_demos(NUM_DEMOS, live_demos=True)


if __name__ == "__main__":
    main()
