import os
import sys
from pathlib import Path
from enum import StrEnum, auto
from dataclasses import dataclass
from .exceptions import PathNotFoundError
from ..etc import is_bundled
import __main__

@dataclass
class Paths:
    PROGRAM: Path = None    # 실행 파일이 위치한 경로
    PACK: Path = None       # PyInstaller 빌드 파일/폴더 경로 또는 __main__의 파일 경로
    DATA: Path = None       # 프로그램 데이터 저장 경로

PATHS = Paths()

class PathTypes(StrEnum):
    NONE = auto()
    FOLDER = auto()
    FILE = auto()

def _update_program_path():
    if is_bundled():
        PATHS.PROGRAM = Path(sys.executable).parent
    else:
        main_file = Path(__main__.__file__).resolve()
        PATHS.PROGRAM = main_file.parent

def _update_package_path():
    if is_bundled():
        PATHS.PACK = Path(sys._MEIPASS)
    else:
        main_file = Path(__main__.__file__).resolve()
        PATHS.PACK = main_file.parent

def _update_program_data_path():
    PATHS.DATA = Path(os.getenv("APPDATA")) / "WindowsShortcutManager"

def _update_all_paths():
    _update_program_path()
    _update_package_path()
    _update_program_data_path()

_update_all_paths()

def get_path(base_path: Path, *subpaths: str, create: PathTypes = PathTypes.NONE) -> Path:
    """
    주어진 base_path에서 추가 경로(subpaths)를 연결해 반환합니다.
    경로가 존재하지 않으면 create 인자에 따라 파일 또는 폴더를 생성합니다.
    """
    target = base_path.joinpath(*subpaths)

    if not target.exists():
        if create == PathTypes.FILE:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.touch(exist_ok=True)
        elif create == PathTypes.FOLDER:
            target.mkdir(parents=True, exist_ok=True)
        elif create == PathTypes.NONE:
            raise PathNotFoundError(target)
        
    return target
