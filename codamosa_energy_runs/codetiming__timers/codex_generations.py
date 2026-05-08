

# Generated at 2026-04-26 11:02:40.905066
# Unit test for method max of class Timers
def test_Timers_max():  
    timers = Timers()
    timers.add("test_timer", 1.0)
    timers.add("test_timer", 2.0)
    timers.add("test_timer", 3.0)
    assert timers.max("test_timer") == 3.0


# Generated at 2026-04-26 11:02:45.483294
# Unit test for method median of class Timers
def test_Timers_median():    
    timers = Timers()
    
    timers.add("test_timer", 1.0)
    timers.add("test_timer", 2.0)
    timers.add("test_timer", 3.0)
    
    assert timers.median("test_timer") == 2.0, "Expected median to be 2.0"

    timers.add("test_timer", 4.0)
    
    assert timers.median("test_timer") == 2.5, "Expected median to be 2.5"

    timers.add("test_timer", 5.0)
    
    assert timers.median("test_timer") == 3.0, "Expected median to be 3.0"

    print("All median tests passed!")

# Call the test function
test_Timers_median()

# Generated at 2026-04-26 11:02:49.328170
# Unit test for method mean of class Timers
def test_Timers_mean(): 
    timers = Timers()
    timers.add("test1", 1)
    timers.add("test1", 1)
    timers.add("test1", 3)
    assert timers.mean("test1") == 1.6666666666666667 # Correct mean value for 1,1,3
    timers.clear() # Clear timers
    assert timers.count("test1") == 0 # After clearing, count should be 0
    timers.add("test1", 2)
    assert timers.mean("test1") == 2.0 # Correct mean value for single timing
    assert timers.count("test1") == 1 # Count should be 1 after adding a single timing


# Call the test
test_Timers_mean()

# Generated at 2026-04-26 11:02:51.669049
# Unit test for method min of class Timers
def test_Timers_min(): 
    timers = Timers()
    timers.add("timer1", 1.0)
    timers.add("timer1", 2.0)
    timers.add("timer1", 3.0)
    assert timers.min("timer1") == 1.0
    assert timers.min("non_existent_timer") == 0.0  # Will raise KeyError


# Generated at 2026-04-26 11:02:56.082916
# Unit test for method min of class Timers
def test_Timers_min(): 
    timers = Timers()
    timers.add('test_timer', 5)
    timers.add('test_timer', 10)
    assert timers.min('test_timer') == 5
    timers.add('test_timer', 3)
    assert timers.min('test_timer') == 3
    timers.add('test_timer', 3)
    assert timers.min('test_timer') == 3
    try:
        timers.min('non_existing_timer')
    except KeyError as e:
        assert str(e) == "'non_existing_timer'"
    else:
        assert False, "Expected KeyError not raised"
        
test_Timers_min()

# Generated at 2026-04-26 11:03:00.359548
# Unit test for method median of class Timers
def test_Timers_median(): 
    timers = Timers()
    timers.add("test_timer", 1.0)
    timers.add("test_timer", 3.0)
    timers.add("test_timer", 2.0)

    assert timers.median("test_timer") == 2.0  # The median of (1.0, 2.0, 3.0) is 2.0

    timers.add("test_timer", 4.0)
    assert timers.median("test_timer") == 2.5  # The median of (1.0, 2.0, 3.0, 4.0) is 2.5

    timers.clear()
    try:
        timers.median("test_timer")  # Should raise a KeyError
    except KeyError:
        pass  # Expected behavior

# Run the test
test_Timers_median()  # Should not raise any assertion error if the function works correctly


# Generated at 2026-04-26 11:03:04.058662
# Unit test for method min of class Timers
def test_Timers_min():    
    timers = Timers()
    timers.add("test_timer", 5.0)
    timers.add("test_timer", 3.0)
    timers.add("test_timer", 7.0)
    
    assert timers.min("test_timer") == 3.0
    assert timers.min("non_existing_timer") # Should raise KeyError

