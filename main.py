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

    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')    
    
    def get_cpu_percent(self):
        cpu_percent = psutil.cpu_percent(interval=0.1)
        return cpu_percent

    def get_memory_info(self):
        memory_info = psutil.virtual_memory()
        return{
            'total' : memory_info.total,
            'available' : memory_info.available,
            'used' : memory_info.used,
            'percent' : memory_info.percent,
            'free' : memory_info.free
        }
    
    def get_process_info(self):
        processes = []

        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'status']):
            try: 
                processes.append({
                    'pid' : proc.info['pid'],
                    'name' : proc.info['name'],
                    'cpu' : proc.info['cpu_percent'],
                    'memory' : proc.info['memory_percent'],
                    'status' : proc.info['status']
                })

            except Exception as e :
                print("Error in the code", e)

        return processes
    
    def get_top_memory_process(self, processes, top_n=5):
        sorted_process = sorted(processes, key= lambda x : x['memory'], reverse=True)
        return sorted_process


    def run(self):
        while self.running:
            print("Info")
          
            print(self.get_memory_info())
            
            processes  = self.get_top_memory_process(self.get_process_info())
            print(processes)
             
            
                
                

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