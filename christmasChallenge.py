fname = ['Cupid','Moon','Zippy','Dancer','Blizzard','Sparkle','Flash','Holly','Cosy','Star','Frostie','Prancer','Lumi','Wiggles','Thundersnow','Snowball','Vixen','Snuggly','Donner','Olive','Dasher','Comet','Blitzen','Rudolph','Mistletoe','Ditzie']
hname = ['Det','Zu','Zoon',"O'",'Nuo','Kind','Kaen','Fa','Ab','Fra','Sina','De','Den','Lut','Iza','Av','Von','Suo','Ek','Alk','Mc','Ex','Og','Poika','Af','Ate']
sname = ['Wintersly','Joutsen','Pakkanen','Hirvieläin','Bikkjekaldt','Skyloni','Vaerfast','Rantaski','Sommerfugl','Kuurason','Skoghundski','Tinseltoes','Haukkaskil','Edderkopp','Snaigė','Sateenkari','Flurry','Ornski','Icicle','Wolfstamper','Mittens','Sleighson','Flakerski','Lumimyrsky','Myrsky','Elkson']
#Asks for users input
print('Welcome to reindeer generator')
firstName = input('Enter your first name: ')
secondName = input('Enter your second name: ')
#Makes sure input is in lowercase
firstName = firstName.lower()
secondName = secondName.lower()
#Gets the length the user input
lenFir = len(firstName)
lenSec = len(secondName)
#Works out the Letter required and the position of where it is in the alphabet 
fLetter = firstName[0]
position1 = ord(fLetter) - 97
lLetter = firstName[(lenFir-1)]
position2 = ord(lLetter) - 97
secLastLetter = secondName [(lenSec-1)]
position3 = ord(secLastLetter) - 97

#Outputs the results. 
print('Your reindeer name is ' + (fname[position1]) , (hname[position2]) , (sname[position3]))

