import simpleaudio as sa #for playing .wav files
import time

#invisible characters that when printed to the terminal will manipulate the terminal in our case, we are clearing the output
CLEAR = "\033[2J" #clears the entire terminal screen so it is empty
CLEAR_AND_RETURN = "\033[H" #clears the screen and returns the cursor to the home position so we can print from that position again


def alarm(seconds):
    """
        desc: Count down by clearing the screen at each interval using invisible characters until the timer expires, then play an alarm sound.
    """
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left =  time_left//60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN} Alarm will sound in {minutes_left:02d} : {seconds_left:02d}")
    
    """
    # Load the sound file and play it
    wave_obj = sa.WaveObject.from_wave_file('file directory/alarm.wav')
    play_obj = wave_obj.play()
    time.sleep(3) #lets the sound play for 3 seconds
    play_obj.stop() #stops the sound
    #play_obj.wait_done()  # Wait until sound has finished playing - if it is 20seconds long, it will play for 20 seconds
    """
    
    #The code for the alarm is listed above. this is a makeshift
    count = 1
    print(CLEAR)
    while count <= 5:
        time.sleep(1)
        beeb = "beeb " * count

        print(f"{CLEAR_AND_RETURN} {beeb}")
        count += 1
        

alarm(5)