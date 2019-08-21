import pyglet
import random

sounds = [pyglet.resource.media(
    'sounds/Dtmf' + str(i) + '.wav', streaming=False)
    for i in range(10)]


while True:
    i = random.choice(range(10))
    sound = sounds[i]
    sound.play()
    guess = input('Noise: ')
    if guess == str(i):
        print('correct')
    else:
        print('wrong, answer: ' + str(i))
