import getpass,math,os,secrets,time,random,winsound
try:
    import playsound
except ImportError:
    while True:
        input('Please install the required dependencies before playing.')
cls = lambda: os.system('cls')
def ps(sound):
    if sound=='none':
        winsound.PlaySound(None,winsound.SND_ASYNC)
    else:
        winsound.PlaySound('Resources/'+str(sound)+'.wav',winsound.SND_ASYNC)
def stop():
    ps('none')
    print('')
    while True:
        input('That\'s all for now, thanks!')
def error():
    cls()
    print('')
    print('FATAL ERROR: an unrecoverable problem has occured. Here are some')
    print('possible explanations:')
    print('')
    print('1. Your save data is corrupted, likely caused by entering an')
    print('   invalid Save Code.')
    print('2. You have discovered a bug that needs to be patched.')
    print('')
    print('If your Save Code has been intentionally edited, this is the')
    print('result of your own actions.')
    print('')
    print('If you have not edited your Save Code, please close and reopen')
    print('this program and go to GitHub -> Option 2. This program will not')
    print('react unless restarted, so please close it now.')
    while True:
        input('')
ps('Title')
startOption='0'
githubOption='0'
time.sleep(1)
print('')
print('''                                  ,'\ ''')
print('''    _.----.        ____         ,'  _\   ___    ___     ____''')
print('''_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.''')
print('''\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |''')
print(''' \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |''')
print('''   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |''')
print('''    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |''')
print('''     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |''')
print('''      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |''')
print('''       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |''')
print('''        \_.-'       |__|    `-._ |              '-.|     '-.| |   |''')
print('''                                `'                            '-._|''')
print('')
time.sleep(2.65)
print('                          PythonRed Version')
time.sleep(1.85)
print('')
input('                        Press Enter to begin!')
cls()
print('')
print('1. Continue')
print('2. New Game')
print('3. GitHub')
print('')
while startOption!='2':
    startOption=input('>')
    print('')
    if startOption!='1' and startOption!='2' and startOption!='3':
        cls()
        print('')
        print('Invalid answer!')
        print('')
        print('1. Continue')
        print('2. New Game')
        print('3. GitHub')
        print('')
    elif startOption=='1':
        cls()
        print('')
        print('Saving and continuing coming soon!')
        print('')
        print('1. Continue')
        print('2. New Game')
        print('3. GitHub')
        print('')
    elif startOption=='3':
        cls()
        print('')
        print('1. GitHub Repository Link + README')
        print('2. I Found a Bug / I Recieved a "FATAL ERROR"')
        print('3. I Have a Feature Request')
        print('4. Back')
        print('')
        while githubOption!='4':
            githubOption=input('>')
            if githubOption=='1':
                cls()
                print('')
                print('Please access the GitHub Repository here:')
                print('https://github.com/TurnipGuy30/Pokemon-PythonRed')
                print('From the Repository, scroll down to find the README.')
                print('')
                print('1. GitHub Repository Link + README')
                print('2. I Found a Bug / I Recieved a "FATAL ERROR"')
                print('3. I Have a Feature Request')
                print('4. Back')
                print('')
            elif githubOption=='2':
                cls()
                print('')
                print('Please create an Issue on the Issues page:')
                print('https://github.com/TurnipGuy30/Pokemon-PythonRed/issues')
                print('Please give information regarding what you did to cause')
                print('the error, how to replicate the situation, and, if')
                print('possible, your Save Code. I will do my best to recover')
                print('any lost data.')
                print('')
                print('1. GitHub Repository Link + README')
                print('2. I Found a Bug / I Recieved a "FATAL ERROR"')
                print('3. I Have a Feature Request')
                print('4. Back')
                print('')
            elif githubOption=='3':
                cls()
                print('')
                print('Please create an Issue on the Issues page:')
                print('https://github.com/TurnipGuy30/Pokemon-PythonRed/issues')
                print('Please give reasoning as to why you want your feature')
                print('added to the game. For example, is it a mechanic in')
                print('another Pokemon game? Will it help the code be more')
                print('flexible? And yes, you can ask for a custom Pokemon!')
                print('')
                print('1. GitHub Repository Link + README')
                print('2. I Found a Bug / I Recieved a "FATAL ERROR"')
                print('3. I Have a Feature Request')
                print('4. Back')
                print('')
            elif githubOption!='4':
                    githubOption='0'
    if startOption!='2':
        startOption='0'
