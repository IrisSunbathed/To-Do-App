import subprocess
   

def clear_console():
    subprocess.run('cls', shell=True)
    
def ask_int(message) :
    while True :
        try :
           return int(input(message))
        except ValueError :
            print("Valor no válido.")    
