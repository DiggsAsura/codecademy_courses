# Learn Intermediate Python 3
# 5. Unit Testing
# 2. Unit Testing
# 8. Parameterizing Tests

print('''\n
Parameterizing Tests
------------------------- ''')

# In previous examples, we created test cases for the add_ten() function with
# various inputs. However, the actual logic of our tests really didn't change.
# To decrease repetition, Python provides us a specific toolset for tests
# with only minor differences. This is known as test parameterization.
# By parameterizing tests, we can leverage the functionality of a single
# test to get a large amount of coverage of different inputs.
#
# To accomplish test parameterization, the unittest framework provides us with
# the subTest context manager. Let's refactor our previous test class to 
# utilize it and see it in action:

#!import unittest
#!
#!def times_ten(number):
#!  return number * 100
#!
#!class TestTimesTen(unittest.TestCase):
#!  def test_times_ten(self):
#!    for num in [0, 1000000, -10]:
#!      with self.subTest():
#!        expected_result = num * 10
#!        message = "Expected times_ten(" + str(num) + ') to return ' + str(expected_result)
#!        self.assertEqual(times_ten(num), expected_result, message)
#!
#!unittest.main()

# Here, in our method test_times_ten(), instead of writing individual test cases
# for each input of 0, 10, and 1000000, we can test a collection of inputs by 
# using a loop followed by a with statement and our subTest context manager.
#
# By using subTest, each iteration of our loop is treated as an individual test.
# Python will run the code inside of the context manager on each iteration, and if
# one fails, it will return the failure as a separate test case failure.
#
# Just like before, we are using the assertEqual() method to check
# expected result, and we are expecting (due to an error in times_ten()) that
# the cases of using an input of -10 and 1000000 will fail. Here is the new
# output:

#! ======================================================================
#! FAIL: test_times_ten (__main__.TestTimesTen) (<subtest>)
#! ----------------------------------------------------------------------
#! Traceback (most recent call last):
#!   File "scratch.py", line 12, in test_times_ten
#!     self.assertEqual(times_ten(num), expected_result, message)
#! AssertionError: 100000000 != 10000000 : Expected times_ten(1000000) to return 10000000
#!
#! ======================================================================
#! FAIL: test_times_ten (__main__.TestTimesTen) (<subtest>)
#! ----------------------------------------------------------------------
#! Traceback (most recent call last):
#!   File "scratch.py", line 12, in test_times_ten
#!     self.assertEqual(times_ten(num), expected_result, message)
#! AssertionError: -1000 != -100 : Expected times_ten(-10) to return -100
#!
#! ----------------------------------------------------------------------
#! Ran 1 test in 0.000s
#!
#! FAILED (failures=2)

# If we want to expand our test coverage, we can simply modify the list that our
# loop iterates over. We can test a range of thousands of inputs simply by 
# using the context manager setup to achieve test parameterization.
#
# Optionally, we can give our subtests better readability by making a small
# change in our code for the first argument of self.subTest(). The below code
# has most of our script omitted for brevity but uses the same script we 
# executed above:
#
#! ... more code above...
#!
#! for num in [0, 1000000, -10]:
#!   with self.subTest(num):
#!
#! ... more code below ...

# This makes our test clearer, because our test error message goes from:

#! FAIL: test_times_ten(__main__.TestTimesTen)(<subtest>)

# to:

#! FAIL: test_times_ten(__main__.TestTimesTen) [1000000]

# When working with large amounts of test inputs, it is much easier to 
# distinguish which case failed. We can actually use any message we want as the
# first argument, but using the tested case is usually the best way to
# increase readability for ourselfs and other developers.
#
# By using test parameterization, we made our codebase much cleaner and more
# maintainable. Let's get some practice by refactoring some of our previous
# tests!


print('''\n
Tasks
--------- ''')

# 1. Small World Air is growing and has added many more movie options to the 
#    entertainment system (we can see them inside of entertainment.py)
#
#    Let's adjust our EntertainmentSystemTests class to make sure they all get
#    tested. Replace the call to entertainment.get_daily_movie() with
#    entertainment.get_daily_movies() (our new method)
#
#    Lastly, for better readability, update the variable name daily_movie
#    to daily_movies.
#    After updating this variable name, update the first argument in the call
#    to self.assertIn() to use this new variable name. 
#
# 2. Under our two variables, write a for loop that iterates over daily_movies
#    and stores each iteration value into a variable called movie. For now,
#    let's simply print movie on each iteration.
#
# 3. Indent our self.assertIn() call to be inside the for loop and change the
#    first argument in self.assertIn() from daily_movie to movie to 
#    represent the individual movies on each iteration of the loop.
#
#    Note: Creating this structure might be okay at first glance (and may
#    even make you wonder why we need the context manager), but if we run our
#    test, we will see that the test will fail in the middle of our movies 
#    collection and won't check the rest (it stops at Black Widow and not
#    Spiral)! This is because like many testing frameworks, unittest will fail
#    and stop on the first failure it encounters.
#
# 4. Lastly, under our print statement of movie but before our assertIn call,
#    insert a self.subTest() to wrap our test method. To make sure we can
#    distinguish test cases between each movie, pass a single argument of
#    movie into self.subTest()
#
#    Don't forget to preface the context manager with a with statement and 
#    indent our self.assertIn() statement. Now, we can observe testing
#    multiple movies and if they are licensed or not.

import unittest
import entertainment3

class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    daily_movies = entertainment3.get_daily_movies()
    licensed_movies = entertainment3.get_licensed_movies()

    # Write your code below:
    for movie in daily_movies:
      print(movie)
      with self.subTest(movie):
        self.assertIn(movie, licensed_movies)

unittest.main()