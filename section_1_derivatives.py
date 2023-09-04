# write the function df that returns the analytical gradient of f
# i.e. use your skills from calculus to take the derivative, then implement the formula
# if you do not calculus then feel free to ask wolframalpha, e.g.:
# https://www.wolframalpha.com/input?i=d%2Fda%28sin%283*a%29%29%29

def gradf(a, b, c):
  return [-3*(a**2) - 0.5*(a**(-0.5)), 3*cos(3*b) + 2.5*(b**1.5), 1/c**2] # todo, return [df/da, df/db, df/dc]

# expected answer is the list of
ans = [-12.353553390593273, 10.25699027111255, 0.0625]
yours = gradf(2, 3, 4)
for dim in range(3):
  ok = 'OK' if abs(yours[dim] - ans[dim]) < 1e-5 else 'WRONG!'
  print(f"{ok} for dim {dim}: expected {ans[dim]}, yours returns {yours[dim]}")

# now estimate the gradient numerically without any calculus, using
# the approximation we used in the video.
# you should not call the function df from the last cell

h = 1e-6;
ans1 = (f(2+h,3,4)-f(2,3,4)) / h
ans2 = (f(2,3+h,4)-f(2,3,4)) / h
ans3 = (f(2,3,4+h)-f(2,3,4)) / h
# -----------
numerical_grad = [ans1, ans2, ans3] # TODO
# -----------

for dim in range(3):
  ok = 'OK' if abs(numerical_grad[dim] - ans[dim]) < 1e-5 else 'WRONG!'
  print(f"{ok} for dim {dim}: expected {ans[dim]}, yours returns {numerical_grad[dim]}")

# there is an alternative formula that provides a much better numerical
# approximation to the derivative of a function.
# learn about it here: https://en.wikipedia.org/wiki/Symmetric_derivative
# implement it. confirm that for the same step size h this version gives a
# better approximation.
h = 1e-6;
ans1 = (f(2+h,3,4)-f(2-h,3,4)) / (2*h)
ans2 = (f(2,3+h,4)-f(2,3-h,4)) / (2*h)
ans3 = (f(2,3,4+h)-f(2,3,4-h)) / (2*h)
# -----------
numerical_grad2 = [ans1, ans2, ans3] # TODO
# -----------

for dim in range(3):
  ok = 'OK' if abs(numerical_grad2[dim] - ans[dim]) < 1e-5 else 'WRONG!'
  print(f"{ok} for dim {dim}: expected {ans[dim]}, yours returns {numerical_grad2[dim]}")