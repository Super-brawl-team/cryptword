class Debugger:
    RED="\033[31m"
    YELLOW="\033[33m"
    BLUE="\033[34m"
    GREEN="\033[32m"

    @staticmethod
    def error(msg):   
        print(f"{Debugger.RED}[ERROR] {msg}")
    @staticmethod
    def warning(msg): 
        print(f"{Debugger.YELLOW}[WARNING] {msg}")
    @staticmethod
    def info(msg):    
        print(f"{Debugger.BLUE}[INFO] {msg}")
    @staticmethod
    def input(msg):    
        return input(f"{Debugger.GREEN}[TERMINAL] {msg}")
