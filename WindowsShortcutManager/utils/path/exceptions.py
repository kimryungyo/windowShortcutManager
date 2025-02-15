class PathNotFoundError(Exception):
    def __init__(self, path):
        message = (
            f"요청된 경로가 존재하지 않습니다. ({path})"
            "경로를 생성하려면 create 인자를 PathTypes.FILE 또는 PathTypes.FOLDER로 지정해주세요."
        )
        super().__init__(message)