cls()
print('')
print('If you chose "New Game" by accident, please quit now.')
print('Otherwise, press Enter to start a new game, and thanks')
input('for playing!')
cls()
print('')
print('Please wait..')
print('')
ps('Flutey')
pokemon=[['0','MISSINGNO.','NULL','60000','10000','10000','10000','10000','10000','10000'],['1','BULBASAUR','GRASS','318','45','49','49','65','65','45'],['2','IVYSAUR','GRASS','405','60','62','63','80','80','60'],['3','VENUSAUR','GRASS','525','80','82','83','100','100','80'],['4','CHARMANDER','FIRE','309','39','52','43','60','50','65'],['5','CHARMELEON','FIRE','405','58','64','58','80','65','80'],['6','CHARIZARD','FIRE','534','78','84','78','109','85','100'],['7','SQUIRTLE','WATER','314','44','48','65','50','64','43'],['8','WARTORTLE','WATER','405','59','63','80','65','80','58'],['9','BLASTOISE','WATER','530','79','83','100','85','105','78'],['10','CATERPIE','BUG','195','45','30','35','20','20','45'],['11','METAPOD','BUG','205','50','20','55','25','25','30'],['12','BUTTERFREE','BUG','395','60','45','50','90','80','70'],['13','WEEDLE','BUG','195','40','35','30','20','20','50'],['14','KAKUNA','BUG','205','45','25','50','25','25','35'],['15','BEEDRILL','BUG','395','65','90','40','45','80','75'],['16','PIDGEY','NORMAL','251','40','45','40','35','35','56'],['17','PIDGEOTTO','NORMAL','349','63','60','55','50','50','71'],['18','PIDGEOT','NORMAL','479','83','80','75','70','70','101'],['19','RATTATA','NORMAL','253','30','56','35','25','35','72'],['20','RATICATE','NORMAL','413','55','81','60','50','70','97'],['21','SPEAROW','NORMAL','262','40','60','30','31','31','70'],['22','FEAROW','NORMAL','442','65','90','65','61','61','100'],['23','EKANS','POISON','288','35','60','44','40','54','55'],['24','ARBOK','POISON','448','60','95','69','65','79','80'],['25','PIKACHU','ELECTRIC','320','35','55','40','50','50','90'],['26','RAICHU','ELECTRIC','485','60','90','55','90','80','110'],['27','SANDSHREW','GROUND','300','50','75','85','20','30','40'],['28','SANDSLASH','GROUND','450','75','100','110','45','55','65'],['29','NIDORAN♀','POISON','275','55','47','52','40','40','41'],['30','NIDORINA','POISON','365','70','62','67','55','55','56'],['31','NIDOQUEEN','POISON','505','90','92','87','75','85','76'],['32','NIDORAN♂','POISON','273','46','57','40','40','40','50'],['33','NIDORINO','POISON','365','61','72','57','55','55','65'],['34','NIDOKING','POISON','505','81','102','77','85','75','85'],['35','CLEFAIRY','FAIRY','323','70','45','48','60','65','35'],['36','CLEFABLE','FAIRY','483','95','70','73','95','90','60'],['37','VULPIX','FIRE','299','38','41','40','50','65','65'],['38','NINETALES','FIRE','505','73','76','75','81','100','100'],['39','JIGGLYPUFF','NORMAL','270','115','45','20','45','25','20'],['40','WIGGLYTUFF','NORMAL','435','140','70','45','85','50','45'],['41','ZUBAT','POISON','245','40','45','35','30','40','55'],['42','GOLBAT','POISON','455','75','80','70','65','75','90'],['43','ODDISH','GRASS','320','45','50','55','75','65','30'],['44','GLOOM','GRASS','395','60','65','70','85','75','40'],['45','VILEPLUME','GRASS','490','75','80','85','110','90','50'],['46','PARAS','BUG','285','35','70','55','45','55','25'],['47','PARASECT','BUG','405','60','95','80','60','80','30'],['48','VENONAT','BUG','305','60','55','50','40','55','45'],['49','VENOMOTH','BUG','450','70','65','60','90','75','90'],['50','DIGLETT','GROUND','265','10','55','25','35','45','95'],['51','DUGTRIO','GROUND','425','35','100','50','50','70','120'],['52','MEOWTH','NORMAL','290','40','45','35','40','40','90'],['53','PERSIAN','NORMAL','440','65','70','60','65','65','115'],['54','PSYDUCK','WATER','320','50','52','48','65','50','55'],['55','GOLDUCK','WATER','500','80','82','78','95','80','85'],['56','MANKEY','FIGHTING','305','40','80','35','35','45','70'],['57','PRIMEAPE','FIGHTING','455','65','105','60','60','70','95'],['58','GROWLITHE','FIRE','350','55','70','45','70','50','60'],['59','ARCANINE','FIRE','555','90','110','80','100','80','95'],['60','POLIWAG','WATER','300','40','50','40','40','40','90'],['61','POLIWHIRL','WATER','385','65','65','65','50','50','90'],['62','POLIWRATH','WATER','510','90','95','95','70','90','70'],['63','ABRA','PSYCHIC','310','25','20','15','105','55','90'],['64','KADABRA','PSYCHIC','400','40','35','30','120','70','105'],['65','ALAKAZAM','PSYCHIC','500','55','50','45','135','95','120'],['66','MACHOP','FIGHTING','305','70','80','50','35','35','35'],['67','MACHOKE','FIGHTING','405','80','100','70','50','60','45'],['68','MACHAMP','FIGHTING','505','90','130','80','65','85','55'],['69','BELLSPROUT','GRASS','300','50','75','35','70','30','40'],['70','WEEPINBELL','GRASS','390','65','90','50','85','45','55'],['71','VICTREEBEL','GRASS','490','80','105','65','100','70','70'],['72','TENTACOOL','WATER','335','40','40','35','50','100','70'],['73','TENTACRUEL','WATER','515','80','70','65','80','120','100'],['74','GEODUDE','ROCK','300','40','80','100','30','30','20'],['75','GRAVELER','ROCK','390','55','95','115','45','45','35'],['76','GOLEM','ROCK','495','80','120','130','55','65','45'],['77','PONYTA','FIRE','410','50','85','55','65','65','90'],['78','RAPIDASH','FIRE','500','65','100','70','80','80','105'],['79','SLOWPOKE','WATER','315','90','65','65','40','40','15'],['80','SLOWBRO','WATER','490','95','75','110','100','80','30'],['81','MAGNEMITE','ELECTRIC','325','25','35','70','95','55','45'],['82','MAGNETON','ELECTRIC','465','50','60','95','120','70','70'],['83','FARFETCH\D','NORMAL','377','52','90','55','58','62','60'],['84','DODUO','NORMAL','310','35','85','45','35','35','75'],['85','DODRIO','NORMAL','470','60','110','70','60','60','110'],['86','SEEL','WATER','325','65','45','55','45','70','45'],['87','DEWGONG','WATER','475','90','70','80','70','95','70'],['88','GRIMER','POISON','325','80','80','50','40','50','25'],['89','MUK','POISON','500','105','105','75','65','100','50'],['90','SHELLDER','WATER','305','30','65','100','45','25','40'],['91','CLOYSTER','WATER','525','50','95','180','85','45','70'],['92','GASTLY','GHOST','310','30','35','30','100','35','80'],['93','HAUNTER','GHOST','405','45','50','45','115','55','95'],['94','GENGAR','GHOST','500','60','65','60','130','75','110'],['95','ONIX','ROCK','385','35','45','160','30','45','70'],['96','DROWZEE','PSYCHIC','328','60','48','45','43','90','42'],['97','HYPNO','PSYCHIC','483','85','73','70','73','115','67'],['98','KRABBY','WATER','325','30','105','90','25','25','50'],['99','KINGLER','WATER','475','55','130','115','50','50','75'],['100','VOLTORB','ELECTRIC','330','40','30','50','55','55','100'],['101','ELECTRODE','ELECTRIC','490','60','50','70','80','80','150'],['102','EXEGGCUTE','GRASS','325','60','40','80','60','45','40'],['103','EXEGGUTOR','GRASS','530','95','95','85','125','75','55'],['104','CUBONE','GROUND','320','50','50','95','40','50','35'],['105','MAROWAK','GROUND','425','60','80','110','50','80','45'],['106','HITMONLEE','FIGHTING','455','50','120','53','35','110','87'],['107','HITMONCHAN','FIGHTING','455','50','105','79','35','110','76'],['108','LICKITUNG','NORMAL','385','90','55','75','60','75','30'],['109','KOFFING','POISON','340','40','65','95','60','45','35'],['110','WEEZING','POISON','490','65','90','120','85','70','60'],['111','RHYHORN','GROUND','345','80','85','95','30','30','25'],['112','RHYDON','GROUND','485','105','130','120','45','45','40'],['113','CHANSEY','NORMAL','450','250','5','5','35','105','50'],['114','TANGELA','GRASS','435','65','55','115','100','40','60'],['115','KANGASKHAN','NORMAL','490','105','95','80','40','80','90'],['116','HORSEA','WATER','295','30','40','70','70','25','60'],['117','SEADRA','WATER','440','55','65','95','95','45','85'],['118','GOLDEEN','WATER','320','45','67','60','35','50','63'],['119','SEAKING','WATER','450','80','92','65','65','80','68'],['120','STARYU','WATER','340','30','45','55','70','55','85'],['121','STARMIE','WATER','520','60','75','85','100','85','115'],['122','MR. MIME','PSYCHIC','460','40','45','65','100','120','90'],['123','SCYTHER','BUG','500','70','110','80','55','80','105'],['124','JYNX','ICE','455','65','50','35','115','95','95'],['125','ELECTABUZZ','ELECTRIC','490','65','83','57','95','85','105'],['126','MAGMAR','FIRE','495','65','95','57','100','85','93'],['127','PINSIR','BUG','500','65','125','100','55','70','85'],['128','TAUROS','NORMAL','490','75','100','95','40','70','110'],['129','MAGIKARP','WATER','200','20','10','55','15','20','80'],['130','GYARADOS','WATER','540','95','125','79','60','100','81'],['131','LAPRAS','WATER','535','130','85','80','85','95','60'],['132','DITTO','NORMAL','288','48','48','48','48','48','48'],['133','EEVEE','NORMAL','325','55','55','50','45','65','55'],['134','VAPOREON','WATER','525','130','65','60','110','95','65'],['135','JOLTEON','ELECTRIC','525','65','65','60','110','95','130'],['136','FLAREON','FIRE','525','65','130','60','95','110','65'],['137','PORYGON','NORMAL','395','65','60','70','85','75','40'],['138','OMANYTE','ROCK','355','35','40','100','90','55','35'],['139','OMASTAR','ROCK','495','70','60','125','115','70','55'],['140','KABUTO','ROCK','355','30','80','90','55','45','55'],['141','KABUTOPS','ROCK','495','60','115','105','65','70','80'],['142','AERODACTYL','ROCK','515','80','105','65','60','75','130'],['143','SNORLAX','NORMAL','540','160','110','65','65','110','30'],['144','ARTICUNO','ICE','580','90','85','100','95','125','85'],['145','ZAPDOS','ELECTRIC','580','90','90','85','125','90','100'],['146','MOLTRES','FIRE','580','90','100','90','125','85','90'],['147','DRATINI','DRAGON','300','41','64','45','50','50','50'],['148','DRAGONAIR','DRAGON','420','61','84','65','70','70','70'],['149','DRAGONITE','DRAGON','600','91','134','95','100','100','80'],['150','MEWTWO','PSYCHIC','680','106','110','90','154','90','130'],['151','MEW','PSYCHIC','600','100','100','100','100','100','100']]
introComplete=False
introAnswer=''
playerName=''
starterChoice=''
starterAnswer=''
starterConfirm=False
starter=''
currentLocation=''
currentMusic=''
option=''
startMenu=False
surf=False
party1=['']
party2=['']
party3=['']
party4=['']
party5=['']
party6=['']
bag=[['',0],['',0]]
def encounter():
    victory=False
    escape=False
    while victory==False and escape==False:
        print('')
        input('A wild POKéMON appeared!')
        input('...')
        input('You got away safely!')
        escape=True
    victory=escape=False
