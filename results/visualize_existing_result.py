import argparse
import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))

from agents.Trainer import Trainer
from utilities.data_structures.Config import Config


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', help='path of pkl data file', required=True)
    parser.add_argument('--save_path', help='path of saved result', required=True)
    parser.add_argument('--title', help='title of result image', default='Result')
    args = parser.parse_args()
    pkl_path = args.data_path
    save_path = args.save_path

    config = Config()
    trainer = Trainer(config=config, agents=None)
    trainer.visualise_preexisting_results(save_image_path=save_path, data_path=pkl_path, title='whatever')

