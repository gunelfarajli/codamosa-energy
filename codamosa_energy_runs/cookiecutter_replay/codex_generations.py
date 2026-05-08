

# Generated at 2026-04-26 11:24:58.955793
# Unit test for function dump
def test_dump(): 
    # Define a replay directory and template name for testing
    test_replay_dir = 'replay_test_dir'
    test_template_name = 'test_template'
    # Define a context dictionary with the required cookiecutter key
    test_context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'author_name': 'Test Author'
        }
    }
    # Call the dump function to write the test context to a file
    dump(test_replay_dir, test_template_name, test_context)

    # Check if the file has been created
    replay_file = get_file_name(test_replay_dir, test_template_name)
    assert os.path.exists(replay_file), "Replay file was not created."

    # Check if the content of the file is correct
    with open(replay_file, 'r') as infile:
        loaded_context = json.load(infile)

# Generated at 2026-04-26 11:25:03.590836
# Unit test for function load
def test_load(): 
    # Assume test data
    replay_dir = "test_replay"
    template_name = "test_template"
    context = {
        "cookiecutter": {
            "project_name": "Test Project",
            "author": "Test Author"
        }
    }
    
    # Dumping test data to json file
    dump(replay_dir, template_name, context)
    
    # Loading the data back
    loaded_context = load(replay_dir, template_name)
    
    assert loaded_context == context, 'Loaded context does not match original context'
# Run unit test
test_load()  # This will run the test when the script is executed


## Next steps
# - Expand testing coverage to other functions: dump, get_file_name
# - Consider using a testing framework like pytest for more structured testing
# - Handle cleanup after tests to ensure test isolation
# - Test with edge cases, like empty directories, missing keys, etc.

# Generated at 2026-04-26 11:25:08.237818
# Unit test for function load
def test_load(): 
    replay_dir = 'replays'
    template_name = 'test_template'
    expected_context = {
        'cookiecutter': {
            'project_name': 'test_project',
            'author_name': 'test_author',
        }
    }

    # Prepare test environment
    make_sure_path_exists(replay_dir)
    dump(replay_dir, template_name, expected_context)

    # Call the load function
    actual_context = load(replay_dir, template_name)

    # Assert the loaded context matches the expected context
    assert actual_context == expected_context

    # Clean up test environment
    os.remove(get_file_name(replay_dir, template_name))
    os.rmdir(replay_dir)

# Run the test
test_load()

# Generated at 2026-04-26 11:25:12.506667
# Unit test for function dump
def test_dump(): 
    # Create a dummy replay directory and template name
    replay_dir = 'dummy_replay_dir'
    template_name = 'dummy_template'
    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'author': 'Tester'
        }
    }

    # Run the dump function
    dump(replay_dir, template_name, context)
    
    # Check if the file was created
    file_name = get_file_name(replay_dir, template_name)
    assert os.path.exists(file_name), "File was not created"

    # Check the contents of the file
    with open(file_name, 'r') as infile:
        loaded_context = json.load(infile)
    
    assert loaded_context == context, "Context does not match the original"

    # Clean up
    os.remove(file_name)
    os.rmdir(replay_dir)


# Generated at 2026-04-26 11:25:17.407403
# Unit test for function load
def test_load(): 
    replay_dir = 'test_dir'
    template_name = 'test_template'
    context = {'cookiecutter': {'key': 'value'}}
    
    # Create the replay directory and file for testing
    make_sure_path_exists(replay_dir)
    dump(replay_dir, template_name, context)
    
    # Test loading the context
    loaded_context = load(replay_dir, template_name)
    assert loaded_context == context, f"Expected {context} but got {loaded_context}"

    # Clean up
    os.remove(get_file_name(replay_dir, template_name))
    os.rmdir(replay_dir)

# If you want to run the test

