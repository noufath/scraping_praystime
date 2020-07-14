from choice import choice
from exitchoice import ExitChoice
from menu import Menu

class Main:
    print('## Info Jadwal Sholat di Indonesia ##','\n')
    menu = Menu('Pilih Menu')
    menu.add_choice([choice('Input Kode Kota'), choice('Lihat Kode Kota'), ExitChoice('Exit')])
    menu.input()

