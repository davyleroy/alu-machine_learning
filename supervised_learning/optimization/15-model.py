#!/usr/bin/env python3
""" Train Model with different optimization parameters"""

import tensorflow as tf


def model(Data_train, Data_valid, layers, activations, alpha=0.001,
          beta1=0.9, beta2=0.999, epsilon=1e-8, decay_rate=1,
          batch_size=32, epochs=5, save_path='/tmp/model.ckpt'):
    """ Function that trains a model with tensorflow using mini-batch gradient
        descent, to also analyze validaiton data, and optimize using Adam
        optimization algorithm

    Args:
        Data_train (tuple): tuple of numpy.ndarray of shape (m, 784) containing
            the training data and labels
            m: number of data points
            784: number of features
        Data_valid (tuple): tuple of numpy.ndarray of shape (m, 784) containing
            the validation data and labels
            m: number of data points
            784: number of features
        layers (list): list containing the number of nodes in each layer of the
            network
        activations (list): list containing the activation functions for each
            layer of the network
        alpha (float): learning rate
        beta1 (float): weight used for first moment
        beta2 (float): weight used for second moment
        epsilon (float): small number used to avoid division by zero
        decay_rate (float): weight used to determine the rate at which alpha
            will decay
        batch_size (int): number of data points in a batch
        epochs (int): number of times the training should pass through the
            whole dataset
        save_path (str): path to where the model should be saved
    Returns:
        str: the path where the model was saved
    """