# Generated at 2026-04-26 11:25:22.075925
# Unit test for function dump
def test_dump():  
    # Arrange
    replay_dir = "test_dir"
    template_name = "test_template"
    context = {
        "cookiecutter": {
            "project_name": "Test Project",
            "author": "Test Author"
        }
    }
    
    # Act
    dump(replay_dir, template_name, context)
    
    # Assert
    expected_file_path = os.path.join(replay_dir, "test_template.json")
    
    # Check if the file is created
    assert os.path.isfile(expected_file_path), "File was not created"
    
    # Check if the file content is correct
    with open(expected_file_path, 'r') as f:
        file_content = json.load(f)
        assert file_content == context, "File content does not match the expected context"
    
    # Cleanup
    os.remove(expected_file_path)
    os.rmdir(replay_dir)


# Generated at 2026-04-26 11:25:24.596591
# Unit test for function get_file_name
def test_get_file_name(): 
    # Setup
    replay_dir = "/path/to/replay/dir"
    template_name = "test_template"
    
    # Expected output
    expected_output = "/path/to/replay/dir/test_template.json"
    
    # Call function and assert result
    assert get_file_name(replay_dir, template_name) == expected_output


# Generated at 2026-04-26 11:25:27.500579
# Unit test for function load
def test_load(): 
    replay_dir = 'path/to/replay/dir' 
    template_name = 'test_template' 
    context = { 'cookiecutter': { 'project_slug': 'test_project' } }
    
    # First, dump the context to a file
    dump(replay_dir, template_name, context)
    
    # Now, load the context back from the file
    loaded_context = load(replay_dir, template_name)
    
    assert loaded_context == context, f"Expected {context}, but got {loaded_context}"


# Generated at 2026-04-26 11:25:31.999982
# Unit test for function dump
def test_dump(): 
    # Arrange
    replay_dir = 'test_replay'
    template_name = 'test_template' 
    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'author': 'Test Author'
        }
    }

    # Make sure the replay directory exists
    make_sure_path_exists(replay_dir)

    # Act
    dump(replay_dir, template_name, context)

    # Assert
    replay_file = get_file_name(replay_dir, template_name)
    with open(replay_file, 'r') as infile:
        loaded_context = json.load(infile)
    
    assert loaded_context == context, f"Expected {context}, but got {loaded_context}"

    # Clean up
    os.remove(replay_file)
    os.rmdir(replay_dir)


# Generated at 2026-04-26 11:25:35.630153
# Unit test for function load
def test_load(): 
    """Test the load function."""
    replay_dir = 'test_replay_dir'
    template_name = 'test_template'
    context = {'cookiecutter': {'project_name': 'Test Project'}}
    
    # Prepare test data
    make_sure_path_exists(replay_dir)
    dump(replay_dir, template_name, context)
    
    # Load the context from the replay file
    loaded_context = load(replay_dir, template_name)
    
    assert loaded_context == context, "Loaded context does not match the original context"
    
    # Clean up
    os.remove(get_file_name(replay_dir, template_name))
    os.rmdir(replay_dir)

# Call the test function
test_load()
print("test_load passed.") if test_load() is None else print("test_load failed.")
# This script defines functions to save and load JSON data to and from files,
# specifically for cookiecutter templates. The test_load function validates
# the load function

# Generated at 2026-04-26 11:25:40.457497
# Unit test for function dump
def test_dump(): 
    """Unit test for dump function."""
    replay_dir = 'test_replay'
    template_name = 'test_template'
    context = {'cookiecutter': {'project_name': 'Test Project'}}

    # Create the replay directory
    make_sure_path_exists(replay_dir)

    # Call the dump function
    dump(replay_dir, template_name, context)

    # Verify that the file was created
    replay_file = get_file_name(replay_dir, template_name)
    assert os.path.exists(replay_file), 'Replay file was not created'

    # Verify that the file contents are correct
    with open(replay_file, 'r') as infile:
        loaded_context = json.load(infile)
        assert loaded_context == context, 'Replay file contents do not match expected context'

    # Clean up
    os.remove(replay_file)
    os.rmdir(replay_dir)



