import unittest

import numpy
import six

import chainer
from chainer import cuda
from chainer.testing import attr

from deepmark_chainer.net import small_lstm


class TestSmallLSTM(unittest.TestCase):

    def setUp(self):
        self.x = numpy.random.randint(0, 10, (10, 20)).astype(numpy.int32)
        self.l = small_lstm.SmallLSTM()

    def check_forward(self, xp):
        x = chainer.Variable(xp.asarray(self.x))
        self.l(x)

    def test_forward_cpu(self):
        self.check_forward(numpy)

    @attr.gpu
    def test_forward_gpu(self):
        self.l.to_gpu()
        self.check_forward(cuda.cupy)
