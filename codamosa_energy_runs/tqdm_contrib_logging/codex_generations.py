

# Generated at 2026-04-26 14:18:15.866213
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():  # pragma: no cover
    import logging
    from tqdm import trange
    import io

    log = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    with io.StringIO() as buf, redirect_stdout(buf):
        with tqdm_logging_redirect(ncols=100, loggers=[log]) as pbar:
            for i in trange(9):
                log.info("Processing %d", i)
                pbar.update(1)
    output = buf.getvalue()
    assert "Processing" in output
    assert "Processing 0" in output
    assert "Processing 1" in output
    assert "Processing 2" in output
    assert "Processing 3" in output
    assert "Processing 4" in output
    assert "Processing 5" in output
    assert "Processing 6" in output
    assert "Processing 7" in output

# Generated at 2026-04-26 14:18:21.054894
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    
    import io

    # Create a logger
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)
    log_stream = io.StringIO()
    stream_handler = logging.StreamHandler(log_stream)
    logger.addHandler(stream_handler)

    # Use the logging_redirect_tqdm context manager
    with logging_redirect_tqdm(loggers=[logger]) as pbar:
        for i in range(5):
            logger.info(f"Logging message {i}")
            pbar.update(1)

    # Check the output in the log stream
    output = log_stream.getvalue().strip()
    assert "Logging message 0" in output
    assert "Logging message 1" in output
    assert "Logging message 2" in output
    assert "Logging message 3" in output
    assert "Logging message 4" in output
    assert output.count("Logging message") == 5

# Call the test function
test

# Generated at 2026-04-26 14:18:24.426280
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm(): 
    import logging
    import time

    # Create a logger and set level to INFO
    logger = logging.getLogger('TestLogger')
    logging.basicConfig(level=logging.INFO)

    # Use the logging_redirect_tqdm context manager
    with logging_redirect_tqdm(loggers=[logger]):
        for i in range(5):
            logger.info(f"Logging iteration {i + 1}")
            time.sleep(1)  # Simulate work being done


# Generated at 2026-04-26 14:18:29.754883
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm(): 
    import io
    import contextlib
    
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    with logging_redirect_tqdm(loggers=[logger]):
        logger.info("This is a test message")
    
    # Verify that the message is redirected to tqdm
    output = stream.getvalue()
    assert "This is a test message" in output
    assert "INFO:test_logger:This is a test message" not in output

# Call the test function
test_logging_redirect_tqdm()

# Generated at 2026-04-26 14:18:36.716360
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit(): 
    import io
    import sys

    log_stream = io.StringIO()
    sys.stdout = log_stream

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create a custom logging handler
    handler = _TqdmLoggingHandler()
    logger.addHandler(handler)

    # Test logging a message
    logger.info("Test message")

    # Flush the handler to ensure the message is printed
    handler.flush()

    sys.stdout = sys.__stdout__  # Reset stdout

    # Capture the output
    output = log_stream.getvalue()
    assert "Test message" in output
    print("Test passed.")

# Call the test function
test__TqdmLoggingHandler_emit()

# Generated at 2026-04-26 14:18:41.664004
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    
    import logging
    import time

    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Simulate a task with tqdm and logging
    with tqdm_logging_redirect(total=10, desc='Processing', bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}'):
        for i in range(10):
            logger.info(f'Iteration {i}')
            time.sleep(0.1)  # Simulate work

# Run the test
test_tqdm_logging_redirect()  # This will execute the test function

# Generated at 2026-04-26 14:18:45.434153
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():  
    import logging
    from tqdm import trange
    
    LOG = logging.getLogger(__name__)
    
    logging.basicConfig(level=logging.INFO)
    
    with tqdm_logging_redirect(total=10) as pbar:
        for i in trange(10):
            if i == 5:
                LOG.info("Testing logging redirection")  # Should be redirected to tqdm.write
            pbar.update(1)  # Update the tqdm progress bar
    
    # Check the output or any assertions as needed

