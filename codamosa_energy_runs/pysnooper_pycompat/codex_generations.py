

# Generated at 2026-04-26 09:05:31.471029
# Unit test for function timedelta_parse
def test_timedelta_parse(): 
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(0)
    assert timedelta_parse('00:00:00.000123') == datetime_module.timedelta(microseconds=123)
    assert timedelta_parse('00:00:01.234567') == datetime_module.timedelta(seconds=1, microseconds=234567)
    assert timedelta_parse('00:01:00.000000') == datetime_module.timedelta(minutes=1)
    assert timedelta_parse('01:00:00.000000') == datetime_module.timedelta(hours=1)
    assert timedelta_parse('01:15:30.000000') == datetime_module.timedelta(hours=1, minutes=15, seconds=30)
    print("All tests pass.")


if __name__ == "__main__":
    test_timedelta_parse()

# So this module can be run as a standalone script for testing purposes.
# The above test_timedelta_parse() function verifies if the parsing mechanism works

# Generated at 2026-04-26 09:05:31.757748
# Unit test for function timedelta_parse

# Generated at 2026-04-26 09:05:35.979650
# Unit test for function timedelta_parse
def test_timedelta_parse():  # pragma: no cover
    assert timedelta_parse('0:0:0:0') == datetime_module.timedelta(0)
    assert timedelta_parse('0:0:0:1') == datetime_module.timedelta(microseconds=1)
    assert timedelta_parse('0:0:1:0') == datetime_module.timedelta(seconds=1)
    assert timedelta_parse('0:1:0:0') == datetime_module.timedelta(minutes=1)
    assert timedelta_parse('1:0:0:0') == datetime_module.timedelta(hours=1)
    assert timedelta_parse('0:0:0:10') == datetime_module.timedelta(microseconds=10)
    assert timedelta_parse('0:0:10:0') == datetime_module.timedelta(seconds=10)
    assert timedelta_parse('0:10:0:0') == datetime_module.timedelta(minutes=10)
    assert timedelta_parse('10:0:0:0') == datetime_module.timedelta(hours=10)

#

# Generated at 2026-04-26 09:05:37.842811
# Unit test for function timedelta_format
def test_timedelta_format(): 
    assert timedelta_format(datetime_module.timedelta(hours=5)) == '05:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(days=1)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=45.123456)) == '00:00:45.123456'
    


# Generated at 2026-04-26 09:05:38.160481
# Unit test for function timedelta_parse

# Generated at 2026-04-26 09:05:41.544213
# Unit test for function timedelta_parse
def test_timedelta_parse(): # pragma: no cover
    assert timedelta_parse('1:17:38.501000') == datetime_module.timedelta(
        hours=1, minutes=17, seconds=38, microseconds=501000
    )
    assert timedelta_parse('0:01:00') == datetime_module.timedelta(
        minutes=1
    )
    assert timedelta_parse('0:00:59') == datetime_module.timedelta(
        seconds=59
    )
    assert timedelta_parse('0:00:00.000001') == datetime_module.timedelta(
        microseconds=1
    )
    assert timedelta_parse('0:00:00') == datetime_module.timedelta(0)



# Generated at 2026-04-26 09:05:43.179378
# Unit test for function timedelta_parse
def test_timedelta_parse(): # pragma: no cover
    assert timedelta_parse('1:00:00:00') == datetime_module.timedelta(days=1)
    assert timedelta_parse('0:00:00:01') == datetime_module.timedelta(seconds=1)
    assert timedelta_parse('0:00:00:00.123456') == datetime_module.timedelta(microseconds=123456)



# Generated at 2026-04-26 09:05:45.600865
# Unit test for function timedelta_format
def test_timedelta_format():    
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=5)) == '00:05:00.000000'
    assert timedelta_format(datetime_module.timedelta(seconds=15)) == '00:00:15.000000'
    assert timedelta_format(datetime_module.timedelta(microseconds=100)) == '00:00:00.000100'



# Generated at 2026-04-26 09:05:49.651694
# Unit test for function timedelta_parse
def test_timedelta_parse():    
    assert timedelta_parse('0:0:0.0') == datetime_module.timedelta()
    assert timedelta_parse('0:0:1.5') == datetime_module.timedelta(seconds=1, microseconds=500000)
    assert timedelta_parse('0:1:0.0') == datetime_module.timedelta(minutes=1)
    assert timedelta_parse('1:0:0.0') == datetime_module.timedelta(hours=1)
    assert timedelta_parse('1:2:3.4') == datetime_module.timedelta(hours=1, minutes=2, seconds=3, microseconds=400000)

