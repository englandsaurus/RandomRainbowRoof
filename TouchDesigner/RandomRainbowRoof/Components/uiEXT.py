class UI:
	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
	
	def SwitchPage(self, current_page, next_page):
		current_page.par.display = 0
		next_page.allowCooking = True
		next_page.par.display = 1
		current_page.allowCooking = False