# Generated at 2026-04-26 11:25:44.621392
# Unit test for function get_file_name
def test_get_file_name():    
    assert get_file_name("test_dir", "template_name") == "test_dir/template_name.json", "Test failed!"
    assert get_file_name("test_dir", "template_name.json") == "test_dir/template_name.json", "Test failed!"
    assert get_file_name("test_dir", "template_name.txt") == "test_dir/template_name.txt.json", "Test failed!"
    print("All tests passed!")

test_get_file_name()  # Run the unit test

# Generated at 2026-04-26 11:25:49.757859
# Unit test for function load
def test_load(): 
    """Unit test for load function."""
    # Define a temporary replay directory and template name
    replay_dir = '/tmp/replay'  # You would normally use a library like tempfile
    template_name = 'test_template'

    # Create expected json context
    expected_context = {
        'cookiecutter': {
            'project_slug': 'test_slug',
            'project_name': 'Test Project'
        }
    }

    # Prepare the environment for testing
    make_sure_path_exists(replay_dir)
    dump(replay_dir, template_name, expected_context)

    # Now test the load function
    loaded_context = load(replay_dir, template_name)

    # Assert that the loaded context equals the expected context
    assert loaded_context == expected_context, f'Expected {expected_context}, but got {loaded_context}'

    # Clean up - delete the replay file
    os.remove(get_file_name(replay_dir, template_name))

# Call the test

# Generated at 2026-04-26 11:25:54.958685
# Unit test for function load
def test_load():    
    # Prepare test data
    test_replay_dir = "test_replay_dir"
    test_template_name = "test_template"
    test_context = {
        "cookiecutter": {
            "project_name": "Test Project",
            "author": "John Doe"
        }
    }
    
    # Dump the test context to a replay file
    dump(test_replay_dir, test_template_name, test_context)

    # Test the load function
    loaded_context = load(test_replay_dir, test_template_name)

    # Assert that the loaded context matches the original context
    assert loaded_context == test_context, f"Expected: {test_context}, but got: {loaded_context}"


# Run the test
test_load()
"""
Expected: {'cookiecutter': {'project_name': 'Test Project', 'author': 'John Doe'}}, but got: {'cookiecutter': {'project_name': 'Test Project', 'author': 'John Doe'}}
"""

# Generated at 2026-04-26 11:25:58.046476
# Unit test for function load
def test_load(): 
    # Arrange
    replay_dir = 'test_replay_dir'
    template_name = 'test_template'
    context = {
        'cookiecutter': {
            'project_name': 'Test Project'
        }
    }
    dump(replay_dir, template_name, context)
    
    # Act
    loaded_context = load(replay_dir, template_name)
    
    # Assert
    assert loaded_context == context, f"Expected {context}, but got {loaded_context}"


# Generated at 2026-04-26 11:26:00.828886
# Unit test for function dump
def test_dump(): 
    replay_dir = '/tmp/test' 
    template_name = 'test_template' 
    context = {'cookiecutter': {'project_name': 'Test Project', 'author': 'John Doe'}} 

    # Call the dump function
    dump(replay_dir, template_name, context)

    # Check if the file is created and data is written correctly
    replay_file = get_file_name(replay_dir, template_name) 
    assert os.path.exists(replay_file)
    with open(replay_file, 'r') as infile: 
        data = json.load(infile) 
        assert data == context


# Generated at 2026-04-26 11:26:03.330752
# Unit test for function load
def test_load(): 
    replay_dir = "path/to/replay"
    template_name = "template_name"
    context = {"cookiecutter": {"key": "value"}}
    
    # Create a replay file for testing
    dump(replay_dir, template_name, context)
    
    # Load the context from the replay file
    loaded_context = load(replay_dir, template_name)
    
    # Check if the loaded context is the same as the original
    assert loaded_context == context, "Loaded context does not match original context"


