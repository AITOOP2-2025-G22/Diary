from diaries.TsujiDiary import TsujiDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [TsujiDiary(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()