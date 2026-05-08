

# Generated at 2026-04-26 11:46:18.350057
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():    
    class TestClass:
        def __init__(self, known_param: int, catch_all: CatchAll = None):
            self.known_param = known_param
            self.catch_all = catch_all or {}

    obj = TestClass(known_param=1, catch_all={'extra_param1': 'value1'})
    
    kvs = {'known_param': 1, 'catch_all': {'extra_param1': 'value1', 'extra_param2': 'value2'}}
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    
    assert result == {'known_param': 1, 'extra_param2': 'value2'}

test__CatchAllUndefinedParameters_handle_to_dict()

# Generated at 2026-04-26 11:46:22.451132
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():    
    class TestClass:
        def __init__(self, param1, param2):
            self.param1 = param1
            self.param2 = param2
    
    kvs = {'param1': 1, 'param2': 2, 'unused_param': 3}
    try:
        _RaiseUndefinedParameters.handle_from_dict(TestClass, kvs)
    except UndefinedParameterError as e:
        assert str(e) == "Received undefined initialization arguments {'unused_param': 3}"
    else:
        assert False, "Expected UndefinedParameterError was not raised."
    print("Test passed.")

# Run the unit test
test__RaiseUndefinedParameters_handle_from_dict()  # Output: Test passed.

# Generated at 2026-04-26 11:46:28.082835
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict():  
    class TestClass:
        def __init__(self, a: int, b: str):
            self.a = a
            self.b = b

    # Test case 1: all parameters are defined
    params = {'a': 1, 'b': 'test'}
    expected = {'a': 1, 'b': 'test'}
    result = _RaiseUndefinedParameters.handle_from_dict(TestClass, params)
    assert result == expected

    # Test case 2: one undefined parameter
    params = {'a': 1, 'b': 'test', 'c': 3}
    try:
        _RaiseUndefinedParameters.handle_from_dict(TestClass, params)
        assert False, "Expected UndefinedParameterError was not raised"
    except UndefinedParameterError as e:
        assert str(e) == "Received undefined initialization arguments {'c': 3}"

    # Test case 3: no parameters provided
    params = {}

# Generated at 2026-04-26 11:46:36.679466
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():        
    # Given
    class TestClass:
        def __init__(self, name: str, age: int, catch_all: CatchAll = None):
            self.name = name
            self.age = age
            self.catch_all = catch_all or {}

    # Create an instance of the _CatchAllUndefinedParameters class
    catch_all_handler = _CatchAllUndefinedParameters()
    
    # Set up a test object
    obj = TestClass(name='John', age=30, catch_all={'extra_param': 'value'})
    
    # Create a dictionary of key-value pairs to pass to handle_to_dict
    kvs = {
        'name': 'John',
        'age': 30,
        'extra_param': 'value'
    }

    # When
    result = catch_all_handler.handle_to_dict(obj, kvs)

    # Then

# Generated at 2026-04-26 11:46:44.206432
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():    
    @dataclasses.dataclass
    class Example:
        name: str
        catch_all: CatchAll = dataclasses.field(default_factory=dict)

    action = _CatchAllUndefinedParameters()
    init_function = action.create_init(Example)

    # Create an instance of Example with unknown parameters
    obj = init_function(name='Test', unknown_param='value')
    
    # Verify the catch_all field has captured the unknown parameters
    assert obj.catch_all == {'unknown_param': 'value'}

# Run the unit test
test__CatchAllUndefinedParameters_create_init()

# Generated at 2026-04-26 11:46:49.823763
# Unit test for method handle_dump of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_dump():  
    # Define a class with a CatchAll field
    @dataclasses.dataclass
    class TestClass:
        defined_field: str
        catch_all: CatchAll = dataclasses.field(default_factory=dict)

    # Create an instance of the TestClass
    instance = TestClass(defined_field="test", catch_all={"extra_key": "extra_value"})

    # Call handle_dump
    result = _CatchAllUndefinedParameters.handle_dump(instance)

    # Assert that the result contains the catch_all field
    assert result == {"extra_key": "extra_value"}

# Run the unit test
test__CatchAllUndefinedParameters_handle_dump()

# Generated at 2026-04-26 11:46:53.397354
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict(): 
    class TestClass: 
        def __init__(self, a: int, b: str): 
            pass
    
    obj = TestClass
    valid_kvs = {'a': 1, 'b': 'test'}
    invalid_kvs = {'a': 1, 'b': 'test', 'c': 3}  # extra key
    
    # Should return {'a': 1, 'b': 'test'}
    assert _RaiseUndefinedParameters.handle_from_dict(obj, valid_kvs) == valid_kvs
    
    try:
        # This should raise an UndefinedParameterError
        _RaiseUndefinedParameters.handle_from_dict(obj, invalid_kvs)
    except UndefinedParameterError as e:
        assert str(e) == "Received undefined initialization arguments {'c': 3}"