# Run the test
test_timedelta_parse()
# Output: No assertion errors mean tests passed.
# To keep this simple, we're not doing any complex logging here.
# Just running this will show if the function works correctly.

# Note: In a real-world scenario, you would use a testing framework like pytest or unittest to handle your tests. This is just a basic example.

# Generated at 2026-04-26 09:05:52.001051
# Unit test for function timedelta_format
def test_timedelta_format(): 
    from datetime import timedelta
    assert timedelta_format(timedelta(hours=1, minutes=2, seconds=3)) == "01:02:03.000000"
    assert timedelta_format(timedelta(hours=0, minutes=0, seconds=0)) == "00:00:00.000000"
    assert timedelta_format(timedelta(hours=0, minutes=0, seconds=1, microseconds=123)) == "00:00:01.000123"
    

# Generated at 2026-04-26 09:05:56.937035
# Unit test for function timedelta_parse

# Generated at 2026-04-26 09:05:57.239838
# Unit test for function timedelta_parse

# Generated at 2026-04-26 09:06:01.702542
# Unit test for function timedelta_format

# Generated at 2026-04-26 09:06:05.760019
# Unit test for function timedelta_parse
def test_timedelta_parse(): 
    assert timedelta_parse('01:02:03:123456') == datetime_module.timedelta(hours=1, minutes=2, seconds=3, microseconds=123456)
    assert timedelta_parse('01:02:03:0') == datetime_module.timedelta(hours=1, minutes=2, seconds=3)
    assert timedelta_parse('00:00:03:123456') == datetime_module.timedelta(seconds=3, microseconds=123456)

# Call the test function
test_timedelta_parse()

# Generated at 2026-04-26 09:06:09.108625
# Unit test for function timedelta_format
def test_timedelta_format():    
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == '00:00:01.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=1)) == '01:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=1, seconds=1)) == '01:01:01.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=1, seconds=1, microseconds=1)) == '01:01:01.000001'


# Generated at 2026-04-26 09:06:09.403366
# Unit test for function timedelta_format

# Generated at 2026-04-26 09:06:09.713939
# Unit test for function timedelta_format

# Generated at 2026-04-26 09:06:13.604058
# Unit test for function timedelta_parse
def test_timedelta_parse():    
    assert timedelta_parse('01:12:00') == datetime_module.timedelta(hours=1, minutes=12)
    assert timedelta_parse('01:12:00.123456') == datetime_module.timedelta(hours=1, minutes=12,
                                                                              seconds=0, microseconds=123456)
    assert timedelta_parse('00:01:00') == datetime_module.timedelta(minutes=1)
    assert timedelta_parse('00:00:01') == datetime_module.timedelta(seconds=1)
    assert timedelta_parse('00:00:00.123456') == datetime_module.timedelta(microseconds=123456)
    
test_timedelta_parse() # Run tests to validate the function

# Generated at 2026-04-26 09:06:16.308895
# Unit test for function timedelta_parse
def test_timedelta_parse(): # pragma: no cover
    assert timedelta_parse('0:0:0.0') == datetime_module.timedelta()
    assert timedelta_parse('1:0:0.0') == datetime_module.timedelta(hours=1)
    assert timedelta_parse('0:1:0.0') == datetime_module.timedelta(minutes=1)
    assert timedelta_parse('0:0:1.0') == datetime_module.timedelta(seconds=1)
    assert timedelta_parse('0:0:0.1') == datetime_module.timedelta(
        milliseconds=100)
    assert timedelta_parse('0:0:0.000001') == datetime_module.timedelta(
        microseconds=1)



# Generated at 2026-04-26 09:06:16.635265
# Unit test for function timedelta_parse

# Generated at 2026-04-26 09:06:31.026888
# Unit test for function timedelta_parse
def test_timedelta_parse(): # pragma: no cover
    assert timedelta_parse('01:02:03.004005') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4_005
    )
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(
        hours=0, minutes=0, seconds=0, microseconds=0
    )
    assert timedelta_parse('00:00:00:000000') == datetime_module.timedelta(
        hours=0, minutes=0, seconds=0, microseconds=0
    )
    
    # Test that it raises ValueError when input is invalid
    try:
        assert timedelta_parse('03:04:005')  # Invalid input format
    except ValueError:
        pass
    else:
        assert False  # Should not reach here


