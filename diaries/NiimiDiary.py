from diaries.AbstractDiary import AbstractDiary

class NiimiDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-16"
    def get_summary(self):
        return "GitHubがとても難しかった"
    def get_author(self):
        return "Sample"