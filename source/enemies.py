#Enemies
import pygame
import game
from sprite import Sprite

#This makes enemies patrol back and forth 
# class Enemy:
# 	def __init__(self):
# 		self.sprite = Sprite("test.png", (500, 500))
# 		self.direction=False
# 	def draw(self):
# 		self.sprite.draw()
# 		if self.direction==False: 
# 			self.sprite.rect.x += 10
			
# 		else:
# 			self.sprite.rect.x -= 10

# 		if (self.sprite.rect.right>=1280 and self.direction==False) or (self.direction==True and self.sprite.rect.left<=0):
# 			self.direction=not self.direction
# 	def damage(self):
# 		if game.alvey.rect.colliderect(self.sprite.rect) == True:
# 			game.alvey.health -= 100







