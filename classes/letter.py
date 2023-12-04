class Letter:
    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos

    def add_to_list(self, letter_list):
        letter_list.append(self)

    def display(self, font, screen):
        letter_text = font.render(self.name, False, "white")
        letter_rect = letter_text.get_rect(midbottom=(int(self.x_pos), int(self.y_pos)))
        screen.blit(letter_text, letter_rect)

    def move(self, position):
        self.y_pos += position





