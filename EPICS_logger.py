import epics
import time

time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
device = input('Please input device PV name: ')

fh = open('%s_%s.log' %(device, time),'w')
epics.camonitor('%s' %device,writer=fh.write)

print("Data logging......")

stop = input('If you want to stop EPICS logger, please input any key:')
print()

if stop == True:
    epics.camonitor_clear('%s' %device)
    fh.close()

read_file = input("Input any key to show data log, input 0 to exit: ")
