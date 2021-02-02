## Pokemon PythonRed

### To Play:

First, you need to have `Python` installed, obviously. If this isn't already done, you can find the insaller [here](https://sdassq-my.sharepoint.com/:u:/g/personal/ba004629_bac_qld_edu_au/ESCL5J4RZcFLrzRbpcnyy6EBjn22m7ZuFJQMH7HiIW0XFw?e=cFyr1g) (v3.6.8). This should also install `pip` which is required in the next step.

Next, you need to open Command Prompt (or another Command Line) and _individually_ run the following commands to install dependencies:

`pip install pillow`

`pip install playsound`

`pip install pygame`

When that's all done, to download the game, please see [Releases](https://github.com/TurnipGuy30/Pokemon-PythonRed/releases)!

### Important Notes:

* This is not meant to be a perfect recreation of _Pokémon Red_. It’s just a test of my own coding skills. So basically, if you’re looking to play _Pokémon Red_ on PC, you can find an emulator.
* Throughout this process, I will only be able to refer to online resources. This is because I want to limit myself to specific conditions that I can’t fully explain. One of these conditions is I can’t access the official game.
* This is my first GitHub project, and I’m not very acquainted to its features and capabilities.
* I've only recently learnt Markdown, specifically for this project.

Summary: **_Don’t Judge_!**

###### Here's a Poké Ball for you!
![](https://tse2.mm.bing.net/th/id/OIP.VHV4L97MJfgNd5DMRep1oQHaHZ?w=201&h=200&c=7&o=5&dpr=1.5&pid=1.7)

### Progress / To Do:

##### Progress Overview
It's going well, more coming soon!

#### Story Elements (SPOILERS - COVER LEFT OF PAGE WITH HAND AND SCROLL)

[Kanto Map](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/3bddf750-53a0-4a9f-872f-8d13685a758f/d3c4hsg-5acbd78f-c4cb-4f40-a87a-05700ac859a4.png/v1/fill/w_900,h_882,q_75,strp/labeled_map_of_kanto_by_rythos-d3c4hsg.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwic3ViIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl0sIm9iaiI6W1t7InBhdGgiOiIvZi8zYmRkZjc1MC01M2EwLTRhOWYtODcyZi04ZDEzNjg1YTc1OGYvZDNjNGhzZy01YWNiZDc4Zi1jNGNiLTRmNDAtYTg3YS0wNTcwMGFjODU5YTQucG5nIiwid2lkdGgiOiI8PTkwMCIsImhlaWdodCI6Ijw9ODgyIn1dXX0.Ycjt66m7t9k-8tio4Tsc0YTsP_nu7Lz2cGBm4CdZWN8)

* [x] Start menu
 * Pokemon logo
* [x] Intro
 * Nidorino picture
 * Choose name
* [ ] Pallet Town
 * Select starter
* [ ] Route 1
 * No encounters coming back
* [ ] Viridian City
 * Locked Gym
 * West blocked until later
* [ ] Oak's Parcel
 * Cannot proceed until after completion
* [ ] Route 2
 * Bush on right
* [ ] Viridian Forest
 * Maze, trainers, and encounters randomised
* [ ] Pewter City / Brock's challenge
 * Cannot proceed until after Gym
* [ ] Route 3
 * Lots of trainers
* [ ] Mt. Moon
 * Another maze, fossils
* [ ] Route 4
 * Can jump to from Cave
* [ ] Cerulean City
 * Nugget Bridge / Route 24
 * Surf West to Cave
* Route 25

Etc.

#### To Do
* [ ] Create Pokédex variable (explained later in Elements -> Pokémon Data)
* [ ] Find _Pokémon Red_ offset list
* [ ] Find _Pokémon Red_ Event Flags list (PKHeX?)
* [ ] Create battle systems
* [ ] Saving
* [ ] Pokemon Centers and Linking
* [ ] HM system

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

There will also need to be a list of moves learned when levelling up, but I'm not sure how to implement that.

#### Menus
As far as I know, Python cannot support Pokémon Red’s menu layouts, so some changes will be needed:

Using a rough example from LGPE (***non-spoiler***), this:

> Are you a boy or a girl?
>  
> Boy  
> Girl

Would become this:

> Are you a boy or a girl?
> 
> 1. Boy
> 2. Girl
> 
> _

However, this requires a bit of extra work. If the answer is invalid, the question must be asked again. Maybe like this:

```
...
//variables
...
playerGender = ‘’ #var must already exist
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

Of course, the custom _invalid_ message can change depending on the situation.

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

###### For reading this far, you get the privelege of seeing this li'l guy who, sadly, won't be in the game (maybe!):
![](https://tse2.mm.bing.net/th/id/OIP.odJ_-1cegyviucDJCNG_XAAAAA?w=136&h=180&c=7&o=5&dpr=1.5&pid=1.7)
