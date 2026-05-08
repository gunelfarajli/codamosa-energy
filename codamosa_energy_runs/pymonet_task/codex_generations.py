

# Generated at 2026-04-26 13:35:14.088656
# Unit test for method bind of class Task
def test_Task_bind(): 
    def task1(): 
        return Task.of(10)

    def task2(value): 
        return Task.of(value + 5)

    result = task1().bind(task2)
    result.fork(print, print)

test_Task_bind() # Expected output: 15

# Generated at 2026-04-26 13:35:16.827555
# Unit test for method map of class Task
def test_Task_map():    
    # Create a resolved Task
    task = Task.of(5)

    # Define a mapping function
    def add_ten(x):
        return x + 10

    # Apply the map method
    mapped_task = task.map(add_ten)

    # Prepare a function to test the mapped Task
    def test_mapping(resolve, reject):
        mapped_task.fork(reject, resolve)

    # Test the mapping
    result = []
    test_mapping(result.append, result.append)
    
    assert result == [15], "The mapping did not yield the expected result"


# Generated at 2026-04-26 13:35:20.635469
# Unit test for method map of class Task
def test_Task_map():    
    def sample_function(value):
        return value * 2
    
    # create a Task which resolves to 5
    task = Task.of(5)

    # apply the map function
    result_task = task.map(sample_function)

    # create a function to resolve the result
    def resolver(reject, resolve):
        result = result_task.fork(reject, resolve)
        return result

    # resolve the task
    assert resolver(lambda x: x, lambda x: x) == 10

# Run the test
test_Task_map()  # Should not raise any assertion error

# Generated at 2026-04-26 13:35:23.815277
# Unit test for method map of class Task
def test_Task_map():    
    # Test successful resolution of Task
    task = Task.of(5)

    def increment(x):
        return x + 1
    
    mapped_task = task.map(increment)
    
    def resolve(value):
        assert value == 6, f"Expected 6 but got {value}"
    
    def reject(value):
        raise AssertionError(f"Expected task to resolve but got rejection: {value}")

    mapped_task.fork(reject, resolve)


# Generated at 2026-04-26 13:35:25.952251
# Unit test for method map of class Task
def test_Task_map(): 
    task = Task.of(5)
    mapped_task = task.map(lambda x: x * 2)
    result = []
    mapped_task.fork(result.append, result.append)
    
    assert result == [10]


# Generated at 2026-04-26 13:35:32.402654
# Unit test for method map of class Task
def test_Task_map(): 
    def add_one(x): 
        return x + 1
    
    task = Task.of(5)
    mapped_task = task.map(add_one)

    def resolve(val): 
        assert val == 6, f'Expected 6, got {val}'

    mapped_task.fork(lambda err: print(err), resolve)

test_Task_map() # should not raise assertion error

# Generated at 2026-04-26 13:35:37.146709
# Unit test for method map of class Task
def test_Task_map():    
    # Task that resolves to 2
    task = Task.of(2)
    # Map function that adds 3
    mapped_task = task.map(lambda x: x + 3)

    def resolve(value):
        assert value == 5, "Expected 5"

    def reject(reason):
        raise AssertionError(f"Expected resolved, got rejection: {reason}")

    # Executing the fork method to test the map
    mapped_task.fork(reject, resolve)

test_Task_map()

# Generated at 2026-04-26 13:35:40.208650
# Unit test for method map of class Task
def test_Task_map():    
    def task_fn(reject, resolve):
        resolve(5)

    task = Task(task_fn)

    # Applying map to double the value
    doubled_task = task.map(lambda x: x * 2)

    # Collect result
    result = []

    def reject(value):
        result.append(f"rejected: {value}")

    def resolve(value):
        result.append(f"resolved: {value}")

    # Execute the task
    doubled_task.fork(reject, resolve)

    assert result == ["resolved: 10"], "Test failed: expected resolved value to be 10"


# Generated at 2026-04-26 13:35:44.194789
# Unit test for method bind of class Task
def test_Task_bind():    
    # Define a simple Task that resolves to a value
    task1 = Task.of(5)

    # Define a function that returns a new Task based on the input
    def add_ten(x):
        return Task.of(x + 10)

    # Bind the function to the task and execute
    result_task = task1.bind(add_ten)

    # Initialize the results variable
    result_value = None
    error_value = None

    # Execute the Task and capture the result

