from WindowsShortcutManager.utils.logger import SingletonLogger
from WindowsShortcutManager.utils.env import SingletonEnvValues
from WindowsShortcutManager.utils.path import PATHS

LOG_PATH = PATHS.DATA / "main.log"
logger = SingletonLogger(str(LOG_PATH))

ENV_PATH = PATHS.PACK / ".env"
env = SingletonEnvValues(ENV_PATH)

def main():
    ...

if __name__ == "__main__":
    main()