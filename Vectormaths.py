from sympy import *
init_printing()

#noramlized and unit vectors


def norm_unit_vector():
    v = Matrix([[2, 2, -1]])
    v.norm()

    u = v.normalized()
    print(u)
    u.norm()

def angle_of_vectors():
    
    '''
    Cos(Theta) = x *   y <- Dot Product not Multplication
            _________
            ||X|| ||Y||
    '''

    x = Matrix([[1, 0, 0]])
    y = Matrix([[0, 1, 0]])

    xy_dot = DotProduct(x, y)

    xy_norm = (x.norm() * y.norm())

    res = xy_dot / xy_norm
    print(res)