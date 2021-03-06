from __future__ import print_function
import numpy as np
import tensorflow as tf

from edward.stats import bernoulli
from scipy import stats

sess = tf.Session()

def _assert_eq(val_ed, val_true):
    with sess.as_default():
        assert np.allclose(val_ed.eval(), val_true)

def _test_entropy(p):
    val_true = stats.bernoulli.entropy(p)
    _assert_eq(bernoulli.entropy(p), val_true)
    _assert_eq(bernoulli.entropy(tf.constant(p)), val_true)
    _assert_eq(bernoulli.entropy(tf.constant([p])), val_true)

def test_entropy_scalar():
    _test_entropy(0.5)
    _test_entropy(0.75)

def test_entropy_1d():
    _test_entropy([0.1, 0.9, 0.1])
    _test_entropy([0.5, 0.75, 0.2])