# Run the test
test__RaiseUndefinedParameters_handle_from_dict()

# Generated at 2026-04-26 11:46:58.749189
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict(): 
    from dataclasses import dataclass
    
    @dataclass
    class TestClass:
        a: int
        b: str
        
    test_dict = {'a': 1, 'b': 'test', 'c': 3}
    try:
        _RaiseUndefinedParameters.handle_from_dict(TestClass, test_dict)
    except UndefinedParameterError as e:
        assert str(e) == "Received undefined initialization arguments {'c': 3}"
    else:
        raise Exception("Expected UndefinedParameterError not raised.")
    
    # Test with no unknown parameters
    result = _RaiseUndefinedParameters.handle_from_dict(TestClass, {'a': 1, 'b': 'test'})
    assert result == {'a': 1, 'b': 'test'}

# Run the unit test
test__RaiseUndefinedParameters_handle_from_dict()

# Generated at 2026-04-26 11:47:02.077763
# Unit test for method create_init of class _UndefinedParameterAction
def test__UndefinedParameterAction_create_init():    
    class DummyClass:        
        def __init__(self, a: int, b: int):
            self.a = a
            self.b = b
    
    # Create an instance of _UndefinedParameterAction
    action = _CatchAllUndefinedParameters()

    # Get the modified __init__ method
    modified_init = action.create_init(DummyClass)
    
    # Create an instance of DummyClass using the modified __init__
    instance = DummyClass.__new__(DummyClass)  # Create an instance without calling __init__
    modified_init(instance, a=1, b=2)

    # Verify that the instance was initialized correctly
    assert instance.a == 1
    assert instance.b == 2

# Run the test
test__UndefinedParameterAction_create_init()
# If there are no assertion errors, the test passed successfully.
print("Test passed successfully.")    

# Generated at 2026-04-26 11:47:05.762519
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init():    
    @dataclasses.dataclass
    class MyClass:
        a: int
        b: int

        # Avoid the need for a `__init__`
        __init__ = _IgnoreUndefinedParameters.create_init(MyClass)

    obj = MyClass(1, 2)
    assert obj.a == 1
    assert obj.b == 2
    
    # Call with unknown argument, should not raise an exception
    obj = MyClass(1, 2, c=3)
    assert obj.a == 1
    assert obj.b == 2

# Run the unit test
test__IgnoreUndefinedParameters_create_init()

# Generated at 2026-04-26 11:47:23.170000
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict(): 
    # Create an instance of the class that has handle_to_dict defined
    action = _IgnoreUndefinedParameters()
    
    # Define the input parameters
    obj = "test_obj"
    kvs = {"key1": "value1", "key2": "value2"}
    
    # Call the method and capture the output
    output = action.handle_to_dict(obj, kvs)
    
    # Define the expected output
    expected_output = {"key1": "value1", "key2": "value2"}
    
    # Assert if the output is as expected
    assert output == expected_output, f"Expected {expected_output}, got {output}"

# Run the unit test
test__UndefinedParameterAction_handle_to_dict()

# Generated at 2026-04-26 11:47:26.272518
# Unit test for method create_init of class _IgnoreUndefinedParameters
def test__IgnoreUndefinedParameters_create_init(): 
    class TestClass:
        def __init__(self, a: int, b: int = 0):
            self.a = a
            self.b = b

    obj = TestClass
   
    init_func = _IgnoreUndefinedParameters.create_init(obj)
    
    class TestInstance:
        def __init__(self, a: int, b: int = 0):
            self.a = a
            self.b = b
 
    instance = TestInstance(a=5, c=10)
    
    init_func(instance, a=5, c=10)
    
    assert instance.a == 5
    assert instance.b == 0
  
# Run the test
test__IgnoreUndefinedParameters_create_init()

# Generated at 2026-04-26 11:47:29.882071
# Unit test for method handle_to_dict of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_handle_to_dict():    
    class TestClass:
        def __init__(self, a: int, b: int, catch_all: Optional[CatchAllVar] = None):
            self.a = a
            self.b = b
            self.catch_all = catch_all if catch_all is not None else {}

    test_obj = TestClass(a=1, b=2, catch_all={'c': 3, 'd': 4})
    params = { 'a': 1, 'b': 2, 'catch_all': {'c': 3, 'd': 4} }
    
    # This will invoke the method and should return the updated params dictionary
    result = _CatchAllUndefinedParameters.handle_to_dict(test_obj, params)

    # The result should be equal to the original params since the catch_all
    # field contains no additional undefined parameters

