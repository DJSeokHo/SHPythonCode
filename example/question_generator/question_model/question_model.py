# _*_ coding: utf-8 _*_
# @Time : 2023/04/11 10:13 AM
# @Author : Coding with cat
# @File : question_model
# @Project : SHPythonCode
from enum import Enum


class QuestionPropertyType(Enum):
    OTHER = 0
    EASY = 1
    HARD = 2


class QuestionType(Enum):
    # 수학, 역사 지리, 동영상, 보드 게임, 언어, 교통, 암호, 포토, 키타
    OTHER = 0
    MATH = 1
    HISTORY_AND_GEOGRAPHY = 2
    VIDEO = 3
    BOARD_GAME = 4
    LANGUAGE = 5
    TRAFFIC = 6
    DECODE = 7
    PHOTO = 8


class AnswerActionType(Enum):
    OTHER = 0
    SELECTION = 1
    INPUT = 2
    LOCATION = 3
    QR = 4
    AR = 5
    SIMILARITY = 6


class QuestionModel:
    property: QuestionPropertyType = QuestionPropertyType.OTHER  # 속성
    level: int = 0  # 레벨
    difficulty_value: int = 0  # 난의도 값
    type: QuestionType = QuestionType.OTHER  # 문제 유형

    address: str = ""  # 대략 문제 장소
    latitude: float = 0  # 문제 장소 위도 (옵션)
    longitude: float = 0  # 문제 장소 경도 (옵션)

    order: str = ""  # 지시
    content_text: str = ""  # 내용 글
    content_images: [str] = []  # 내용 이미지
    content_links: [str] = []  # 내용 링크

    answer_action_type: AnswerActionType = AnswerActionType.OTHER  # 답 유형
    answer_options: [str] = []  # 답 옵션 (선택 항목, 입력 항목)
    correct_answers: [str] = []  # 정답 (글, QR 내용, ....)

    solution: str = ""  # 문제 해석 (옵션)
    author: str = ""  # 문제 저작
    date: str = ""  # 작성 날짜
