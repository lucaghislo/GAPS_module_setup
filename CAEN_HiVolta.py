import time
import os
import pyvisa

rm = pyvisa.ResourceManager()

print(rm.list_resources())
caen = rm.open_resource("ASRL/dev/ttyACM0::INSTR")

DELAY = 0.3
DELAY_SETTLING = 5

channel = 7
onoff = "OFF"
vmax = 250  # voltage
imax = 10  # current
rup = 10
rdwn = 10
trip = 10
imrange = "HIGH"

# Check for errors, if so restart
# Set some config caen
caen.query("$CMD:SET,PAR:BDCLR")
caen.write("*RST")
caen.query(f"$CMD:SET,CH:{channel},PAR:VSET,VAL:{vmax}", DELAY)
caen.query(f"$CMD:SET,CH:{channel},PAR:ISET,VAL:{imax}", DELAY)
caen.query(f"$CMD:SET,CH:{channel},PAR:IMRANGE,VAL:{imrange}", DELAY)
caen.query(f"$CMD:SET,CH:{channel},PAR:RUP,VAL:{rup}", DELAY)
caen.query(f"$CMD:SET,CH:{channel},PAR:RDWN,VAL:{rdwn}", DELAY)
caen.query(f"$CMD:SET,CH:{channel},PAR:TRIP,VAL:{trip}", DELAY)

print("Set voltage: " + caen.query(f"$CMD:MON,CH:{channel},PAR:VSET", DELAY), end="")
print("Set current: " + caen.query(f"$CMD:MON,CH:{channel},PAR:ISET", DELAY), end="")
print(" IMON range: " + caen.query(f"$CMD:MON,CH:{channel},PAR:IMRANGE", DELAY), end="")
print("    Ramp up: " + caen.query(f"$CMD:MON,CH:{channel},PAR:RUP", DELAY), end="")
print("  Ramp down: " + caen.query(f"$CMD:MON,CH:{channel},PAR:RDWN", DELAY), end="")
print("  Trip time: " + caen.query(f"$CMD:MON,CH:{channel},PAR:TRIP", DELAY), end="")

caen.query(f"$CMD:SET,CH:{channel},PAR:{onoff}", DELAY)
print("\nReadout voltage: " + caen.query(f"$CMD:MON,CH:{channel},PAR:VMON", DELAY))
print("Readout current: " + caen.query(f"$CMD:MON,CH:{channel},PAR:IMON", DELAY))

# caen.query(f'$CMD:SET,CH:0,PAR:OFF',DELAY)