# Generated at 2026-04-26 14:18:49.211570
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():  
    import logging
    from tqdm import trange
    
    LOG = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)
    
    with logging_redirect_tqdm():
        for i in trange(9):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
    
    # logging restored
    LOG.info("Logging restored after context manager.")
    
test_logging_redirect_tqdm()   

# Generated at 2026-04-26 14:18:54.250605
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():  
    import io  
    import pytest  
      
    # Initialize the handler and logger  
    log_stream = io.StringIO()  
    tqdm_handler = _TqdmLoggingHandler()  
    logger = logging.getLogger("test_logger")  
    logger.addHandler(tqdm_handler)  
    logger.setLevel(logging.DEBUG)  
    
    # Redirect the logging output to the StringIO stream  
    tqdm_handler.setStream(log_stream)  
    
    # Test logging at different levels  
    logger.debug("This is a debug message.")  
    logger.info("This is an info message.")  
    logger.warning("This is a warning message.")  
    logger.error("This is an error message.")  
    logger.critical("This is a critical message.")  
    
    # Check if the messages are emitted correctly  
    output = log_stream.getvalue()  
    assert "This is a debug message." in output  
    assert "This is an info message." in output  

# Generated at 2026-04-26 14:18:56.992620
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():  # pragma: no cover
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import tqdm_logging_redirect

    # Configure logging
    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)

    with tqdm_logging_redirect(loggers=[LOG], total=10) as pbar:
        for i in trange(10):
            pbar.update(1)
            LOG.info(f"Processed item {i+1}")

# Generated at 2026-04-26 14:19:08.050080
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():   
    import logging

    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    logging.basicConfig(level=logging.INFO)

    with tqdm_logging_redirect(loggers=[logger]) as pbar:
        for i in range(10):
            logger.info(f'Processing item {i}')
            pbar.update(1)

# Run the test
test_tqdm_logging_redirect()

# Generated at 2026-04-26 14:19:11.442403
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():    
    import io

    # Create a logger
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)

    # Test the logging redirect
    with logging_redirect_tqdm(loggers=[logger]):
        for _ in range(3):
            logger.info("Logging info message.")
    
    # Check the output
    output = stream.getvalue().strip()
    assert output == "Logging info message.\nLogging info message.\nLogging info message."
    print("Test passed!")

# Uncomment below to run the test
# test_logging_redirect_tqdm()

# Generated at 2026-04-26 14:19:14.365793
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit(): 
    import io
    import pytest

    # Create a stream to capture the output
    stream = io.StringIO()
    handler = _TqdmLoggingHandler()
    handler.setStream(stream)

    # Create a test log record
    log_record = logging.LogRecord(
        name='test_logger',
        level=logging.INFO,
        pathname='',
        lineno=0,
        msg='Test message',
        args=None,
        exc_info=None
    )

    # Call the emit method
    handler.emit(log_record)

    # Check the output
    output = stream.getvalue()
    assert 'Test message' in output


# Generated at 2026-04-26 14:19:18.192414
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():  
    import io
    import logging
    import tqdm

    # Create a logger
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)

    # Capture logging output
    log_stream = io.StringIO()
    handler = logging.StreamHandler(log_stream)
    handler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(handler)

    # Run logging_redirect_tqdm in a context manager
    with logging_redirect_tqdm(loggers=[logger], tqdm_class=tqdm):
        # Simulate some logging
        for i in range(5):
            logger.info(f"Logging iteration {i}")

    # Get output from the StringIO stream
    output = log_stream.getvalue()

    # Check if the output was redirected correctly
    assert "Logging iteration 0" in output
    assert "Logging iteration 1" in output
    assert "Logging iteration 2" in output

# Generated at 2026-04-26 14:19:21.575988
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():  
    import time  
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)
    with tqdm_logging_redirect(total=5, loggers=[log]) as pbar:
        for i in range(5):
            time.sleep(1)
            log.info(f'Iteration: {i+1}')
            pbar.update(1)

