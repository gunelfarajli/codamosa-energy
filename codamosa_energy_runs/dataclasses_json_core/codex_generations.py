

# Generated at 2026-04-26 11:35:12.582251
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder(): 
    encoder = _ExtendedEncoder()  # Constructor test
    assert encoder is not None  # Ensure the encoder is instantiated


# Generated at 2026-04-26 11:35:16.625551
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default(): 
    encoder = _ExtendedEncoder()

    # Test with a Collection (list)
    list_input = [1, 2, 3]
    assert encoder.default(list_input) == list_input

    # Test with a Collection (dict)
    dict_input = {'key': 'value'}
    assert encoder.default(dict_input) == dict_input

    # Test with a datetime
    datetime_input = datetime(2021, 1, 1, tzinfo=timezone.utc)
    assert encoder.default(datetime_input) == datetime_input.timestamp()

    # Test with a UUID
    from uuid import uuid4
    uuid_input = uuid4()
    assert encoder.default(uuid_input) == str(uuid_input)

    # Test with an Enum
    class TestEnum(Enum):
        VALUE1 = 'value1'
        VALUE2 = 'value2'

    enum_input = TestEnum.VALUE1
    assert encoder.default(enum_input) == enum_input.value

    # Test with a Decimal

# Generated at 2026-04-26 11:35:20.439030
# Unit test for method default of class _ExtendedEncoder
def test__ExtendedEncoder_default():    
    # Create an instance of _ExtendedEncoder
    encoder = _ExtendedEncoder()
    
    # Test with a dictionary (Mapping)
    mapping = {'key1': 'value1', 'key2': 'value2'}
    assert encoder.default(mapping) == mapping
    
    # Test with a list (Collection)
    collection = [1, 2, 3, 4, 5]
    assert encoder.default(collection) == collection
    
    # Test with a datetime object
    dt = datetime(2022, 1, 1, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()
    
    # Test with a UUID object
    from uuid import uuid4
    uid = uuid4()
    assert encoder.default(uid) == str(uid)
    
    # Test with an Enum object
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    
    color = Color.RED


# Generated at 2026-04-26 11:35:24.294290
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    
    encoder = _ExtendedEncoder()
    assert encoder.default(datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)) == 1577836800.0
    assert encoder.default(UUID('12345678-1234-5678-1234-567812345678')) == '12345678-1234-5678-1234-567812345678'
    assert encoder.default(Enum('TestEnum', 'A B C')) == 'A'  # Assuming 'A' is the default value
    assert encoder.default(Decimal('10.5')) == '10.5'
    assert encoder.default([]) == []
    assert encoder.default({}) == {}
    
test__ExtendedEncoder()

# Generated at 2026-04-26 11:35:27.754571
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder(): 
    encoder = _ExtendedEncoder()
    assert encoder.default(datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone.utc)) == 1609516800.0
    assert encoder.default(UUID("12345678123456781234567812345678")) == "12345678-1234-5678-1234-567812345678"
    assert encoder.default(EnumExample.VALUE1) == "value1"
    assert encoder.default(Decimal('12.34')) == "12.34"
    assert encoder.default({'key': 'value'}) == {'key': 'value'}
    assert encoder.default(['item1', 'item2']) == ['item1', 'item2']
    assert encoder.default(123) == 123
    assert encoder.default(3.14) == 3.14
    assert encoder.default(True) == True
    assert encoder.default(None) == None


# Generated at 2026-04-26 11:35:31.650106
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():   
    encoder = _ExtendedEncoder()
    assert isinstance(encoder, json.JSONEncoder), "Encoder should be an instance of json.JSONEncoder"
    assert encoder.default(datetime.now()) is not None, "Datetime should be encoded"
    assert encoder.default(UUID('12345678123456781234567812345678')) is not None, "UUID should be encoded"
    assert encoder.default(Enum('TestEnum', 'A B')) is not None, "Enum should be encoded"
    assert encoder.default(Decimal('10.5')) is not None, "Decimal should be encoded"
    assert encoder.default({"key": "value"}) is not None, "Dictionary should be encoded"
    assert encoder.default(["value1", "value2"]) is not None, "List should be encoded"

