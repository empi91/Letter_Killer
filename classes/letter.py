class Letter:
    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos

    def add_to_list(self, letter_list):
        letter_list.append(self)

    def display(self, font, screen):
        letter_text = font.render(self.name, False, "white")
        if self.x_pos <= screen.get_width() / 2:
            letter_rect = letter_text.get_rect(topleft=(int(self.x_pos), int(self.y_pos)))
        else:
            letter_rect = letter_text.get_rect(topright=(int(self.x_pos), int(self.y_pos)))

        screen.blit(letter_text, letter_rect)

    def move(self, level):
        self.y_pos += level





