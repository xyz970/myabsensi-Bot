import os
import pytz
import time
from datetime import datetime as date


class absensi:
    """
    Class absensi()
    """

    def __init__(self):
        """
        docstring
        """
        pass
    switch = {
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday"
        }

    # now = date.today().strftime("%A")
    now = date.now(pytz.timezone('Asia/Jakarta')).strftime("%A")

    
    def senin():
        """
        Daftar absensi Senin
        """
        now = date.now(pytz.timezone('Asia/Jakarta')).strftime("%A")
        print("Senin")

        if now == 8:
            for i in range(3):
                os.system('noti --telegram -m "Absen Basis data yaaa.... Jangan lupaa"')
                time.sleep(1000)
        elif now == 10:
             for i in range(3):
                os.system('noti --telegram -m "Absen Logika Algoritma yaaa.... Jangan lupaa"')
                time.sleep(1000)
        elif now == 13:
             for i in range(3):
                os.system('noti --telegram -m "Absen Pemrograman Dasar yaaa.... Jangan lupaa"')
                time.sleep(1000)
        elif now == 18:
             for i in range(3):
                os.system('noti --telegram -m "Absen Agama yaaa.... Jangan lupaa"')
                time.sleep(1000)




    def selasa():
        """
        Daftar absensi Selasa
        """
        now = date.now(pytz.timezone('Asia/Jakarta')).strftime("%A")
        second = date.now(pytz.timezone('Asia/Jakarta')).strftime("%M")
        print("Selasa")

        if now == 7 and second == 30:
            for i in range(3):
                os.system('noti --telegram -m "Basic English yaaa.... Jangan lupaa"')
                time.sleep(1000)
        elif now == 10 and second == 30:
             for i in range(3):
                os.system('noti --telegram -m "Basic English yaaa.... Jangan lupaa"')
                time.sleep(1000)

    def rabu():
        """
        Daftar absensi Rabu
        """
        now = date.now(pytz.timezone('Asia/Jakarta')).strftime("%A")
        # print("Rabu")
        if now == 8:
            for i in range(3):
                os.system('noti --telegram -m "Absen Workshop Pengembangan Perangkat Lunak.. Jangan lupaa"')
                time.sleep(1000)
        elif now == 10:
             for i in range(3):
                os.system('noti --telegram -m "Absen Workshop Pengembangan Perangkat Lunak.. Jangan lupaa"')
                time.sleep(1000)
        elif now == 18:
             for i in range(3):
                os.system('noti --telegram -m "Absen Pancasila.. Jangan lupaa"')
                time.sleep(1000)
        

    def kamis():
        """
        Daftar absensi Kamis
        """
        print("Kamis")
        now = date.now(pytz.timezone('Asia/Jakarta')).strftime("%A")
        if now == 8:
            for i in range(3):
                os.system('noti --telegram -m "Absen Workshop Basis Data.. Jangan lupaa"')
                time.sleep(1000)
        elif now == 10:
             for i in range(3):
                os.system('noti --telegram -m "Absen Workshop Basis Data.. Jangan lupaa"')
                time.sleep(1000)
        elif now == 13:
             for i in range(3):
                os.system('noti --telegram -m "Absen Workshop Pengembangan Perangkat Lunak.. Jangan lupaa"')
                time.sleep(1000)
        elif now == 15:
             for i in range(3):
                os.system('noti --telegram -m "Absen Workshop Pengembangan Perangkat Lunak.. Jangan lupaa"')
                time.sleep(1000)
    
    def jumat():
        """
        Daftar absensi Jumat
        """
        print("Jumat")
        now = date.now(pytz.timezone('Asia/Jakarta')).strftime("%A")
        if now == 13:
            for i in range(3):
                os.system('noti --telegram -m "Absen Workshop Basis Data.. Jangan lupaa"')
                time.sleep(1000)
        elif now == 15:
             for i in range(3):
                os.system('noti --telegram -m "Absen Workshop Basis Data.. Jangan lupaa"')
                time.sleep(1000)


    while True:
        if now == "Monday":
        # senin = senin
        # senin
        # print("bla")
            senin()
        elif now == "Tuesday":
            # selasa = selasa
            selasa()
        elif now == "Wednesday":
            # rabu = rabu
            rabu()
            # print(nowtz)
        elif now == "Thursday":
            # kamis = kamis
            kamis()
        elif now == "Friday":
            # jumat = jumat
            jumat()
        else:
            break

