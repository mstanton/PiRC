from gpiozero import CPUTemperature

cpuTemp = CPUTemperature()
while True:
   print(cpuTemp.temperature)