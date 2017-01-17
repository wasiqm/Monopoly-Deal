from graphics import *
from button import *
from settings import *
from ImageButton import *
from game import *
import webbrowser

class MenuInterface:
    def __init__(self, win):
        """The main menu for the game. Players will use the menu to view documentation,
        run the game, and choose teams.
        menu = MenuInterface(myWin)"""

        self.win = win
        self.settings = Settings("game_settings.txt")

        self.playerOne = ""
        self.playerOneGraphic = ""

        self.playerTwo = ""
        self.playerTwoGraphic = ""


    def run(self):
        """Runs the main menu. Draws all of the necessary images to the screen."""
        self.game_background = Image(Point(512, 325),"Images/temp_background.png")
        self.game_background.draw(self.win)

        self.game_title = Image(Point(512, 550), "Images/temp_logo.png")
        self.game_title.draw(self.win)

        self.game_version = Text(Point(980, 15), "version " + self.settings.access('game_version'))
        self.game_version.draw(self.win)

        self.game_developers = Text(Point(135, 15), "Developed by " + self.settings.access('game_developers'))
        self.game_developers.draw(self.win)

        self.play_button = ImageButton(self.win, Point(512, 400), "Images/button_img.png", "Start Game")
        self.play_button.setFontSize(18)
        self.play_button.activate()

        self.documentation_button = ImageButton(self.win, Point(512, 300), "Images/button_img.png", "Documentation")
        self.documentation_button.activate()

        self.quit_button = ImageButton(self.win, Point(512, 200), "Images/button_img.png", "Quit Game")
        self.quit_button.activate()

        pt = self.win.getMouse()

        while not self.quit_button.clicked(pt):
            if self.documentation_button.clicked(pt):
                webbrowser.open("http://ryan-coulson.com/daskapital/docs.html")
            elif self.play_button.clicked(pt):
                self.play_button.undraw()
                self.documentation_button.undraw()
                self.quit_button.undraw()


                self.playerCountry_CA = ImageButton(self.win, Point(378, 360), "Images/canada_circle.png","")
                self.playerCountry_CA.activate()

                self.playerCountry_US = ImageButton(self.win, Point(512, 360), "Images/america_circle.png","")
                self.playerCountry_US.activate()

                self.playerCountry_CH = ImageButton(self.win, Point(646, 360), "Images/china_circle.png","")
                self.playerCountry_CH.activate()

                self.playerCountry_UK = ImageButton(self.win, Point(378, 220), "Images/uk_circle.png","")
                self.playerCountry_UK.activate()

                self.playerCountry_RU = ImageButton(self.win, Point(512, 220), "Images/russia_circle.png","")
                self.playerCountry_RU.activate()

                self.playerCountry_EU = ImageButton(self.win, Point(646, 220), "Images/eu_circle.png","")
                self.playerCountry_EU.activate()

                for player in range(1,3):
                    self.subtitle = Text(Point(512, 470), "Player " + str(player) + ": Choose Country")
                    self.subtitle.setSize(24)
                    self.subtitle.setStyle("bold")
                    self.subtitle.draw(self.win)

                    while True:
                        pt = self.win.getMouse()

                        if self.playerCountry_US.clicked(pt):
                            if player == 1:
                                self.playerOne = "United States"
                                self.playerOneGraphic = "Images/iamerica_circle.png"
                            else:
                                self.playerTwo = "United States"
                                self.playerTwoGraphic = "Images/iamerica_circle.png"

                            self.playerCountry_US.hide_circle()
                            break

                        elif self.playerCountry_CH.clicked(pt):
                            if player == 1:
                                self.playerOne = "China"
                                self.playerOneGraphic = "Images/ichina_circle.png"
                            else:
                                self.playerTwo = "China"
                                self.playerTwoGraphic = "Images/ichina_circle.png"

                            self.playerCountry_CH.hide_circle()
                            break

                        elif self.playerCountry_RU.clicked(pt):
                            if player == 1:
                                self.playerOne = "Russia"
                                self.playerOneGraphic = "Images/irussia_circle.png"
                            else:
                                self.playerTwo = "Russia"
                                self.playerTwoGraphic = "Images/irussia_circle.png"

                            self.playerCountry_RU.hide_circle()
                            break

                        elif self.playerCountry_EU.clicked(pt):
                            if player == 1:
                                self.playerOne = "European Union"
                                self.playerOneGraphic = "Images/ieu_circle.png"
                            else:
                                self.playerTwo = "European Union"
                                self.playerTwoGraphic = "Images/ieu_circle.png"

                            self.playerCountry_EU.hide_circle()
                            break

                        elif self.playerCountry_CA.clicked(pt):
                            if player == 1:
                                self.playerOne = "Canada"
                                self.playerOneGraphic = "Images/icanada_circle.png"
                            else:
                                self.playerTwo = "Canada"
                                self.playerTwoGraphic = "Images/icanada_circle.png"
                            self.playerCountry_CA.hide_circle()
                            break

                        elif self.playerCountry_UK.clicked(pt):
                            if player == 1:
                                self.playerOne = "United Kingdom"
                                self.playerOneGraphic = "Images/iuk_circle.png"
                            else:
                                self.playerTwo = "United Kingdom"
                                self.playerTwoGraphic = "Images/iuk_circle.png"

                            self.playerCountry_UK.hide_circle()
                            break

                        elif self.quit_button.clicked(pt):
                            self.undraw()
                            self.run()

                    self.subtitle.undraw()

                    if player == 2:
                        self.undraw()
                        gui = GraphicsInterface(self.win)
                        gui.update_player_country(1, self.playerOne, self.playerOneGraphic)
                        gui.update_player_country(2, self.playerTwo, self.playerTwoGraphic)
                        gui.run()
                        break

                self.undraw()
                break
            pt = self.win.getMouse()

        self.win.close()

    def undraw(self):
        """Undraws all images from the screen."""
        self.game_developers.undraw()
        self.game_background.undraw()
        self.game_title.undraw()
        self.game_version.undraw()
        self.subtitle.undraw()
        self.playerCountry_US.undraw()
        self.playerCountry_CH.undraw()
        self.playerCountry_EU.undraw()
        self.playerCountry_RU.undraw()
        self.playerCountry_CA.undraw()
        self.playerCountry_UK.undraw()
        self.quit_button.undraw()

    def get_team(self, p):
        """Returns the teams that each player selected at the beginning of the
        game."""
        if p == 1:
            return self.playerOne
        elif p == 2:
            return self.playerTwo
        else:
            print("error")


if __name__ == "__main__":
    win = GraphWin("MenuInterface", 1024, 650)
    win.setCoords(0, 0, 1024, 650)

    menu = MenuInterface(win)
    menu.run()


