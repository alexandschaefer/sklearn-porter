# -*- coding: utf-8 -*-

import os
import subprocess as subp

import numpy as np
import random as rd

from sklearn.datasets import load_iris
from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_digits
from sklearn.utils import shuffle

from tests.estimator.classifier.SeparatedData import SeparatedData


class Classifier(SeparatedData):

    TEST_N_RANDOM_FEATURE_SETS = 20
    TEST_N_EXISTING_FEATURE_SETS = 20

    def setUp(self):
        np.random.seed(1)
        rd.seed(1)
        self._init_env()

    def tearDown(self):
        self._clear_estimator()

    def _init_env(self):
        for param in ['TEST_N_RANDOM_FEATURE_SETS', 'TEST_N_EXISTING_FEATURE_SETS']:
            n = os.environ.get(param, None)
            if n is not None and str(n).strip().isdigit():
                n = int(n)
                if n > 0:
                    self.__setattr__(param, n)

    def load_binary_data(self, shuffled=True):
        samples = load_breast_cancer()
        self.X = shuffle(samples.data) if shuffled else samples.data
        self.y = shuffle(samples.target) if shuffled else samples.target
        self.n_features = len(self.X[0])

    def load_iris_data(self, shuffled=True):
        samples = load_iris()
        self.X = shuffle(samples.data) if shuffled else samples.data
        self.y = shuffle(samples.target) if shuffled else samples.target
        self.n_features = len(self.X[0])

    def load_digits_data(self, shuffled=True):
        samples = load_digits()
        self.X = shuffle(samples.data) if shuffled else samples.data
        self.y = shuffle(samples.target) if shuffled else samples.target
        self.n_features = len(self.X[0])

    def _clear_estimator(self):
        self.estimator = None
        cmd = 'rm -rf tmp'.split()
        subp.call(cmd)