# Generated at 2026-04-26 11:35:34.985564
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder(): 
    encoder = _ExtendedEncoder()
    assert isinstance(encoder, json.JSONEncoder), "Encoder is not an instance of JSONEncoder"
    assert encoder.default("test") == json.JSONEncoder.default(encoder, "test"), "Default method did not return expected result for string input"
    assert encoder.default(1) == json.JSONEncoder.default(encoder, 1), "Default method did not return expected result for integer input"
    assert encoder.default(1.0) == json.JSONEncoder.default(encoder, 1.0), "Default method did not return expected result for float input"
    assert encoder.default(True) == json.JSONEncoder.default(encoder, True), "Default method did not return expected result for boolean input"



# Generated at 2026-04-26 11:35:35.936115
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder(): 
    encoder = _ExtendedEncoder()
    assert isinstance(encoder, json.JSONEncoder)


# Generated at 2026-04-26 11:35:39.597017
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder(): 
    encoder = _ExtendedEncoder()
    
    # Test with a list
    result = encoder.default([1, 2, 3])
    assert result == [1, 2, 3], "Should return the same list"
    
    # Test with a dict
    result = encoder.default({'a': 1, 'b': 2})
    assert result == {'a': 1, 'b': 2}, "Should return the same dict"
    
    # Test with a datetime
    dt = datetime(2021, 1, 1, 12, 0, 0)
    result = encoder.default(dt)
    assert result == dt.timestamp(), "Should return the timestamp of the datetime"
    
    # Test with a UUID
    test_uuid = UUID('12345678-1234-5678-1234-567812345678')
    result = encoder.default(test_uuid)

# Generated at 2026-04-26 11:35:43.168660
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():   
    assert _ExtendedEncoder().default(1) == 1
    assert _ExtendedEncoder().default("test") == "test"
    assert _ExtendedEncoder().default([1, 2, 3]) == [1, 2, 3]
    assert _ExtendedEncoder().default({"key": "value"}) == {"key": "value"}
    assert _ExtendedEncoder().default(datetime(2022, 1, 1)) == 1640995200.0
    assert _ExtendedEncoder().default(UUID("123e4567-e89b-12d3-a456-426614174000")) == "123e4567-e89b-12d3-a456-426614174000"
    assert _ExtendedEncoder().default(Enum('TestEnum', 'A B C')(1)) == 1
    assert _ExtendedEncoder().default(Decimal('5.67')) == '5.67'



# Generated at 2026-04-26 11:36:03.513835
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():   
    encoder = _ExtendedEncoder()
    assert encoder is not None


# Generated at 2026-04-26 11:36:06.962143
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    
    encoder = _ExtendedEncoder()
    assert encoder.default(Decimal('10.5')) == '10.5'
    assert encoder.default(datetime(2021, 1, 1, 1, 1, 1)) == datetime(2021, 1, 1, 1, 1, 1).timestamp()
    assert encoder.default(UUID('12345678-1234-5678-1234-567812345678')) == '12345678-1234-5678-1234-567812345678'
    assert encoder.default(Enum('TestEnum', 'Value1 Value2', type=str).Value1) == 'Value1'
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default({'key': 'value'}) == {'key': 'value'}
    assert encoder.default("string") == "string"
    assert encoder.default(42)

# Generated at 2026-04-26 11:36:09.765869
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder(): 
    encoder = _ExtendedEncoder()
    assert isinstance(encoder, json.JSONEncoder)
    assert encoder.default([]) == []
    assert encoder.default({}) == {}
    assert encoder.default(datetime.now()) is not None
    assert encoder.default(UUID('12345678-1234-5678-1234-567812345678')) == '12345678-1234-5678-1234-567812345678'
    assert encoder.default(Enum('TestEnum', 'FOO BAR').FOO) == 'FOO'
    assert encoder.default(Decimal('10.5')) == '10.5'