# Generated at 2026-04-26 11:26:05.310783
# Unit test for function get_file_name
def test_get_file_name():  
    assert get_file_name('replays', 'my_template') == 'replays/my_template.json'
    assert get_file_name('replays', 'my_template.json') == 'replays/my_template.json'
    assert get_file_name('replays', 'my_template_with_extension.txt') == 'replays/my_template_with_extension.txt.json'


# Generated at 2026-04-26 11:26:08.087880
# Unit test for function dump
def test_dump(): 
   replay_dir = "test_replay_dir"
   template_name = "test_template"
   context = {"cookiecutter": {"key": "value"}}

   dump(replay_dir, template_name, context)

   with open(get_file_name(replay_dir, template_name), 'r') as infile: 
       loaded_context = json.load(infile) 
   
   assert loaded_context == context
   assert os.path.exists(get_file_name(replay_dir, template_name))


# Generated at 2026-04-26 11:26:10.917994
# Unit test for function load
def test_load():  # pragma: no cover
    """Test load function."""
    # Define test parameters
    replay_dir = './replay'
    template_name = 'test_template'
    context = {
        'cookiecutter': {
            'project_slug': 'test_project',
            'project_name': 'Test Project',
        }
    }

    # Create replay directory and save context to file
    dump(replay_dir, template_name, context)

    # Load context from file using load function
    loaded_context = load(replay_dir, template_name)

    # Check if loaded context matches the original context
    assert loaded_context == context, "Loaded context does not match the original context"


# Generated at 2026-04-26 11:26:15.522823
# Unit test for function dump
def test_dump(): 
    # Create mock parameters
    replay_dir = "mock_replay_dir"
    template_name = "mock_template"
    context = {
        "cookiecutter": {
            "project_name": "Test Project",
            "author": "John Doe"
        }
    }
    
    # Call the function to test
    dump(replay_dir, template_name, context)
    
    # Verify if the file has been created
    expected_file_path = get_file_name(replay_dir, template_name)
    assert os.path.exists(expected_file_path), f"Expected file not found at {expected_file_path}"

    # Verify the content of the file
    with open(expected_file_path, 'r') as file:
        data = json.load(file)
        assert data == context, "The content of the file does not match the expected context"
    
    # Clean up the created file
    os.remove(expected_file_path)


# Generated at 2026-04-26 11:26:19.875344
# Unit test for function load
def test_load(): 
    # Setting up a test case
    replay_dir = 'path/to/replay_dir'
    template_name = 'test_template'
    
    # Creating a mock context to save
    context_to_save = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'author': 'Test Author'
        }
    }
    
    # Saving the context to a file
    dump(replay_dir, template_name, context_to_save)
    
    # Loading the context from the file
    loaded_context = load(replay_dir, template_name)
    
    # Asserting that the loaded context matches the saved context
    assert loaded_context == context_to_save, "Loaded context does not match saved context."

# Running the test
test_load() 

# Generated at 2026-04-26 11:26:22.890024
# Unit test for function dump
def test_dump():                     
    # Prepare test data
    replay_dir = './test_replay'         
    template_name = 'test_template'    
    context = {                
        "cookiecutter": {        
            "project_name": "Test Project"
        }
    }
    
    # Test dump function
    dump(replay_dir, template_name, context)  
    
    # Verify the output file is created
    assert os.path.isfile(get_file_name(replay_dir, template_name)) == True 
    
    # Read the content of the file to verify
    with open(get_file_name(replay_dir, template_name), 'r') as infile:
        data = json.load(infile)
        
    assert data == context  # Check if the data matches the input context


# Generated at 2026-04-26 11:26:26.606880
# Unit test for function load
def test_load(): 
    # Create a temporary directory and file for testing
    replay_dir = './test_replay'
    template_name = 'test_template'
    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'author_name': 'Test Author'
        }
    }
    dump(replay_dir, template_name, context)
    
    # Load the context back from the file
    loaded_context = load(replay_dir, template_name)

    # Assert that the loaded context matches the original context
    assert loaded_context == context

    # Clean up test files and directory
    os.remove(get_file_name(replay_dir, template_name))
    os.rmdir(replay_dir)

