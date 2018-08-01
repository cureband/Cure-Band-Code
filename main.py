import time
import os

bpm = 151

if 40 < bpm < 180:
    os.system("/home/pi/Desktop/Scripts/{}.sh".format(bpm))

else:
    time.sleep(1)
    #Insert Read
    bpm1 = 230

    time.sleep(1)
    #Insert Read
    bpm2 = 230

    time.sleep(1)
    #Insert Read
    bpm3 = 230

    time.sleep(1)
    #Insert Read
    bpm4 = 230


    time.sleep(1)
    #Insert Read
    bpm5 = 230

    if(bpm-bpm1)+(bpm2-bpm3)+(bpm4-bpm5) > 500:
        print("Suspected Cardic Arrest")
        #Play Sound
        
        time.sleep(1)
	#Insert Read
        bpm6 = 230

        time.sleep(1)
	#Insert Read
        bpm7 = 230

        time.sleep(1)
	#Insert Read
        bpm8 = 230

        time.sleep(1)
	#Insert Read
        bpm9 = 230

        if (bpm-bpm1)+(bpm2-bpm3)+(bpm4-bpm5)+(bpm6-bpm7)+(bpm8-bpm9) > 1000:
            print("Cardic Arrest")

        else:
            if (bpm-bpm1)+(bpm2-bpm3)+(bpm4-bpm5)+(bpm6-bpm7)+(bpm8-bpm9) < -1000:

                print("Cardic Arrest")
            
            else:
                print("No Problem")
                pass
            

    else:
        if(bpm-bpm1)+(bpm2-bpm3)+(bpm4-bpm5) < -500:
            print("Suspected Cardic Arrest")
            #Play Sound
        
            time.sleep(1)
            #Insert Read
            bpm6 = 230

            time.sleep(1)
            #Insert Read
            bpm7 = 230

            time.sleep(1)
            #Insert Read
            bpm8 = 230

            time.sleep(1)
            #Insert Read
            bpm9 = 230

            if (bpm-bpm1)+(bpm2-bpm3)+(bpm4-bpm5)+(bpm6-bpm7)+(bpm8-bpm9) > 1000:
                print("Cardic Arrest")

            else:
                if (bpm-bpm1)+(bpm2-bpm3)+(bpm4-bpm5)+(bpm6-bpm7)+(bpm8-bpm9) < -1000:

                   print("Cardic Arrest")
            
                else:
                    print("No Problem")
                    pass

        else:
            print("No Suspected Cardic Attack At This Point To Check One More Time")

            if 40 < bpm < 180:
                print("All Good")

            else:
                time.sleep(1)
		#Insert Read
                bpm12 = 230

                time.sleep(1)
		#Insert Read
                bpm22 = 230

                time.sleep(1)
		#Insert Read
                bpm32 = 230

                time.sleep(1)
		#Insert Read
                bpm42 = 230

                time.sleep(1)
		#Insert Read
                bpm52 = 230

                time.sleep(1)
		#Insert Read
                bpm62 = 230

                time.sleep(1)
		#Insert Read
                bpm72 = 230

                time.sleep(1)
		#Insert Read
                bpm82 = 230

                time.sleep(1)
		#Insert Read
                bpm92 = 230

                time.sleep(1)
                #Insert Read
                bpm102 = 230

                if (bpm12-bpm22)+(bpm32-bpm42)+(bpm52-bpm62)+(bpm72-bpm82)+(bpm92-bpm102) > 1000:
                    print("Cardic Arrest")
                else:
                    if (bpm-bpm1)+(bpm2-bpm3)+(bpm4-bpm5)+(bpm6-bpm7)+(bpm8-bpm9) < -1000:
                        print("Cardic Arrest")

                    else:
                        print("All Good")
                        pass
                              













