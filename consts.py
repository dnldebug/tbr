from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Drive_Train import claw, andar, turn, rotate, cancela

hub = PrimeHub()

colors = (Color.GREEN, Color.BLUE, Color.GRAY, Color.YELLOW)
#andar(15) -> trem cinza
#andar(25) -> trem amarelo
#andar(35) -> trem verde
#andar(45) -> trem azul
#andar(30) -> sair da plataforma(com a regua)

def Open():
  claw.run_target(2000, 0)

def close():
    claw.run_target(2000, 100)

def low():
    claw.run_target(2000, 130)

def mid():
    claw.run_target(2000, 220)

def deposit():
    claw.run_target(1800, 600)

def cancela_esquerda():
    cancela.run_angle(1800, 180)

def volta_esquerda():
    cancela.run_angle(1800, -105)

def cancela_direita():
    cancela.run_angle(1800, -180)

def volta_direita():
    cancela.run_angle(1800, 150)