# Generated at 2026-04-26 13:35:49.364284
# Unit test for method map of class Task
def test_Task_map():  
    # Define a simple task that returns a number
    task = Task.of(5)
    
    # Use map to transform the value from 5 to 10
    mapped_task = task.map(lambda x: x * 2)
    
    # Create a function to handle the resolved value
    def handle_result(value):
        assert value == 10, f"Expected 10, but got {value}"
    
    # Execute the task and verify the result
    mapped_task.fork(lambda e: None, handle_result)

test_Task_map()  # Run the test

# Generated at 2026-04-26 13:35:54.296216
# Unit test for method map of class Task
def test_Task_map():  
    task = Task.of(3)
    result = task.map(lambda x: x * 2)
    
    def resolve(value):
        assert value == 6, f"Expected 6 but got {value}"

    def reject(value):
        assert False, f"Expected no rejection but got rejection with {value}"

    result.fork(reject, resolve)


# Generated at 2026-04-26 13:35:58.838194
# Unit test for method map of class Task
def test_Task_map():    
    def fork(_, resolve):
        resolve(5)
    
    task = Task(fork)
    
    def add_one(x):
        return x + 1
    
    new_task = task.map(add_one)
    
    def resolve(value):
        assert value == 6, f"Expected 6, but got {value}"
    
    new_task.fork(lambda _: None, resolve)

# Run unit test
test_Task_map()

# Generated at 2026-04-26 13:36:03.966351
# Unit test for method bind of class Task
def test_Task_bind():    
    # Define a function that returns a Task
    def add_one(x):
        return Task.of(x + 1)

    # Create an initial Task
    initial_task = Task.of(2)

    # Bind the add_one function to the initial Task
    result_task = initial_task.bind(add_one)

    # Create a function to resolve the Task
    def resolve_task(task):
        result = []
        task.fork(
            lambda err: result.append(f"Error: {err}"),
            lambda value: result.append(f"Success: {value}")
        )
        return result[0]

    # Assert the result of the bind operation
    assert resolve_task(result_task) == "Success: 3"

# Running the test
test_Task_bind()
print("Test passed")

# Generated at 2026-04-26 13:36:08.484561
# Unit test for method bind of class Task
def test_Task_bind():    
    def successful_task(value):
        return Task.of(value)

    def failing_task(value):
        return Task.reject(value)

    # Create a Task that resolves to 5
    task = Task.of(5)

    # Use bind to create a new Task that adds 5 to the result
    new_task = task.bind(lambda x: successful_task(x + 5))

    # Fork the new Task and check the result
    new_task.fork(
        reject=lambda x: print(f"Rejected with: {x}"),
        resolve=lambda y: print(f"Resolved with: {y}")
    )

    # Create a Task that fails
    failing_new_task = task.bind(lambda x: failing_task(x - 5))

    # Fork the failing Task and check the result
    failing_new_task.fork(
        reject=lambda x: print(f"Rejected with: {x}"),
        resolve=lambda y: print(f"Resolved with: {y}")
    )

test

# Generated at 2026-04-26 13:36:12.550647
# Unit test for method bind of class Task
def test_Task_bind():    
    # Define a task that resolves to a value
    task1 = Task.of(5)
    
    # Define a function that takes a value and returns a new Task
    def increment(value):
        return Task.of(value + 1)
    
    # Use bind to apply the function to the task
    result_task = task1.bind(increment)
    
    # Prepare variables to store the result of the fork
    result_value = None
    error_value = None
    
    # Run the task

# Generated at 2026-04-26 13:36:18.188848
# Unit test for method bind of class Task
def test_Task_bind():  
    # Setup a Task that resolves to a value
    task1 = Task.of(5)

    # Create a function that converts a value into a new Task
    def add_to_task(x):
        return Task.of(x + 10)

    # Bind the function to the task
    result_task = task1.bind(add_to_task)

    # Create a function to capture the result
    def capture_result(reject, resolve):
        result_task.fork(reject, resolve)

    # Capture the result
    result = []
    capture_result(lambda e: result.append(f"Error: {e}"), lambda v: result.append(f"Success: {v}"))

    assert result[0] == "Success: 15", f"Expected Success: 15 but got {result[0]}"

# Run the test
test_Task_bind()

