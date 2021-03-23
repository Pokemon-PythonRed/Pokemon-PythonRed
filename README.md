## Pokémon PythonRed

### Important Notes:

* This is _not_ a perfect recreation of Pokémon Red; it's a custom story that takes place in the fictional Kanto region.

### To Play:

First, ensure you have `Python` installed. If not, you can find the latest installer [here](https://www.python.org/downloads/ "Python Latest"). Tick the box that says `Add Python to PATH` during installation.

However, if you are using a work/school computer and are not an administrator, you don't need to tick `py launcher`, which requires Administrator priveledges to install. This is because Python IDLE (what you're installing) is the same thing anyway.

This also installs `pip` which is required in the next step.

Open Command Prompt and _individually_ run any any below commands to install dependencies:

`pip install playsound`

When that's all done, to download the game, please download the latest (top) [Release](https://github.com/TurnipGuy30/Pokemon-PythonRed/releases)!

For contributions and feature requests, please create an [Issue](https://github.com/TurnipGuy30/Pokemon-PythonRed/issues)!

## SPOILERS PAST THE POKÉ BALL!
###### (scrolling past is not recommended if you have never played Pokémon Red)
![SPOILER ALERT!](https://tse2.mm.bing.net/th/id/OIP.VHV4L97MJfgNd5DMRep1oQHaHZ?w=201&h=200&c=7&o=5&dpr=1.5&pid=1.7)

<br><br><br><br>

### Progress:

![Kanto Region Map](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/3bddf750-53a0-4a9f-872f-8d13685a758f/d3c4hsg-5acbd78f-c4cb-4f40-a87a-05700ac859a4.png/v1/fill/w_900,h_882,q_75,strp/labeled_map_of_kanto_by_rythos-d3c4hsg.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwic3ViIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl0sIm9iaiI6W1t7InBhdGgiOiIvZi8zYmRkZjc1MC01M2EwLTRhOWYtODcyZi04ZDEzNjg1YTc1OGYvZDNjNGhzZy01YWNiZDc4Zi1jNGNiLTRmNDAtYTg3YS0wNTcwMGFjODU5YTQucG5nIiwid2lkdGgiOiI8PTkwMCIsImhlaWdodCI6Ijw9ODgyIn1dXX0.Ycjt66m7t9k-8tio4Tsc0YTsP_nu7Lz2cGBm4CdZWN8 "Kanto Region Map")

<br>

![HP Calulation Formula](HP_calc.webp "HP Formula")
![Stat Calculation Formula](Statcalc_gen12.png "Stat Formula")

* [x] Start menu
 * Pokemon logo
* [x] Intro
 * Nidorino picture
 * Choose name
* [x] Pallet Town
 * Select starter
* [x] Route 1
 * No encounters coming back
* [x] Viridian City
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

### Pokémon Data
The entire Kanto Pokédex will be stored as a variable, with a list item for each species:

```
pokemon = [[],[],[]...]
```

Each `[]` includes this:

```
[Pokédex #, Name, Type, Total Stats, Base HP, Base ATK, Base DEF, Base SP. ATK, Base SP. DEF, Base SPD]
```
Catch Rate will be based on Total Stats.

For simplicity, Pokémon will only have one type each, and one attack each (a _type_-type attack)

#### _That's all, watch this space, and thanks!_

###### For reading this far, you get the privelege of seeing this li'l guy who just _might_ be a starter:
![](https://tse2.mm.bing.net/th/id/OIP.odJ_-1cegyviucDJCNG_XAAAAA?w=136&h=180&c=7&o=5&dpr=1.5&pid=1.7 "Mah Boi Mudkip")
