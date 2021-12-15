import datetime as date
import os
import time as tm
class Greet():
    """
    Greeting (Ucapan selamat Pagi dan selamat malam)
    """
    def __init__(self):
        pass

    def onNight(self):
        """
        Ucapan Selamat malam
        """
        waktu = tm.strftime('%H')
        if waktu == '7':
            os.system('noti --telegram -m "Jangan Lupa istirahat\n Selamat Malam.. <3"')
        

    def onMorning(self):
        """
        Ucapan Selamat Pagi
        """
        waktu = tm.strftime('%H')
        if waktu == '21':
            os.system('noti --telegram -m "Selamat pagi.."')
    