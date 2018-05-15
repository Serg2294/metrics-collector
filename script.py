import psutil
import sys
if sys.argv[1] == "cpu":
        print('system.cpu.idle {0:.1f}'.format(psutil.cpu_times_percent(interval=1).idle))
        print('system.cpu.user {0:.1f}'.format(psutil.cpu_times_percent(interval=1).user))
        print('system.cpu.guest {0:.1f}'.format(psutil.cpu_times_percent(interval=1).guest))
        print('system.cpu.iowait {0:.1f}'.format(psutil.cpu_times_percent(interval=1).iowait))
        print('system.cpu.steal {0:.1f}'.format(psutil.cpu_times_percent(interval=1).steal))
        print('system.cpu.system {0:.1f}'.format(psutil.cpu_times_percent(interval=1).system))
elif sys.argv[1] == "mem":
        print('virtual total {0}'.format(psutil.virtual_memory().total))
        print('virtual used {0}'.format(psutil.virtual_memory().used))
        print('virtual free {0}'.format(psutil.virtual_memory().free))
        print('virtual shared {0}'.format(psutil.virtual_memory().shared))
        print('swap total {0}'.format(psutil.swap_memory().total))
        print('swap used {0}'.format(psutil.swap_memory().used))
        print('swap free {0}'.format(psutil.swap_memory().free))
else:
        print('Wrong argumet. Please write cpu or mem.')
