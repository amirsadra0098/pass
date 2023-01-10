import string
import random
import colorama



print(colorama.Fore.GREEN+'''
      
            
                    _            __      ___   ___   ___   ___  
                   | |           \ \    / _ \ / _ \ / _ \ / _ \ 
      ___  __ _  __| |_ __ __ _   \ \  | | | | | | | (_) | (_) |
     / __|/ _` |/ _` | '__/ _` |   > > | | | | | | |\__, |> _ < 
     \__ \ (_| | (_| | | | (_| |  / /  | |_| | |_| |  / /| (_) |
     |___/\__,_|\__,_|_|  \__,_| /_/    \___/ \___/  /_/  \___/ 
                                                        
            amirsadra 0098 >>>>>>>>>>
            instagram: @sdr_vob & @36sdr
            telegram: @sdr_vob
            
            
            ''')


larg = int(input(colorama.Fore.YELLOW+'please enter paswoord length : \n'))
sdr = string.ascii_letters+string.digits +"*&^%$#@!?:<>=-+./\_"
pss= ''.join([random.choice(sdr) for i in range(larg)])
print(colorama.Fore.BLUE+"your password is ready : \n\n {}\n".format(pss))



#instagram: @36sdr


#im sadra


