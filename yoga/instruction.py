import subprocess

def get_diff_angles(ref_angle, real_angle):
    tolerance = 5
    if(real_angle <= ref_angle + tolerance) and (real_angle >= ref_angle - tolerance):
        return 1
    if(real_angle >= ref_angle + tolerance):
        return 2
    if(real_angle <= ref_angle - tolerance):
        return 3
    return 0




def instruction(bodypart, case, audio=True):
    if(case==1):
        message = "Well done. Your" + bodypart + "is in position. Don't change it."

    elif (case==2):
        message = "Bend your " + bodypart
    elif (case==3):
        message = "Extend your " + bodypart
    elif (case==4):
        message = "Get into position " 
    elif (case==5):
        message = "Lets get the yoga party started. Come into warrior two, left knee in front" 
    elif (case==6):
        message = "Where are you? Get into position"
    elif (case==7):
        message = 'Yogaalign can not detect you. Check your camera and restart the program!'
    elif (case==8):
        message = 'Cheese. Picture is taken. Hold the pose for ten seconds!'
    #write out to wav file 
    if(audio==True):
        b = 'espeak -w temp.wav "%s" 2>>/dev/null' % message  
        #speak aloud
        c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % message #speak aloud
        p = subprocess.Popen(b, stdout=subprocess.PIPE, shell=True)
        p = subprocess.Popen(c, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
    else:
        print(message)
    return
