import yaml
import os
import glob

from elements import *
from .check import check_config_file

PATH_ROBOT_CONFIG = os.path.join("bots","*.yaml")

## modify this dict for adding bots type!
robot_type = {
    "bot1" : Default,
    "bot2": Bot1,
    "bot3": BotSeek,
    "RL": ReinforcmentLearning_LEARN
}

def create_bots():
    list_of_bots = glob.glob(PATH_ROBOT_CONFIG)
    bots = []
    for file in list_of_bots:
        try:
            bot_config = yaml.safe_load(open(file, 'r'))
            check_config_file(bot_config)
        except:
            raise ValueError("Errore nel file di configurazione dei robots")
        bot = robot_type[bot_config["core"]](
                        name = bot_config["name"],
                        position = [bot_config["start_position"]["x"], bot_config["start_position"]["y"]],
                        size = bot_config["size"],
                        color = [bot_config["color"]["R"], bot_config["color"]["G"], bot_config["color"]["B"]],
                        speed = bot_config["speed"]
                        )
        bots.append(bot)
    return bots