"""
설정 데이터를 JSON 형식으로 입출력하는 기능을 제공합니다.
indent=4 옵션을 사용하여 포맷팅합니다.
"""

import json

def load_json(file_path: str) -> dict:
    """
    주어진 파일 경로에서 JSON 데이터를 읽어 dict로 반환합니다.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(file_path: str, data: dict):
    """
    주어진 데이터를 JSON 파일로 저장합니다.
    indent=4 옵션을 사용합니다.
    """
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
