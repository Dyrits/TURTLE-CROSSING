import time
from turtle import Screen
from player import Player
from garage import Garage
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True

player = Player()
garage = Garage()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

while game_is_on:
    time.sleep(0.1)
    garage.create_car()
    player.check_position()
    garage.move_cars()
    screen.update()

    for car in garage.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        garage.speed_up()
        scoreboard.update_scoreboard()


screen.exitonclick()
