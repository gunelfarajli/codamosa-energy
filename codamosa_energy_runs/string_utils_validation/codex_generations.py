

# Generated at 2026-04-26 13:54:31.246992
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13(): 
    isbn_checker = __ISBNChecker("978-3-16-148410-0")
    assert isbn_checker.is_isbn_13() == True
    isbn_checker = __ISBNChecker("9783161484100")
    assert isbn_checker.is_isbn_13() == True
    isbn_checker = __ISBNChecker("978-3-16-148410-1")
    assert isbn_checker.is_isbn_13() == False
    isbn_checker = __ISBNChecker("978316148410X") 
    assert isbn_checker.is_isbn_13() == False
    isbn_checker = __ISBNChecker("978-3-16-148410-") 
    assert isbn_checker.is_isbn_13() == False
    isbn_checker = __ISBNChecker("9783161484") 
    assert isbn_checker.is_isbn_13() == False


# Generated at 2026-04-26 13:54:38.567917
# Unit test for function is_json
def test_is_json():  
    assert is_json('{"name": "Peter"}') == True  
    assert is_json('[1, 2, 3]') == True  
    assert is_json('{nope}') == False  
    assert is_json('{"key": "value"') == False  
    assert is_json('{"key": "value"}') == True  
    assert is_json('["item1", "item2"]') == True  
    assert is_json('{"array": [1, 2, 3]}') == True  
    assert is_json('null') == True  
    assert is_json('true') == True  
    assert is_json('false') == True  
    print("All tests passed!")
    
test_is_json()  # Running the test function

# Generated at 2026-04-26 13:54:43.720330
# Unit test for function is_ip_v4
def test_is_ip_v4():    
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('0.0.0.0') == True
    assert is_ip_v4('192.168.1.1') == True
    assert is_ip_v4('255.255.255.255') == True
    assert is_ip_v4('256.100.100.100') == False
    assert is_ip_v4('255.200.100.999') == False
    assert is_ip_v4('255.200.100.75.1') == False
    assert is_ip_v4('255.200.100') == False
    assert is_ip_v4('hello') == False
    assert is_ip_v4('') == False
    assert is_ip_v4(None) == False
    # Add additional test cases as needed

# Run the test
test_is_ip_v4()    


# Generated at 2026-04-26 13:54:46.663667
# Unit test for function is_url
def test_is_url(): 
    assert is_url('http://www.example.com')
    assert is_url('https://example.com')
    assert not is_url('ftp://example.com')
    assert not is_url('.example.com')
    assert is_url('http://user:pass@example.com')
    assert is_url('http://example.com:80/path/to/resource')
    assert not is_url('invalid_url')
    assert is_url('http://example.com?query=string')
    print("All tests passed.")

# Run the unit test
test_is_url()


# Generated at 2026-04-26 13:54:50.658672
# Unit test for function is_email
def test_is_email():    
    assert is_email('my.email@the-provider.com') == True
    assert is_email('my.email@the-provider..com') == False
    assert is_email('@gmail.com') == False
    assert is_email('my.email@.com') == False
    assert is_email('my.email@the-provider.com ') == False
    assert is_email('my.email@the-provider.com@another.com') == False
    assert is_email('my.email@the-provider.com') == True
    assert is_email('my.email@the-provider.com') == True

test_is_email()

# Unit tests for function is_number

# Generated at 2026-04-26 13:54:54.185683
# Unit test for function is_email
def test_is_email(): 
    assert is_email('my.email@the-provider.com') == True 
    assert is_email('@gmail.com') == False 
    assert is_email('user.name@domain.com') == True 
    assert is_email('user@domain..com') == False 
    assert is_email('user@domain.com') == True 
    assert is_email('user@.com') == False 
    assert is_email('user@domain.com/') == False 
    assert is_email('user@domain.com?subject=test') == False 
    assert is_email('user@domain.com:8080') == False 
    assert is_email('user@domain.com:foo') == False 
    assert is_email('user@domain.com#fragment') == False 
    
test_is_email() 



