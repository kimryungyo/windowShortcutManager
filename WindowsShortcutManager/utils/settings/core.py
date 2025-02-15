"""
설정 관리의 핵심 기능을 제공하는 모듈입니다.
Settings 클래스는 설정 데이터의 저장, 조회, 수정, 삭제,
JSON 입출력, 변경 이벤트 콜백 등록 등의 기능을 제공합니다.
"""

from ..singleton import singleton
from copy import deepcopy
from .storage import load_json, save_json
from .exceptions import KeyNotFoundError

class Settings:
    def __init__(self, initial_data: dict = None, default_data: dict = None):
        """
        :param initial_data: 초기 설정 데이터를 dict 형태로 전달 (우선순위 높음)
        :param default_data: 기본 설정 데이터 (기본값)
        """
        self._data = {}
        self._default = default_data or {}
        self._callbacks = []  # 변경 시 호출할 콜백 함수 리스트

        # 기본값 적용 후 초기 데이터 병합
        self._data = deepcopy(self._default)
        if initial_data:
            self.update(initial_data)

    def get(self, key: str, default=None):
        """
        dot notation 지원: 예를 들어, "database.host" 와 같이 사용 가능.
        """
        keys = key.split(".")
        value = self._data
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                if default is not None:
                    return default
                raise KeyNotFoundError(f"Key '{key}' not found.")
        return value

    def set(self, key: str, value):
        """
        dot notation 지원하여 값을 설정합니다.
        변경 시 등록된 콜백 함수들을 호출합니다.
        """
        keys = key.split(".")
        d = self._data
        for k in keys[:-1]:
            if k not in d or not isinstance(d[k], dict):
                d[k] = {}
            d = d[k]
        d[keys[-1]] = value

        # 콜백 호출
        self._trigger_callbacks(key, value)

    def remove(self, key: str):
        """
        설정에서 지정 key를 제거합니다.
        """
        keys = key.split(".")
        d = self._data
        for k in keys[:-1]:
            if k in d and isinstance(d[k], dict):
                d = d[k]
            else:
                raise KeyNotFoundError(f"Key '{key}' not found.")
        if keys[-1] in d:
            removed_value = d.pop(keys[-1])
            self._trigger_callbacks(key, None)
            return removed_value
        else:
            raise KeyNotFoundError(f"Key '{key}' not found.")

    def update(self, new_data: dict):
        """
        기존 설정 데이터에 대해 new_data 딕셔너리를 병합합니다.
        중첩된 dict에 대해서도 재귀적으로 업데이트합니다.
        """
        def recursive_update(orig, upd):
            for k, v in upd.items():
                if isinstance(v, dict) and isinstance(orig.get(k), dict):
                    recursive_update(orig[k], v)
                else:
                    orig[k] = v
                    self._trigger_callbacks(k, v)
        recursive_update(self._data, new_data)

    def to_dict(self) -> dict:
        """
        내부 설정 데이터를 dict 형태로 반환합니다.
        """
        return deepcopy(self._data)

    def load_from_file(self, file_path: str):
        """
        JSON 파일에서 설정 데이터를 읽어와 병합합니다.
        JSON 파일은 indent=4 로 포맷된 데이터여야 합니다.
        """
        data = load_json(file_path)
        self.update(data)

    def save_to_file(self, file_path: str):
        """
        현재 설정 데이터를 JSON 파일로 저장합니다.
        저장 시 indent=4 로 저장합니다.
        """
        save_json(file_path, self._data)

    def register_callback(self, callback):
        """
        설정이 변경될 때 호출될 콜백 함수를 등록합니다.
        callback: function(key: str, value) 형태.
        """
        if callback not in self._callbacks:
            self._callbacks.append(callback)

    def unregister_callback(self, callback):
        """
        등록된 콜백 함수를 해제합니다.
        """
        if callback in self._callbacks:
            self._callbacks.remove(callback)

    def _trigger_callbacks(self, key: str, value):
        """
        설정 변경 시 등록된 모든 콜백 함수를 호출합니다.
        """
        for callback in self._callbacks:
            try:
                callback(key, value)
            except Exception as e:
                # 개별 콜백의 예외는 로깅하거나 무시할 수 있음.
                # 여기서는 간단히 출력.
                print(f"Callback error on key '{key}': {e}")

@singleton
class SingletonSettings(Settings):
    def __init__(self, initial_data: dict = None, default_data: dict = None):
        super().__init__(initial_data, default_data)