# Generated at 2026-04-26 13:36:23.056105
# Unit test for method map of class Task
def test_Task_map(): 
    t = Task.of(5)
    assert t.map(lambda x: x * 2).fork(lambda x: x, lambda x: x) == 10
    assert t.map(lambda x: x + 3).fork(lambda x: x, lambda x: x) == 8
    assert t.map(lambda x: x - 1).fork(lambda x: x, lambda x: x) == 4
    assert t.map(lambda x: x / 5).fork(lambda x: x, lambda x: x) == 1.0

    task_rejected = Task.reject('Error')
    assert task_rejected.map(lambda x: x * 2).fork(lambda x: x, lambda x: x) == 'Error'

print(f"Running unit tests...")
test_Task_map()
print(f"All unit tests passed!") 

# Generated at 2026-04-26 13:36:25.602733
# Unit test for method map of class Task
def test_Task_map(): 
    task = Task.of(2)
    assert task.map(lambda x: x * 2).fork(lambda x: x, lambda y: y) == 4
    assert task.map(lambda x: x + 3).fork(lambda x: x, lambda y: y) == 5


# Generated at 2026-04-26 13:36:29.200718
# Unit test for method map of class Task
def test_Task_map(): 
    task = Task.of(5)
    result_task = task.map(lambda x: x * 2) 

    def resolve(value):
        assert value == 10, f"Expected 10, but got {value}"

    def reject(value):
        assert False, f"Expected no rejection, but got {value}"

    result_task.fork(reject, resolve)


# Generated at 2026-04-26 13:36:34.261473
# Unit test for method bind of class Task
def test_Task_bind():  
    # Initialize a Task that resolves with a value of 5
    task1 = Task.of(5)
    
    # Define a function to be used with bind that returns a new Task
    def add_one(value):
        return Task.of(value + 1)
    
    # Now, use bind to apply the add_one function to task1
    task2 = task1.bind(add_one)
    
    # To see the result, we need to call the fork method with a resolve function
    def resolve(result):
        assert result == 6, f'Expected 6, got {result}'
        print(f'Test passed! Result: {result}')
    
    # Fork the task2 to execute it
    task2.fork(lambda err: print(f'Error: {err}'), resolve)

# Run the test
test_Task_bind()

# Generated at 2026-04-26 13:36:39.081274
# Unit test for method map of class Task
def test_Task_map():    
    task = Task.of(5)
    
    assert task.map(lambda x: x + 1).fork(lambda e: e, lambda x: x) == 6
    assert task.map(lambda x: x * 2).fork(lambda e: e, lambda x: x) == 10
    assert task.map(lambda x: x - 3).fork(lambda e: e, lambda x: x) == 2


# Generated at 2026-04-26 13:36:43.526964
# Unit test for method map of class Task
def test_Task_map(): 
    # Arrange
    task = Task.of(3)

    # Act
    result_task = task.map(lambda x: x + 2)
    resolved_value = []

    # Fork the task to resolve it and collect the value
    result_task.fork(reject=lambda x: None, resolve=lambda value: resolved_value.append(value))

    # Assert
    assert resolved_value[0] == 5, f"Expected 5 but got {resolved_value[0]}"


# Generated at 2026-04-26 13:36:47.968879
# Unit test for method map of class Task
def test_Task_map():    
    task = Task.of(2)
    result_task = task.map(lambda x: x + 3)
    
    def resolve(value):
        assert value == 5, f"Expected 5, but got {value}"

    result_task.fork(lambda _: None, resolve)

test_Task_map()  # Should pass without assertion errors

# Generated at 2026-04-26 13:36:53.405526
# Unit test for method map of class Task
def test_Task_map(): 
    # Create a Task that resolves to the value 5
    task = Task.of(5)

    # Define a function to map over the Task
    def increment(x):
        return x + 1

    # Use the map method to create a new Task
    mapped_task = task.map(increment)

    # Function to resolve the Task
    def resolve(value):
        assert value == 6, f"Expected 6 but got {value}"

    # Call the fork method of the mapped Task
    mapped_task.fork(lambda _: None, resolve)

# Run the unit test
test_Task_map()

# Generated at 2026-04-26 13:37:00.046881
# Unit test for method bind of class Task
def test_Task_bind():   
    task1 = Task.of(10)
    task2 = task1.bind(lambda x: Task.of(x + 5))
    task2.fork(lambda error: print("Error:", error), lambda result: print("Success:", result))

