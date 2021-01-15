import numpy as np


def stormer(dt, mass, particles, method, k1, args_method):
        count1 = method(mass, particles, k1, **args_method)
        particles[:, 2:] += .5*dt*k1[:, 2:]
        
        count2 = method(mass, particles, k1, **args_method)
        particles[:, :2] += dt*k1[:, :2]

        count3 = method(mass, particles, k1, **args_method)
        particles[:, 2:] += .5*dt*k1[:, 2:]
        
        return count1+count2+count3

class Stormer_verlet:
    def __init__(self, dt, nbodies, method,args_method):
        self.dt = dt
        self.method = method
        self.args_method = args_method
        self.k1 = np.zeros((nbodies, 4))
        self.count = 0
        self.count_eval_force = 0

    def init(self, mass, particles):
        pass

    def update(self, mass, particles):
        self.count_eval_force +=stormer(self.dt, mass, particles, self.method, self.k1, self.args_method)
        self.count += 3
        
class Optimized_815:
    def __init__(self, dt, nbodies, method, args_method):
        self.dt = dt
        self.method = method
        self.args_method = args_method
        self.k1 = np.zeros((nbodies, 4))
        self.gamma = np.zeros(15)
        self.gamma[0]  =  0.74167036435061295344822780
        self.gamma[1]  = -0.40910082580003159399730010
        self.gamma[2]  =  0.19075471029623837995387626
        self.gamma[3]  = -0.57386247111608226665638773
        self.gamma[4]  =  0.29906418130365592384446354
        self.gamma[5]  =  0.33462491824529818378495798
        self.gamma[6]  =  0.31529309239676659663205666
        self.gamma[7]  = -0.79688793935291635401978884
        self.gamma[8]  = self.gamma[6]
        self.gamma[9]  = self.gamma[5]
        self.gamma[10] = self.gamma[4]
        self.gamma[11] = self.gamma[3]
        self.gamma[12] = self.gamma[2]
        self.gamma[13] = self.gamma[1]
        self.gamma[14] = self.gamma[0]
        self.count = 0
        self.count_eval_force = 0

        
    def init(self, mass, particles):
        pass

    def update(self, mass, particles):
        for g in self.gamma:
            self.count_eval_force += stormer(g*self.dt, mass, particles, self.method, self.k1, self.args_method)
            self.count += 3