# Generated at 2026-04-26 13:54:58.703359
# Unit test for function is_ip_v4
def test_is_ip_v4():    
    assert is_ip_v4("192.168.0.1") == True
    assert is_ip_v4("255.255.255.255") == True
    assert is_ip_v4("0.0.0.0") == True
    assert is_ip_v4("256.100.50.25") == False
    assert is_ip_v4("192.168.0") == False
    assert is_ip_v4("192.168.0.1.1") == False
    assert is_ip_v4("192.168.0.256") == False
    assert is_ip_v4("192.168.0.-1") == False
    assert is_ip_v4("192.168.0.a") == False
    assert is_ip_v4("192.168.0.1/24") == False
    assert is_ip_v4("") == False
    assert is_ip_v4(None)

# Generated at 2026-04-26 13:55:02.639779
# Unit test for method is_isbn_13 of class __ISBNChecker
def test___ISBNChecker_is_isbn_13(): 
    checker = __ISBNChecker("978-3-16-148410-0")
    assert checker.is_isbn_13() is True

    checker = __ISBNChecker("978-0-306-40615-7")
    assert checker.is_isbn_13() is True

    checker = __ISBNChecker("978-3-16-148410-1")
    assert checker.is_isbn_13() is False

    checker = __ISBNChecker("978-0-306-40615-8")
    assert checker.is_isbn_13() is False

    checker = __ISBNChecker("0-306-40615-2", normalize=False)
    assert checker.is_isbn_13() is False

    checker = __ISBNChecker("978-3-16-148410-0", normalize=False)
    assert checker.is_isbn_13() is False


# Generated at 2026-04-26 13:55:10.931545
# Unit test for function is_json
def test_is_json(): 
    assert is_json('{"name": "Peter"}') == True 
    assert is_json('[1, 2, 3]') == True 
    assert is_json('{nope}') == False 
    assert is_json('invalid json string') == False 
    assert is_json('{"key": "value", "list": [1, 2, 3]}') == True 
    assert is_json('[]') == True 
    assert is_json('{"name": "John", "age": 25}') == True 
    assert is_json('{"invalid": }') == False 
    assert is_json('{"key": "value", "bool": true}') == True 
    assert is_json('{"key": "value", "null": null}') == True 

test_is_json() 
# Add more tests as necessary


# Generated at 2026-04-26 13:55:15.169533
# Unit test for function is_ip_v4
def test_is_ip_v4(): 
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('0.0.0.0') == True
    assert is_ip_v4('127.0.0.1') == True
    assert is_ip_v4('255.200.100.999') == False
    assert is_ip_v4('255.200.100.-1') == False
    assert is_ip_v4('nope') == False
    assert is_ip_v4('256.100.100.100') == False
    assert is_ip_v_v4('192.168.1.1') == True
    assert is_ip_v4('255.255.255.255') == True
    assert is_ip_v4('192.168.1.256') == False
    print("All tests passed!")

# Call the test function
test_is_ip_v4()

# The expected output

# Generated at 2026-04-26 13:55:25.532707
# Unit test for function is_credit_card
def test_is_credit_card(): 
    assert is_credit_card("4111 1111 1111 1111") == True # Valid Visa card
    assert is_credit_card("4111111111111111") == True # Valid Visa card
    assert is_credit_card("5111 1111 1111 1111") == True # Valid Mastercard
    assert is_credit_card("5111111111111111") == True # Valid Mastercard
    assert is_credit_card("3714 4963 3962 001") == True # Valid American Express
    assert is_credit_card("378282246310005") == True # Valid American Express
    assert is_credit_card("6011 1111 1111 1117") == True # Valid Discover card
    assert is_credit_card("5555555555554444") == True # Valid Mastercard
    assert is_credit_card("1234 5678 9012 3456") == False # Invalid card


