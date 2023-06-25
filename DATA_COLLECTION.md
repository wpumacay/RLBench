# Data Collection using RLBench

## Setup

Clone and install our fork (we have some modified tasks):

```shell
git clone https://github.com/wpumacay/RLBench.git && cd RLBench
# Checkout the branch with modified task
git checkout test_data_collection
# Make sure we have cached the path to our repository
export RLBENCH_ROOT=$(pwd)
```

Source the virtual environment used for PyRep and RLBench:

```shell
# Source this way in case of using virtualenv
. venv/bin/activate
# Source this way in case of using conda
conda activate rlbench-env
```

Install our fork (will replace the original version of RLBench)

```shell
# Install main requirements for RLBench to work
pip install -r requirements.txt
# Installing some extra requirements (e.g. `dataset_generator` requires `absl-py`)
pip install -r requirements-extra.txt
# Install the fork
pip install .
```

## Collect demos

We can use the helper script [`dataset_generator.py`][0], like this:

```shell
# Go back to our cloned repository
cd $RLBENCH_ROOT
# Collect some demostrations for our modified task
python tools/dataset_generator.py --tasks=put_block_in_bin --variations=2 --episodes_per_task=5
```

The demos will be saved in the folder `/tmp/rlbench_data/TASK_NAME`, which for
our case would be `/tmp/rlbench_data/put_block_in_bin`. There you'll find first
the variations, and in each variation you'll find the episodes recorded.

The generated output will look more or less like this:

![dataset-generator-output][img_dataset_generator_output]

[//]: # (References)

<!-- URLS -->

[0]: <https://github.com/stepjam/RLBench/blob/master/tools/dataset_generator.py> (script-github-dataset-generator)

<!-- IMAGES -->

[img_dataset_generator_output]: readme_files/img_screenshot_saved_from_dataset_generator.png
