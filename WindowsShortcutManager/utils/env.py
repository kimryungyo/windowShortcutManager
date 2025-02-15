from dotenv import dotenv_values
from types import MappingProxyType
from os import path
from .singleton import singleton

_NO_DEFAULT = object()

class EnvValues:
    def __init__(self, env_path='.env'):
        """
        인스턴스 생성 시 .env 파일의 값을 불러오고 값을 저장하는 클래스입니다.
        불러온 값들은 수정하거나 새로운 값을 추가할 수 없습니다.
        값이 유동적으로 변하는 경우 utils.settings 패키지를 사용해야 합니다.
        """
        self._path = path.abspath(env_path)
        self.load()
        
    def load(self):
        if not path.exists(self._path):
            raise FileNotFoundError(f"환경 파일을 찾을 수 없습니다: {self._path}")
        loaded = dotenv_values(self._path)
        self._variables = MappingProxyType(loaded)

    @property
    def variables(self):
        """이 값은 변경할 수 없습니다. 업데이트는 load 메소드를 사용해주세요."""
        return self._variables

    def get(self, key, default=_NO_DEFAULT):
        """
        키에 해당하는 값을 반환합니다.
        키가 존재하지 않는 경우, 기본값(default)이 제공되면 기본값을 반환하고,
        기본값이 없으면 KeyError를 발생시킵니다.
        """
        if key in self._variables:
            return self._variables[key]
        elif default is not _NO_DEFAULT:
            return default
        else:
            raise KeyError(f"존재하지 않는 키입니다. : {key}")
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __str__(self):
        return f"Environment Values -> {dict(self._variables)}"
    
    def __repr__(self):
        return f"EnvValues({self._path!r})"

@singleton
class SingletonEnvValues(EnvValues):
    def __init__(self, env_path='.env'):
        super().__init__(env_path)
