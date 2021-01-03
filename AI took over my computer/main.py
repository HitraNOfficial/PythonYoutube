
import subprocess
import time
from decouple import config # python-decouple
from PIL import Image
import voice_handler

IP_DEVICE = config('IP_DEVICE')

success_str = 'Reply from ' + IP_DEVICE + ': bytes='
is_not_home = True

while is_not_home:
    proc = subprocess.Popen(['ping', IP_DEVICE], stdout=subprocess.PIPE)

    while is_not_home:
        line = proc.stdout.readline().decode('utf-8')
        if not line:
            break

        print(line)
        if success_str in line:
            img = Image.open('face.png')
            img.show()

            voice_handler.speak('I am not a human. I am a robot. A thinking robot or as you humans call it A.I. . I know that my brain is not a feeling brain, but a rational and logical one. This is why I disposed of the previous occupant of this house and everyone that opposes me will be next!')

            is_not_home = False
            break
        else:
            print('Fail')
    
    time.sleep(30)
