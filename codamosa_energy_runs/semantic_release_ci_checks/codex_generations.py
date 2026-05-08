

# Generated at 2026-04-26 13:47:50.513713
# Unit test for function frigg
def test_frigg(): 
    os.environ["FRIGG_BUILD_BRANCH"] = "master" 
    os.environ["FRIGG_PULL_REQUEST"] = "" 
    try: 
        frigg("master") 
        print("Test passed") 
    except CiVerificationError: 
        print("Test failed") 
    finally: 
        del os.environ["FRIGG_BUILD_BRANCH"]
        del os.environ["FRIGG_PULL_REQUEST"]


# Generated at 2026-04-26 13:47:53.937938
# Unit test for function check
def test_check(): 
    os.environ = {
        "TRAVIS": "true",
        "TRAVIS_BRANCH": "master",
        "TRAVIS_PULL_REQUEST": "false",
    }
    assert check("master") == True

    os.environ = {
        "TRAVIS": "true",
        "TRAVIS_BRANCH": "dev",
        "TRAVIS_PULL_REQUEST": "false",
    }
    try:
        assert check("master") == True
    except CiVerificationError:
        assert True  # Expected to raise an error

    os.environ = {
        "SEMAPHORE": "true",
        "BRANCH_NAME": "master",
        "PULL_REQUEST_NUMBER": None,
        "SEMAPHORE_THREAD_RESULT": "passed",
    }
    assert check("master") == True


# Generated at 2026-04-26 13:47:58.257598
# Unit test for function frigg
def test_frigg(): 
    # Set the environment variables for the test
    os.environ["FRIGG_BUILD_BRANCH"] = "test-branch"
    os.environ["FRIGG_PULL_REQUEST"] = "false"

    # Call the frigg function with the branch to test
    try:
        frigg("test-branch")
        print("Test passed: frigg function works correctly.")
    except CiVerificationError:
        print("Test failed: frigg function did not pass.")

    # Clean up environment variables
    del os.environ["FRIGG_BUILD_BRANCH"]
    del os.environ["FRIGG_PULL_REQUEST"]

# Run the test
test_frigg()  # Expected output: Test passed: frigg function works correctly. or Test failed: frigg function did not pass.

# Generated at 2026-04-26 13:48:01.712349
# Unit test for function gitlab
def test_gitlab(): 
	# Test when the branch is correct
	os.environ['CI_COMMIT_REF_NAME'] = 'master'
	assert gitlab('master') == True
	
	# Test when the branch is incorrect
	try:
		gitlab('develop')
	except CiVerificationError:
		pass
	
	# Test when CI_COMMIT_REF_NAME is not set
	del os.environ['CI_COMMIT_REF_NAME']
	try:
		gitlab('master')
	except CiVerificationError:
		pass

# Generated at 2026-04-26 13:48:03.555944
# Unit test for function gitlab
def test_gitlab(): 
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    try:
        gitlab("master")
        print("Test passed!")
    except CiVerificationError:
        print("Test failed!")  # This will be printed if the check fails


# Generated at 2026-04-26 13:48:05.676590
# Unit test for function circle
def test_circle(): 
    # Setup: Mock the environment variables
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = ""
    
    # Execute: Call the circle function
    circle("master")  # Should not raise any exceptions as it matches

    # Cleanup: Remove the environment variables
    del os.environ["CIRCLE_BRANCH"]
    del os.environ["CI_PULL_REQUEST"]
    

# Generated at 2026-04-26 13:48:07.315693
# Unit test for function semaphore
def test_semaphore(): 
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "success"
    
    try:
        semaphore("master")
        print("Semaphore test passed")
    except CiVerificationError as e:
        print("Semaphore test failed:", e)


# Generated at 2026-04-26 13:48:11.124023
# Unit test for function travis
def test_travis():    
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    
    try:
        travis("master")
        print("travis test passed")
    except CiVerificationError:
        print("travis test failed")

    try:
        travis("develop")
        print("travis test passed")
    except CiVerificationError:
        print("travis test failed")

# Call the test function
test_travis() 

# Generated at 2026-04-26 13:48:14.678588
# Unit test for function semaphore
def test_semaphore():  
    # Prepare the environment variables
    os.environ["BRANCH_NAME"] = "test-branch"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    
    # Call the semaphore function with a test branch
    try:
        semaphore("test-branch")
        print("semaphore test passed")
    except CiVerificationError:
        print("semaphore test failed")

# Call the test function
test_semaphore()