# Running the test
test_Task_bind()  # This should output: Success: 15

# Generated at 2026-04-26 13:37:04.456959
# Unit test for method map of class Task
def test_Task_map():    
    task = Task.of(2)
    mapped_task = task.map(lambda x: x + 3)
    
    def resolve(value):        
        assert value == 5, f"Expected 5 but got {value}"
        
    mapped_task.fork(lambda _: None, resolve) # testing the resolve case
    
    rejected_task = Task.reject("error")
    mapped_rejected_task = rejected_task.map(lambda x: x + 3)

    def reject(value):        
        assert value == "error", f"Expected 'error' but got {value}"
        
    mapped_rejected_task.fork(reject, lambda _: None) # testing the reject case


# Generated at 2026-04-26 13:37:09.081376
# Unit test for method bind of class Task
def test_Task_bind(): 
    # Create a Task that resolves to a value
    task1 = Task.of(5)

    # Create a function to be used with bind
    def add_two(value):
        return Task.of(value + 2)

    # Bind the function to the Task
    result_task = task1.bind(add_two)

    # Create a function to run the Task and capture the result
    def run_task(task):
        result = None
        error = None

        def resolve(value):
            nonlocal result
            result = value

        def reject(value):
            nonlocal error
            error = value

        task.fork(reject, resolve)
        return result, error

    # Run the result Task and check the output
    result, error = run_task(result_task)
    
    assert result == 7, f"Expected 7, but got {result}"
    assert error is None, f"Expected no error, but got {error}"

# Execute

# Generated at 2026-04-26 13:37:14.308555
# Unit test for method bind of class Task
def test_Task_bind():  
    # Setup
    def successful_fn(value):
        return Task.of(value + 1)

    def failing_fn(value):
        return Task.reject("Error: " + str(value))

    # Create a successful Task
    task = Task.of(1)

    # Test successful binding
    result_task = task.bind(successful_fn)
    # Mock the fork method to test resolution
    def resolve(value):
        assert value == 2, f"Expected 2 but got {value}"
    
    result_task.fork(lambda err: print(err), resolve)

    # Create a failing Task
    task_fail = Task.of(1).bind(failing_fn)

    # Test failing binding
    result_task_fail = task_fail.bind(failing_fn)
    # Mock the fork method to test rejection
    def reject(error):
        assert error == "Error: 2", f"Expected 'Error: 2' but got {error}"


# Generated at 2026-04-26 13:37:19.114877
# Unit test for method map of class Task
def test_Task_map():  
    # Defining a sample Task
    task = Task.of(5)  

    # Applying map to increment the value by 1
    increment_task = task.map(lambda x: x + 1)
    
    # Using a promise pattern to resolve the Task
    increment_task.fork(
        lambda err: print(f'Rejected: {err}'),  # Handle rejection
        lambda res: print(f'Resolved: {res}')   # Handle resolution
    )
    
# Run the test
test_Task_map()

# Generated at 2026-04-26 13:37:25.779008
# Unit test for method bind of class Task
def test_Task_bind():    
    # success case
    task1 = Task.of(2)    
    task2 = task1.bind(lambda x: Task.of(x + 2))    
    result = task2.fork(lambda e: e, lambda v: v)    
    assert result == 4, f"Expected 4, but got {result}"
    
    # failure case
    task3 = task1.bind(lambda x: Task.reject("error"))    
    result_error = task3.fork(lambda e: e, lambda v: v)    
    assert result_error == "error", f"Expected 'error', but got {result_error}"

    print("All test cases for Task.bind have passed.")

# Run the test
test_Task_bind()

# Generated at 2026-04-26 13:37:35.372659
# Unit test for method bind of class Task
def test_Task_bind(): 
    # Create a resolved Task that contains the number 5
    task = Task.of(5)

    # Create a function that takes a number and returns a new Task resolving with the number multiplied by 2
    def multiply_by_2(x):
        return Task.of(x * 2)

    # Use bind to apply the multiply_by_2 function to the resolved value in the Task
    result_task = task.bind(multiply_by_2)

    # Create a variable to store the result from the result_task
    result_value = None

    # Fork the resulting Task and capture the resolved value

