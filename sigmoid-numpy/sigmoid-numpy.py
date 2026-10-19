import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    a=[]
    y=np.array(x)
    x=1/(1+np.exp(-y))
    a.append(x)
    return np.array(a)