# Run the test
test_load() 

"""
End of cookiecutter.replay.
"""

# Generated at 2026-04-26 11:26:29.113776
# Unit test for function load
def test_load(): 
    # Setup
    replay_dir = 'test_replay_dir' 
    template_name = 'test_template' 
    expected_context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'author_name': 'Test Author'
        }
    }
    
    # Create a replay file
    dump(replay_dir, template_name, expected_context)
    
    # Execute
    loaded_context = load(replay_dir, template_name)
    
    # Verify
    assert loaded_context == expected_context, f"Expected: {expected_context}, but got: {loaded_context}"


# Generated at 2026-04-26 11:26:31.564104
# Unit test for function dump
def test_dump(): 
    # Setup
    replay_dir = 'test_replays'
    template_name = 'test_template'
    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'author': 'Test Author'
        }
    }
    
    # Execute
    dump(replay_dir, template_name, context)
    
    # Verify
    replay_file = get_file_name(replay_dir, template_name)
    with open(replay_file) as f:
        loaded_context = json.load(f)
    
    assert loaded_context == context, f"Expected {context}, but got {loaded_context}"


# Generated at 2026-04-26 11:26:35.094372
# Unit test for function load
def test_load(): 
    replay_dir = '/path/to/replay_dir'
    template_name = 'template_name'
    
    # Create mock data and write it to the replay file
    mock_context = {
        'cookiecutter': {
            'foo': 'bar'
        }
    }
    
    # Ensure the directory exists for the test
    make_sure_path_exists(replay_dir)
    
    replay_file = get_file_name(replay_dir, template_name)
    
    with open(replay_file, 'w') as outfile:
        json.dump(mock_context, outfile, indent=2)

    # Test the load function
    loaded_context = load(replay_dir, template_name)
    
    # Assert the loaded context is equal to the mock context
    assert loaded_context == mock_context, "Loaded context does not match mock context"
    
    # Cleanup the replay file after the test
    os.remove(replay_file)


# Generated at 2026-04-26 11:26:38.444716
# Unit test for function load
def test_load(): 
    replay_dir = 'some_dir'  # Directory where replay files are stored
    template_name = 'test_template'  # Name of the template
    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'author_name': 'John Doe'
        }
    }

    # Create a replay file to test loading
    dump(replay_dir, template_name, context)

    # Now load the context from the replay file
    loaded_context = load(replay_dir, template_name)

    # Assert that the loaded context matches the original context
    assert loaded_context == context, "Loaded context does not match original context!"

# Run the test
test_load()

# Generated at 2026-04-26 11:26:41.086259
# Unit test for function dump
def test_dump(): 
    # arrange
    replay_dir = 'test_dir'
    template_name = 'test_template'
    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'author_name': 'Test Author'
        }
    }
    
    # act
    dump(replay_dir, template_name, context)

    # assert
    expected_file_path = get_file_name(replay_dir, template_name)
    with open(expected_file_path, 'r') as f:
        loaded_context = json.load(f)
    
    assert loaded_context == context
    os.remove(expected_file_path)  # Clean up the test file


# Generated at 2026-04-26 11:26:45.509382
# Unit test for function load
def test_load(): 
    # Create a temporary replay directory and test file
    replay_dir = 'temp_replay_dir'
    template_name = 'test_template'
    context = {'cookiecutter': {'key1': 'value1'}}
    
    # Create the directory
    make_sure_path_exists(replay_dir)
    
    # Create the test file
    dump(replay_dir, template_name, context)
    
    # Load the context from the file
    loaded_context = load(replay_dir, template_name)
    
    # Check if the loaded context is equal to the original context
    assert loaded_context == context, "Loaded context does not match the original context"
    
    # Clean up
    os.remove(get_file_name(replay_dir, template_name))
    os.rmdir(replay_dir)


