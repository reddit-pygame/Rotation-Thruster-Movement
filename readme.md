# Rotation Thruster Movement   
This is a challenge designed for [/r/pygame](https://www.reddit.com/r/pygame/)  
[Link to challenge thread.](https://www.reddit.com/r/pygame/comments/3fe60j/challenge_thruster_style_movement/)

This challenge uses a new base code from the previous, though the overall structure is very similar.  If you have any questions regarding functionality don't hesitate to ask.

## Challenge:  
The initial base code gives us a spaceship on a starfield.  Currently the player moves with the arrow keys and the ship travels in the direction pressed (standard 8-directional movement).  This is a little bit boring.  For this challenge we will implement thruster style movement.

##### Primary goals:  
* Make the game framerate independent using delta-time.  This will require using the return value of the call to `App.clock.tick` and passing this information to various update functions as needed.
* Change to thruster style movement.  The up-arrow should always make the ship travel forward (with respect to itself), and the left and right arrows should rotate the ship.
* Implement acceleration for a more spacey feel.  Instead of the up-key instantly making the sprite travel at its static speed, make it accelerate the sprite up to a certain top speed.  The player should continue to move even when the up key is released.

##### Extra mile goals:  
If the above is too simple, really the sky is the limit.  Things to consider are screen wrapping; particles for the ship engines; and of course weaponry, lifebars, asteroids, and enemies if you have the ambition.  Take it as far as you want and share your results.


### Base code:  
Running `main.py` will start the program.  The player is updated and drawn by a `level.Level` instance.


### Suggestions:    
You can find an example of updating with delta-time in Pygame here:  
https://github.com/Mekire/pygame-delta-time/blob/master/dt_example.py  
Also, if you have never read them, I highly recommend these articles (not Python):
http://gafferongames.com/game-physics/fix-your-timestep/  
http://gameprogrammingpatterns.com/game-loop.html  
For rotation, making sure the center of the rotating sprite doesn't move is important.  Any time you rotate an image, the bounding rectangle size changes.  You will need to set the new rectangles center to the position of the previous rectangles center.  Moving in the direction of a specific angle will require some rudimentary (but essential) trigonometry.  Also, remember that pygame rects can not hold floats; this may be important.


### Notes:    
As always, feel free to ignore as much of my code as you like and implement everything yourself if you so desire.

