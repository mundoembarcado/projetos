from datetime import datetime
import time
import subprocess
import os
valor = input("Digite o Horário: ")
while(1):
    
# datetime object containing current date and time
    now = datetime.now()
 
   # print("now =", now)

# dd/mm/YY H:M:S
    dt_string = now.strftime("%H:%M")
    print("date and time =", dt_string)
    if (dt_string == valor):
        print('ok')
        subprocess.Popen([os.path.join("C:/", "Program Files", "VideoLAN", "VLC", "vlc.exe"),"http://sc3.radiocaroline.net:8030/listen.m3u"])
        os._exit(0)
    else:
        print("Aguarde")

    time.sleep(15)   