test_Timers_min()

# Generated at 2026-04-26 11:03:08.190281
# Unit test for method min of class Timers
def test_Timers_min(): 
    timers = Timers()
    timers.add("test_timer", 1.0)
    timers.add("test_timer", 2.0)
    timers.add("test_timer", 3.0)

    result = timers.min("test_timer")
    assert result == 1.0, f"Expected 1.0, but got {result}"

    timers.clear()
    result = timers.min("test_timer")
    assert result == 0, f"Expected 0, but got {result}"

test_Timers_min() # Run the test

# Generated at 2026-04-26 11:03:11.502873
# Unit test for method mean of class Timers
def test_Timers_mean(): 
    timers = Timers()
    timers.add('test_timer', 2.0)
    timers.add('test_timer', 4.0)
    timers.add('test_timer', 6.0)
    
    assert timers.mean('test_timer') == 4.0, "Mean should be 4.0"

# Running the test
test_Timers_mean()  # Should not raise an assertion error if the function works correctly

# Generated at 2026-04-26 11:03:15.329922
# Unit test for method median of class Timers
def test_Timers_median():    
    timers = Timers()
    # Test with no values
    timers.add("test", 1.0)
    timers.add("test", 2.0)
    timers.add("test", 3.0)
    
    assert timers.median("test") == 2.0

    timers.add("test", 4.0)
    assert timers.median("test") == 2.5

    timers.add("test", 5.0)
    assert timers.median("test") == 3.0

    # Adding an odd number of values
    timers.add("test", 6.0)
    timers.add("test", 7.0)
    assert timers.median("test") == 4.0

    # Checking with an empty timer
    try:
        timers.median("empty")
    except KeyError as e:
        assert str(e) == "'empty'"
    
    print("All tests passed!")

#

# Generated at 2026-04-26 11:03:20.102595
# Unit test for method mean of class Timers
def test_Timers_mean():   
    timers = Timers()
    timers.add('test', 1.0)
    timers.add('test', 2.0)
    timers.add('test', 3.0)
    assert timers.mean('test') == 2.0, "Should be 2.0"
    
test_Timers_mean()  # Call the test function

# Generated at 2026-04-26 11:03:23.333320
# Unit test for method median of class Timers
def test_Timers_median():    
    timers = Timers()
    timers.add('test', 1.0)
    timers.add('test', 2.0)
    timers.add('test', 3.0)
    
    assert round(timers.median('test'), 1) == 2.0
    
    timers.add('test', 4.0)
    
    assert round(timers.median('test'), 1) == 2.5

    # Edge case: No timings
    try:
        timers.median('non_existent')
    except KeyError:
        assert True
    else:
        assert False
    
    print("All tests passed.")

# Run the test function
test_Timers_median() 

# Generated at 2026-04-26 11:03:26.681937
# Unit test for method min of class Timers
def test_Timers_min(): 
    timers = Timers()
    timers.add("test_timer", 1.0)
    timers.add("test_timer", 2.0)
    timers.add("test_timer", 3.0)

    assert timers.min("test_timer") == 1.0


# Generated at 2026-04-26 11:03:28.159870
# Unit test for method max of class Timers
def test_Timers_max(): 
    timer = Timers()
    timer.add("test", 3.5)
    timer.add("test", 2.5)

    assert timer.max("test") == 3.5


# Generated at 2026-04-26 11:03:32.232993
# Unit test for method median of class Timers
def test_Timers_median(): 
    timers = Timers()
    timers.add("test_timer", 1)
    timers.add("test_timer", 3)
    timers.add("test_timer", 2)
    assert timers.median("test_timer") == 2.0

    timers.add("test_timer", 4)
    assert timers.median("test_timer") == 2.5

    timers.add("test_timer", 5)
    assert timers.median("test_timer") == 3.0

    try:
        timers.median("nonexistent_timer")
    except KeyError:
        pass  # Expected behavior

test_Timers_median()