# Generated at 2026-04-26 11:26:52.079609
# Unit test for function load
def test_load(): 
    import tempfile
    import shutil

    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    
    # Define replay file name
    template_name = 'test_template'
    replay_file = get_file_name(temp_dir, template_name)

    # Write a test context to the replay file
    test_context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'author': 'Test Author'
        }
    }
    with open(replay_file, 'w') as outfile:
        json.dump(test_context, outfile, indent=2)

    # Now test the load function
    loaded_context = load(temp_dir, template_name)

    # Assertions to verify the loaded context matches the expected context
    assert loaded_context == test_context, "Loaded context does not match the expected context"
    
    # Cleanup the temporary directory
    shutil.rmtree(temp_dir)

# Run the unit test
test_load()  # This

# Generated at 2026-04-26 11:26:55.573904
# Unit test for function load
def test_load(): 
    # Test loading valid data
    replay_dir = 'path/to/replay_dir'
    template_name = 'template_name'
    context = {'cookiecutter': {'key': 'value'}}
    
    # We need to create the replay dir and file before loading
    make_sure_path_exists(replay_dir)
    replay_file = get_file_name(replay_dir, template_name)
    with open(replay_file, 'w') as outfile:
        json.dump(context, outfile, indent=2)
        
    # Now we can test the load function
    loaded_context = load(replay_dir, template_name)
    assert loaded_context == context, "Loaded context did not match the original context"    

    # Test loading non-existent file
    try:
        load(replay_dir, 'non_existent_template_name')
    except FileNotFoundError:
        pass  # Expected behavior, file does not exist

# Generated at 2026-04-26 11:26:59.227264
# Unit test for function load
def test_load(): 
    """Test load function."""
    replay_dir = 'test_replays'
    template_name = 'test_template'
    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'author_name': 'Test Author',
        }
    }
    
    # Dump the context to a replay file
    dump(replay_dir, template_name, context)
    
    # Load the context from the replay file
    loaded_context = load(replay_dir, template_name)
    
    # Assert that the loaded context is equal to the original context
    assert loaded_context == context, f'Expected: {context}, but got: {loaded_context}'

# Run the unit test
test_load()

# Generated at 2026-04-26 11:27:02.670732
# Unit test for function load
def test_load(): 
    """Test the load function."""
    replay_dir = "./replay_dir"
    template_name = "test_template"
    context = {"cookiecutter": {"key": "value"}}
    
    # Create a replay file for testing
    dump(replay_dir, template_name, context)
    
    # Load the context
    loaded_context = load(replay_dir, template_name)
    
    # Assert that the loaded context is the same as the original context
    assert loaded_context == context, "Loaded context does not match original context"
    
    # Clean up the replay file after testing
    os.remove(get_file_name(replay_dir, template_name))


# Generated at 2026-04-26 11:27:04.965414
# Unit test for function load
def test_load(): 
	# Arrange
	replay_dir = "path_to_replay_dir"
	template_name = "template_name"
	expected_context = {"cookiecutter": {"key": "value"}}

	# Create a mock file with expected content
	with open(get_file_name(replay_dir, template_name), 'w') as f:
		json.dump(expected_context, f)

	# Act
	context = load(replay_dir, template_name)

	# Assert
	assert context == expected_context

	# Clean up
	os.remove(get_file_name(replay_dir, template_name))


# Generated at 2026-04-26 11:27:08.995107
# Unit test for function load
def test_load(): 
    # arrange
    test_replay_dir = 'test_replay'
    test_template_name = 'test_template'
    test_context = {'cookiecutter': {'project_name': 'Test Project'}}
    
    # Ensure replay directory exists
    make_sure_path_exists(test_replay_dir)
    
    # dump the test context to a file
    dump(test_replay_dir, test_template_name, test_context)

    # act
    loaded_context = load(test_replay_dir, test_template_name)

    # assert
    assert loaded_context == test_context

    # Cleanup
    os.remove(get_file_name(test_replay_dir, test_template_name)) 
    os.rmdir(test_replay_dir)