# Generated at 2026-04-26 11:36:14.178295
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():     
    encoder = _ExtendedEncoder()

    assert encoder.default("test_string") == "test_string"
    assert encoder.default(1) == 1
    assert encoder.default(1.1) == 1.1
    assert encoder.default(True) is True
    assert encoder.default(None) is None
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default({"key": "value"}) == {"key": "value"}

    from datetime import datetime
    dt = datetime(2021, 1, 1, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    from uuid import uuid4
    uid = uuid4()
    assert encoder.default(uid) == str(uid)

    from enum import Enum
    class TestEnum(Enum):
        A = 1
        B = 2

    assert encoder.default(TestEnum.A) == 1



# Generated at 2026-04-26 11:36:18.300425
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    
    assert _ExtendedEncoder().default([1, 2, 3]) == [1, 2, 3]
    assert _ExtendedEncoder().default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    assert _ExtendedEncoder().default(datetime(2022, 1, 1, 0, 0, 0, tzinfo=timezone.utc)) == 1640995200.0
    assert _ExtendedEncoder().default(UUID('12345678-1234-5678-1234-567812345678')) == '12345678-1234-5678-1234-567812345678'
    assert _ExtendedEncoder().default(Enum('TestEnum', 'value1 value2')) == 'value1'
    assert _ExtendedEncoder().default(Decimal('10.5')) == '10.5'
    assert _ExtendedEncoder().default(None)

# Generated at 2026-04-26 11:36:21.957129
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():     
    encoder = _ExtendedEncoder()
    assert encoder.default(123) == 123
    assert encoder.default("test") == "test"
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default({"key": "value"}) == {"key": "value"}
    assert encoder.default(datetime(2020, 1, 1)) == 1577836800.0
    assert encoder.default(UUID("12345678-1234-5678-1234-567812345678")) == "12345678-1234-5678-1234-567812345678"
    assert encoder.default(EnumExample.VALUE1) == "value1"
    assert encoder.default(Decimal("10.5")) == "10.5"  # Assuming Decimal is to be converted to string
    assert encoder.default(None) == None


# Generated at 2026-04-26 11:36:26.853295
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder(): 
    encoder = _ExtendedEncoder()
    assert isinstance(encoder, _ExtendedEncoder)  # Check if instance is created
    assert encoder.default(123) == 123  # Test integer
    assert encoder.default("test") == "test"  # Test string
    assert encoder.default([1, 2, 3]) == [1, 2, 3]  # Test list
    assert encoder.default({"key": "value"}) == {"key": "value"}  # Test dictionary
    assert encoder.default(datetime(2021, 1, 1, 0, 0, 0)) == 1609459200.0  # Test datetime to timestamp
    assert encoder.default(UUID("12345678-1234-5678-1234-567812345678")) == "12345678-1234-5678-1234-567812345678"  # Test UUID

# Generated at 2026-04-26 11:36:30.499104
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder(): 
    encoder = _ExtendedEncoder()
    assert encoder is not None

    # Test for default method with collection
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test for default method with datetime
    dt = datetime(2023, 3, 14, 15, 9, 26, tzinfo=timezone.utc)
    assert encoder.default(dt) == dt.timestamp()

    # Test for default method with UUID
    from uuid import uuid4
    uid = uuid4()
    assert encoder.default(uid) == str(uid)

    # Test for default method with Enum
    class SampleEnum(Enum):
        FIRST = 'first'
        SECOND = 'second'
    
    assert encoder.default(SampleEnum.FIRST) == 'first'

    #

# Generated at 2026-04-26 11:36:34.611462
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():    
    import datetime    
    import uuid    
    import enum    
    import decimal    

    class TestEnum(enum.Enum):
        TEST_VALUE = "test_value"

    encoder = _ExtendedEncoder()

    # Test encoding a collection
    collection = [1, 2, 3]
    assert encoder.default(collection) == [1, 2, 3]

    # Test encoding a mapping
    mapping = {"key": "value"}
    assert encoder.default(mapping) == {"key": "value"}

    # Test encoding a datetime
    dt = datetime(2021, 1, 1, 12, 0, 0)
    assert encoder.default(dt) == dt.timestamp()

    # Test encoding a UUID
    test_uuid = uuid.uuid4()
    assert encoder.default(test_uuid) == str(test_uuid)

    # Test encoding an Enum
    enum_value = TestEnum.TEST_VALUE
    assert encoder.default(enum_value) == enum_value.value

    #

# Generated at 2026-04-26 11:36:38.358165
# Unit test for constructor of class _ExtendedEncoder
def test__ExtendedEncoder():  
    encoder = _ExtendedEncoder()
    assert encoder.default({"key": "value"}) == {"key": "value"}
    assert encoder.default([1, 2, 3]) == [1, 2, 3]
    assert encoder.default(datetime(2021, 1, 1, 0, 0, 0, tzinfo=timezone.utc)) == 1609459200.0
    assert encoder.default(UUID('12345678123456781234567812345678')) == '12345678-1234-5678-1234-567812345678'
    assert encoder.default(Enum('Color', 'RED GREEN BLUE')('RED')) == 'RED'
    assert encoder.default(Decimal('10.5')) == '10.5'
    assert encoder.default("string") == "string"

# Run the test
test__ExtendedEncoder()

# This code provides the implementation for the _ExtendedEncoder class in a JSON serialization context