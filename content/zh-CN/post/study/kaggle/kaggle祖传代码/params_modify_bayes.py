# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 16:08
# @Author  : zhao pengfei
# @Email   : zsonghuan@gmail.com
# @File    : ensemble.py
import pandas as pd
import numpy as np
from tqdm import tqdm
from skopt.utils import use_named_args
from ensemble_boxes import *
from skopt import gp_minimize
from skopt.space import Categorical, Integer, Real

def calculate_final_score(method, iou_thr, skip_box_thr, sigma=0.5):
    # 计算模型，返回一个分数，使得这个分数最大。
    return map
    # 使得map最大


def log(text):
    with open('opt.log', 'a+') as logger:
        logger.write(f'{text}\n')


def optimize(space, method, n_calls=10):
    @use_named_args(space)
    def score(**params):
        log('-'*5 + f'{method}' + '-'*5)
        log(params)
        final_score = calculate_final_score(method=method, **params)
        log(f'final_score = {final_score}')
        log('-'*10)
        return -final_score

    return gp_minimize(func=score, dimensions=space, n_calls=n_calls)

if __name__ == '__main__':
    # map = calculate_final_score('non_maximum_weighted', 0.588, 0.000)/6
    # print(map)
    space = [
        Real(0, 1, name='iou_thr'),
        Real(0.0, 1, name='skip_box_thr'),
    ]


    opt_result = optimize(
        space,
        method='non_maximum_weighted',
        n_calls=50,
    )

    best_final_score = -opt_result.fun
    best_iou_thr = opt_result.x[0]
    best_skip_box_thr = opt_result.x[1]
    print('-' * 13 + 'non_maximum_weighted' + '-' * 14)
    print(f'[Best Iou Thr]: {best_iou_thr:.3f}')
    print(f'[Best Skip Box Thr]: {best_skip_box_thr:.3f}')
    print(f'[Best Score]: {best_final_score:.4f}')
    print('-' * 30)
    """
    print('''Best parameters:
        - max_depth=%d
        - learning_rate=%.6f
        - max_features=%d
        - min_samples_split=%d
        - min_samples_leaf=%d''' % (res_gp.x[0], res_gp.x[1], 
                                res_gp.x[2], res_gp.x[3], 
                                res_gp.x[4]))
    
    from skopt.plots import plot_convergence
​
    plot_convergence(res_gp)
    """