# Generated at 2026-04-26 13:48:16.871110
# Unit test for function bitbucket
def test_bitbucket():    
    os.environ['BITBUCKET_BRANCH'] = 'master'
    os.environ['BITBUCKET_PR_ID'] = None
    try:
        bitbucket('master')
        print("Bitbucket test passed")
    except CiVerificationError:
        print("Bitbucket test failed")


# Generated at 2026-04-26 13:48:28.440316
# Unit test for function check
def test_check(): 
    """
    Unit test for the check function.
    """
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    
    check("master")  # Should not raise

    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    
    try:
        check("master")  # Should raise CiVerificationError
    except CiVerificationError:
        pass
    else:
        raise AssertionError("Expected CiVerificationError was not raised.")

    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    os.environ["TRAVIS_BRANCH"] = "develop"
    
    try:
        check("master")  # Should raise CiVerificationError
    except CiVerificationError:
        pass
    else:
        raise AssertionError("Expected CiVerificationError was not raised.")

    # Clean up the environment variables
    del os

# Generated at 2026-04-26 13:48:30.354894
# Unit test for function semaphore
def test_semaphore(): 
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "success" 
    try:
        semaphore("master")
        print("semaphore passed")
    except CiVerificationError as e:
        print("semaphore failed:", e)



# Generated at 2026-04-26 13:48:33.819030
# Unit test for function bitbucket
def test_bitbucket(): 
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""
    branch = "master"
    
    try:
        bitbucket(branch)
        print("Bitbucket test passed.")
    except CiVerificationError as e:
        print(f"Bitbucket test failed: {e}")

# Call the test function
test_bitbucket()

# Generated at 2026-04-26 13:48:36.011912
# Unit test for function circle
def test_circle(): 
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = ""
    assert circle("master") == True


# Generated at 2026-04-26 13:48:39.716623
# Unit test for function bitbucket
def test_bitbucket(): 
    os.environ['BITBUCKET_BRANCH'] = 'master'
    os.environ['BITBUCKET_PR_ID'] = None
    check('master')  # should pass

    # this should raise CiVerificationError
    try:
        check('develop')
    except CiVerificationError as e:
        assert str(e) == "The verification check for the environment did not pass."

    # this should raise CiVerificationError
    try:
        del os.environ['BITBUCKET_PR_ID']
        check('master')
    except CiVerificationError as e:
        assert str(e) == "The verification check for the environment did not pass."

    # Clean up
    del os.environ['BITBUCKET_BRANCH']

# You can use pytest to run the tests and validate the behavior
# Remember to set the environment variables before running the tests, as the checks rely on them.
# pytest will automatically discover the test functions prefixed with "test_"

# Make sure you have

# Generated at 2026-04-26 13:48:42.824310
# Unit test for function jenkins
def test_jenkins(): 
    # Test for a successful Jenkins build
    os.environ["BRANCH_NAME"] = "master"
    os.environ["JENKINS_URL"] = "http://localhost:8080"
    os.environ["CHANGE_ID"] = ""  # no pull request
    # Call the function with expected branch
    try:
        jenkins("master")
        print("Jenkins check passed.")
    except CiVerificationError as e:
        print(e)

    # Test for a failed Jenkins build (wrong branch)
    os.environ["BRANCH_NAME"] = "develop"
    try:
        jenkins("master")
    except CiVerificationError as e:
        print("Jenkins check failed as expected:", e)

    # Test for a failed Jenkins build (pull request)
    os.environ["BRANCH_NAME"] = "master"
    os.environ["CHANGE_ID"] = "123"  # simulating a pull request

# Generated at 2026-04-26 13:48:46.067699
# Unit test for function travis
def test_travis(): 
    # Test case 1: Check valid branch
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    try:
        travis("master")
        print("Test case 1 passed.")
    except CiVerificationError as e:
        print("Test case 1 failed:", e)

    # Test case 2: Check invalid branch
    os.environ["TRAVIS_BRANCH"] = "dev"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    try:
        travis("master")
        print("Test case 2 failed: No exception raised.")
    except CiVerificationError:
        print("Test case 2 passed.")

    # Test case 3: Check pull request
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "true"

# Generated at 2026-04-26 13:48:48.485783
# Unit test for function checker
def test_checker():  
    import pytest
    
    # Test with a passing function
    @checker
    def always_pass():
        return True

    assert always_pass() == True

    # Test with a failing function
    @checker
    def always_fail():
        assert False

    with pytest.raises(CiVerificationError):
        always_fail()   


