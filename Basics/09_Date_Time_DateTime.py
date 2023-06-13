'''
QtCore 모듈의 QDate, QTime, QDateTime 클래스를 이용해서 어플리케이션에
날짜와 시간을 표시할 수 있습니다.
'''

# 날짜 표시하기(QDate)
## QDate 클래스는 날짜와 관련된 기능들을 제공합니다.

from PyQt5.QtCore import QDate, Qt, QTime, QDateTime

now = QDate.currentDate()
print(now.toString())

# 날짜 형식 설정하기
# toString() 메서드의 format 파라미터를 설정함으로써 날짜의 형식을 정할 수 있다.

print(now.toString('d.M.yy'))
print(now.toString('dd.MM.yyyy'))
print(now.toString('ddd.MMMM.yyyy'))
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))

# 시간 표시하기(QTime)

# 현재 시간 출력하기
time = QTime.currentTime()
print(time.toString())

# currentTime() 메서드는 현재 시간을 반환합니다.
# toString() 메서드는 현재 시간을 문자열로 반환합니다.

# 시간 형식 설정하기
print(time.toString('h.m.s'))
print(time.toString('hh.mm.ss'))
print(time.toString('hh.mm.ss.zzz'))
print(time.toString(Qt.DefaultLocaleLongDate))
print(time.toString(Qt.DefaultLocaleShortDate))

# 날짜와 시간 표시하기(QDateTime)

# QDateTime 클래스를 사용해서 현재 날짜와 시간을 함께 출력할 수 있습니다.

datetime = QDateTime.currentDateTime()
print(datetime.toString())

# 날짜와 시간 형식 설정하기

print(datetime.toString('d.M.yy hh:mm:ss'))
print(datetime.toString('dd.MM.yyyy, hh:mm:ss'))
print(datetime.toString(Qt.DefaultLocaleLongDate))
print(datetime.toString(Qt.DefaultLocaleShortDate))

