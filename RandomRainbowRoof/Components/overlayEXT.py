from random import randint
import traceback
import sys
import os
from datetime import datetime

class Overlays:
    def __init__(self, ownerComp):
        self.ownerComp 	= ownerComp
        self.timer      = op('transition_timer')
        self.overlayList = op('list_of_overlays')
        self.source 	= ownerComp.op('source')
        self.source_null 	= ownerComp.op('source_null')
        self.next_source    = ownerComp.op('next_source') 
        self.next_source_null= ownerComp.op('next_source_null')
        self.path = project.folder + "/Overlays"
        if os.path.exists(self.path):
            print("Overlays folder exists: " + self.path)
        else:
            print("Creating Overlays folder: " + self.path)
            os.mkdir(self.path)
        
        self.overlayList.par.rootfolder = self.path
        self.Load_tox(self.source, "heatnoise")
        self.Load_tox(self.next_source, "heatnoise")
        self.connect_operators()
        self.Setup_menu()
        print(f'{datetime.now()}: {__class__.__name__} class initialized from {self.ownerComp.name}.')
        pass 

    def Setup_menu(self):
        try:
            overlays_menu = [cell.val for cell in self.overlayList.col("name")[1:]]
            self.ownerComp.par.Setoverlay.menuLabels = overlays_menu
            self.ownerComp.par.Setoverlay.menuNames = overlays_menu
        except Exception:
            print("Exception in user code:")
            print("-"*60)
            traceback.print_exc(file=sys.stdout)
            print("-"*60)
        pass
    
    def Create_new_overlay(self, name):
        try:
            # TODO: Make this look for the base so we aren't double creating stuff
            # Create select CHOP to get our mode channel	
            newOp = self.ownerComp.parent().create(baseCOMP, name)
            newOp.nodeX = self.ownerComp.nodeX + self.ownerComp.nodeWidth + 25
            newOp.color = (1, 0.1, 0.1)
            newOp.par.externaltox = app.userPaletteFolder + '/MW-TouchDesigner-Tools/Utilities/base_overlay_switcher/overlay_template.tox'
            newOp.par.reinitnet.pulse()
            overlay_path = self.path + '/' + name + '.tox'
            newOp.par.externaltox = overlay_path
            newOp.save(overlay_path)           
            newOp.destroy()
            self.Setup_menu()
            print(f'{datetime.now()}: Created new Show Moment Base: ' + name)
        except Exception:
            print("Exception in user code:")
            print("-"*60)
            traceback.print_exc(file=sys.stdout)
            print("-"*60)
        pass

    def Set_overlay(self, overlay):
        try:
            
            if '.tox' not in overlay:
                overlay = overlay + '.tox'           
            #TODO have this handled as an exception instead
            if self.overlayList.row(overlay) is None: #check if we can find the tox
                print(overlay, " not found, cannot change overlay. Check the .tox is named properly and lives in the /Overlays folder")
                pass
            self.next_source.allowCooking = True
            self.next_source.par.externaltox = self.path + '/' + overlay #load the corresponding TOX into the 
            self.next_source.par.enablecloningpulse.pulse()
            self.next_source.par.reinitnet.pulse() #Re-initialize the TOX we just loaded
            self.timer.par.cuepulse.pulse() #start the transition over to the new mode
            self.connect_operators()
        except Exception:
            print("Exception in user code:")
            print("-"*60)
            traceback.print_exc(file=sys.stdout)
            print("-"*60)
        pass
    
    def Complete_transition(self):
        self.Load_tox(self.source, str(self.next_source.par.externaltox))
        self.connect_operators()
        pass

    def Disable_inactive_operators(self):
        self.next_source.allowCooking = False   
        pass

    def Load_tox(self, source, tox):
        """
        load_tox Loads and initializes a .tox from the Overlays folder into a specified base

        :param self: self
        :param source: Specifies the Base to load the .tox into
        :param tox: String representation of the .tox file to load, .tox extension is added automatically if not provided
        :return: Nothing
        """
        try:
            tox_path = tox
            if tox_path is "random":
                tox_path = str(self.overlayList[randint(1, self.overlayList.numRows - 1), 0])

            if self.path not in tox_path:
                tox_path = self.path + '/' + tox_path
            if '.tox' not in tox_path:
                tox_path = tox_path + '.tox'
            source.par.externaltox = tox_path
            #source.par.enablecloningpulse.pulse()
            source.par.reinitnet.pulse()
            #source.outputConnectors[0].connect(self.ownerComp.op(source.name + '_null'))
        except Exception: 
            print("Exception in user code:")
            print("-"*60)
            traceback.print_exc(file=sys.stdout)
            print("-"*60)
        pass
        
    def connect_operators(self):
        try: 
            self.source.outputConnectors[0].connect(self.source_null)
            self.next_source.outputConnectors[0].connect(self.next_source_null)
        except Exception: 
            print("Exception in user code:")
            print("-"*60)
            traceback.print_exc(file=sys.stdout)
            print("-"*60)
        pass