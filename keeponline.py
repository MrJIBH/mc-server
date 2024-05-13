import os
import time

def check_internet():
    response = os.system("ping -c 1 1.1.1.1 > /dev/null 2>&1")
    return response == 0

def main():
    while True:
        if check_internet():
            print("¡Hay conexión a Internet!")
        else:
            print("No hay conexión a Internet.")
        time.sleep(1800)  # Espera 30 minutos (1800 segundos)

if __name__ == "__main__":
    main()