# Generated at 2026-04-26 11:03:35.431598
# Unit test for method min of class Timers
def test_Timers_min(): 
    timers = Timers()
    timers.add('test', 3.5)
    timers.add('test', 2.5)
    timers.add('test', 4.0)
    assert timers.min('test') == 2.5
    
    timers.add('test', 1.0)
    assert timers.min('test') == 1.0

    timers.add('test', 5.0)
    assert timers.min('test') == 1.0
    
    timers.add('new_test', 10.0)
    assert timers.min('new_test') == 0.0
    
    try:
        timers.min('nonexistent')
    except KeyError:
        pass
    else:
        assert False, "Expected KeyError for nonexistent timer"

# Run the test
test_Timers_min()
print("Test passed!")

# Generated at 2026-04-26 11:03:39.046219
# Unit test for method median of class Timers
def test_Timers_median():    
    timers = Timers()
    timers.add("test_timer", 1.0)
    timers.add("test_timer", 2.0)
    timers.add("test_timer", 3.0)

    assert timers.median("test_timer") == 2.0
    
    # Testing for even number of elements
    timers.add("test_timer", 4.0)
    assert timers.median("test_timer") == 2.5

    # Testing for empty timer
    empty_timer = Timers()
    try:
        empty_timer.median("non_existent_timer")
    except KeyError:
        pass  # Expected behavior

# Run the test
test_Timers_median()

# Generated at 2026-04-26 11:03:42.225013
# Unit test for method median of class Timers
def test_Timers_median(): 
    t = Timers()
    
    # Test with an empty timer
    assert t.median("test_timer") == 0, "Median of empty timer should be 0"

    # Test with a single value
    t.add("test_timer", 5)
    assert t.median("test_timer") == 5, "Median of single value should be that value"

    # Test with multiple values
    t.add("test_timer", 1)
    t.add("test_timer", 3)
    t.add("test_timer", 4)
    t.add("test_timer", 2)
    
    assert t.median("test_timer") == 3, "Median should be 3 for the values 1, 2, 3, 4, 5"

    # Test with odd number of values
    t.add("test_timer", 6)

# Generated at 2026-04-26 11:03:45.444728
# Unit test for method median of class Timers
def test_Timers_median(): 
    timers = Timers()
    timers.add("test_timer", 1)
    timers.add("test_timer", 2)
    timers.add("test_timer", 3)
    assert timers.median("test_timer") == 2, "Expected median is 2"
    print("Test passed!")

# Run the test
test_Timers_median()

# Generated at 2026-04-26 11:03:47.557863
# Unit test for method max of class Timers
def test_Timers_max():    
    timers = Timers()
    timers.add('test1', 1.0)
    timers.add('test1', 2.0)
    timers.add('test1', 3.0)
    
    assert timers.max('test1') == 3.0, "Test case failed"
    assert timers.max('test2') == 0, "Test case failed"  # should raise KeyError


# Generated at 2026-04-26 11:03:51.357682
# Unit test for method max of class Timers
def test_Timers_max(): 
    timers = Timers() 
    timers.add("test_timer", 1.0) 
    timers.add("test_timer", 2.0) 
    timers.add("test_timer", 3.0) 
    assert timers.max("test_timer") == 3.0 
    timers.clear() 
    timers.add("test_timer", 5.0) 
    assert timers.max("test_timer") == 5.0 
    assert timers.max("non_existent_timer") == KeyError


# Generated at 2026-04-26 11:03:53.917912
# Unit test for method min of class Timers
def test_Timers_min(): 
    timers = Timers()
    timers.add("test", 1.0)
    timers.add("test", 3.0)
    assert timers.min("test") == 1.0  # Expected output: 1.0
    timers.add("test", 2.0)
    assert timers.min("test") == 1.0  # Expected output: 1.0
    timers.add("test", 0.5)
    assert timers.min("test") == 0.5  # Expected output: 0.5

# Unit tests for method max of class Timers