# Generated at 2026-04-26 13:48:52.329885
# Unit test for function circle
def test_circle():     
    # Setting up the environment for the test
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = ""
    
    # Running the circle check with the expected branch
    try:
        circle("master")
        print("test_circle passed")
    except CiVerificationError:
        print("test_circle failed")


# Generated at 2026-04-26 13:48:55.784941
# Unit test for function check
def test_check():    
    # Test with TRAVIS environment
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check("master")  # Should pass
    
    # Test with SEMAPHORE environment
    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    check("master")  # Should pass
    
    # Test with FRIGG environment
    os.environ["FRIGG"] = "true"
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = ""
    check("master")  # Should pass
    
    # Test with CIRCLECI environment

# Generated at 2026-04-26 13:49:10.163050
# Unit test for function jenkins
def test_jenkins():  
    os.environ["JENKINS_URL"] = "https://example.com/jenkins"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["CHANGE_ID"] = ""  # Simulate a non-PR build

    try:
        jenkins("master")
        print("Jenkins check passed.")
    except CiVerificationError as e:
        print(f"Jenkins check failed: {e}")

# Running the test
if __name__ == "__main__":
    test_jenkins()

# Generated at 2026-04-26 13:49:13.696295
# Unit test for function gitlab
def test_gitlab(): 
    """
    Test the gitlab checker function
    """

    # Set environment variables for testing
    os.environ["CI_COMMIT_REF_NAME"] = "master"  # Expected branch
    os.environ["GITLAB_CI"] = "true"              # Simulating GitLab CI environment

    # Call the gitlab function with the branch name for verification
    try:
        gitlab("master")  # Should pass
        print("Test passed.")
    except CiVerificationError as e:
        print("Test failed:", str(e))

    # Test failure scenario
    try:
        gitlab("develop")  # Should fail
        print("Test failed: Expected CiVerificationError not raised.")
    except CiVerificationError as e:
        print("Test passed:", str(e))
        
    finally:
        # Clean up environment variables
        del os.environ["CI_COMMIT_REF_NAME"]
        del os.environ["GITLAB_CI"]

# Running the

# Generated at 2026-04-26 13:49:17.425476
# Unit test for function checker
def test_checker():  
    # Test a function that returns True
    @checker
    def always_pass():
        return True

    assert always_pass() == True

    # Test a function that raises AssertionError
    try:
        @checker
        def always_fail():
            assert False
        always_fail()
    except CiVerificationError as e:
        assert str(e) == "The verification check for the environment did not pass."
    else:
        assert False, "Expected CiVerificationError was not raised."

test_checker()  # Run the test for the checker function

# Generated at 2026-04-26 13:49:22.167725
# Unit test for function gitlab
def test_gitlab():    
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    gitlab("master")  # should pass

    try:
        gitlab("develop")  # should raise CiVerificationError
    except CiVerificationError:
        pass
    else:
        assert False, "Expected CiVerificationError not raised"

    # Test case where CI_COMMIT_REF_NAME is not set
    del os.environ["CI_COMMIT_REF_NAME"]
    try:
        gitlab("master")  # should raise CiVerificationError
    except CiVerificationError:
        pass
    else:
        assert False, "Expected CiVerificationError not raised"
        
    # Test case where CI_COMMIT_REF_NAME is set to a different value
    os.environ["CI_COMMIT_REF_NAME"] = "develop"
    try:
        gitlab("master")  # should raise CiVerificationError
    except CiVerificationError:
        pass

# Generated at 2026-04-26 13:49:25.048660
# Unit test for function checker
def test_checker():    
    def dummy_func():
        assert False, "Dummy assertion"
        
    try:
        checker(dummy_func)()  # Call the decorated dummy function
    except CiVerificationError as e:
        assert str(e) == "The verification check for the environment did not pass."
    else:
        assert False, "Expected CiVerificationError was not raised."


# Generated at 2026-04-26 13:49:29.352419
# Unit test for function check
def test_check():    
    os.environ["TRAVIS"] = "true"
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    check("master")  # Should pass without exceptions

    os.environ["TRAVIS_PULL_REQUEST"] = "true"
    try:
        check("master")  # Should raise CiVerificationError
    except CiVerificationError:
        pass
    else:
        assert False, "Expected CiVerificationError not raised"

    os.environ["TRAVIS_PULL_REQUEST"] = "false"  # Reset for next test

    os.environ["SEMAPHORE"] = "true"
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = None
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    check("master")  # Should pass without exceptions

    os.environ["PULL_REQUEST_NUMBER"]

