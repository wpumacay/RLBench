from typing import List
import numpy as np
from pyrep.objects.proximity_sensor import ProximitySensor
from pyrep.objects.shape import Shape
from rlbench.backend.task import Task
from rlbench.backend.conditions import DetectedCondition


class PutBlockInBin(Task):

    def init_task(self):
        self.sns_success = ProximitySensor('sns_success')
        self.obj_block = Shape('obj_block')
        self.register_graspable_objects([self.obj_block])
        self.register_success_conditions(
            [DetectedCondition(self.obj_block, self.sns_success)])

    def init_episode(self, index: int) -> List[str]:
        tomato1 = Shape('tomato1')
        tomato2 = Shape('tomato2')
        x1, y1, z1 = tomato2.get_position()
        x2, y2, z2 = self.obj_block.get_position()
        x3, y3, z3 = tomato1.get_position()
        pos = np.random.randint(3)
        if pos == 0:
            self.obj_block.set_position([x1, y1, z2])
            tomato2.set_position([x2, y2, z1])
        elif pos == 2:
            self.obj_block.set_position([x3, y3, z2])
            tomato1.set_position([x2, y2, z3])

        return ['put block in bin',
                'drop the block into the bin',
                'pick up the block and leave it in the trash can']

    def variation_count(self) -> int:
        return 1
