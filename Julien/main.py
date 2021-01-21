from VirtuaVelo import virtuavelo

g = virtuavelo()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()