"""
def encounter(species,level,canEscape):

"""
cls()
time.sleep(5)
while True:
    if introComplete==False:
        ps('Intro')
        print('')
        input('OAK: Hello there! Welcome to the world of POKéMON! My name is OAK!')
        input('People call me the POKéMON PROFESSOR!')
        print('')
        print("""    `._ """)
        print("""     \ `. """)
        print("""      \  `. """)
        print("""       .   `. """)
        print("""       j     :-----+...-. """)
        print("""       /  _,'   /""_     `.     _,..._ """)
        print("""     ,'  '      .-"c|"`+- -+--"'      `-.._ """)
        print('''   ,'            """+_ |       _,--""--.._ `---.. ''')
        print("""  '     _             "'      '\          `--._  `. """)
        print(""" |    -'                      _.'              `-. `. """)
        print(""" (     __   ,.----.._        \``-.                |  `._ """)
        print('''  `.  /_ """   ___.| ,.      j  `.`.   ,          `.    `. ''')
        print('''    `'| |    ,'    '.'/'""'"'   j`. \,'|  _________||""`-'`. ''')
        print("""      `_.\   j       j      __-'|_/'"._:."  __       .    " """)
        print("""          | /        /      \ `/        |`.   .   ..._`. """)
        print("""          ||        /       | /         | |    :.'    -/ """)
        print("""          |'    _,-'        |.`.       ,' |   | |\_ """)
        print("""    _     | `--'     _,-    . `.`--- ,'   /   |  .\`-.. """)
        print('''    |`v,-'"""'`-.,.-'        `._``--'  _,'    |  | \  ,' ''')
        print(""",--'`- _       \ \              '""''`'       `_,'  +- """)
        print(""" -.'    \       . |                        /`     ,---. """)
        print(""" -`\    |       | L                        `-'     '""'`\ """)
        print(''' '---...:_      / \                          |   ,.-""".| ''')
        print("""          '---+'   \                         ' ,'       ` """)
        print("""               '`''".                       / /          `. """)
        print("""                     \                     j |            '. """)
        print("""                      `.                   | |              \ """)
        print("""                        \ _                |/             /\| """)
        print("""                         / "-   --""----+--'             / || """)
        print('''                        `v'"""""-..     |      `..__.,.-'-.,, ''')
        print("""                         |         `-.,'           .`.J     / """)
        print("""                         |            |             '---...' """)
        print("""                         |     .     / """)
        print("""                         |    | `,  j """)
        print("""                        ..--+'"--_  / """)
        print("""                         `-.|     \' """)
        print("""                             `----' """)
        print('')
        input('This world is inhabited by powerful creatures called POKéMON!')
        input('For some people, POKéMON are pets. Others use them for fights.')
        input('Myself... I study POKéMON as a profession. However, they are')
        input('mysterious and there is a lot we have yet to discover about them.')
        print('')
        print('First, what is your name?')
        print('')
        print('1. NEW NAME')
        print('2. PYTHON')
        print('3. ASH')
        print('')
        while introAnswer!='1' and introAnswer!='2' and introAnswer!='3':
            introAnswer=input('>')
        if introAnswer=='2':
            playerName='PYTHON'
        elif introAnswer=='3':
            playerName='ASH'
        elif introAnswer=='1':
            print('')
            print('(Caps, 15 chars. max)')
            print('')
            playerName=input('>')
            while len(playerName)>15 or playerName=='':
                playerName=input('>')
        else:
            print('Invalid answer!')
        playerName=playerName.upper()
        print('')
        input(f'Right! So your name is {playerName}!')
        print('')
        input('Now, since you\'re so raring to go, I\'ve prepared a rival for you.')
        input('He will go on an adventure just like yours, and battle you along')
        input('the way.')
        print('')
        print('...Erm, what is his name again?')
        print('')
        input('>')
        print('')
        input('...')
        input('Ha, did you really think I\'d forgotten our Champion\'s name?')
        input('His name is JOHNNY! He decided to donate his strong POKéMON and start')
        input('his journey over, using only the best techniques. You\'ll meet him soon!')
        print('')
        input(playerName+'! Your very own POKéMON legend is about to unfold! A world of')
        input('dreams and adventures with POKéMON awaits! Let\'s go!')
        ps('Pallet')
        print('')
        input('...')
        input(f'{playerName} is playing the WII U!')
        input('...')
        input('Alright, that\'s enough POKKEN! Time to get going!')
        input(playerName+' eagerly heads downstairs.')
        print('')
        input('MOM: Right. All kids leave home some day. Have a good time!')
        input('PROFESSOR OAK, next door, is looking for you.')
        print('')
        input(f'After running outside, {playerName} heads to OAK\'s LAB.')
        print('')
        input('However, it seems OAK isn\'t there! But suspicious-looking person')
        input(f'person meets {playerName} at the door. He takes a step back, takes a look')
        input(f'at {playerName}, and walks away to the NORTH. {playerName} decides to')
        input('follow from a distance.')
        print('')
        input(f'{playerName} watches the stranger head into some long grass and is about')
        input('to follow after them, when a voice starts shouting.')
        print('')
        input('OAK: Hey! Wait! Don\'t go out!')
        print('')
        input(f'{playerName} turns around to see OAK running up from behind.')
        print('')
        input('OAK: It\'s unsafe! Wild POKéMON live in tall grass! You need your own')
        input('POKéMON for your protection. Here, come with me!')
        print('')
        input(f'{playerName} follows OAK to the LAB.')
        ps('OakLab')
        print('')
        input(f'OAK: Here, {playerName}! There are 3 POKé BALLS here, each containing a')
        input('starter POKéMON! They each have a lot of potential!')
        print('')
        input(f'{playerName} tells OAK about his suspicious encounter.')
        print('')
        input('OAK: Ah! It seems you\'ve already met JOHNNY then! He must\'ve already come')
        input('along and... yes, he\'s taken a SQUIRTLE... You see, these starter POKéMON are')
        input('perfect for beginner trainers, but were very rare until JOHNNY discovered')
        input('their habitats. He\'s done a lot for people all around the world.')
        print('')
        input('But enough about that! It\'s your turn to choose a POKéMON! There has been a')
        input('surge of rare encounters lately, and we\'re doing our best, but no trainers')
        input('want them because it requires a lot of strategy to bring out their potential.')
        print('')
        input('Oh! I know! Why don\'t you choose out of all the POKéMON we have! Of course,')
        input('these 3 starter POKéMON are available too. Choose!')
        print('')
        print('Choose a POKéMON:')
        print('')
        print('1. BULBASAUR')
        print('2. CHARMANDER')
        print('3. SQUIRTLE')
        print('4. DIGLETT')
        print('5. MACHOP')
        print('6. GASTLY')
        print('7. LAPRAS')
        print('8. EEVEE')
        while starterConfirm==False:
            print('')
            starterChoice=input('>')
            if starterChoice=='1':
                print('')
                print('Are you sure you want the SEED POKéMON, BULBASAUR? (y/n)')
                while starterAnswer!='y' and starterAnswer!='n':
                    starterAnswer=input('>')
                starterAnswer=starterAnswer.upper()
                if starterAnswer=='Y':
                    starter=1
                    starterConfirm=True
                starterAnswer=''
            elif starterChoice=='2':
                print('')
                print('Are you sure you want the LIZARD POKéMON, CHARMANDER? (y/n)')
                while starterAnswer!='y' and starterAnswer!='n':
                    starterAnswer=input('>')
                starterAnswer=starterAnswer.upper()
                if starterAnswer=='Y':
                    starter=4
                    starterConfirm=True
                starterAnswer=''
            elif starterChoice=='3':
                print('')
                print('Are you sure you want the TINYTURTLE POKéMON, SQUIRTLE? (y/n)')
                while starterAnswer!='y' and starterAnswer!='n':
                    starterAnswer=input('>')
                starterAnswer=starterAnswer.upper()
                if starterAnswer=='Y':
                    starter=7
                    starterConfirm=True
                starterAnswer=''
            elif starterChoice=='4':
                print('')
                print('Are you sure you want the MOLE POKéMON, DIGLETT? (y/n)')
                while starterAnswer!='y' and starterAnswer!='n':
                    starterAnswer=input('>')
                starterAnswer=starterAnswer.upper()
                if starterAnswer=='y':
                    starter=50
                    starterConfirm=True
                starterAnswer=''
            elif starterChoice=='5':
                print('')
                print('Are you sure you want the SUPERPOWER POKéMON, MACHOP? (y/n)')
                while starterAnswer!='y' and starterAnswer!='n':
                    starterAnswer=input('>')
                starterAnswer=starterAnswer.upper()
                if starterAnswer=='Y':
                    starter=66
                    starterConfirm=True
                starterAnswer=''
            elif starterChoice=='6':
                print('')
                print('Are you sure you want the GAS POKéMON, GASTLY? (y/n)')
                while starterAnswer!='y' and starterAnswer!='n':
                    starterAnswer=input('>')
                starterAnswer=starterAnswer.upper()
                if starterAnswer=='Y':
                    starter=92
                    starterConfirm=True
                starterAnswer=''
            elif starterChoice=='7':
                print('')
                print('Are you sure you want the TRANSPORT POKéMON, LAPRAS? (y/n)')
                while starterAnswer!='y' and starterAnswer!='n':
                    starterAnswer=input('>')
                starterAnswer=starterAnswer.upper()
                if starterAnswer=='Y':
                    starter=131
                    starterConfirm=True
                starterAnswer=''
            elif starterChoice=='8':
                print('')
                print('Are you sure you want the EVOLUTION POKéMON, EEVEE? (y/n)')
                while starterAnswer!='y' and starterAnswer!='n':
                    starterAnswer=input('>')
                starterAnswer=starterAnswer.upper()
                if starterAnswer=='Y':
                    starter=133
                    starterConfirm=True
                starterAnswer=''
            elif starterChoice=='0':
                print('')
                print('Ae yu se yu wt te ^"!;@~?#\\*% PKEMN, MISSINGNO.? (y/n)')
                while starterAnswer!='y' and starterAnswer!='n':
                    starterAnswer=input('>')
                starterAnswer=starterAnswer.upper()
                if starterAnswer=='Y':
                    starter=0
                    starterConfirm=True
                starterAnswer=''
        print('')
        input(f'{playerName} recieved {pokemon[starter][1]}!')
        print('')
        input('OAK: Now, I\'m sure you\'re just itching to battle, but you\'ll get your')
        input('chance soon enough.')
        input('Oh! Take this! All new trainers get one!')
        print('')
        input(f'{playerName} obtained POKéDEX!')
        print('')
        input('This POKéDEX is a high-tech machine that collects data on every POKéMON')
        input('you meet!')
        print('')
        input('Now go! NORTH along ROUTE 1, straight to VIRDIAN CITY!')
        print('')
        input(f'{playerName} went out and approached the tall grass on ROUTE 1, feeling')
        input('ready to go!')
        ps('none')
        print('')
        input('Meanwhile, at OAK\'s LAB...')
        print('')
        input('OAK: Oh, JOHNNY... He\'s really unstoppable, defeating RED and all.')
        input('With his shortcuts, he must have already reached VIRDIAN FOREST!')
        print('')
        input('...')
        print('')
        input('*INCOMING CALL*')
        print('')
        input('BRENDAN: Hi, PROFESSOR OAK! Have you seen MAY?')
        input('She ran off and I can\'t find her anywhere!')
        print('')
        input('OAK: ...')
        print('')
        input('You see... she\'s headed to PEWTER CITY with JOHNNY.')
        print('')
        input('INTRO COMPLETE!')
        print('')
        party1=[int(pokemon[starter][0]),str(pokemon[starter][1]),5,random.randint(1,15),random.randint(1,15),random.randint(1,15),random.randint(1,15),random.randint(1,15),random.randint(1,15)]
        introComplete=True
        currentLocation='Route1-S'
    elif startMenu==True:
        print('')
        print('1. POKéDEX')
        print('2. POKéMON')
        print('3. ITEM')
        print(f'4. {playerName}')
        print('5. SAVE')
        print('6. OPTION')
        print('7. EXIT')
        print('')
        while option=='':
            option=input('>')
            if option=='1':
                stop()
            elif option=='2':
                print('')
                if party1!=['']:
                    print('1. '+party1[1])
                if party2!=['']:
                    print('2. '+party2[1])
                if party3!=['']:
                    print('3. '+party3[1])
                if party4!=['']:
                    print('4. '+party4[1])
                if party5!=['']:
                    print('5. '+party5[1])
                if party6!=['']:
                    print('6. '+party6[1])
            elif option=='3':
                stop()
            elif option=='4':
                stop()
            elif option=='5':
                stop()
            elif option=='6':
                stop()
            elif option=='7':
                startMenu==False
            else:
                option=''
    elif currentLocation=='Pallet':
        if currentMusic!='Pallet':
            ps('Pallet')
            currentMusic='Pallet'
        print('')
        print('CURRENT LOCATION: PALLET TOWN')
        print('"Shades of your journey await!"')
        print('')
        print('1. Head NORTH to SOUTH ROUTE 1')
        print('2. Head SOUTH to AQUA-ROUTE ?')
        print(f'3. {playerName}\'s House')
        print('4. OAK\'s LAB')
        print('')
        while option=='':
            option=input('>')
            if option=='1':
                currentLocation='Route1-S'
            elif option=='2':
                print('')
                input('The water is a deep, clear blue.')
                print('')
            elif option=='3':
                currentLocation='PlayerHouse'
            elif option=='4':
                print('')
                input('Coming soon!')
                print('')
            elif option=='s':
                startMenu=True
            else:
                option=''
        option=''
    elif currentLocation=='PlayerHouse':
        if currentMusic!='Pallet':
            ps('Pallet')
            currentMusic='Pallet'
        print('')
        print(f'CURRENT LOCATION: {playerName}\'S HOUSE - DOWNSTAIRS')
        print('')
        print('1. Talk to MOM')
        print('2. Head UPSTAIRS')
        print('3. Leave to PALLET TOWN')
        print('')
        while option=='':
            option=input('>')
            if option=='1':
                print('')
                input(f'MOM: It looks like you and {party1[1]} are having fun together!')
                print('')
            elif option=='2':
                currentLocation='PlayerHouse-U'
            elif option=='3':
                currentLocation='Pallet'
            else:
                option=''
        option=''
    elif currentLocation=='PlayerHouse-U':
        if currentMusic!='Pallet':
            ps('Pallet')
            currentMusic='Pallet'
        print('')
        print(f'CURRENT LOCATION: {playerName}\'S HOUSE - UPSTAIRS')
        print('')
        print('1. PC')
        print('2. Wii U')
        print('3. Head DOWNSTAIRS')
        print('')
        while option=='':
            option=input('>')
            if option=='1':
                print('')
                input('Coming soon!')
                print('')
            elif option=='2':
                print('')
                input(f'Why play POKKEN when you can spend time with {party1[1]}?')
                print('')
            elif option=='3':
                currentLocation='PlayerHouse'
            else:
                option=''
        option=''
    elif currentLocation=='Route1-S':
        if currentMusic!='Route1':
            ps('Route1')
            currentMusic='Route1'
        print('')
        print('CURRENT LOCATION: SOUTH ROUTE 1')
        print('')
        print('1. Head NORTH to NORTH ROUTE 1')
        print('2. Head SOUTH to PALLET TOWN')
        print('')
        while option=='':
            option=input('>')
            if option=='1':
                encounter()
                currentLocation='Route1-N'
            elif option=='2':
                currentLocation='Pallet'
            else:
                option=''
        option=''
    elif currentLocation=='Route1-N':
        if currentMusic!='Route1':
            ps('Route1')
            currentMusic='Route1'
        print('')
        print('CURRENT LOCATION: NORTH ROUTE 1')
        print('')
        print('1. Head NORTH to VIRIDIAN CITY')
        print('2. Head SOUTH to SOUTH ROUTE 1')
        print('')
        while option=='':
            option=input('>')
            if option=='1':
                currentLocation='Viridian'
            elif option=='2':
                currentLocation='Route1-S'
            else:
                option=''
        option=''
    elif currentLocation=='Viridian':
        if currentMusic!='Viridian':
            ps('Viridian')
            currentMusic='Viridian'
        print('')
        print('CURRENT LOCATION: VIRIDIAN CITY')
        print('"The eternally green paradise"')
        print('')
        print('(Beyond this point has not yet been made, sorry!)')
        print('')
        print('1. Head NORTH to ROUTE 2')
        print('2. Head SOUTH to NORTH ROUTE 1')
        print('3. Head WEST to ???')
        print('4. POKéMON CENTER')
        print('5. POKé MART')
        print('6. VIRIDIAN GYM')
        print('')
        while option=='':
            option=input('>')
            if option=='1':
                print('')
                input('Coming soon!')
                print('')
            elif option=='2':
                currentLocation='Route1-N'
            elif option=='3':
                print('')
                input('There\'s a gate!')
                input('...')
                input('It seems to be locked!')
                print('')
            elif option=='4':
                print('')
                input('Coming soon!')
                print('')
            elif option=='5':
                print('')
                input('Coming soon!')
                print('')
            elif option=='6':
                print('')
                input('...')
                input('The door\'s locked!')
                print('')
            else:
                option=''
        option=''
    else:
        error() ## --- Mystery Gift #2: "HACKER" ---
