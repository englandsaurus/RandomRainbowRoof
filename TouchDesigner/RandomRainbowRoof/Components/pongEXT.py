import threading
import time

class Pong:
	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
		self.bullet = ownerComp.op('bsolver1')
		self.start_trigger = ownerComp.op('start_sim')
		self.ball = ownerComp.op('ball')
		self.winner = ownerComp.op('win_animation/winner')
		self.win_trigger = ownerComp.op('win_animation/win_trigger')
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
		print(Channel.index)
		self.winner.par.const0value = Channel.index
		self.win_trigger.par.trigger.pulse()
		self.bullet.par.initall.pulse()
		pass