# Run the test
test_load() 
print("Test passed!") 

# Generated at 2026-04-26 11:27:11.205323
# Unit test for function load
def test_load(): 
    # Arrange
    replay_dir = 'test_replay'
    template_name = 'test_template'
    
    # Create a test replay file
    context = {'cookiecutter': {'project_name': 'Test Project'}}
    dump(replay_dir, template_name, context)
    
    # Act
    loaded_context = load(replay_dir, template_name)
    
    # Assert
    assert loaded_context == context, f"Expected {context} but got {loaded_context}" 


# Generated at 2026-04-26 11:27:13.650221
# Unit test for function load
def test_load(): 
    replay_dir = './replay'
    template_name = 'example_template'
    # Create mock json data
    context = {
        'cookiecutter': {
            'project_name': 'Example Project',
            'author': 'John Doe',
        }
    }
    # Dump the mock data to replay_dir
    dump(replay_dir, template_name, context)
    
    # Load the data back using the load function
    loaded_context = load(replay_dir, template_name)

    assert loaded_context == context, "Loaded context does not match the original context"


# Generated at 2026-04-26 11:27:17.556715
# Unit test for function load
def test_load(): 
    """Test the load function."""
    # Create a temporary directory and file for testing
    replay_dir = "temp_replay_dir"
    template_name = "test_template"
    context = {
        "cookiecutter": {
            "project_name": "Test Project",
            "author_name": "Test Author"
        }
    }

    dump(replay_dir, template_name, context)  # Save the context to a file
    loaded_context = load(replay_dir, template_name)  # Load the context from the file

    assert loaded_context == context  # Check if loaded context matches the original context
    os.remove(get_file_name(replay_dir, template_name))  # Clean up the temporary file
    os.rmdir(replay_dir)  # Clean up the temporary directory


# Run the unit test
if __name__ == "__main__":
    test_load()

# Generated at 2026-04-26 11:27:22.544882
# Unit test for function load
def test_load(): 
    # Arrange
    replay_dir = '/path/to/replay'
    template_name = 'template'
    expected_context = {'cookiecutter': {'project_name': 'TestProject'}}
    
    # Create a mock JSON file for testing
    mock_replay_file = get_file_name(replay_dir, template_name)
    make_sure_path_exists(replay_dir)  # Ensure replay directory exists
    with open(mock_replay_file, 'w') as mock_file:
        json.dump(expected_context, mock_file)

    # Act
    context = load(replay_dir, template_name)

    # Assert
    assert context == expected_context

    # Clean up
    os.remove(mock_replay_file)
    
test_load()  # Run the test

# Generated at 2026-04-26 11:27:30.954391
# Unit test for function dump
def test_dump(): 
    # Prepare the test data
    replay_dir = './test_replay'
    template_name = 'test_template'
    context = {'cookiecutter': {'key1': 'value1', 'key2': 'value2'}}
    
    # Call the dump function
    dump(replay_dir, template_name, context)
    
    # Check if the file exists and the content is correct
    replay_file = get_file_name(replay_dir, template_name)
    assert os.path.exists(replay_file), "Replay file does not exist"
    
    with open(replay_file, 'r') as infile:
        loaded_context = json.load(infile)
    
    assert loaded_context == context, "Loaded context does not match the original context"

    # Clean up
    os.remove(replay_file)
    os.rmdir(replay_dir)  # Only works if the directory is empty



