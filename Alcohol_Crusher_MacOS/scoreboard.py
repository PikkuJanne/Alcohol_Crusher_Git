import pygame.font

class Scoreboard:
    """Class to report scoring info."""

    def __init__(self, ac_game):
        """Initialize scorekeeping attributes."""
        self.ac_game = ac_game
        self.screen = ac_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ac_game.settings
        self.stats = ac_game.stats

        #Font settings for scoring info.
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont('helvetica', 48)

        #Prepare initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Turn score into rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #Display score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -15
        self.score_rect.top = 15

    def prep_high_score(self):
        """Turn High Score into rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        #Center high score at top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_lives(self):
        """Draw the remaining fists on the screen."""
        image_width = self.ac_game.fist.small_image.get_rect().width
        for i in range(self.stats.fists_left):
            x_position = 10 + i * (image_width + 10)  # 10px margin from the left and between fists
            y_position = 10  # 10px margin from the top
            self.screen.blit(self.ac_game.fist.small_image, (x_position, y_position))

    def show_score(self):
        """Draw scores and level to screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.show_lives() 

    def check_high_score(self):
        """Check to see if theres a new High Score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Turn level into rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        #Position level below score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 5



        
