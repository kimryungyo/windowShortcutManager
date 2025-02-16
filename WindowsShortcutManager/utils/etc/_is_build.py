import sys

def is_bundled():
    """
    실행된 파일이 패키징된 파일인지 확인합니다.
    """
    return hasattr(sys, 'frozen')