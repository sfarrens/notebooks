from .sparse import soft_thresh


# Function that performs simple forward backward splitting.
def forwardBackward(observation, first_guess, mask, lambda_, n_iter=300,
                    gamma=1.0):

    alpha_rec = first_guess

    for i in range(n_iter):

        alpha_temp = alpha_rec - gamma * grad(observation, alpha_rec, mask)
        alpha_rec = sparse.soft_thresh(alpha_temp, lambda_)
        cost = cost_func(observation, alpha_rec, mask, lambda_)

    return alpha_rec
