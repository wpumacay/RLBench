import codecs
import os

from setuptools import setup

# Version meaning (X.Y.Z)
# X: Major version (e.g. vastly different scene, platform, etc)
# Y: Minor version (e.g. new tasks, major changes to existing tasks, etc)
# Z: Patch version (e.g. small changes to tasks, bug fixes, etc)


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    version=get_version("rlbench/__init__.py"),
    packages=[
        "rlbench",
        "rlbench.backend",
        "rlbench.action_modes",
        "rlbench.tasks",
        "rlbench.task_ttms",
        "rlbench.robot_ttms",
        "rlbench.sim2real",
        "rlbench.assets",
        "rlbench.gym",
    ],
    package_data={
        "": ["*.ttm", "*.obj", "**/**/*.ttm", "**/**/*.obj"],
        "rlbench": ["task_design.ttt"],
    },
)