# Generated at 2026-04-26 11:03:55.742375
# Unit test for method min of class Timers
def test_Timers_min(): 
    timers = Timers()
    timers.add('test_timer', 1.2)
    timers.add('test_timer', 3.4)
    timers.add('test_timer', 2.5)
    
    # Test the min method
    assert timers.min('test_timer') == 1.2


# Generated at 2026-04-26 11:04:00.159964
# Unit test for method median of class Timers
def test_Timers_median(): 
    timers = Timers()
    timers.add("timer1", 1.0)
    timers.add("timer1", 2.0)
    timers.add("timer1", 3.0)
    timers.add("timer1", 4.0)
    timers.add("timer1", 5.0)
    assert timers.median("timer1") == 3.0  # Expected median for [1.0, 2.0, 3.0, 4.0, 5.0]

    timers.add("timer2", 1.0)
    timers.add("timer2", 3.0)
    timers.add("timer2", 2.0)
    assert timers.median("timer2") == 2.0  # Expected median for [1.0, 2.0, 3.0]

    timers.add("timer3", 4.0)

# Generated at 2026-04-26 11:04:06.672396
# Unit test for method mean of class Timers
def test_Timers_mean(): 
    timers = Timers() 
    timers.add("timer1", 1.0) 
    timers.add("timer1", 2.0) 
    timers.add("timer1", 3.0) 
    assert timers.mean("timer1") == 2.0, "Mean should be 2.0"

# Call the test function
test_Timers_mean()

# Generated at 2026-04-26 11:04:10.023288
# Unit test for method median of class Timers
def test_Timers_median(): 
    timers = Timers()
    timers.add('test_timer', 1.0)
    timers.add('test_timer', 2.0)
    timers.add('test_timer', 3.0)
    assert timers.median('test_timer') == 2.0

    timers.add('test_timer', 4.0)
    assert timers.median('test_timer') == 2.5  # Since the median of [1.0, 2.0, 3.0, 4.0] is 2.5
    
    timers.add('test_timer', 5.0)
    assert timers.median('test_timer') == 3.0  # The median of [1.0, 2.0, 3.0, 4.0, 5.0] is 3.0

    print("All tests passed!")


# Run the test
test_Timers_median()

# Generated at 2026-04-26 11:04:13.337716
# Unit test for method min of class Timers
def test_Timers_min(): 
    timers = Timers()

    # Adding some timing values
    timers.add("test_timer", 1.0)
    timers.add("test_timer", 2.0)
    timers.add("test_timer", 0.5)

    assert timers.min("test_timer") == 0.5  # The minimum value should be 0.5
    assert timers.min("non_existent_timer")  # This should raise a KeyError

# Running the test
test_Timers_min()

# If you want to suppress the output of Assertion Errors, you can wrap the test in a try/except block:
# try:
#     test_Timers_min()
#     print("All tests passed.")
# except AssertionError as e:
#     print(f"Test failed: {e}")

# Generated at 2026-04-26 11:04:19.791509
# Unit test for method mean of class Timers
def test_Timers_mean(): 
    timers = Timers()
    timers.add("test_timer", 1.0)
    timers.add("test_timer", 2.0)
    timers.add("test_timer", 3.0)
    
    # Expect the mean of the timer to be 2.0
    assert timers.mean("test_timer") == 2.0, f"Expected 2.0 but got {timers.mean('test_timer')}"
    
    # Test with an empty timer
    try:
        timers.mean("empty_timer")
    except KeyError:
        pass  # Expected behavior

test_Timers_mean()  # Running the unit test to verify the Timers.mean method

# Generated at 2026-04-26 11:04:23.697626
# Unit test for method min of class Timers
def test_Timers_min(): 
    timers = Timers()
    timers.add('timer1', 10)
    timers.add('timer1', 20)
    timers.add('timer1', 30)

    # Test for the minimum value
    assert timers.min('timer1') == 10.0, "Min value should be 10.0"
    
    # Adding a smaller value
    timers.add('timer1', 5)
    assert timers.min('timer1') == 5.0, "Min value should be 5.0"
    
    # Testing a timer that has no values should raise KeyError
    try:
        timers.min('timer2')
    except KeyError:
        assert True
    else:
        assert False, "KeyError should have been raised for non-existing timer"

