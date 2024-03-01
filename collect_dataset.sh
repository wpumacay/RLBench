

python tools/dataset_generator.py --tasks=open_drawer \
                                  --save_path=$HOME/data/rlbench_data \
                                  --image_size=128,128 \
                                  --renderer=opengl3 \
                                  --episodes_per_task=1 \
                                  --processes=1

