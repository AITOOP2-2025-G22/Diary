
from diaries.NiimiDiary import NiimiDiary
from diaries.TsujiDiary import TsujiDiary
from diaries.SendaDiary import SendaDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [ NiimiDiary(),TsujiDiary(),SendaDiary()]



for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()