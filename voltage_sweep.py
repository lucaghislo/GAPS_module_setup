import time
import os
import pyvisa

caen_DELAY = 1
caen_channel = 7
delay = 5

rm = pyvisa.ResourceManager()
caen = rm.open_resource("ASRL/dev/ttyACM0::INSTR")
caen.query("$CMD:SET,PAR:BDCLR")
caen.write("*RST")

for voltage in range(0, 240, 10):
    caen.query(f"$CMD:SET,CH:{caen_channel},PAR:VSET,VAL:{voltage}", caen_DELAY)
    time.sleep(5)
    print(
        f"Current @ -{voltage}V: "
        + caen.query(f"$CMD:MON,CH:{caen_channel},PAR:IMON", caen_DELAY)
    )
