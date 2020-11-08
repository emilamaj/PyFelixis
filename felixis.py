#Principe du calcul de l'état t+dt:
#Traitement indépendant des branches parallèles, aux bornes d'une source de tension constante.
#Calcul récursif itéré / Relaxation des curseurs / Linéarisation et inversion de matrice.

class Component:
    def __init__(self, c_id, n_poles, values, state, nodes):
        self.c_id = c_id
        self.n_poles = n_poles
        self.values = values
        self.state = state
        self.nodes = nodes

    def update(self):
        pass

class Resistor(Component):
    def update(self):
        pass
        
class Circuit:
    t = 0 #Current time
    components = [] #List of the components instances
    node_count = 0 #Total number of nodes in the circuit

    node_V = []
    node_I = []
    store = []
    def __init__(self):
        pass
    def getVoltage(self, n1, n2, tminus=1):
        pass
    def getCurrent(self, to_node, from_component, tminus=1):
        pass
    def setVoltage(self, n1, n2):
        pass
    def setCurrent(self, to_node, from_component, tminus=1):
        pass
    
    @staticmethod
    def fromNetlist(netString):
        #Felixis does not use SPICE "nets", but assigns a number to circuit nodes. 
        newC = Circuit()#Instance to return
        for line in netString.splitlines():
            continue
        return newC

class Simulation:
    duration = 1 #Duration of the simulation in seconds
    dt = 1e-6 #Simulation step size
    snapPeriod = 1e-3 #Time between two snapshots of the watchlist
    tminusMax = 3 #Number of circuit states to store (to compute the next states)

    t = 0 #Current time
    circuits = []#List of circuits stored by the simulation
    def __init__(self, duration, snapPeriod, dt, tminusMax):
        self.duration = duration
        self.snapPeriod = snapPeriod
        self.dt = dt
        self.tminusMax = tminusMax

        self.t = 0
        self.circuts = [Circuit()]