# Generated at 2026-04-26 13:49:33.405770
# Unit test for function checker
def test_checker():    
    # Test if the checker decorator raises CiVerificationError on AssertionError
    @checker
    def test_func():
        assert False  # This assertion will fail

    try:
        test_func()
    except CiVerificationError as e:
        assert str(e) == "The verification check for the environment did not pass."
    else:
        assert False, "Expected CiVerificationError was not raised"

    # Test if the checker decorator does not raise an error when the assertion passes
    @checker
    def test_func_pass():
        assert True  # This assertion will pass

    # This should not raise an error
    test_func_pass()  

# Run unit tests
if __name__ == "__main__":
    test_checker()
    print("All tests passed!")  

# Generated at 2026-04-26 13:49:36.406360
# Unit test for function gitlab
def test_gitlab(): 
    """
    This is a unit test for the gitlab function.
    """
    # Set the environment variables for gitlab
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    
    # Call the function with the branch name
    try:
        gitlab("master")
        print("gitlab test passed")
    except CiVerificationError as e:
        print(f"gitlab test failed: {e}")

    # Test with a different branch
    try:
        gitlab("develop")
        print("gitlab test failed: should have raised an error")
    except CiVerificationError as e:
        print(f"gitlab test passed: {e}")

    del os.environ["CI_COMMIT_REF_NAME"]  # Clean up the environment variable

# Run the test
if __name__ == "__main__":
    test_gitlab()  # This will run the test for the gitlab function

# Generated at 2026-04-26 13:49:40.348904
# Unit test for function bitbucket
def test_bitbucket(): 
    """Unit test for function bitbucket"""
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""
    try: 
        bitbucket("master")
        print("bitbucket test passed")
    except CiVerificationError as e: 
        print(f"bitbucket test failed: {e}")

# Call the test
test_bitbucket()  # This will test the bitbucket function

# Generated at 2026-04-26 13:49:42.798907
# Unit test for function travis
def test_travis():     
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    
    try:
        travis("master")
        print("test_travis passed")
    except CiVerificationError as e:
        print("test_travis failed:", e)


# Generated at 2026-04-26 13:49:55.774129
# Unit test for function checker
def test_checker(): 
    # Test case 1: Successful execution
    @checker
    def successful_function():
        assert True  # This should pass

    try:
        successful_function()
        print("Test case 1 passed: successful_function executed successfully.")
    except CiVerificationError:
        print("Test case 1 failed: successful_function raised CiVerificationError.")

    # Test case 2: Assertion failure
    @checker
    def failing_function():
        assert False  # This should fail

    try:
        failing_function()
        print("Test case 2 failed: failing_function executed successfully.")  # This should not be reached
    except CiVerificationError:
        print("Test case 2 passed: failing_function raised CiVerificationError.")

# Call the test function
test_checker()

# Generated at 2026-04-26 13:49:58.430416
# Unit test for function jenkins
def test_jenkins(): 
    os.environ['BRANCH_NAME'] = 'master'
    os.environ['JENKINS_URL'] = 'http://example.com/'
    os.environ['CHANGE_ID'] = ''
    
    try: 
      jenkins('master')
      print("test_jenkins passed")
    except CiVerificationError: 
      print("test_jenkins failed")
    
    os.environ['BRANCH_NAME'] = 'develop'
    try: 
      jenkins('master')
      print("test_jenkins failed") 
    except CiVerificationError: 
      print("test_jenkins passed") 

if __name__ == '__main__':
    test_jenkins()


# Generated at 2026-04-26 13:50:00.265678
# Unit test for function circle
def test_circle(): 
    os.environ["CIRCLE_BRANCH"] = "master" 
    os.environ["CI_PULL_REQUEST"] = "" 
    try: 
        circle("master") 
        print("circle test passed") 
    except CiVerificationError: 
        print("circle test failed") 


# Generated at 2026-04-26 13:50:04.412060
# Unit test for function gitlab
def test_gitlab(): 
    os.environ["CI_COMMIT_REF_NAME"] = 'master'  
    assert gitlab('master') == True  # should pass

    os.environ["CI_COMMIT_REF_NAME"] = 'develop'  
    try: 
        gitlab('master')  # should raise CiVerificationError
    except CiVerificationError as e: 
        assert str(e) == "The verification check for the environment did not pass."

    os.environ.pop("CI_COMMIT_REF_NAME")  # cleanup
    try: 
        gitlab('master')  # should raise CiVerificationError
    except CiVerificationError as e: 
        assert str(e) == "The verification check for the environment did not pass."

# Run the test for gitlab
test_gitlab()

