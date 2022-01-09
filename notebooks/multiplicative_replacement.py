from skbio.stats.composition import closure
import numpy as np

# This also works on count data directly
def multiplicative_replacement(mat, delta=None):
    r"""Replace all zeros with small non-zero values
    It uses the multiplicative replacement strategy [1]_ ,
    replacing zeros with a small positive :math:`\delta`
    and ensuring that the compositions still add up to 1.
    Parameters
    ----------
    mat: array_like
       a matrix of proportions where
       rows = compositions and
       columns = components
    delta: float, optional
       a small number to be used to replace zeros
       If delta is not specified, then the default delta is
       :math:`\delta = \frac{1}{N^2}` where :math:`N`
       is the number of components
    Returns
    -------
    numpy.ndarray, np.float64
       A matrix of proportions where all of the values
       are nonzero and each composition (row) adds up to 1
    Raises
    ------
    ValueError
       Raises an error if negative proportions are created due to a large
       `delta`.
    Notes
    -----
    This method will result in negative proportions if a large delta is chosen.
    References
    ----------
    .. [1] J. A. Martin-Fernandez. "Dealing With Zeros and Missing Values in
           Compositional Data Sets Using Nonparametric Imputation"
    Examples
    --------
    >>> import numpy as np
    >>> from skbio.stats.composition import multiplicative_replacement
    >>> X = np.array([[.2,.4,.4, 0],[0,.5,.5,0]])
    >>> multiplicative_replacement(X)
    array([[ 0.1875,  0.375 ,  0.375 ,  0.0625],
           [ 0.0625,  0.4375,  0.4375,  0.0625]])
    """
    mat = np.array(mat)
    z_mat = (mat == 0)

    num_feats = mat.shape[-1]
    tot = np.sum(z_mat, axis=-1, keepdims=True)

    if delta is None:
        delta = np.min((np.min(mat[mat > 0])*.55, (1. / num_feats)**2))

    zcnts = 1 - ((tot * delta)/mat.sum(axis=-1, keepdims=True))
    if np.any(zcnts) < 0:
        raise ValueError('The multiplicative replacment created negative '
                         'proportions. Consider using a smaller `delta`.')
    mat = np.where(z_mat, delta, zcnts * mat)
    return mat.squeeze()