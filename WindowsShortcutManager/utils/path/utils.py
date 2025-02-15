import math
from pathlib import Path

def format_filesize(size_bytes: int) -> str:
    """바이트 단위의 크기를 사람이 단위가 붙은 문자열로 변환합니다."""
    if size_bytes == 0:
        return "0B"
    size_units = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = 1024 ** i
    s = round(size_bytes / p, 2)
    return f"{s} {size_units[i]}"

def get_file_size(file_path: Path) -> str:
    """특정 파일의 크기를 단위가 적용된 문자열로 반환합니다."""
    size_bytes = file_path.stat().st_size
    return format_filesize(size_bytes)

# pathlib 내장 라이브러리에서 같은 기능을 제공하여 사용하지 않음
# get_path의 create 인자를 사용하여 경로를 생성하거나 아래 코드 사용
# from pathlib import Path / Path.touch or Path.makedir

# def create_path(dir_path: str) -> str:
#     """디렉토리가 존재하지 않으면 생성하고 해당 경로를 반환합니다."""
#     if not os.path.isdir(dir_path):
#         os.makedirs(dir_path, exist_ok=True)
#     return dir_path

# def create_file(file_path: str, data: str = '') -> str:
#     """파일이 존재하지 않으면 생성하고 데이터를 기록한 후 경로를 반환합니다."""
#     if not os.path.exists(file_path):
#         directory = os.path.dirname(file_path)
#         if directory and not os.path.exists(directory):
#             os.makedirs(directory, exist_ok=True)
#         with open(file_path, 'w', encoding='utf-8') as target_file:
#             target_file.write(data)
#     return file_path