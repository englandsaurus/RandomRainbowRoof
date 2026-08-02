import threading
import time

class Pong:
	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
		self.bullet = ownerComp.op('bsolver1')
		self.start_trigger = ownerComp.op('start_sim')
		self.ball = ownerComp.op('ball')
		self.winner = ownerComp.op('Win_animation/winner')
		print(f'{__class__.__name__} class initialized from {self.ownerComp.name}.')
		pass
	
	def Score_point(self, Channel):
		if Channel.index == 1:
			self.ball.par.linvelx = -10
		else:
			self.ball.par.linvelx = 10
		self.bullet.par.initall.pulse()
		self.start_trigger.par.trigger.pulse()
		pass
	
	def Win_game(self, Channel):
		self.winner[0].val = Channel
