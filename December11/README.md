# Chronal Charge
You watch the Elves and their sleigh fade into the distance as they head toward the North Pole.

Actually, you're the one fading. The falling sensation returns.

The low fuel warning light is illuminated on your wrist-mounted device. Tapping it once causes it 
to project a hologram of the situation: a __300x300__ grid of fuel cells and their current power 
levels, some negative. You're not sure what negative power means in the context of time travel, 
but it can't be good.

Each fuel cell has a coordinate ranging from __1 to 300__ in both the X (horizontal) and Y (vertical) 
direction. In `X,Y` notation, the top-left cell is `1,1`, and the top-right cell is `300,1`.

The interface lets you select any __3x3 square__ of fuel cells. To increase your chances of getting 
to your destination, you decide to choose the 3x3 square with the __largest total power.__

The power level in a given fuel cell can be found through the following process:

 - Find the fuel cell's __rack ID,__ which is its __X coordinate plus 10.__
 - Begin with a power level of the __rack ID__ times the __Y coordinate.__
 - Increase the power level by the value of the __grid serial number__ (your puzzle input).
 - Set the power level to itself multiplied by the __rack ID.__
 - Keep only the __hundreds digit__ of the power level (so `12`**`3`**`45` becomes `3`; numbers with no hundreds digit become 
 `0`).
 - __Subtract 5__ from the power level.
 
For example, to find the power level of the fuel cell at `3,5` in a grid with serial number `8`:

 - The rack ID is `3 + 10 =`**`13`**.
 - The power level starts at `13 * 5 =`**`65`**.
 - Adding the serial number produces `65 + 8 =`**`73`**.
 - Multiplying by the rack ID produces `73 * 13 =`**`949`**.
 - The hundreds digit of `949` is **`9`**.
 - Subtracting 5 produces `9 - 5 =`**`4`**.

So, the power level of this fuel cell is **`4`**.

Here are some more example power levels:

 - Fuel cell at  `122,79`, grid serial number `57`: power level `-5`.
 - Fuel cell at `217,196`, grid serial number `39`: power level  `0`.
 - Fuel cell at `101,153`, grid serial number `71`: power level  `4`.

Your goal is to find the 3x3 square which has the largest total power. The square must be entirely 
within the 300x300 grid. Identify this square using the `X,Y` coordinate of its 
__top-left fuel cell.__ For example:

For grid serial number `18`, the largest total 3x3 square has a top-left corner of **`33,45`** (with 
a total power of `29`); these fuel cells appear in the middle of this 5x5 region:

<pre>
-2  -4   4   4   4
-4   <b>4   4   4</b>  -5
 4   <b>3   3   4</b>  -4
 1   <b>1   2   4</b>  -3
-1   0   2  -5  -2
</pre>

For grid serial number `42`, the largest 3x3 square's top-left is **`21,61`** (with a total power of 
`30`); they are in the middle of this region:

<pre>
-3   4   2   2   2
-4   <b>4   3   3</b>   4
-5   <b>3   3   4</b>  -4
 4   <b>3   3   4</b>  -3
 3   3   3  -5  -1
</pre>

__What is the `X,Y` coordinate of the top-left fuel cell of the 3x3 square with the largest total 
power?__

Your puzzle answer was `20,83`.

## Part Two 
You discover a dial on the side of the device; it seems to let you select a square of __any size,__ 
not just 3x3. Sizes from 1x1 to 300x300 are supported.

Realizing this, you now must find the __square of any size with the largest total power.__ Identify 
this square by including its size as a third parameter after the top-left coordinate: a 9x9 
square with a top-left corner of `3,5` is identified as `3,5,9`.

For example:

 - For grid serial number `18`, the largest total square (with a total power of `113`) is 16x16 and 
 has a top-left corner of `90,269`, so its identifier is __`90,269,16`__.
 - For grid serial number `42`, the largest total square (with a total power of `119`) is 12x12 and 
 has a top-left corner of `232,251`, so its identifier is __`232,251,12`__.

__What is the `X,Y,size` identifier of the square with the largest total power?__

Your puzzle answer was `237,281,10`.

__Both parts of this puzzle are complete! They provide two gold stars: \*\*__