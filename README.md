## Pokemon PythonRed

### Important Notes:

* This is not meant to be a perfect recreation of _Pokémon Red_. It’s just a test of my own coding skills. So basically, if you’re looking to play _Pokémon Red_ on PC, you can find an emulator.
* Throughout this process, I will only be able to refer to online resources. This is because I want to limit myself to specific conditions that I can’t fully explain. One of these conditions is I can’t access the official game (or related ROMs).
* This is my first GitHub project, and I’m not very acquainted to its features and capabilities.

Summary: **_Don’t Judge_!**

###### Note to players: to download, please see [Releases](https://github.com/TurnipGuy30/Pokemon-PythonRed/releases)!

![](https://tse2.mm.bing.net/th/id/OIP.VHV4L97MJfgNd5DMRep1oQHaHZ?w=201&h=200&c=7&o=5&dpr=1.5&pid=1.7)

### Progress / To Do:

##### Progress Overview
I've done the bare minimum so far, I need some resources to start properly:

* _Pokémon Red_ offset list
* _Pokémon Red_ Event Flags list
* _Pokémon Red_’s entire story line (dialogue, trainer names, cutscenes, etc.)

#### My Current Process
* (_check!_) Create the .py file and start GitHub repository
* Find the resources listed above
* (_check!_) Actually begin coding, starting with the basics of a variable list.
* (_check!_) Code intro, then make first pre-release!

#### To Do
* Create Pokédex variable (explained later in Elements -> Pokémon Data)
* Find solution for in-game music
* Check out the _pygame_ Python module

###### For contributions, try one of ^THESE^, or check for typos in this document!

### Changed Elements:

#### Pokémon Data
The entire Kanto Pokédex will be stored as a variable, with a list item for each species:

```
Pokemon = [[],[],[]...]
```

Each `[]` includes this:

```
[Pokédex #, Name, Type 1, Type 2, Base HP, Base ATK, Base DEF, Base SP. ATK, Base SP. DEF, Base SPD, Catch Rate]
```

#### Menus
As far as I know, Python cannot support Pokémon Red’s menu layouts, so some changes will be needed:

Using an example from the game, this:

> Are you a boy or a girl?
>  
> Boy
> Girl

Will become this:

> Are you a boy or a girl?
> 
> 1. Boy
> 2. Girl
> 
> _

However, this requires a _lot_ of extra work. If the answer is invalid, the question must be asked again. Maybe like this:

```
...
//variables
...
playerGender = ‘’
...

print(‘Are you a boy or a girl?’)
print(‘’)

print(‘1. Boy’)
print(‘2. Girl’)
print(‘’)

while playerGender != ‘1’ and playerGender != ‘2’:

    playerGender=input(‘>’)
    print(‘’)

if playerGender != ‘1’ and playerGender != ‘2’:

    print(‘Invalid answer!’)
    print(‘’)
```

Of course, the custom _invalid_ message can change depending on the situation. In this example, as it takes place in talking to the Professor, I could use something like `Sorry, didn’t quite catch that!`.

#### _Lots_ of Variables
Basically everything the game keeps track of:
* Trainer info
* Party info
* If a place has been visited yet, for Fly locations (each city separately)
* If cutscenes have been triggered yet
* ‘Event flags’
* Pokédex
* Trainer battle info
* Game mechanic settings for accessibility

#### Saving System
So all of ^THOSE^ variables in a string that can be entered at the program’s startup so it can be read and loaded up. But, as the program is updated, the strings must change. This shouldn’t be too hard to implement.

#### Multiplayer?
Link Trades and Battles supported by Keys that contain Party information:

Battles should be relatively simple:
* Two people with the game open the Link Battle screen in the Pokémon Centre, one chooses Send Key, the other chooses Receive Key.
* The ‘Send Key’ player is given a ‘Key’ (string of digits) to email to the ‘Receive Key’ player, who inputs the Key into their menu. This key contains all of the ‘Send Key’ player’s information; Trainer name, party info, etc..
* The battle then carries out on the Receiver’s device, each player taking turns moving (i.e. a Pokémon battle).

If Exp. is involved, though likely not:
* The Receiver can gain Exp. on their device, and they can email the Sender another Key to input into their device, giving them the Exp. earned from the battle.

However, this allows a player to directly edit their party information, which is not a good idea. Trades would have even more cheating potential, so they might come in ‘a later update’!

#### _That's all, watch this space, and thanks!_

###### For reading this far, you get the privelege of seeing this:
![](https://tse2.mm.bing.net/th/id/OIP.odJ_-1cegyviucDJCNG_XAAAAA?w=136&h=180&c=7&o=5&dpr=1.5&pid=1.7)
