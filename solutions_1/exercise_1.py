def are_floats_within_tolerance(a, b, tol):
    return abs(a - b) <= tol


a = 3.14159
b = 3.14160
tol = 0.0001

if are_floats_within_tolerance(a, b, tol):
    print("a and b are within the tolerance.")
else:
    print("a and b are not within the tolerance.")