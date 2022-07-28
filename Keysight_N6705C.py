from serial import *
import serial.tools.list_ports
import time
import os
import pyvisa

rm = pyvisa.ResourceManager()

print(rm.list_resources())
keysight = rm.open_resource('USB0::10893::3842::MY56006348::0::INSTR')

# channel 1
vset_ch1 = 2.4
iset_ch1 = 0.5

# channel 3
vset_ch3 = 2.4
iset_ch3 = 0.15

# channel 4
vset_ch4 = 3.3
iset_ch4 = 0.05

# channel 1
keysight.write(f'VOLTage:LEVel {vset_ch1},(@1);:CURRent:LEVel {iset_ch1},(@1)')

# channel 3
keysight.write(f'VOLTage:LEVel {vset_ch3},(@3);:CURRent:LEVel {iset_ch3},(@3)')

# channel 4
keysight.write(f'VOLTage:LEVel {vset_ch4},(@4);:CURRent:LEVel {iset_ch4},(@4)')


keysight.write('OUTP ON,(@1,3,4)')