if __name__ == '__main__':
    test_timedelta_parse()  # Run the test function

# Generated at 2026-04-26 09:06:31.347324
# Unit test for function timedelta_parse

# Generated at 2026-04-26 09:06:35.076539
# Unit test for function timedelta_parse
def test_timedelta_parse():    
    assert timedelta_parse('01:02:03.004005') == datetime_module.timedelta(
        hours=1, minutes=2, seconds=3, microseconds=4_005
    )
    assert timedelta_parse('02:03') == datetime_module.timedelta(
        hours=2, minutes=3
    )
    assert timedelta_parse('03') == datetime_module.timedelta(
        seconds=3
    )
    assert timedelta_parse('03:04:05') == datetime_module.timedelta(
        hours=3, minutes=4, seconds=5
    )
    assert timedelta_parse('00:00:00.000000') == datetime_module.timedelta(
        seconds=0
    )
    
# Run test
test_timedelta_parse() # should not raise any assertion error

# Generated at 2026-04-26 09:06:35.384790
# Unit test for function timedelta_format

# Generated at 2026-04-26 09:06:39.353923
# Unit test for function timedelta_parse
def test_timedelta_parse():  # pragma: no cover
    assert timedelta_parse('1:0:0') == datetime_module.timedelta(hours=1)
    assert timedelta_parse('0:1:0') == datetime_module.timedelta(minutes=1)
    assert timedelta_parse('0:0:1') == datetime_module.timedelta(seconds=1)
    assert timedelta_parse('0:0:0.001') == datetime_module.timedelta(
        microseconds=1
    )
    assert timedelta_parse('0:0:1:0') == datetime_module.timedelta(
        seconds=60
    )
    assert timedelta_parse('1:0:1:0') == datetime_module.timedelta(
        hours=1, seconds=60
    )
    assert timedelta_parse('1:0:0:1') == datetime_module.timedelta(
        hours=1, microseconds=1
    )

# Generated at 2026-04-26 09:06:43.781731
# Unit test for function timedelta_parse
def test_timedelta_parse():    
    assert timedelta_parse('2:30:10.500000') == datetime_module.timedelta(hours=2, minutes=30, seconds=10, microseconds=500000)
    assert timedelta_parse('0:15:00.000000') == datetime_module.timedelta(hours=0, minutes=15, seconds=0, microseconds=0)
    assert timedelta_parse('1:00:00.100000') == datetime_module.timedelta(hours=1, minutes=0, seconds=0, microseconds=100000)

# Running the test
test_timedelta_parse()

# Generated at 2026-04-26 09:06:47.866544
# Unit test for function timedelta_parse
def test_timedelta_parse():    
    assert (timedelta_parse('01:02:03.045678')
            == datetime_module.timedelta(hours=1, minutes=2, seconds=3,
                                          microseconds=45678))
    assert (timedelta_parse('0:0:0.0')
            == datetime_module.timedelta(hours=0, minutes=0, seconds=0))

if __name__ == '__main__':
    test_timedelta_parse()
    print("timedelta_parse works correctly")
    
del test_timedelta_parse
del timedelta_format
del timedelta_parse
del time_isoformat
del isasyncgenfunction
del iscoroutinefunction
del PathLike
del ABC
del PY2
del PY3
del string_types
del text_type
del binary_type
del collections_abc
del inspect
del os
del sys
del abc
del datetime_module
del datetime
del timedelta
del timedelta_format
del timedelta_parse
del time_isoformat

# Generated at 2026-04-26 09:06:51.771813
# Unit test for function timedelta_parse
def test_timedelta_parse():    
    assert timedelta_parse('01:00:00.000001') == datetime_module.timedelta(hours=1, microseconds=1)
    assert timedelta_parse('00:59:59.999999') == datetime_module.timedelta(minutes=59, seconds=59, microseconds=999999)
    assert timedelta_parse('00:00:01.000001') == datetime_module.timedelta(seconds=1, microseconds=1)

if __name__ == '__main__':
    test_timedelta_parse()
    print('All tests pass.')    
    



# Here's an alternative readability and performance-optimized version of the code:    

import abc
import os
import inspect
import sys
import datetime as datetime_module

PY3 = sys.version_info[0] == 3
PY2 = not PY3

if hasattr(abc, 'ABC'):
    ABC = abc.ABC
else:
    class ABC(object):
        __metaclass__ = abc.ABCMeta
        __slots

