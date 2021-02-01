import numpy as np

def HSP_neighbors(X_train,X_test):
    data_idx = np.arange(len(X_train))
    query_idx = np.arange(len(X_test))

    g = {}

    for query in query_idx:
        g[query] = []

    for query in query_idx:
        idx_candidates = np.copy(data_idx)

        while idx_candidates.shape[0]>1:
            candidates = [X_train[idx] for idx in idx_candidates]

            distances = (((candidates-X_test[query])**2).sum(axis=1))**(1/2)
            neighbors = distances.argsort()

            neighbor = int(idx_candidates[neighbors[0]])

            g[query].append(neighbor)


            new_candidates = []

            for candidate in idx_candidates:
                if distance(X_train[candidate],X_test[query]) < distance(X_train[candidate],X_train[neighbor]):
                    new_candidates.append(candidate)

            idx_candidates = np.array(new_candidates)

    return list(g.values())