# Run the unit test
test_Timers_min()

# Generated at 2026-04-26 11:04:25.860038
# Unit test for method min of class Timers
def test_Timers_min(): 
    timers = Timers()
    timers.add("test_timer", 2.0)
    timers.add("test_timer", 3.0)
    timers.add("test_timer", 1.0)
    assert timers.min("test_timer") == 1.0


# Generated at 2026-04-26 11:04:30.984966
# Unit test for method mean of class Timers
def test_Timers_mean():  # pragma: no cover
    timers = Timers()
    timers.add("test_timer", 1.0)
    timers.add("test_timer", 2.0)
    timers.add("test_timer", 3.0)
    assert timers.mean("test_timer") == 2.0, "Mean should be 2.0"

# Generated at 2026-04-26 11:04:34.809965
# Unit test for method min of class Timers
def test_Timers_min():    
    timers = Timers()
    timers.add("test_timer", 10.0)
    timers.add("test_timer", 5.0)
    timers.add("test_timer", 15.0)
    assert timers.min("test_timer") == 5.0

    timers.add("test_timer", 3.0)
    assert timers.min("test_timer") == 3.0

    try:
        timers.min("non_existing_timer")
    except KeyError as e:
        assert str(e) == "KeyError: 'non_existing_timer'"

# Run the unit test
test_Timers_min()

# Generated at 2026-04-26 11:04:38.680011
# Unit test for method median of class Timers
def test_Timers_median():    
    timers = Timers()
    timers.add("test_timer", 1.0)
    timers.add("test_timer", 2.0)
    timers.add("test_timer", 3.0)
    
    assert timers.median("test_timer") == 2.0, "Expected median is 2.0"
    
    timers.add("test_timer", 4.0)
    
    assert timers.median("test_timer") == 2.5, "Expected median is 2.5"

    timers.add("test_timer", 5.0)
    
    assert timers.median("test_timer") == 3.0, "Expected median is 3.0"

    print("All tests passed!")

# Run the unit test
test_Timers_median()  # Expected output: All tests passed!


# Generated at 2026-04-26 11:04:42.063805
# Unit test for method mean of class Timers
def test_Timers_mean(): 
    timers = Timers()
    timers.add('test_timer', 1.0)
    timers.add('test_timer', 2.0)
    timers.add('test_timer', 3.0)
    
    assert timers.mean('test_timer') == 2.0, "Mean should be 2.0"
    assert timers.mean('non_existent_timer') is math.nan, "Mean should be NaN for non-existent timer"


# Generated at 2026-04-26 11:04:44.520864
# Unit test for method max of class Timers
def test_Timers_max():    
    timers = Timers()
    timers.add('test_timer', 1.0)
    timers.add('test_timer', 2.0)
    timers.add('test_timer', 3.0)

    assert timers.max('test_timer') == 3.0
    
    timers.clear()  # Use clear to reset the timers for further tests
    print("test_Timers_max passed!")



# Generated at 2026-04-26 11:04:48.429830
# Unit test for method median of class Timers
def test_Timers_median():    
    timers = Timers()
    timers.add("test1", 1.0)
    timers.add("test1", 2.0)
    timers.add("test1", 3.0)
    assert timers.median("test1") == 2.0, "Should be 2.0"
    
    timers.add("test1", 4.0)
    timers.add("test1", 5.0)
    assert timers.median("test1") == 3.0, "Should be 3.0"

    timers.add("test1", 6.0)
    assert timers.median("test1") == 3.5, "Should be 3.5"

    timers.add("test1", 7.0)
    timers.add("test1", 8.0)
    assert timers.median("test1") == 4.5, "Should be 4.5"
    
    timers.add

