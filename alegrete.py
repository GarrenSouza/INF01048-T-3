import numpy as np


def compute_mse(theta_0, theta_1, data):
    acum_error = 0.0
    for k in range(len(data)):
        acum_error += (first_order_pol(theta_0, theta_1, data[k][0]) - data[k][1])**2
    return acum_error / len(data)


def first_order_pol(theta_0, theta_1, x):
    return theta_0 + theta_1 * x


def step_gradient(theta_0, theta_1, data, alpha):
    df_dtheta_0 = 0
    df_dtheta_1 = 0
    for k in range(len(data)):
        e = first_order_pol(theta_0, theta_1, data[k][0]) - data[k][1]
        df_dtheta_0 += e
        df_dtheta_1 += e * data[k][0]
    df_dtheta_0 *= 2/len(data)
    df_dtheta_1 *= 2/len(data)
    return (theta_0-alpha*df_dtheta_0, theta_1-alpha*df_dtheta_1)


def fit(data, theta_0, theta_1, alpha, num_iterations):
    theta_0_record = [theta_0]
    theta_1_record = [theta_1]
    t0 = theta_0
    t1 = theta_1
    for i in range(num_iterations):
        t0, t1 = step_gradient(t0, t1, data, alpha)
        theta_0_record.append(t0)
        theta_1_record.append(t1)
    return theta_0_record, theta_1_record