# Generated at 2026-04-26 13:37:40.623031
# Unit test for method map of class Task
def test_Task_map():    
    # create a Task that resolves to 3
    task = Task.of(3)

    # map the Task using a function that multiplies the value by 2
    result_task = task.map(lambda x: x * 2)

    # resolve the result Task
    result_task.fork(
        lambda err: print(f"Error: {err}"),
        lambda res: print(f"Success: {res}")
    )

# Run the test
test_Task_map()

# Generated at 2026-04-26 13:37:44.938706
# Unit test for method map of class Task
def test_Task_map(): 
    task = Task.of(1)
    mapped_task = task.map(lambda x: x + 1)

    def resolve(value):
        assert value == 2, f"Expected 2, but got {value}"

    def reject(value):
        assert False, f"Expected task to be resolved, but got rejection with value: {value}"

    mapped_task.fork(reject, resolve)

test_Task_map()  # should pass without asserting

# Generated at 2026-04-26 13:37:50.620386
# Unit test for method bind of class Task
def test_Task_bind():    
    task1 = Task.of(3)
    task2 = Task.of(4)
    
    # Define a simple function that wraps a Task
    def add_task(x):
        return Task.of(x + 5)

    result = task1.bind(add_task).fork(lambda x: x, lambda x: x)
    assert result == 8, f"Expected 8 but got {result}"

    result = task2.bind(add_task).fork(lambda x: x, lambda x: x)
    assert result == 9, f"Expected 9 but got {result}"

# Run the unit test
test_Task_bind()

# Generated at 2026-04-26 13:37:55.585869
# Unit test for method bind of class Task
def test_Task_bind():    
    # Define a function to be used for testing
    def task_fn(x):
        return Task.of(x + 1)

    # Create an initial Task
    initial_task = Task.of(5)

    # Use the bind method to chain tasks
    result_task = initial_task.bind(task_fn)

    # Simulate calling the task
    result = []

    def reject(value):
        result.append(f"Rejected with: {value}")

    def resolve(value):
        result.append(f"Resolved with: {value}")

    result_task.fork(reject, resolve)

    # Check the results
    assert result[0] == "Resolved with: 6", "Test failed: Expected 6"

# Run unit test
test_Task_bind()
print("Test passed!")

# Generated at 2026-04-26 13:38:02.214008
# Unit test for method bind of class Task
def test_Task_bind(): 
    # Create a Task that resolves to 5
    task = Task.of(5)

    # Create a function that takes a number and returns a new Task
    def add_task(n):
        return Task.of(n + 1)

    # Use bind to chain the tasks
    result_task = task.bind(add_task)

    # Define a way to capture the resolved value
    def resolve(value):
        print("Resolved:", value)  # Expecting 6

    # Fork the task to execute it
    result_task.fork(lambda e: print("Rejected:", e), resolve)

# Run the test
test_Task_bind()

# Generated at 2026-04-26 13:38:04.990784
# Unit test for method map of class Task
def test_Task_map(): 
    task1 = Task.of(5)
    task_mapped = task1.map(lambda x: x + 1)
    
    result = []

    def resolve(value):
        result.append(value)

    task_mapped.fork(lambda x: None, resolve)

    assert result[0] == 6, f"Expected 6 but got {result[0]}"



# Generated at 2026-04-26 13:38:07.896824
# Unit test for method map of class Task
def test_Task_map(): 
    # Arrange
    value = 42
    task = Task.of(value) # Create a resolved Task
    # Act
    mapped_task = task.map(lambda x: x + 1) # Should map the value of task
    resolved_value = []
    mapped_task.fork(lambda err: None, lambda val: resolved_value.append(val)) # Execute the task
    # Assert
    assert resolved_value[0] == 43, "Expected result value should be 43"


# Generated at 2026-04-26 13:38:12.812099
# Unit test for method bind of class Task
def test_Task_bind(): 
    def success_fn(x):
        return Task.of(x + 1)
    
    def failure_fn(x):
        return Task.reject(x)

    task = Task.of(5)
    result_task = task.bind(success_fn)
    
    def resolve(val):
        assert val == 6, f'Expected 6 but got {val}'

    result_task.fork(failure_fn, resolve)

    failed_task = Task.of(5).bind(failure_fn)

    def reject(val):
        assert val == 5, f'Expected 5 but got {val}'

    failed_task.fork(reject, resolve)

test_Task_bind()  # Run the test