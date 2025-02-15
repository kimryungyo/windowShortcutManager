from WindowsShortcutManager.utils.logger import SingletonLogger
from WindowsShortcutManager.utils.env import SingletonEnvValues
from WindowsShortcutManager.utils.path import get_path, PathTypes, PATHS, get_file_size, PathNotFoundError
from time import sleep

LOG_PATH = PATHS.DATA / "main.log"
logger = SingletonLogger(str(LOG_PATH))

ENV_PATH = PATHS.PACK / ".env"
env = SingletonEnvValues(ENV_PATH)

print(env.get("PROJECT_PATH", False))

logger.info(f"{PATHS.PACK=}")
logger.info(f"{PATHS.PROGRAM=}")
logger.info(f"{PATHS.DATA=}")