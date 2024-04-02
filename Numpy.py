import numpy as np

print(np.__version__)


my_list = [1, 23, 45, 67, 89]
my_array_from_list = np.array(my_list)
my_array_from_list *= 10
print(my_array_from_list)
# [ 10 230 450 670 890]

my_tuple = (14, -3.23)
my_array_from_tuple = np.array(my_tuple)
print(my_array_from_tuple)
# [14. - 3.23]

array = np.arange(10)
print(array)
# [0 1 2 3 4 5 6 7 8 9]
array = np.arange(10, 15, 0.5)
print(array)
# [10.  10.5 11.  11.5 12.  12.5 13.  13.5 14.  14.5]

# Linspace

array = np.linspace(0, 30, 11)
print(array)
# [ 0.  3.  6.  9. 12. 15. 18. 21. 24. 27. 30.]

array = np.linspace(0, 30, 11, retstep=True)
print(array)
# (array([ 0.,  3.,  6.,  9., 12., 15., 18., 21., 24., 27., 30.]), 3.0)

# zeros()

array = np.zeros(10)
print(array)
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# ones()

array = np.ones(10)
print(array)
# [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

array = np.zeros((2, 3, 3))
print(array)
# [[[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]
#
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]]


# AVENUMPY

ave_vector = np.array([4, 8, 15, 16, 23, 42])
print(ave_vector[1])
# 8

ave_vector[1] = 14
print(ave_vector)
# [ 4 14 15 16 23 42]

ave_array = np.arange(35)
print(ave_array)
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
# 24 25 26 27 28 29 30 31 32 33 34]


ave_array.shape = (7, 5)
print(ave_array)
# [[ 0  1  2  3  4]
# [ 5  6  7  8  9]
# [10 11 12 13 14]
# [15 16 17 18 19]
# [20 21 22 23 24]
# [25 26 27 28 29]
# [30 31 32 33 34]]

print(ave_array[1])
# [5 6 7 8 9]

print(ave_array[5, 2])
# 27

zero_mod_2_mask = 0 == (ave_array % 2)
print(zero_mod_2_mask)
# [[ True False  True False  True]
# [False  True False  True False]
# [ True False  True False  True]
# [False  True False  True False]
# [ True False  True False  True]
# [False  True False  True False]
# [ True False  True False  True]]

sub_array = ave_array[zero_mod_2_mask]
print(sub_array)
# [ 0  2  4  6  8 10 12 14 16 18 20 22 24 26 28 30 32 34]


print(sub_array[sub_array > 10])
# [12 14 16 18 20 22 24 26 28 30 32 34]

zero_mod_4_mask = 0 == (ave_array % 4)
print(zero_mod_4_mask)

combined_mask = np.logical_and(zero_mod_4_mask, zero_mod_2_mask)
print(combined_mask)

sub_array = ave_array[combined_mask]
print(sub_array)
# [ 0  4  8 12 16 20 24 28 32]


ave_3D_array = np.arange(70)
ave_3D_array.shape = (2, 7, 5)
print(ave_3D_array)
# [[[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]
#  [20 21 22 23 24]
#  [25 26 27 28 29]
#  [30 31 32 33 34]]
#
# [[35 36 37 38 39]
#  [40 41 42 43 44]
#  [45 46 47 48 49]
#  [50 51 52 53 54]
#  [55 56 57 58 59]
#  [60 61 62 63 64]
#  [65 66 67 68 69]]]

ave_3D_array = 5*ave_3D_array-10
print(ave_3D_array)
# [[[-10  -5   0   5  10]
#  [ 15  20  25  30  35]
#  [ 40  45  50  55  60]
#  [ 65  70  75  80  85]
#  [ 90  95 100 105 110]
#  [115 120 125 130 135]
#  [140 145 150 155 160]]
#
# [[165 170 175 180 185]
#  [190 195 200 205 210]
#  [215 220 225 230 235]
#  [240 245 250 255 260]
#  [265 270 275 280 285]
#  [290 295 300 305 310]
#  [315 320 325 330 335]]]


left_mat = np.arange(6).reshape((2, 3))
rigth_mat = np.arange(15).reshape((3, 5))

dot_product = (np.dot(left_mat, rigth_mat))
print(dot_product)
# [[ 25  28  31  34  37]
# [ 70  82  94 106 118]]

summar = ave_3D_array.sum()
print(summar)
# 11375

summar = ave_3D_array.sum(axis=0)
print(summar)
# [[155 165 175 185 195] Сложение поэлементно
# [205 215 225 235 245]
# [255 265 275 285 295]
# [305 315 325 335 345]
# [355 365 375 385 395]
# [405 415 425 435 445]
# [455 465 475 485 495]]

summar = ave_3D_array.sum(axis=1)
print(summar)
# [[ 455  490  525  560  595] сложение столбцов
# [1680 1715 1750 1785 1820]]

