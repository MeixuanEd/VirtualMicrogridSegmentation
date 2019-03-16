import numpy as np

class OrnsteinUhlenbeckActionNoise(object):
    """
    Implementation of an Ornstein–Uhlenbeck process for exploration. Based on:
    https://github.com/openai/baselines/blob/master/baselines/ddpg/noise.py
    https://math.stackexchange.com/questions/1287634/implementing-ornstein-uhlenbeck-in-matlab
    """
    def __init__(self, mu, sigma=0.1 , theta=.15, dt=1e-2, x0=None):
        self.theta = theta
        self.mu = mu
        self.sigma = sigma
        self.dt = dt
        self.x0 = x0
        self.reset()

    def __call__(self):
        x = (self.x_prev + self.theta * (self.mu - self.x_prev) * self.dt +
             self.sigma * np.sqrt(self.dt) * np.random.normal(size=self.mu.shape))
        self.x_prev = x
        return x

    def reset(self):
        self.x_prev = self.x0 if self.x0 is not None else np.zeros_like(self.mu)

    def __repr__(self):
        return 'OrnsteinUhlenbeckActionNoise(mu={}, sigma={})'.format(self.mu,
                                                                      self.sigma)