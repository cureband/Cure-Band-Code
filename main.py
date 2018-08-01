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

	if (bpm-bpm1)+(bpm2-bpm3)+(bpm4-bpm5) > 500:
		#Play Sound ???
		
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
			#Cardic Arrest

		else:
			if (bpm-bpm1)+(bpm2-bpm3)+(bpm4-bpm5)+(bpm6-bpm7)+(bpm8-bpm9) < -1000:
				# Cardic Arrest

			else:
				#No Problems




	else:
		if (bpm-bpm1)+(bpm2-bpm3)+(bpm4-bpm5) < -500:
			#play sound?

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
			#Cardic Arrest

			else:
				if (bpm-bpm1)+(bpm2-bpm3)+(bpm4-bpm5)+(bpm6-bpm7)+(bpm8-bpm9) < -1000:
					# Cardic Arrest

				else:
					#No Problems


		else:
			#No Suspected Cardic Attack At This Point To Check One More Time
			if 40 < bpm < 180:


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

				if (bpm-bpm1)+(bpm2-bpm3)+(bpm4-bpm5)+(bpm6-bpm7)+(bpm8-bpm9) > 1000:
					#Cardic Arrest

				else:
					if (bpm-bpm1)+(bpm2-bpm3)+(bpm4-bpm5)+(bpm6-bpm7)+(bpm8-bpm9) < -1000:
						# Cardic Arrest

					else:
						#No Problems




