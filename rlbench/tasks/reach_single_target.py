from typing import List, Tuple

from pyrep.objects.proximity_sensor import ProximitySensor
from rlbench.backend.conditions import DetectedCondition
from rlbench.backend.task import Task


class ReachSingleTarget(Task):
    def init_task(self) -> None:
        sns_success = ProximitySensor("sns_success")
        self.register_success_conditions(
            [DetectedCondition(self.robot.arm.get_tip(), sns_success)]
        )

    def init_episode(self, index: int) -> List[str]:
        return ["reach the red target", "reach the red object"]

    def variation_count(self) -> int:
        return 1

    def base_rotation_bounds(self) -> Tuple[List[float], List[float]]:
        return [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]
