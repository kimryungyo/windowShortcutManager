# [ study ] - 새로 알게 된 정보
#
# __init__ 메소드를 주로 '생성자' 또는 '초기화 메소드'라고 부르지만
# 파이썬에서는 __init__ 함수는 기존에 생성된 인스턴스를 초기화하는 역할만 수행한다.
# 새 인스턴스를 만드는 역할은 __new__ 메소드가 수행하기 때문에
# 파이썬에서는 두 메소드의 차이를 명확히 알고 있어야 한다.
# 추가적으로, __new__ 메소드는 클래스 메소드와 유사하게 클래스를 이용해 호출해야 한다.
#
# 자바나 C++ 등의 언어에서는 생성자가 인스턴스를 만드는 동시에 초기화를 수행하기 때문에
# 두 용어에 크게 문제가 없지만, 파이썬에서는 초기화 메소드라고 부르는 게 좋을 거 같다.


#
# [ note ]
#
# 클래스를 싱글턴으로 만들어주는 데코레이터입니다.
# 이 프로젝트에서는 모든 모듈에서 공유해야하는 Logger, 설정, 경로 클래스 등에 사용됩니다.
#

import functools

def singleton(cls):
    """
    클래스에 적용하면 해당 클래스가 싱글턴 패턴으로 동작하도록 만드는 데코레이터입니다.
    데코레이터가 적용된 클래스의 인스턴스는 하나만 생성되며, __init__은 최초 생성 시에만 호출됩니다.
    """
    orig_new = cls.__new__
    orig_init = cls.__init__

    # 기존 초기화 메소드를 대체할 함수입니다.
    # 각 인스턴스당 초기화 메소드를 단 한번만 호출할 수 있도록 해줍니다.
    # 이미 초기화 된 인스턴스에 다시 초기화를 할 일이 없다면 없어도 되는 부분입니다.
    @functools.wraps(orig_init)
    def new_init(self, *args, **kwargs):
        if not getattr(self, '_initialized', False):
            orig_init(self, *args, **kwargs)
            self._initialized = True

    # 기존 생성자 메소드(__new__)를 대체할 함수입니다.
    # 싱글턴 기법을 적용해주는 부분으로, 첫 인스턴스 생성시에만 기존 생성자를 호출해 새 인스턴스를 만듭니다.
    # 만들어진 인스턴스는 클래스에 저장하며, 다음부터는 새 인스턴스를 만들 때마다 해당 인스턴스를 반환합니다.
    # 아래 코드의 경우 orig_new에 추가 인자를 전달하지 않고 있는데,
    # 클래스의 __new__ 메소드가 추가 인자를 받고 있는 경우 수정이 필요합니다.
    # 전 아직 __new__ 메소드를 직접 정의해본 적은 없어서 패스  
    def new_singleton(cls_, *args, **kwargs):
        if not hasattr(cls_, '_instance'):
            cls_._instance = orig_new(cls_)
        return cls_._instance

    # 대체 메소드들을 클래스에 적용합니다.
    cls.__init__ = new_init
    cls.__new__ = staticmethod(new_singleton)
    return cls