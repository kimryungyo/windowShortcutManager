"""
설정 데이터의 유효성을 검사하기 위한 기본 Validator 클래스 및 확장 가능한 구조를 제공합니다.
필요에 따라 사용자 정의 Validator를 추가할 수 있습니다.
"""

class BaseValidator:
    """
    모든 Validator가 상속할 기본 클래스입니다.
    validate 메소드를 재정의하여 사용합니다.
    """
    def validate(self, key: str, value) -> bool:
        """
        설정 값이 유효한지 검사합니다.
        :param key: 설정의 key
        :param value: 설정의 value
        :return: 유효하면 True, 아니면 False
        """
        raise NotImplementedError("validate 메소드를 구현하세요.")