# Generated at 2026-04-26 11:47:32.758838
# Unit test for method handle_to_dict of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_to_dict():  
    class TestClass:
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

    obj = TestClass(1, 2, 3)
    kvs = {'a': 1, 'b': 2, 'c': 3}

    # Testing the handle_to_dict method from _UndefinedParameterAction
    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)

    assert result == {'a': 1, 'b': 2, 'c': 3}, f"Expected {{'a': 1, 'b': 2, 'c': 3}} but got {result}"



# Generated at 2026-04-26 11:47:36.966770
# Unit test for method handle_dump of class _UndefinedParameterAction
def test__UndefinedParameterAction_handle_dump(): 
    class MockClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.unknown = {"c": 3}

    mock_instance = MockClass(1, 2)
    mock_instance.unknown = {"c": 3}

    result = _CatchAllUndefinedParameters.handle_dump(mock_instance)
    assert result == {"c": 3}

test__UndefinedParameterAction_handle_dump()

# Generated at 2026-04-26 11:47:40.240235
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init():    
    @dataclasses.dataclass
    class Foo:
        x: int
        y: CatchAll  # Catch all for unknown parameters

        __init__ = _CatchAllUndefinedParameters.create_init(Foo)

    # Case 1: Initialize with known parameters only
    foo1 = Foo(x=1)
    assert foo1.x == 1
    assert foo1.y == {}

    # Case 2: Initialize with known and unknown parameters
    foo2 = Foo(x=2, z=3, w=4)
    assert foo2.x == 2
    assert foo2.y == {'z': 3, 'w': 4}

    # Case 3: Initialize with unknown parameters only
    foo3 = Foo(z=5, w=6)
    assert foo3.x is None  # x is not initialized
    assert foo3.y == {'z': 5, 'w': 6}

    # Case 

# Generated at 2026-04-26 11:47:43.473762
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict(): 
    from dataclasses import dataclass
    
    @dataclass
    class TestClass:
        a: int
        b: str
    
    # Test case: All parameters are defined
    params = {'a': 1, 'b': 'test'}
    result = _RaiseUndefinedParameters.handle_from_dict(TestClass, params)
    assert result == params  # Expecting original parameters as output
    
    # Test case: One undefined parameter
    params = {'a': 1, 'b': 'test', 'c': 3}
    try:
        _RaiseUndefinedParameters.handle_from_dict(TestClass, params)
    except UndefinedParameterError as e:
        assert str(e) == "Received undefined initialization arguments {'c': 3}"
    
    # Test case: No parameters
    params = {}
    result = _RaiseUndefinedParameters.handle_from_dict(TestClass, params)
    assert result == {}  # Expecting empty dict as output


# Run the test

# Generated at 2026-04-26 11:47:48.179349
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init(): 
    @dataclasses.dataclass
    class TestClass:
        a: int
        b: int
        c: CatchAll
        
        # Adding the original init function for the test
        def __init__(self, a: int, b: int, c: CatchAll = None):
            self.a = a
            self.b = b
            self.c = c if c else {}
        
    init_function = _CatchAllUndefinedParameters.create_init(TestClass)
    
    # Create an instance of TestClass using the new init function.
    instance = TestClass(1, 2, {'x': 3})
    
    # Check if the instance is created correctly.
    assert instance.a == 1
    assert instance.b == 2
    assert instance.c == {'x': 3}

    # Test with undefined parameters

# Generated at 2026-04-26 11:47:52.243027
# Unit test for method handle_from_dict of class _RaiseUndefinedParameters
def test__RaiseUndefinedParameters_handle_from_dict(): 
    from dataclasses import dataclass
    
    @dataclass
    class TestClass:
        a: int
        b: str
        
    # Test case 1: No unknown parameters
    known_parameters = {'a': 1, 'b': 'test'}
    result = _RaiseUndefinedParameters.handle_from_dict(TestClass, known_parameters)
    assert result == known_parameters
    
    # Test case 2: One unknown parameter
    known_parameters = {'a': 1, 'b': 'test', 'c': 'unknown'}
    try:
        _RaiseUndefinedParameters.handle_from_dict(TestClass, known_parameters)
    except UndefinedParameterError as e:
        assert str(e) == "Received undefined initialization arguments {'c': 'unknown'}"
    
    # Test case 3: Multiple unknown parameters
    known_parameters = {'a': 1, 'b': 'test', 'c': 'unknown', 'd': 'another_unknown'}

# Generated at 2026-04-26 11:47:56.934486
# Unit test for method create_init of class _CatchAllUndefinedParameters
def test__CatchAllUndefinedParameters_create_init(): 
    # Define a dummy class to test
    @dataclasses.dataclass
    class TestClass:
        a: int
        b: CatchAllVar = None
    
    # Create an instance of the class
    instance = TestClass(1, {'c': 3, 'd': 4})
    
    # Check if the catch-all field has captured the extra parameters
    assert instance.b == {'c': 3, 'd': 4}
    
    # Check if the known parameters were correctly assigned
    assert instance.a == 1