# Generated at 2026-04-26 11:27:35.112445
# Unit test for function load
def test_load():  
    # Create a temporary directory and a test file with valid content
    os.makedirs('./test_replay', exist_ok=True)
    test_filename = get_file_name('./test_replay', 'test_template')
    
    # Prepare context with the required 'cookiecutter' key
    test_context = {'cookiecutter': {'project_name': 'TestProject'}}
    
    # Dump the test context into the file
    dump('./test_replay', 'test_template', test_context)
    
    # Load the context back from the file
    loaded_context = load('./test_replay', 'test_template')
    
    # Clean up the test file and directory
    os.remove(test_filename)
    os.rmdir('./test_replay')
    
    # Check if the loaded context matches the original context
    assert loaded_context == test_context, "Loaded context does not match the original context."

# Run the test
test_load()

# Generated at 2026-04-26 11:27:37.892905
# Unit test for function load
def test_load(): 
    # Set up the test
    replay_dir = "path/to/replay"
    template_name = "test_template"
    context = {
        "cookiecutter": {
            "project_name": "Test Project",
            "author": "Test Author"
        }
    }
    
    # First, dump the context to a file
    dump(replay_dir, template_name, context)
    
    # Now, load the context from the file
    loaded_context = load(replay_dir, template_name)
    
    # Check if the loaded context is the same as the original context
    assert loaded_context == context, "Loaded context does not match the original context"

# Note: In a real unit test, you would use a framework like pytest or unittest
# and also include cleanup code to remove the test files after the test is done.

# Generated at 2026-04-26 11:27:40.681141
# Unit test for function dump
def test_dump(): 
    context = {
        "cookiecutter": {
            "project_name": "test_project",
            "author_name": "Test Author",
        }
    }
    
    # Define a replay directory (ensure it exists)
    replay_dir = "test_replay"
    make_sure_path_exists(replay_dir)
    
    # Attempt to dump the context to a file
    dump(replay_dir, "test_template", context)
    
    # Verify that the file is created and contains the expected content
    replay_file = get_file_name(replay_dir, "test_template")
    with open(replay_file, 'r') as infile:
        loaded_context = json.load(infile)
    
    assert loaded_context == context, "Dumped context does not match the original context."


# Generated at 2026-04-26 11:27:43.392568
# Unit test for function load
def test_load(): 
    """Unit test for load function"""
    # Setting up the test
    replay_dir = 'test_dir'
    template_name = 'test_template'
    context = {'cookiecutter': {'project_name': 'Test Project'}}
    
    # Creating the directory and dumping initial context
    make_sure_path_exists(replay_dir)
    dump(replay_dir, template_name, context)
    
    # Load the context back
    loaded_context = load(replay_dir, template_name)
    
    # Assert the loaded context is equal to the original context
    assert loaded_context == context, f"Expected {context}, got {loaded_context}"

# Running the unit test
test_load() 
print("Test passed!") 

# Generated at 2026-04-26 11:27:46.440308
# Unit test for function load
def test_load():    
    # Given
    replay_dir = 'replay'
    template_name = 'template_name'
    context = {
        'cookiecutter': {
            'project_name': 'my_project',
            'author': 'John Doe'
        }
    }
    
    # Prepare the replay file
    dump(replay_dir, template_name, context)

    # When
    result = load(replay_dir, template_name)

    # Then
    assert result == context, f"Expected {context} but got {result}"


# Generated at 2026-04-26 11:31:43.879205
# Unit test for function dump
def test_dump(): 
    # Prepare test data
    replay_dir = "test_replay"
    template_name = "test_template"
    context = {'cookiecutter': {'name': 'test_project', 'version': '0.1.0'}}
    
    # Call the function
    dump(replay_dir, template_name, context)
    
    # Verify the file was created and contains the correct data
    replay_file = get_file_name(replay_dir, template_name)
    with open(replay_file, 'r') as infile:
        loaded_context = json.load(infile)
    
    assert loaded_context == context, "The loaded context does not match the original context."
    
    # Clean up
    os.remove(replay_file)
    os.rmdir(replay_dir)  # Remove the directory if empty
