from diaries.AbstractDiary import AbstractDiary

class takahashiDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-16"
    def get_summary(self):
        return "大変な1日だった"
    def get_author(self):
        return "takahashi"