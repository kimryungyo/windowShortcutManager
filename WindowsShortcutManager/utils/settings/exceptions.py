"""
설정 관련 커스텀 예외들을 정의합니다.
"""

class SettingsError(Exception):
    """설정 관련 기본 예외"""
    pass

class KeyNotFoundError(SettingsError):
    """설정 데이터에서 key를 찾지 못했을 때 발생하는 예외"""
    pass
