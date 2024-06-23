# Install an external module and use it to perform an operation of your interest

# pip install pyttsx3

import pyttsx3

engine = pyttsx3.init()
engine.say("""Twinkle, twinkle, little star,
How I wonder what you are.
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often through my curtains peep,
For you never shut your eye,
‘Till the sun is in the sky.

As your bright and tiny spark,
Lights the traveller in the dark,–
Though I know not what you are,
Twinkle, twinkle, little star.""")
engine.runAndWait()