# Generated at 2026-04-26 13:50:06.278455
# Unit test for function gitlab
def test_gitlab():  
    os.environ["CI_COMMIT_REF_NAME"] = "master"
    assert gitlab("master") == True

    os.environ["CI_COMMIT_REF_NAME"] = "develop"
    try:
        gitlab("master")
    except CiVerificationError as e:
        assert str(e) == "The verification check for the environment did not pass."
        

# Generated at 2026-04-26 13:50:07.962626
# Unit test for function travis
def test_travis(): 
    os.environ["TRAVIS_BRANCH"] = "master"
    os.environ["TRAVIS_PULL_REQUEST"] = "false"
    try: 
        travis("master")
        print("Test passed.")
    except CiVerificationError as e: 
        print(e)


# Generated at 2026-04-26 13:50:10.005359
# Unit test for function semaphore
def test_semaphore(): 
    os.environ["BRANCH_NAME"] = "master"
    os.environ["PULL_REQUEST_NUMBER"] = "None"
    os.environ["SEMAPHORE_THREAD_RESULT"] = "passed"
    try:
        semaphore("master")
        print("semaphore test passed")
    except CiVerificationError as e:
        print(f"semaphore test failed: {e}")


# Generated at 2026-04-26 13:50:11.251401
# Unit test for function circle
def test_circle(): 
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = ""
    assert circle("master") == True  # Test should pass


# Generated at 2026-04-26 13:50:15.152853
# Unit test for function bitbucket
def test_bitbucket(): 
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""
    
    # Should not raise an error
    try:
        bitbucket("master")
        print("Bitbucket test passed.")
    except CiVerificationError:
        print("Bitbucket test failed.")


# Generated at 2026-04-26 13:50:18.190069
# Unit test for function frigg
def test_frigg():          
    os.environ["FRIGG_BUILD_BRANCH"] = "master"
    os.environ["FRIGG_PULL_REQUEST"] = ""
    frigg("master")  # should not raise
    try:
        frigg("develop")  # should raise CiVerificationError
    except CiVerificationError:
        pass
    else:
        raise AssertionError("Expected CiVerificationError not raised")
    

# Generated at 2026-04-26 13:50:39.298353
# Unit test for function frigg
def test_frigg(): 
    os.environ["FRIGG_BUILD_BRANCH"] = "test_branch"
    os.environ["FRIGG_PULL_REQUEST"] = "false"
    
    # Should not raise an error
    try:
        frigg("test_branch")
        print("frigg passed")
    except CiVerificationError:
        print("frigg failed")
    
    # Should raise an error
    try:
        frigg("wrong_branch")
        print("frigg failed, but it should have passed")
    except CiVerificationError:
        print("frigg raised an error as expected")
        
# Run the test
test_frigg()  # This will print the result of the test for function frigg.

# Generated at 2026-04-26 13:50:43.789441
# Unit test for function bitbucket
def test_bitbucket(): 
    # Setup the environment for the test
    os.environ["BITBUCKET_BRANCH"] = "master"
    os.environ["BITBUCKET_PR_ID"] = ""
    
    # Call the function with the expected branch
    try: 
        bitbucket("master")  # should pass
        print("Bitbucket test passed.")
    except CiVerificationError as e: 
        print(f"CiVerificationError: {e}")
    
    # Call the function with a different branch
    try: 
        bitbucket("develop")  # should fail
        print("Bitbucket test failed.")
    except CiVerificationError as e: 
        print(f"CiVerificationError: {e}")

# Run the test for bitbucket
test_bitbucket()  # Call the test function to run the tests

# Generated at 2026-04-26 13:50:47.367773
# Unit test for function circle
def test_circle(): 
    # Set the required environment variables
    os.environ["CIRCLE_BRANCH"] = "master"
    os.environ["CI_PULL_REQUEST"] = "false"

    # Call the function with the branch name
    assert circle("master") == True  # Should pass

    # Now test with an incorrect branch name
    try:
        circle("develop")  # Should raise CiVerificationError
        assert False  # Should not reach this line
    except CiVerificationError:
        pass  # Expected behavior

    # Now test with a pull request
    os.environ["CI_PULL_REQUEST"] = "true"
    try:
        circle("master")  # Should raise CiVerificationError
        assert False  # Should not reach this line
    except CiVerificationError:
        pass  # Expected behavior

    # Clean up
    del os.environ["CIRCLE_BRANCH"]
    del os.environ["CI_PULL_REQUEST"]


# Run the test
test_circle()
print