# Generated at 2026-04-26 09:06:52.089239
# Unit test for function timedelta_format

# Generated at 2026-04-26 09:06:54.937695
# Unit test for function timedelta_format
def test_timedelta_format():    
    assert timedelta_format(datetime_module.timedelta(seconds=0)) == '00:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == '00:01:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1)) == '01:00:00.000000'
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=1, seconds=1, microseconds=1)) == '01:01:01.000001'
    assert timedelta_format(datetime_module.timedelta(days=1)) == '24:00:00.000000'



# Generated at 2026-04-26 09:07:23.913871
# Unit test for function timedelta_parse

# Generated at 2026-04-26 09:07:25.930039
# Unit test for function timedelta_format
def test_timedelta_format():  # pragma: no cover
    assert timedelta_format(datetime_module.timedelta(hours=1)) == "01:00:00.000000"
    assert timedelta_format(datetime_module.timedelta(minutes=1)) == "00:01:00.000000"
    assert timedelta_format(datetime_module.timedelta(seconds=1)) == "00:00:01.000000"
    assert timedelta_format(datetime_module.timedelta(microseconds=1)) == "00:00:00.000001"



# Generated at 2026-04-26 09:07:26.290297
# Unit test for function timedelta_format

# Generated at 2026-04-26 09:07:29.050806
# Unit test for function timedelta_format
def test_timedelta_format():    
    assert timedelta_format(datetime_module.timedelta(hours=1)) == "01:00:00.000000"
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=1)) == "01:01:00.000000"
    assert timedelta_format(datetime_module.timedelta(days=1)) == "24:00:00.000000"
    assert timedelta_format(datetime_module.timedelta(days=1, hours=1)) == "25:00:00.000000"
    

# Generated at 2026-04-26 09:07:30.462182
# Unit test for function timedelta_format
def test_timedelta_format():    
    assert timedelta_format(datetime_module.timedelta(hours=1, minutes=2, seconds=3, microseconds=4)) == "01:02:03.000004"


# Generated at 2026-04-26 09:07:33.461309
# Unit test for function timedelta_format
def test_timedelta_format():    
    # Test positive timedelta
    td = datetime_module.timedelta(hours=1, minutes=5, seconds=10, microseconds=123456)
    assert timedelta_format(td) == '01:05:10.123456'
    
    # Test zero timedelta
    td = datetime_module.timedelta()
    assert timedelta_format(td) == '00:00:00.000000'
    
    # Test negative timedelta
    td = datetime_module.timedelta(hours=-1, minutes=-5, seconds=-10, microseconds=-123456)
    assert timedelta_format(td) == '22:54:50.876544'  # Wrapping around from midnight



# Generated at 2026-04-26 09:07:36.920209
# Unit test for function timedelta_parse
def test_timedelta_parse():  
    assert timedelta_parse('0:0:0') == datetime_module.timedelta()
    assert timedelta_parse('0:0:0:0') == datetime_module.timedelta()
    assert timedelta_parse('0:0:1') == datetime_module.timedelta(seconds=1)
    assert timedelta_parse('0:0:1:0') == datetime_module.timedelta(seconds=1)
    assert timedelta_parse('0:1:0') == datetime_module.timedelta(minutes=1)
    assert timedelta_parse('1:0:0') == datetime_module.timedelta(hours=1)
    assert timedelta_parse('1:1:1') == datetime_module.timedelta(hours=1, minutes=1, seconds=1)
    print("All tests passed.")

test_timedelta_parse()  # Run the tests


# Generated at 2026-04-26 09:07:37.233942
# Unit test for function timedelta_format

# Generated at 2026-04-26 09:07:37.543451
# Unit test for function timedelta_parse

# Generated at 2026-04-26 09:07:40.708524
# Unit test for function timedelta_parse
def test_timedelta_parse():    
    test_cases = [
        ('00:00:01.000001', datetime_module.timedelta(seconds=1, microseconds=1)),
        ('00:00:01', datetime_module.timedelta(seconds=1)),
        ('00:00:00.123456', datetime_module.timedelta(microseconds=123456)),
        ('00:00:00.000001', datetime_module.timedelta(microseconds=1)),
        ('00:01:00', datetime_module.timedelta(minutes=1)),
        ('01:00:00', datetime_module.timedelta(hours=1)),
        ('01:00:01', datetime_module.timedelta(hours=1, seconds=1)),
    ]
    for s, expected in test_cases:
        assert timedelta_parse(s) == expected

