from prison import Player

class SiriusBlack(Player):
    """
    This is an example player
    """
    def __init__(self): # default constructor
    	self.decisions = []
    
    def studentID(self):
        return "20486960"

    def agentName(self):
        return "SiriusBlack"

    def play(self, myHistory, oppHistory1, oppHistory2):
        if len(self.decisions) == 0 or len(oppHistory1)==0 or len(oppHistory2)==0:
            self.decisions.append(0)
            return 0
        if myHistory[len(myHistory)-1] == oppHistory1[len(oppHistory1)-1] and myHistory[len(myHistory)-1] == oppHistory2[len(oppHistory2)-1]:
            self.decisions.append(0)
            return 0
        elif self.decisions[len(self.decisions)-1]	<> myHistory[len(myHistory)-1] and self.decisions[len(self.decisions)-1] == 0:
            self.decisions.append(0)
            return 0
        self.decisions.append(1)
        return 1

 # pavlov   

# http://www.umass.edu/preferen/Game%20Theory%20Evolving/GTE%20Public/GTE%20Repeated%20Games.pdf    
#def ContriteTFT(self, myHistory, oppHistory1, oppHistory2):

	
