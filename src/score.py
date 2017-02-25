import numpy as np


def pinball_score(tau, y, yp):
    gt = y >= yp
    lt = y < yp
    C = np.sum(y[gt] - yp[gt])*tau + np.sum(yp[lt]-y[lt])*(1-tau)
    return C/len(y)
