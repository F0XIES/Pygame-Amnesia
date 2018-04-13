

from gamelib import*
game = Game(640,480,"flabby bird")#create variable for the game object
bk = Image("day.png",game)#created a variable for an image object
bird = Animation("bird.png",3,game,44,34,frate)
while not game.over:#while the game is running

    game.processInput()
    bk.draw()



    game.update(60)

game.quit()
