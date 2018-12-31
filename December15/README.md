# Beverage Bandits

Having perfected their hot chocolate, the Elves have a new problem: the 
[Goblins](https://en.wikipedia.org/wiki/Goblin) that live in these caves will do anything to steal 
it. Looks like they're here for a fight.

You scan the area, generating a map of the walls (`#`), open cavern (`.`), and starting position of 
every Goblin (`G`) and Elf (`E`) (your puzzle input).

Combat proceeds in __rounds;__ in each round, each unit that is still alive takes a __turn,__ 
resolving all of its actions before the next unit's turn begins. On each unit's turn, it tries to 
__move__ into range of an enemy (if it isn't already) and then __attack__ (if it is in range).

All units are very disciplined and always follow very strict combat rules. Units never move or 
attack diagonally, as doing so would be dishonorable. When multiple choices are equally valid, ties 
are broken in __reading order:__ top-to-bottom, then left-to-right. For instance, the order in 
which units take their turns within a round is the __reading order of their starting positions__ in 
that round, regardless of the type of unit or whether other units have moved after the round 
started. For example:

```
                 would take their
These units:   turns in this order:
  #######           #######
  #.G.E.#           #.1.2.#
  #E.G.E#           #3.4.5#
  #.G.E.#           #.6.7.#
  #######           #######
```

Each unit begins its turn by identifying all possible __targets__ (enemy units). If no targets 
remain, combat ends.

Then, the unit identifies all of the open squares (`.`) that are __in range__ of each target; these 
are the squares which are __adjacent__ (immediately up, down, left, or right) to any target and 
which aren't already occupied by a wall or another unit. Alternatively, the unit might __already__ 
be in range of a target. If the unit is not already in range of a target, and there are no open 
squares which are in range of a target, the unit ends its turn.

If the unit is already in range of a target, it does not __move__, but continues its turn with an 
__attack.__ Otherwise, since it is not in range of a target, it __moves.__

To __move,__ the unit first considers the squares that are __in range__ and determines __which of 
those squares it could reach in the fewest steps.__ A __step__ is a single movement to any 
__adjacent__ (immediately up, down, left, or right) open (`.`) square. Units cannot move into walls 
or other units. The unit does this while considering the __current positions of units__ and does 
not do any prediction about where units will be later. If the unit cannot reach (find an open path 
to) any of the squares that are in range, it ends its turn. If multiple squares are in range and 
__tied__ for being reachable in the fewest steps, the square which is first in __reading order__ is 
chosen. For example:

```
Targets:      In range:     Reachable:    Nearest:      Chosen:
#######       #######       #######       #######       #######
#E..G.#       #E.?G?#       #E.@G.#       #E.!G.#       #E.+G.#
#...#.#  -->  #.?.#?#  -->  #.@.#.#  -->  #.!.#.#  -->  #...#.#
#.G.#G#       #?G?#G#       #@G@#G#       #!G.#G#       #.G.#G#
#######       #######       #######       #######       #######
```

In the above scenario, the Elf has three targets (the three Goblins):

 - Each of the Goblins has open, adjacent squares which are __in range__ (marked with a `?` on the 
 map).
 - Of those squares, four are __reachable__ (marked `@`); the other two (on the right) would 
 require moving through a wall or unit to reach.
 - Three of these reachable squares are __nearest,__ requiring the fewest steps (only `2`) to reach 
 (marked `!`).
 - Of those, the square which is first in reading order is __chosen__ (`+`).

The unit then takes a single __step__ toward the chosen square along the __shortest path__ to that 
square. If multiple steps would put the unit equally closer to its destination, the unit chooses 
the step which is first in reading order. (This requires knowing when there is __more than one 
shortest path__ so that you can consider the first step of each such path.) For example:

```
In range:     Nearest:      Chosen:       Distance:     Step:

#######       #######       #######       #######       #######
#.E...#       #.E...#       #.E...#       #4E212#       #..E..#
#...?.#  -->  #...!.#  -->  #...+.#  -->  #32101#  -->  #.....#
#..?G?#       #..!G.#       #...G.#       #432G2#       #...G.#
#######       #######       #######       #######       #######
```

The Elf sees three squares in range of a target (`?`), two of which are nearest (`!`), and so the 
first in reading order is chosen (`+`). Under "Distance", each open square is marked with its 
distance from the destination square; the two squares to which the Elf could move on this turn 
(down and to the right) are both equally good moves and would leave the Elf `2` steps from being 
in range of the Goblin. Because the step which is first in reading order is chosen, the Elf moves 
__right__ one square.

Here's a larger example of movement:

```
Initially:
#########
#G..G..G#
#.......#
#.......#
#G..E..G#
#.......#
#.......#
#G..G..G#
#########

After 1 round:
#########
#.G...G.#
#...G...#
#...E..G#
#.G.....#
#.......#
#G..G..G#
#.......#
#########

After 2 rounds:
#########
#..G.G..#
#...G...#
#.G.E.G.#
#.......#
#G..G..G#
#.......#
#.......#
#########

After 3 rounds:
#########
#.......#
#..GGG..#
#..GEG..#
#G..G...#
#......G#
#.......#
#.......#
#########
```

Once the Goblins and Elf reach the positions above, they all are either in range of a target or 
cannot find any square in range of a target, and so none of the units can move until a unit dies.

After moving (or if the unit began its turn in range of a target), the unit __attacks.__

To __attack,__ the unit first determines __all__ of the targets that are __in range__ of it by 
being immediately __adjacent__ to it. If there are no such targets, the unit ends its turn. 
Otherwise, the adjacent target with the __fewest hit points__ is selected; in a tie, the adjacent 
target with the fewest hit points which is first in reading order is selected.

The unit deals damage equal to its __attack power__ to the selected target, reducing its hit points 
by that amount. If this reduces its hit points to `0` or fewer, the selected target __dies:__ its 
square becomes `.` and it takes no further turns.

Each __unit__, either Goblin or Elf, has `3` __attack power__ and starts with `200` __hit points.__

For example, suppose the only Elf is about to attack:

<pre>
       HP:            HP:
G....  9       G....  9  
..G..  4       ..G..  4  
..E<b>G</b>.  2  -->  ..E..     
..G..  2       ..G..  2  
...G.  1       ...G.  1  
</pre>

The "HP" column shows the hit points of the Goblin to the left in the corresponding row. The Elf is 
in range of three targets: the Goblin above it (with `4` hit points), the Goblin to its right (with 
`2` hit points), and the Goblin below it (also with `2` hit points). Because three targets are in 
range, the ones with the lowest hit points are selected: the two Goblins with `2` hit points each 
(one to the right of the Elf and one below the Elf). Of those, the Goblin first in reading order 
(the one to the right of the Elf) is selected. The selected Goblin's hit points (`2`) are reduced 
by the Elf's attack power (`3`), reducing its hit points to `-1`, killing it.

After attacking, the unit's turn ends. Regardless of how the unit's turn ends, the next unit in the 
round takes its turn. If all units have taken turns in this round, the round ends, and a new round 
begins.

The Elves look quite outnumbered. You need to determine the __outcome__ of the battle: the __number 
of full rounds that were completed__ (not counting the round in which combat ends) multiplied by 
__the sum of the hit points of all remaining units__ at the moment combat ends. (Combat only ends 
when a unit finds no targets during its turn.)

Below is an entire sample combat. Next to each map, each row's units' hit points are listed from 
left to right.

```
Initially:
#######   
#.G...#   G(200)
#...EG#   E(200), G(200)
#.#.#G#   G(200)
#..G#E#   G(200), E(200)
#.....#   
#######   

After 1 round:
#######   
#..G..#   G(200)
#...EG#   E(197), G(197)
#.#G#G#   G(200), G(197)
#...#E#   E(197)
#.....#   
#######   

After 2 rounds:
#######   
#...G.#   G(200)
#..GEG#   G(200), E(188), G(194)
#.#.#G#   G(194)
#...#E#   E(194)
#.....#   
#######   

Combat ensues; eventually, the top Elf dies:

After 23 rounds:
#######   
#...G.#   G(200)
#..G.G#   G(200), G(131)
#.#.#G#   G(131)
#...#E#   E(131)
#.....#   
#######   

After 24 rounds:
#######   
#..G..#   G(200)
#...G.#   G(131)
#.#G#G#   G(200), G(128)
#...#E#   E(128)
#.....#   
#######   

After 25 rounds:
#######   
#.G...#   G(200)
#..G..#   G(131)
#.#.#G#   G(125)
#..G#E#   G(200), E(125)
#.....#   
#######   

After 26 rounds:
#######   
#G....#   G(200)
#.G...#   G(131)
#.#.#G#   G(122)
#...#E#   E(122)
#..G..#   G(200)
#######   

After 27 rounds:
#######   
#G....#   G(200)
#.G...#   G(131)
#.#.#G#   G(119)
#...#E#   E(119)
#...G.#   G(200)
#######   

After 28 rounds:
#######   
#G....#   G(200)
#.G...#   G(131)
#.#.#G#   G(116)
#...#E#   E(113)
#....G#   G(200)
#######   

More combat ensues; eventually, the bottom Elf dies:

After 47 rounds:
#######   
#G....#   G(200)
#.G...#   G(131)
#.#.#G#   G(59)
#...#.#   
#....G#   G(200)
#######
```
   
Before the 48th round can finish, the top-left Goblin finds that there are no targets remaining, 
and so combat ends. So, the number of __full rounds__ that were completed is __`47`__, and the sum 
of the hit points of all remaining units is `200+131+59+200 =`**`590`**. From these, the 
__outcome__ of the battle is `47 * 590 =`**`27730`**.

Here are a few example summarized combats:

<pre>
#######       #######
#G..#E#       #...#E#   E(200)
#E#E.E#       #E#...#   E(197)
#G.##.#  -->  #.E##.#   E(185)
#...#E#       #E..#E#   E(200), E(200)
#...E.#       #.....#
#######       #######

Combat ends after 37 full rounds
Elves win with 982 total hit points left
Outcome: 37 * 982 = <b>36334</b>
</pre>
<pre>
#######       #######   
#E..EG#       #.E.E.#   E(164), E(197)
#.#G.E#       #.#E..#   E(200)
#E.##E#  -->  #E.##.#   E(98)
#G..#.#       #.E.#.#   E(200)
#..E#.#       #...#.#   
#######       #######   

Combat ends after 46 full rounds
Elves win with 859 total hit points left
Outcome: 46 * 859 = <b>39514</b>
</pre>
<pre>
#######       #######   
#E.G#.#       #G.G#.#   G(200), G(98)
#.#G..#       #.#G..#   G(200)
#G.#.G#  -->  #..#..#   
#G..#.#       #...#G#   G(95)
#...E.#       #...G.#   G(200)
#######       #######   

Combat ends after 35 full rounds
Goblins win with 793 total hit points left
Outcome: 35 * 793 = <b>27755</b>
</pre>
<pre>
#######       #######   
#.E...#       #.....#   
#.#..G#       #.#G..#   G(200)
#.###.#  -->  #.###.#   
#E#G#G#       #.#.#.#   
#...#G#       #G.G#G#   G(98), G(38), G(200)
#######       #######   

Combat ends after 54 full rounds
Goblins win with 536 total hit points left
Outcome: 54 * 536 = <b>28944</b>
</pre>
<pre>
#########       #########   
#G......#       #.G.....#   G(137)
#.E.#...#       #G.G#...#   G(200), G(200)
#..##..G#       #.G##...#   G(200)
#...##..#  -->  #...##..#   
#...#...#       #.G.#...#   G(200)
#.G...G.#       #.......#   
#.....G.#       #.......#   
#########       #########   

Combat ends after 20 full rounds
Goblins win with 937 total hit points left
Outcome: 20 * 937 = <b>18740</b>
</pre>

__What is the outcome of the combat__ described in your puzzle input?

Your puzzle answer was `213692`.

## Part Two 

According to your calculations, the Elves are going to lose badly. Surely, you won't mess up the 
timeline too much if you give them just a little advanced technology, right?

You need to make sure the Elves not only __win__, but also suffer __no losses:__ even the death of 
a single Elf is unacceptable.

However, you can't go too far: larger changes will be more likely to permanently alter spacetime.

So, you need to __find the outcome__ of the battle in which the Elves have the __lowest integer 
attack power__ (at least `4`) that allows them to __win without a single death.__ The Goblins 
always have an attack power of `3`.

In the first summarized example above, the lowest attack power the Elves need to win without losses 
is `15`:

<pre>
#######       #######
#.G...#       #..E..#   E(158)
#...EG#       #...E.#   E(14)
#.#.#G#  -->  #.#.#.#
#..G#E#       #...#.#
#.....#       #.....#
#######       #######

Combat ends after 29 full rounds
Elves win with 172 total hit points left
Outcome: 29 * 172 = <b>4988</b>
</pre>

In the second example above, the Elves need only `4` attack power:

<pre>
#######       #######
#E..EG#       #.E.E.#   E(200), E(23)
#.#G.E#       #.#E..#   E(200)
#E.##E#  -->  #E.##E#   E(125), E(200)
#G..#.#       #.E.#.#   E(200)
#..E#.#       #...#.#
#######       #######

Combat ends after 33 full rounds
Elves win with 948 total hit points left
Outcome: 33 * 948 = <b>31284</b>
</pre>

In the third example above, the Elves need `15` attack power:

<pre>
#######       #######
#E.G#.#       #.E.#.#   E(8)
#.#G..#       #.#E..#   E(86)
#G.#.G#  -->  #..#..#
#G..#.#       #...#.#
#...E.#       #.....#
#######       #######

Combat ends after 37 full rounds
Elves win with 94 total hit points left
Outcome: 37 * 94 = <b>3478</b>
</pre>

In the fourth example above, the Elves need `12` attack power:

<pre>
#######       #######
#.E...#       #...E.#   E(14)
#.#..G#       #.#..E#   E(152)
#.###.#  -->  #.###.#
#E#G#G#       #.#.#.#
#...#G#       #...#.#
#######       #######

Combat ends after 39 full rounds
Elves win with 166 total hit points left
Outcome: 39 * 166 = <b>6474</b>
</pre>

In the last example above, the lone Elf needs `34` attack power:

<pre>
#########       #########   
#G......#       #.......#   
#.E.#...#       #.E.#...#   E(38)
#..##..G#       #..##...#   
#...##..#  -->  #...##..#   
#...#...#       #...#...#   
#.G...G.#       #.......#   
#.....G.#       #.......#   
#########       #########   

Combat ends after 30 full rounds
Elves win with 38 total hit points left
Outcome: 30 * 38 = <b>1140</b>
</pre>

After increasing the Elves' attack power until it is just barely enough for them to win without any 
Elves dying, __what is the outcome__ of the combat described in your puzzle input?

Your puzzle answer was `52688`.

__Both parts of this puzzle are complete! They provide two gold stars: \*\*__