# Uncomment to run the test
# test_tqdm_logging_redirect()

# Generated at 2026-04-26 14:19:24.029814
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm(): 
    import io
    import contextlib

    # Setup
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Test
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info("This is a test log message.")

    # Verify output
    output = stream.getvalue()
    assert "This is a test log message." in output
    assert output.count("This is a test log message.") == 1

# Generated at 2026-04-26 14:19:26.414638
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect(): 
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`") 
                # logging restored

test_tqdm_logging_redirect() 

# Generated at 2026-04-26 14:19:29.553504
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():  
    import io
    from contextlib import redirect_stdout

    log_stream = io.StringIO()
    logging.basicConfig(stream=log_stream, level=logging.INFO)

    log_msg = "This is a test log message."
    with redirect_stdout(io.StringIO()):  # Redirect stdout to suppress tqdm output
        with tqdm_logging_redirect(loggers=[logging.root], tqdm_class=std_tqdm):
            logging.info(log_msg)

    output = log_stream.getvalue().strip()
    assert log_msg in output, "Log message not found in output."
    assert output.count(log_msg) == 1, "Log message should only appear once."

# Run the test function
test_tqdm_logging_redirect()  

# Generated at 2026-04-26 14:19:33.710756
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    
    import logging
    from tqdm import trange
    from tqdm.contrib.logging import logging_redirect_tqdm

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with logging_redirect_tqdm():
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
        # logging restored
# Run the unit test
test_tqdm_logging_redirect()

# Generated at 2026-04-26 14:19:39.178156
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect(): 
    import logging
    from tqdm import tqdm
    from tqdm.contrib.logging import logging_redirect_tqdm
    
    LOG = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)
    
    # Sample test with logging_redirect_tqdm
    with logging_redirect_tqdm():
        for i in range(10):
            if i == 5:
                LOG.info("Logging at iteration 5")
            tqdm.write(f"Iteration {i}")
    
    print("Test completed successfully.")

# Uncomment the line below to run the test
# test_tqdm_logging_redirect()

# Generated at 2026-04-26 14:19:59.271914
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm(): 
    import io
    import sys

    # Create a logger
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)
    log_stream = io.StringIO()
    stream_handler = logging.StreamHandler(log_stream)
    logger.addHandler(stream_handler)

    # Function to test
    with logging_redirect_tqdm(loggers=[logger], tqdm_class=std_tqdm):
        logger.info("Hello World")

    # Get the logged output and check it
    log_output = log_stream.getvalue()
    assert "Hello World" in log_output
    assert "INFO:test_logger:Hello World" not in log_output  # It should not contain the normal log format

# Running the unit test
test_logging_redirect_tqdm() 

# Generated at 2026-04-26 14:20:03.549723
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():  # pragma: no cover
    import time

    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)

    with tqdm_logging_redirect(total=10, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}  {postfix}") as pbar:
        for i in range(10):
            LOG.info(f"Logging iteration {i+1}")
            pbar.update(1)
            time.sleep(0.1)  # Simulate some work

# Uncomment the following line to run the test if this script is executed directly
# test_tqdm_logging_redirect()  

# Generated at 2026-04-26 14:20:07.860018
# Unit test for method emit of class _TqdmLoggingHandler
def test__TqdmLoggingHandler_emit():  # pragma: no cover
    from io import StringIO

    # Create a logger
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.DEBUG)

    # Create a StringIO stream to capture the output
    stream = StringIO()
    handler = _TqdmLoggingHandler()
    handler.setStream(stream)

    # Set a formatter for the handler
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    # Emit a log record
    logger.info("Test message")

    # Check the output in the StringIO stream
    output = stream.getvalue()
    assert "Test message" in output
    assert "INFO" in output

    # Clean up
    logger.removeHandler(handler)
    handler.close()

# Generated at 2026-04-26 14:20:12.329715
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():  
    import logging
    from tqdm import trange
    
    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)
    
    # Test the logging_redirect_tqdm function
    with logging_redirect_tqdm():
        for i in trange(5):
            if i == 2:
                LOG.info("This log message should be redirected to tqdm")
    # At this point, logging should have been redirected and restored.
    print("Test completed.")

# Run the test
if __name__ == "__main__":
    test_logging_redirect_tqdm()

# Generated at 2026-04-26 14:20:16.509327
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    
    import logging
    from tqdm import trange
    
    LOG = logging.getLogger(__name__)

    logging.basicConfig(level=logging.INFO)
    
    with tqdm_logging_redirect(total=10) as pbar:
        for i in trange(10):
            if i == 4:
                LOG.info("console logging redirected to `tqdm.write()`")
            pbar.update(1)

    assert pbar.n == 10  # Check that the progress bar has completed
    assert pbar.last_print_n == 10  # Check that the last printed value is 10

test_tqdm_logging_redirect()  # Run the test

# Generated at 2026-04-26 14:20:20.453845
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm(): 
    """
    Unit test to ensure logging redirects work as expected.
    """
    import logging
    from tqdm import trange
    from io import StringIO

    # Setup a logger
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    log_stream = StringIO()
    handler = logging.StreamHandler(log_stream)
    logger.addHandler(handler)

    # Run the logging redirect
    with logging_redirect_tqdm(loggers=[logger]):
        for i in trange(3):
            logger.info(f'Logging iteration {i}')

    # Retrieve log contents
    log_contents = log_stream.getvalue()

    assert 'Logging iteration 0' in log_contents
    assert 'Logging iteration 1' in log_contents
    assert 'Logging iteration 2' in log_contents
    assert log_contents.count('Logging iteration') == 3  # Check count
    assert 'Logging iteration 1' in log_contents  # Check specific

# Generated at 2026-04-26 14:20:26.762927
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():    
    import logging
    from tqdm import trange

    LOG = logging.getLogger(__name__)

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        with tqdm_logging_redirect(total=9, desc="Processing"):
            for i in trange(9):
                if i == 4:
                    LOG.info("console logging redirected to `tqdm.write()`")
    # logging restored

# Generated at 2026-04-26 14:20:31.151350
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm():  
    import io
    import contextlib
    import logging

    # Set up the logger
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.DEBUG)
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    # Test logging_redirect_tqdm
    with logging_redirect_tqdm(loggers=[logger]):
        logger.info("Test message")
    output = stream.getvalue()

    # Check that the output contains the message
    assert "Test message" in output
    print("Logging redirected to tqdm.write successfully.")

# Run the test
test_logging_redirect_tqdm()

# Generated at 2026-04-26 14:20:35.074620
# Unit test for function tqdm_logging_redirect
def test_tqdm_logging_redirect():  # pragma: no cover
    import logging
    from tqdm import trange

    LOG = logging.getLogger(__name__)

    logging.basicConfig(level=logging.INFO)

    with tqdm_logging_redirect(total=10) as pbar:
        for i in trange(10):
            if i == 4:
                LOG.info("Logging at halfway mark")
            pbar.update(1)

# Generated at 2026-04-26 14:20:39.059448
# Unit test for function logging_redirect_tqdm
def test_logging_redirect_tqdm(): 
    import logging
    from tqdm import trange
    import io
    log_stream = io.StringIO()
    logging.basicConfig(stream=log_stream, level=logging.INFO)
    LOG = logging.getLogger(__name__)

    with logging_redirect_tqdm(loggers=[LOG]):
        for i in trange(3):
            if i == 1:
                LOG.info("console logging redirected to `tqdm.write()`")
    
    log_output = log_stream.getvalue()
    print(log_output)  # Check the log output

# Call the test function
test_logging_redirect_tqdm()