import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


Xs = np.array([ 0.387, 0.723, 1.00, 1.52, 5.20, 9.54, 19.2, 30.1, 39.5])
log_Xs = np.log(Xs)

Ys = np.array([ 0.241, 0.615, 1.00, 1.88, 11.9, 29.5, 84.0, 165.0, 248])
log_Ys = np.log(Ys)
N = 9

# plt.scatter(Xs, Ys)
plt.scatter(log_Xs, log_Ys)
plt.show()
# plt.show()

correlation_coefficient = np.corrcoef(Xs, Ys)
correlation_coefficient_log_transformed = np.corrcoef(log_Xs, log_Ys)
log_Xs_std = np.std(log_Xs, ddof=1)
log_Ys_std = np.std(log_Ys, ddof=1)
slope_logged_transformed = correlation_coefficient_log_transformed*log_Ys_std/log_Xs_std
print(f'Correlation coefficient: {correlation_coefficient[0][1]}')
print(f'Correlation coefficient: {correlation_coefficient_log_transformed[0][1]}')
print(f'Slope of logged transformed: {slope_logged_transformed[0][0]:.2f}')
# sm.qqplot(Xs, line='s')
# plt.title("X distribution")
# # plt.show()
#
# sm.qqplot(np.log(Xs), line='s')
# plt.title("log(X) distribution")
# plt.show()
#
# sm.qqplot(Ys**2, line='s')
# plt.title("Y squared distribution")
# # plt.show()
#
# sm.qqplot(np.log(Ys), line='s')
# plt.title("log(Y) distribution")
# plt.show()