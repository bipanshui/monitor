import psutil
import os
import sys
import time
import signal
from datetime import datetime
from collections import defaultdict

class SystemMonitor:
    def __init__(self):
        self.screen_width = 80
        self.running = True
        self.previous_cpu_times = None
        self.setup_signal_headers()

    def setup_signal_headers(self):
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
 
    def signal_handler(self, signum, frame):
        self.running = False
        print("\nShutting down monitor....")
  
    def run(self):
        while self.running:
            print("Info")
            time.sleep(3)

def main():
    print("Starting linux system monitor....")
    print("Press CTRL+C to exit\n")
    time.sleep(1)

    try:
         monitor = SystemMonitor()
         monitor.run()
    except KeyboardInterrupt:
         print("\nmonitor stopped by user.")
    except Exception as e :
         print(f"\nError :" , {e})
         sys.exit(1)

if __name__ == "__main__":
    main()