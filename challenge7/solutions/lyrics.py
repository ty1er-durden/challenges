def song ( num, colour ):
   #
   # print ("test", num, colour)
   print ("")
   while (num > 0):
      if (num > 1): 
         boottles = num2words (num)
         print (boottles,colour,"bottles sitting on the wall,")
         sya=(boottles+ colour+ "bottles sitting on the wall,")
         speaker.Speak(sya) 
         print (boottles,colour,"bottles sitting on the wall,")
         speaker.Speak(sya) 
         print ("And if one",colour,"bottle should accidentally fall")
         sya=("And if one"+colour+"bottle should accidentally fall")
         speaker.Speak(sya) 
      else :
        boottles = num2words (num)
        print (boottles," ",colour," bottle sitting on the wall,")
        print (boottles," ",colour," bottle sitting on the wall,")
        sya=(boottles + colour+ " bottle sitting on the wall,")
        speaker.Speak(sya) 
        speaker.Speak(sya) 
        print ("And if one",colour," bottle should accidentally fall,")
        sya=("And if one"+ colour+ " bottle should accidentally fall,")
        speaker.Speak(sya) 

      num -=1
      boottles = num2words (num)
      if (num > 1): 
        print ("There’ll be", boottles, colour," bottles sitting on the wall.")
        sya=("There’ll be"+ boottles+ colour + " bottles sitting on the wall.")
        speaker.Speak(sya) 
        print ("")
      else :
        print ("There’ll be", boottles, colour," bottle sitting on the wall.")
        sya=("There’ll be"+ boottles+ colour+" bottle sitting on the wall.")
        speaker.Speak(sya) 
        print ("")
   return   


from num2words import num2words 
import win32com.client 
speaker = win32com.client.Dispatch("SAPI.SpVoice") 
speaker.Speak("Please tell me how many Bottles ? ")
nums = int (input ("Please tell me how many Bottles ? "))
btl = str(nums) + " Bottles of which colour? "
speaker.Speak(btl)
clr = input (btl) 
#clr = input ("Bottles of which colour?")
song ( num=nums, colour=clr )