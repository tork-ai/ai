# -*- coding: utf-8 -*-

pool_size = 20


def images_path(dir_name):
    return 'data/{}'.format(dir_name)


def images_glob_path(dir_name):
    return 'data/{}/*.jpg'.format(dir_name)


def images_order(dir_name):
    return 'images_order.csv'.format(dir_name)

def vectors_path(dir_name):
    return 'images_vec.npz'.format(dir_name)
