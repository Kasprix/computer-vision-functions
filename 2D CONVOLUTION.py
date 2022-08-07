import numpy as np


# No need to rotate mask. X is image, H is mask
def convolve_with_mask(X, H):
    # make sure both X and H are 2-D
    assert( X.ndim == 2)
    assert( H.ndim == 2)

    # get the horizontal and vertical size of X and H
    imageColumns = X.shape[1]
    imageRows = X.shape[0]
    kernelColumns = H.shape[1]
    kernelRows = H.shape[0]

    # calculate the horizontal and vertical size of Y (assume "full" convolution)
    newRows = imageRows + kernelRows - 1
    newColumns = imageColumns + kernelColumns - 1

    # create an empty output array
    Y = np.zeros((newRows,newColumns))


    # go over output locations
    for m in range(newRows):
        for n in range(newColumns):

        # go over input locations
            for i in range(kernelRows):
                for j in range(kernelColumns):
                    if (m-i >= 0) and (m-i < imageRows ) and (n-j >= 0) and (n-j < imageColumns):
                            Y[m,n] = Y[m,n] + H[i,j]*X[m-i,n-j]
            # make sure kernel is within bounds

            # calculate the convolution sum

    return Y


kernel = np.array([[-1,1]])
image=np.array([[0.01,.07,.01], [0.07,.75,.07], [0.01,.07,.01]])

print(convolve_with_mask(image,kernel))