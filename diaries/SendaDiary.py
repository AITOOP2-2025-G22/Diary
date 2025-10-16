from diaries.AbstractDiary import AbstractDiary

class SendaDiary(AbstractDiary):
    def get_date(self):
        return "2021-10-16"
    def get_summary(self):
        return "疲れた"
    def get_author(self):
        return "Senda"