# Generated at 2026-04-26 11:04:51.985267
# Unit test for method min of class Timers
def test_Timers_min():  
    timers = Timers()
    timers.add("test_timer", 2.0)
    timers.add("test_timer", 3.0)
    timers.add("test_timer", 1.0)
    assert timers.min("test_timer") == 1.0
    timers.add("test_timer", 0.0)
    assert timers.min("test_timer") == 0.0
    assert timers.min("non_existing_timer") == 0.0  # Change this line according to your intended behavior

test_Timers_min()  # Call the test function

# Generated at 2026-04-26 11:04:55.932826
# Unit test for method median of class Timers
def test_Timers_median(): # pragma: no cover
    timers = Timers()
    timers.add('my_timer', 10)
    timers.add('my_timer', 20)
    timers.add('my_timer', 30)

    assert timers.median('my_timer') == 20

    timers.add('my_timer', 40)
    timers.add('my_timer', 50)

    assert timers.median('my_timer') == 30

    timers.add('my_timer', 60)
    assert timers.median('my_timer') == 35

    # Test with empty timer
    try:
        timers.median('unknown_timer')
        assert False, "Expected KeyError for unknown_timer"
    except KeyError:
        pass
    # Test with single timing
    timers.add('single_timer', 10)
    assert timers.median('single_timer') == 10

# Run the unit test
test_Timers_median()
print("All tests passed.")  # pragma

# Generated at 2026-04-26 11:05:00.041493
# Unit test for method median of class Timers
def test_Timers_median(): 
    timers = Timers()
    timers.add("test_timer", 1.0)
    timers.add("test_timer", 2.0)
    timers.add("test_timer", 3.0)
    assert timers.median("test_timer") == 2.0
    timers.add("test_timer", 4.0)
    assert timers.median("test_timer") == 2.5
    timers.add("test_timer", 5.0)
    assert timers.median("test_timer") == 3.0
    try:
        timers.median("non_existent_timer")
    except KeyError:
        pass

# Run the unit test if the script is executed directly
if __name__ == "__main__":
    test_Timers_median()
    print("All tests passed.")  # pragma: no cover

# Generated at 2026-04-26 11:05:04.228501
# Unit test for method median of class Timers
def test_Timers_median(): 
    timers = Timers()
    timers.add("test_timer1", 2.0)
    timers.add("test_timer1", 4.0)
    timers.add("test_timer1", 6.0)
    
    assert timers.median("test_timer1") == 4.0, "Should be 4.0"

    timers.add("test_timer1", 8.0)
    assert timers.median("test_timer1") == 5.0, "Should be 5.0"  # New median with 4 values
    
    timers.add("test_timer1", 10.0)
    assert timers.median("test_timer1") == 6.0, "Should be 6.0"  # New median with 5 values
    
    timers.add("test_timer1", 12.0)
    assert timers.median("test_timer1") == 6.0, "Should be 6.0"

# Generated at 2026-04-26 11:05:10.979085
# Unit test for method median of class Timers
def test_Timers_median():   
    timers = Timers()
    timers.add("timer1", 1.0)
    timers.add("timer1", 2.0)
    timers.add("timer1", 3.0)
    
    assert timers.median("timer1") == 2.0, "Median should be 2.0"

    timers.add("timer1", 4.0)
    assert timers.median("timer1") == 2.5, "Median should be 2.5"

    timers.add("timer1", 5.0)
    assert timers.median("timer1") == 3.0, "Median should be 3.0"

    timers.add("timer1", 6.0)
    assert timers.median("timer1") == 3.5, "Median should be 3.5"

    timers.add("timer1", 7.0)
    assert timers.median("timer1") == 4

