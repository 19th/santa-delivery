# Uzdevums: Iziet trasi ar koda palidzību

# Komandas: 
# tello.move_down(50) - nolaisties
# tello.move_up(50) - pacelties
# tello.move_forward(50) - uz priekšu
# tello.move_back(50) - uz aizmuguri
# tello.move_left(50) - pa kreisi
# tello.move_right(50) - pa labi
#
# tello.rotate_clockwise(90) - griezties pulksteņradītāja virzienā
# 
# tello.flip_forward() - flip uz priekšu (mest uz priekšu)
# tello.flip_back() - flip atpakaļ (mest atpakaļ)
# tello.flip_left() - flip pa kreisi (mest pa kreisi)
# tello.flip_right() - flip pa kreisi (mest pa labi)
# 
# Dokumentācija un piemēri
# https://github.com/damiafuentes/DJITelloPy/tree/master
# https://github.com/damiafuentes/DJITelloPy/blob/master/examples/simple.py

from djitellopy import Tello

tello = Tello()
tello.RETRY_COUNT = 0
tello.connect()

print("Battery:", tello.get_battery())
tello.set_speed(20)

# Kodu raksti šeit 