summar = ave_3D_array.sum(axis=2)
print(summar)
# [[   0  125  250  375  500  625  750] сложение строк
# [ 875 1000 1125 1250 1375 1500 1625]]

# Broadcasting Rules

ave_2D_array = np.ones(35, dtype='int_').reshape((7, 5)) * 5
print(ave_2D_array)
# [[5 5 5 5 5]
# [5 5 5 5 5]
# [5 5 5 5 5]
# [5 5 5 5 5]
# [5 5 5 5 5]
# [5 5 5 5 5]
# [5 5 5 5 5]]

ave_random_2D_array = np.random.random((7, 5))
np.set_printoptions(precision=4)
print(ave_3D_array * ave_random_2D_array)
# [[[ -8.9156  -4.4303   0.       1.3055   5.1167]
#  [ 10.1251   2.2555  20.365    4.9475   8.692 ]
#  [  8.5893   1.3225  27.1619  35.221   30.2727]
#  [  3.9592  61.097   12.7969  36.1488  43.7108]
#  [ 66.6629  40.6277  83.3385  61.4161  54.9591]
#  [ 94.7993  89.2237 101.7226   8.4419  32.259 ]
#  [ 41.968   64.4681  84.6927 147.1209  78.4818]]
#
# [[147.1073 150.6296 160.1789  46.9984  94.6586]
#  [128.2518  21.991  162.9199  33.8079  52.1519]
#  [ 46.1673   6.4657 122.2283 147.2876 118.5681]
#  [ 14.6185 213.8393  42.6562 115.2244 133.7036]
#  [196.2852 115.4682 229.1808 163.7762 142.3941]
#  [239.0592 219.3415 244.1342  19.806   74.0763]
#  [ 94.4279 142.2744 183.5009 313.2252 164.3213]]]


# Structured Array

employee_data_def = [('name', 'S6'), ('height', 'f8'),
                     ('weight', 'f8'), ('age', 'i8')]
employee_array = np.zeros((4), dtype=employee_data_def)
print(employee_array)
# [(b'', 0., 0., 0) (b'', 0., 0., 0) (b'', 0., 0., 0) (b'', 0., 0., 0)]
employee_array[3] = ('Donatello', 200, 180, 105)
employee_array[0] = ('Raphael', 198, 150, 125)
print(employee_array)
# [(b'Raphae', 198., 150., 125)(b'',   0.,   0.,   0)
# (b'',   0.,   0.,   0)(b'Donate', 200., 180., 105)]
print(employee_array[1:])
# [(b'',   0.,   0.,   0)(b'',   0.,   0.,   0)
# (b'Donate', 200., 180., 105)]
ages = employee_array['age']
print(ages)
# [125   0   0 105]

company_employee_all = np.zeros((4, 3, 2), dtype=employee_data_def)
print(company_employee_all)
# [[[(b'', 0., 0., 0)(b'', 0., 0., 0)]
#  [(b'', 0., 0., 0)(b'', 0., 0., 0)]
#  [(b'', 0., 0., 0)(b'', 0., 0., 0)]]
#
# [[(b'', 0., 0., 0)(b'', 0., 0., 0)]
#  [(b'', 0., 0., 0)(b'', 0., 0., 0)]
#  [(b'', 0., 0., 0)(b'', 0., 0., 0)]]
#
# [[(b'', 0., 0., 0)(b'', 0., 0., 0)]
#  [(b'', 0., 0., 0)(b'', 0., 0., 0)]
#  [(b'', 0., 0., 0)(b'', 0., 0., 0)]]
#
# [[(b'', 0., 0., 0)(b'', 0., 0., 0)]
#  [(b'', 0., 0., 0)(b'', 0., 0., 0)]
#  [(b'', 0., 0., 0)(b'', 0., 0., 0)]]]
company_employee_all[3, 2, 1] = ('Pipin', 12, 12, 23)
print(company_employee_all)
# [[[(b'',  0.,  0.,  0)(b'',  0.,  0.,  0)]
#  [(b'',  0.,  0.,  0)(b'',  0.,  0.,  0)]
#  [(b'',  0.,  0.,  0)(b'',  0.,  0.,  0)]]
#
# [[(b'',  0.,  0.,  0)(b'',  0.,  0.,  0)]
#  [(b'',  0.,  0.,  0)(b'',  0.,  0.,  0)]
#  [(b'',  0.,  0.,  0)(b'',  0.,  0.,  0)]]
#
# [[(b'',  0.,  0.,  0)(b'',  0.,  0.,  0)]
#  [(b'',  0.,  0.,  0)(b'',  0.,  0.,  0)]
#  [(b'',  0.,  0.,  0)(b'',  0.,  0.,  0)]]
#
# [[(b'',  0.,  0.,  0)(b'',  0.,  0.,  0)]
#  [(b'',  0.,  0.,  0)(b'',  0.,  0.,  0)]
#  [(b'',  0.,  0.,  0)(b'Pipin', 12., 12., 23)]]]