# Generated at 2026-04-26 11:05:15.139328
# Unit test for method max of class Timers
def test_Timers_max(): # pragma: no cover
    # Create an instance of Timers
    timers = Timers()
    
    # Add some timing values
    timers.add('test_timer', 1.5)
    timers.add('test_timer', 2.5)
    timers.add('test_timer', 3.5)
    
    # Check the max value
    assert timers.max('test_timer') == 3.5, "Max value should be 3.5"

    # Add a new value and check max again
    timers.add('test_timer', 4.0)
    assert timers.max('test_timer') == 4.0, "Max value should be 4.0"

    # Create another timer and check max on an empty timer
    timers.add('another_timer', 2.0)
    assert timers.max('another_timer') == 2.0, "Max value should be 2.0"
    
    # Test max function on

# Generated at 2026-04-26 11:05:19.118125
# Unit test for method median of class Timers
def test_Timers_median(): 
    timers = Timers()
    timers.add("test_timer", 1.0)
    timers.add("test_timer", 2.0)
    timers.add("test_timer", 3.0)
    assert timers.median("test_timer") == 2.0, "Median should be 2.0"
    timers.add("test_timer", 4.0)
    assert timers.median("test_timer") == 2.5, "Median should be 2.5"
    timers.add("test_timer", 5.0)
    timers.add("test_timer", 6.0)
    assert timers.median("test_timer") == 3.5, "Median should be 3.5"
    print("All tests passed!")

# Call the test function
test_Timers_median()

# Generated at 2026-04-26 11:05:22.101213
# Unit test for method max of class Timers
def test_Timers_max():    
    # Create a Timers instance
    timers = Timers()

    # Add some timer values
    timers.add("test_timer", 1.2)
    timers.add("test_timer", 3.4)
    timers.add("test_timer", 2.2)

    # Check the maximum value
    max_value = timers.max("test_timer")
    assert max_value == 3.4, f"Expected max value to be 3.4, got {max_value}"


# Generated at 2026-04-26 11:05:25.991023
# Unit test for method mean of class Timers
def test_Timers_mean(): 
    timers = Timers()
    timers.add("test_timer", 1.0)
    timers.add("test_timer", 3.0)
    timers.add("test_timer", 5.0)
    assert timers.mean("test_timer") == 3.0, f"Expected 3.0, got {timers.mean('test_timer')}" # mean should be 3
    timers.add("test_timer", 7.0)
    assert timers.mean("test_timer") == 4.0, f"Expected 4.0, got {timers.mean('test_timer')}" # mean should be 4
    timers.add("test_timer", 9.0)
    assert timers.mean("test_timer") == 5.0, f"Expected 5.0, got {timers.mean('test_timer')}" # mean should be 5

# Run the test
test_Timers_mean()

# Generated at 2026-04-26 11:05:29.919792
# Unit test for method median of class Timers
def test_Timers_median(): 
    timers = Timers()
    timers.add("test", 1)
    timers.add("test", 2)
    timers.add("test", 3)
    assert timers.median("test") == 2
    timers.add("test", 4)
    assert timers.median("test") == 2.5

# Running the test
test_Timers_median()
print("All tests passed!")  

# Generated at 2026-04-26 11:05:33.106840
# Unit test for method mean of class Timers
def test_Timers_mean(): 
    timers = Timers()
    timers.add('test', 1.0)
    timers.add('test', 2.0)
    timers.add('test', 3.0)
    
    assert timers.mean('test') == 2.0, "Mean should be 2.0"
    
test_Timers_mean()

# Generated at 2026-04-26 11:05:37.283937
# Unit test for method median of class Timers
def test_Timers_median(): 
    timers = Timers()
    timers.add('test', 1)
    timers.add('test', 2)
    timers.add('test', 3)
    timers.add('test', 4)
    assert timers.median('test') == 2.5, "The median should be 2.5"

    timers.clear() 
    timers.add('test', 1)
    timers.add('test', 2)
    timers.add('test', 3)
    assert timers.median('test') == 2, "The median should be 2"
    
    timers.clear() 
    timers.add('test', 1) 
    assert math.isnan(timers.median('test')), "The median should be NaN for a single input" 

    timers.clear() 
    timers.add('test', 1) 
    timers.add('test', 1) 