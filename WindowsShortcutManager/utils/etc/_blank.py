from random import choices

BLANKS = ["​", " ", " ", " ", " ", " ", " ", " ", " ", " ", "⠀", " "]

def generate_blank_string(n: int) -> str:
    """
    길이가 n인 공백 문자열을 생성합니다.\n
    12 종류의 문자들로 구성되며, 경우의 수는 다음과 같습니다.\n
    n=8 -> 429,981,696\n
    n=10 -> 61,917,364,224\n
    n=16 -> 184,884,258,895,036,416\n
    """
    return ''.join(choices(BLANKS, k=n))