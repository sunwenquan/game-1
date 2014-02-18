import game
import pygame
import sys
import os
from sprite import Sprite


class TileType:

    """
    This is different from Tile!  This class only has tile types.
    """

    def __init__(self):
        self.tiles = {
            'b': ("testblock-tile.gif", "block"),
            'c': ("testclimb-tile.gif", "climb"),
            'e': ("testenemy-tile.gif", "enemy"),
            't': ("testtrap-tile.gif", "trap"),
            'x': ("testdeath-tile.gif", "death"),
            'r': ("testride-tile.gif", "ride"),
            'p': ("testpowerup-tile.gif", "powerup"),
            'f': ("finished-tile.png", "finished")
        }

    def __getitem__(self, key):
        """
        Don't mind this.  It is simply a way to easily access tiles
        """
        return self.tiles[key]

    def __setitem__(self, key, value):
        """
        Don't mind this.  It is simply a way to easily access tiles
        """
        self.tiles[key] = value


class Tile:

    """
    Represents a singular tile entity
    """

    def __init__(self, tiletype, position):
        self.tile_type = tiletype
        self.position = position
        self.sprite = Sprite(TileType()[tiletype][0], self.position)

    def draw(self):
        self.sprite.draw()


class Map:

    """
    Defines a singular world map
    """

    def __init__(self):
        self.tiles = []
        self.camera_offset = 0
        self.finished = False
        self.scrolling = True

    def draw(self):
        for tile in self.tiles:
            tile.draw()

    def update(self):
        if self.scrolling:
            for tile in self.tiles:
                tile.sprite.rect.x -= 1

    def collides_player(self):
        print "collides_player()"
        for tile in self.tiles:
            tiletop = tile.sprite.rect.copy()
            tileleft = tile.sprite.rect.copy()
            tileright = tile.sprite.rect.copy()
            tilebottom = tile.sprite.rect.copy()
            tiletop.height = 5
            tiletop.width = 22
            tiletop.left += 5
            tileleft.width = 5
            tileleft.height = 22
            tileleft.bottom += 5
            tilebottom.height = 5
            tilebottom.bottom += 27
            tilebottom.width = 20
            tilebottom.left += 6
            tileright.width = 5
            tileright.left += 27
            tileright.height = 22
            tileright.bottom += 5
            alveytile = game.alvey.rect.copy()
            alveytile.height = 25
            alveytile.bottom += 7
            if alveytile.colliderect(tileleft):
                print "LEFTHIT"
                game.alvey.speed = 0
                
                game.alvey.rect.right = tile.sprite.rect.left-1
                if tile.tile_type == 'f':
                    if not self.finished:
                        self.finished = True
                        print("Level complete")
                
            if alveytile.colliderect(tileright):
                print " RIGHTHIT"
                game.alvey.speed = 0
                game.alvey.rect.left = tile.sprite.rect.right+1
                if tile.tile_type == 'f':
                    if not self.finished:
                        self.finished = True
                        print("Level complete")
                
            if game.alvey.rect.colliderect(tilebottom):
                print "BOTTOMHIT"
                game.alvey.speed = 0
                game.alvey.rect.top = tile.sprite.rect.bottom+1
                if tile.tile_type == 'f':
                    if not self.finished:
                        self.finished = True
                        print("Level complete")

            if alveytile.colliderect(tiletop):
                print "TOPHIT"
                #game.alvey.speed = game.alvey.maxspeed/2
                game.alvey.velocity = 0
                game.alvey.rect.bottom = tile.sprite.rect.top+1
                if tile.tile_type == 'f':
                    if not self.finished:
                        self.finished = True
                        print("Level complete")
                return True
            
        return False

    def add(self, tile):
        self.tiles.append(tile)


class MapLoader:

    @staticmethod
    def tile_offset(axis):
        """
        Returns an offset from tile position to real position (eg: * 32)
        """

        return (axis * 32)

    @staticmethod
    def load(filename):
        """
        Loads a map from a given .map file and returns a Map object
        """

        filename = game.rpath + "map/" + filename
        lines = []
        retmap = Map()

        with open(filename) as f:
            for tile_y, line in enumerate(f):
                for tile_x, tile in enumerate(line):
                    if not tile == '.' and not tile == '\n':
                        mT = Tile(tile,
                                 (MapLoader.tile_offset(tile_x),
                                  MapLoader.tile_offset(tile_y)))
                        retmap.add(mT)

        return retmap
