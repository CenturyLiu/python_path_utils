import signal
import os
import time

class SignalHandleTemplate(object):
    def __init__(self) -> None:
        super().__init__()
        self.status = False
    
    def receiveUserSignal1(self,signalNumber, frame):
        self.status = True
        # print("Current status set to True")
        # do not print anything inside signal handler function
        # doing this will lead to reentrant of function "print",
        # leading to error
        return
    
    def receiveUserSignal2(self,signalNumber,frame):
        self.status = False
        # print("Current status set to False")
    
    def main_loop(self):
        count = 0
        while True:
            if self.status == True:
                print("count = %d"%(count))
            count += 1
            count %= 256


if __name__ == '__main__':
    signal_handle = SignalHandleTemplate()
    signal.signal(signal.SIGUSR1, signal_handle.receiveUserSignal1)
    signal.signal(signal.SIGUSR2, signal_handle.receiveUserSignal2)
    print("My PID is %d"%(os.getpid()))
    signal_handle.main_loop()