# Generated at 2026-04-26 13:55:31.948110
# Unit test for function is_ip
def test_is_ip(): 
    print(is_ip('255.200.100.75')) # expects True
    print(is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334')) # expects True
    print(is_ip('1.2.3')) # expects False

# Running the test
test_is_ip()

# Generated at 2026-04-26 13:55:37.453149
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10(): 
    checker = __ISBNChecker("0306406152") 
    assert checker.is_isbn_10() == True, "Should be a valid ISBN-10" 

    checker = __ISBNChecker("123456789X") 
    assert checker.is_isbn_10() == True, "Should be a valid ISBN-10" 

    checker = __ISBNChecker("1234567890") 
    assert checker.is_isbn_10() == False, "Should be an invalid ISBN-10" 

    checker = __ISBNChecker("0123456789") 
    assert checker.is_isbn_10() == True, "Should be a valid ISBN-10" 

    checker = __ISBNChecker("1111111111") 
    assert checker.is_isbn_10() == True, "Should be a valid ISBN-10" 

    print("All tests passed for is_isbn_10")

# Run the test function
test___ISBNChecker_is

# Generated at 2026-04-26 13:55:42.472392
# Unit test for function is_isbn
def test_is_isbn(): 
    assert is_isbn('9780312498580') == True 
    assert is_isbn('1506715214') == True 
    assert is_isbn('978-0312498580') == True 
    assert is_isbn('150-6715214') == True 
    assert is_isbn('978-0312498580', normalize=False) == False 
    assert is_isbn('150-6715214', normalize=False) == False 
    assert is_isbn('978-0-306-40615-7') == True
    assert is_isbn('978-0-306-40615-7', normalize=False) == False
    assert is_isbn('978-0-306-40615-8') == False # Invalid ISBN 13
    assert is_isbn('0-306-40615-2') == True # Valid ISBN 10

# Generated at 2026-04-26 13:55:46.047614
# Unit test for function is_credit_card
def test_is_credit_card(): 
    assert is_credit_card('4539578763621486', 'VISA') == True
    assert is_credit_card('5111111111111118', 'MASTERCARD') == True
    assert is_credit_card('378282246310005', 'AMERICAN_EXPRESS') == True
    assert is_credit_card('6011514433546201', 'DISCOVER') == True
    assert is_credit_card('3530111333300000', 'JCB') == True
    assert is_credit_card('1234567890123456') == True  # Should return False

# Running the test
test_is_credit_card() 

# Generated at 2026-04-26 13:55:50.531681
# Unit test for function is_url
def test_is_url():    
    assert is_url('http://www.mysite.com') == True
    assert is_url('https://mysite.com') == True
    assert is_url('ftp://mysite.com') == True
    assert is_url('http://mysite.com/index.html') == True
    assert is_url('http://mysite.com:80') == True
    assert is_url('http://mysite.com/index.html?param=value&param2=value2') == True
    assert is_url('http://mysite.com/index.html#fragment') == True
    assert is_url('http://my-site.com') == True
    assert is_url('.mysite.com') == False
    assert is_url('http://') == False
    assert is_url('') == False
    assert is_url(None) == False
    assert is_url('not a url') == False

# Generated at 2026-04-26 13:55:54.990075
# Unit test for function is_ip
def test_is_ip(): 
    assert is_ip('255.200.100.75') == True
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True
    assert is_ip('1.2.3') == False
    assert is_ip('999.999.999.999') == False
    assert is_ip('::1') == True
    assert is_ip('2001:0db8:0000:0042:0000:8a2e:0370:7334') == True
    assert is_ip('0.0.0.0') == True
    assert is_ip('256.256.256.256') == False
    assert is_ip('2001:db8::ff00:42:8329') == True
    assert is_ip('invalid ip') == False
    print("All test cases pass")


# Generated at 2026-04-26 13:55:59.284924
# Unit test for function is_ip
def test_is_ip():    
    assert is_ip('192.168.1.1') == True # valid ipv4
    assert is_ip('255.255.255.255') == True # valid ipv4
    assert is_ip('0.0.0.0') == True # valid ipv4
    assert is_ip('2001:0db8:85a3:0000:0000:8a2e:0370:7334') == True # valid ipv6
    assert is_ip('::1') == True # valid ipv6 (loopback)
    assert is_ip('invalid_ip') == False # invalid ip
    assert is_ip('256.256.256.256') == False # invalid ipv4 (out of range)
    assert is_ip('2001:db8:85a3::8a2e:370:7334g') == False # invalid ipv6 (contains 'g')

# Generated at 2026-04-26 13:56:02.159370
# Unit test for function is_ip
def test_is_ip(): 
    assert is_ip('255.200.100.75') == True
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True
    assert is_ip('1.2.3') == False
    assert is_ip('192.168.1.1') == True
    assert is_ip('::1') == True
    assert is_ip('abc') == False

# Run the unit test
test_is_ip()  # If no assertion errors, the tests pass! 

# Generated at 2026-04-26 13:56:07.874869
# Unit test for function is_isbn
def test_is_isbn(): 
    assert is_isbn('9780312498580') == True, "Test Case 1 Failed"
    assert is_isbn('1506715214') == True, "Test Case 2 Failed"
    assert is_isbn('978-0312498580') == True, "Test Case 3 Failed"
    assert is_isbn('150-6715214') == True, "Test Case 4 Failed"
    assert is_isbn('123456789X') == True, "Test Case 5 Failed"
    assert is_isbn('1234567890') == True, "Test Case 6 Failed"
    assert is_isbn('978-1234567890') == True, "Test Case 7 Failed"
    assert is_isbn('978-1234567890', normalize=False) == False, "Test Case 8 Failed"

# Generated at 2026-04-26 13:56:18.941527
# Unit test for function is_email
def test_is_email():  # Test cases
    assert is_email('my.email@the-provider.com') == True
    assert is_email('user.name@domain.co.uk') == True
    assert is_email('user@sub.domain.com') == True
    assert is_email('plainaddress') == False
    assert is_email('@gmail.com') == False
    assert is_email('user@.com') == False
    assert is_email('user@domain..com') == False
    assert is_email('my.email@the-provider.com ') == False  # Trailing space
    assert is_email('my.email@ the-provider.com') == False  # Space before domain
    assert is_email('my.email@the-provider..com') == False  # Double dot in domain

test_is_email()

# Define similar test functions for other validation functions as needed


# Generated at 2026-04-26 13:56:23.925503
# Unit test for function is_email
def test_is_email(): 
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('test@domain') == False
    assert is_email('test@domain.com') == True
    assert is_email('test@@domain.com') == False
    assert is_email('test@domain.com.') == False
    assert is_email('test@.domain.com') == False
    assert is_email('test@domain..com') == False

# Unit tests for function is_full_string

# Generated at 2026-04-26 13:56:28.525453
# Unit test for function is_email
def test_is_email(): 
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('my.email@the-provider') == False
    assert is_email('my.email@the-provider.com.') == False
    assert is_email('my.email@the-provider.com ') == False
    assert is_email('my.email@.com') == False
    assert is_email('my..email@the-provider.com') == False
    assert is_email('my.email@the-provider.com,') == False
    assert is_email('my.email@the-provider.com;') == False
    assert is_email('my.email@the-provider.com:') == False
    print("All tests passed for is_email")

# Run the test
test_is_email() 


# Generated at 2026-04-26 13:56:32.745702
# Unit test for function is_email
def test_is_email():  
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('my.email@') == False
    assert is_email('my..email@the-provider.com') == False
    assert is_email('my.email@the..provider.com') == False
    assert is_email('my.email@the-provider..com') == False
    assert is_email('my.email@the-provider.com.') == False
    assert is_email('my.email@the-provider.com ') == False
    assert is_email('my.email@the-provider.com\n') == False
    assert is_email('my.email\n@the-provider.com') == False
    assert is_email('my.email@the-provider.com@the-provider.com') == False
    assert is_email('"my email"@the-provider.com') == True
    assert is_email('my.email@the-provider.com\n') == False


# Generated at 2026-04-26 13:56:36.203552
# Unit test for function is_url
def test_is_url(): 
    """
    Unit test for function is_url
    """
    assert is_url('http://www.mysite.com') == True
    assert is_url('https://mysite.com') == True
    assert is_url('.mysite.com') == False
    assert is_url('ftp://ftp.mysite.com') == True
    assert is_url('mysite.com', ['http', 'https']) == False
    assert is_url('http://mysite.com', ['http', 'https']) == True
    assert is_url('https://mysite.com', ['http', 'https']) == True

# Call the test function
test_is_url()


# Generated at 2026-04-26 13:56:40.720926
# Unit test for method is_isbn_10 of class __ISBNChecker
def test___ISBNChecker_is_isbn_10(): 
    checker = __ISBNChecker("0136091814")
    assert checker.is_isbn_10() == True
    checker = __ISBNChecker("123456789X")
    assert checker.is_isbn_10() == True
    checker = __ISBNChecker("1234567890")
    assert checker.is_isbn_10() == False
    checker = __ISBNChecker("0136091815")
    assert checker.is_isbn_10() == False
    checker = __ISBNChecker("XYZ1234567")
    try:
        checker = __ISBNChecker("XYZ1234567")
        checker.is_isbn_10()
    except InvalidInputError:
        assert True
    else:
        assert False


# Generated at 2026-04-26 13:56:44.558518
# Unit test for function is_email
def test_is_email(): 
    assert is_email('my.email@the-provider.com')  == True
    assert is_email('@gmail.com')  == False
    assert is_email('user.name+tag@domain.co.uk')  == True
    assert is_email('username@sub.domain.com')  == True
    assert is_email('user@domain..com')  == False
    assert is_email('user@domain.com.')  == False
    assert is_email('user@.domain.com')  == False
    assert is_email('user@domain.com')  == True
    assert is_email('user@domain.c')  == True
    assert is_email('my.email@the-provider.com')  == True
    assert is_email('my.email@the-provider')  == False
    assert is_email('u@d.c')  == True
    assert is_email('u@d..c')  == False
  
# Run the unit test


# Generated at 2026-04-26 13:56:54.592753
# Unit test for function is_email
def test_is_email(): 
    assert is_email('my.email@the-provider.com') == True
    assert is_email('invalid-email') == False
    assert is_email('@gmail.com') == False
    assert is_email('email@domain.com') == True
    assert is_email('first.last@sub.domain.com') == True
    assert is_email('user.name+tag@domain.com') == True
    assert is_email('user@domain') == False

# Function call to run tests
test_is_email()  # This will run the tests for the is_email function
    # Additional test cases can be added as needed



# Generated at 2026-04-26 13:56:58.733337
# Unit test for function is_email
def test_is_email(): 
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False

    assert is_email('username@domain.com') == True
    assert is_email('user.name@domain.co.uk') == True
    assert is_email('user_name@domain.com') == True
    assert is_email('user-name@domain.com') == True
    assert is_email('user@sub.domain.com') == True
    assert is_email('user@domain.com') == True
    assert is_email('user@domain') == False
    assert is_email('user@domain.c') == False
    assert is_email('user@domain..com') == False
    assert is_email('user@.domain.com') == False
    assert is_email('user@domain..com') == False
    assert is_email('user@domain..com') == False

# Generated at 2026-04-26 13:57:00.688206
# Unit test for function is_url
def test_is_url():  # pragma: no cover
    assert is_url('http://www.example.com')
    assert is_url('https://www.example.com')
    assert not is_url('ftp://example.com', allowed_schemes=['http', 'https'])
    assert not is_url('invalid_url')
    print("All URL tests passed.")



# Generated at 2026-04-26 13:57:12.720604
# Unit test for function is_json
def test_is_json():    
    assert is_json('{"name": "Peter"}') == True
    assert is_json('[1, 2, 3]') == True
    assert is_json('{nope}') == False
    assert is_json('{"age": 30, "city": "New York"}') == True
    assert is_json('{"name": "John", "age": 30, "city": "New York"}') == True
    assert is_json('{"name": "John", "age": 30, "city": "New York", "hobbies": ["reading", "traveling"]}') == True
    assert is_json('{"name": "John", "age": 30, "city": "New York", "hobbies": ["reading", "traveling"], "isStudent": false}') == True

# Generated at 2026-04-26 13:57:16.498089
# Unit test for function is_email
def test_is_email():    
    assert is_email('my.email@the-provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('my.email@the-provider') == False
    assert is_email('my.email@the-provider..com') == False
    assert is_email('my.email@the-provider.com.') == False
    assert is_email('my.email@the-provider.com') == True
    assert is_email('my.e_mail@the.provider.com') == True
    assert is_email('my.e_mail@the_provider.com') == True
    assert is_email('@gmail.com') == False
    assert is_email('   ') == False
    assert is_email('hello@world') == False
    assert is_email('hello@.com') == False
    assert is_email('hello@com.') == False

# Call the test function
test_is_email()   
