import numpy as np
from src.matrix import matrix


class KalmanFilter(object):
    """Elementary Kalman filter implementation"""

    def __init__(self, states=2, init=[], cov=[]):
        if not init:
            init = np.zeros((states, 1))
        if not cov:
            cov = np.eye(states, dtype=float) * 1000
        self._states = matrix(init)
        self._covariance = matrix(cov)
        self._transition_matrix = matrix(np.zeros((states, states)))
        self._measurement_matrix = matrix(np.zeros((1, states)))
        self._z_uncertainty = matrix([[0.1, 0], [0, 0.1]])

    def set_sys_matrices(self, F, H):
        self._transition_matrix = matrix(F)
        self._measurement_matrix = matrix(H)
        print("F:\n")
        self._transition_matrix.show()
        print("H:\n")
        self._measurement_matrix.show()

    def _predict(self, motion):
        motion = matrix([[motion[0]], [motion[1]], [0.], [0.]])
        self._states = self._transition_matrix * self._states + motion
        self._covariance = self._transition_matrix * self._covariance * self._transition_matrix.transpose()

    def _update(self, measurement):
        measurement = matrix(measurement)
        error = measurement - (self._measurement_matrix * self._states)
        S = self._measurement_matrix * self._covariance * self._measurement_matrix.transpose() + self._z_uncertainty
        K = self._covariance * self._measurement_matrix.transpose() * S.inverse()
        self._states = self._states + K * error
        self._covariance = (matrix(np.eye(self._states.dimx)) - K * self._measurement_matrix) * self._covariance

    def filter(self, motion, measurement):
        self._predict(motion)
        self.show()
        self._update(measurement)
        self.show()

    def show(self):
        print("States:\n")
        self._states.show()
        print("Covariance:\n")
        self._covariance.show()
