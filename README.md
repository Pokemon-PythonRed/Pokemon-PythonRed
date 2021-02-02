## Pokémon PythonRed

### Important Notes:

* This is not meant to be a perfect recreation of _Pokémon Red_. It’s just a test of my own coding skills. So basically, if you’re looking to play _Pokémon Red_ on PC, you can find an emulator.
* Throughout this process, I will only be able to refer to online resources. This is because I want to limit myself to specific conditions that I can’t fully explain. One of these conditions is I can’t access the official game.
* This is my first GitHub project, and I’m not very acquainted to its features and capabilities.
* I've only recently learnt Markdown, specifically for this project.

Summary: **_Don’t Judge_!**

### To Play:

First, you need to have `Python` installed, obviously. If this isn't already done, you can find the insaller [here](https://sdassq-my.sharepoint.com/:u:/g/personal/ba004629_bac_qld_edu_au/ESCL5J4RZcFLrzRbpcnyy6EBjn22m7ZuFJQMH7HiIW0XFw?e=cFyr1g) (v3.6.8). Make sure to tick the box that says `Add Python to PATH` during installation.

This will also install `pip` which is required in the next step.

Next, you need to open Command Prompt (or another Command Line) and _individually_ run the following commands to install dependencies:

`pip install pillow`

`pip install playsound`

`pip install pygame`

When that's all done, to download the game, please see [Releases](https://github.com/TurnipGuy30/Pokemon-PythonRed/releases)!

For contributions and feature requests, please see [Issues](https://github.com/TurnipGuy30/Pokemon-PythonRed/issues)!

## SPOILERS PAST THE POKÉ BALL!
![](https://tse2.mm.bing.net/th/id/OIP.VHV4L97MJfgNd5DMRep1oQHaHZ?w=201&h=200&c=7&o=5&dpr=1.5&pid=1.7)

### Progress:

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

### Pokémon Data
The entire Kanto Pokédex will be stored as a variable, with a list item for each species:

```
Pokemon = [[],[],[]...]
```

Each `[]` includes this:

```
[Pokédex #, Name, Type 1, Type 2, Base HP, Base ATK, Base DEF, Base SP. ATK, Base SP. DEF, Base SPD, Catch Rate]
```

#### _That's all, watch this space, and thanks!_

###### For reading this far, you get the privelege of seeing this li'l guy who just _might_ be in the game:
![](https://tse2.mm.bing.net/th/id/OIP.odJ_-1cegyviucDJCNG_XAAAAA?w=136&h=180&c=7&o=5&dpr=1.5&pid=1.7)
