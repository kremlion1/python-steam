import time


class GameEntity(object):

    def __init__(self, game, lowest_price, volume, median_price, name, url, img_url):
        self.game=game
        self.lowes_price-lowest_price
        self.volume=volume
        self.median_price=median_price
        self.name=name
        self.url=url
        self.img_url=img_url
        self.updated=time.time()

    def refresh(self):
        self.updated = time.time()


class GameCard(GameEntity):

    def __init__(self, html, game, foil):
        self.game = game
        self.foil = foil

    def refresh(self):
        if not self.foil:
            super.refresh()

    def foil_refresh(self):
        if self.foil:
            super.refresh()


class GamePack(GameCard):
    def __init__(self, game):
        self.foil = False
        self.game = game
        self.name = game.name + '%20Booster%20Pack'


class Emoticon(GameEntity):
    def __init__(self, type):
        self.type = type


class Background(GameEntity):
    def __init__(self, type):
        self.type = type

class Game(object):
    def __init__(self, name, id, profit, emoticons_gems, cards, emoticons, backgrounds, game_pack, favorite):
        self.name = name
        self.id = id
        self.profit = profit
        self.emoticons_gems = emoticons_gems
        self.cards = cards
        self.emoticons = emoticons
        self.backgrounds = backgrounds
        self.game_pack = game_pack
        self.favorite = favorite

    def refresh(self):
        for card in self.cards:
            card.refresh()

    def get_cards(self):
        self.cards = []