from chainer import backend


class GradientScaling(object):

    """Optimizer/UpdateRule hook function for scaling gradient.

    This hook function scales gradient by a constant value.

    Args:
        rate (float): Coefficient for scaling.
    Attributes:
        rate (float): Coefficient for scaling.
    """
    name = 'GradientScaling'
    call_for_each_param = True

    def __init__(self, rate):
        self.rate = rate

    def __call__(self, rule, param):
        g = param.grad
        with backend.get_device_from_array(g):
            g *= self.rate
