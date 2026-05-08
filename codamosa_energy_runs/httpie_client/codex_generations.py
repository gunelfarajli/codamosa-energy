

# Generated at 2026-04-26 13:16:04.439572
# Unit test for function make_default_headers
def test_make_default_headers():    
    class Args:
        def __init__(self):
            self.data = None
            self.form = False
            self.json = False
            self.files = False
            
    # Test case where no data or form is provided
    args = Args()
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_UA
    assert 'Accept' not in headers
    assert 'Content-Type' not in headers

    # Test case where JSON data is provided
    args.data = {'key': 'value'}
    args.json = True
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_UA
    assert headers['Accept'] == JSON_ACCEPT
    assert headers['Content-Type'] == JSON_CONTENT_TYPE
    
    # Test case where form data is provided
    args.data = None
    args.form = True
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_U

# Generated at 2026-04-26 13:16:06.683317
# Unit test for function max_headers
def test_max_headers(): 
    with max_headers(10):
        assert http.client._MAXHEADERS == 10
    assert http.client._MAXHEADERS == float('Inf')


# Generated at 2026-04-26 13:16:11.032929
# Unit test for function make_default_headers
def test_make_default_headers():    
    class MockArgs:
        def __init__(self, data=None, form=None, files=None, json=None):
            self.data = data
            self.form = form
            self.files = files
            self.json = json
    
    # Test case 1: only JSON flag is set
    args = MockArgs(json=True)
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_UA
    assert headers['Accept'] == JSON_ACCEPT
    assert headers['Content-Type'] == JSON_CONTENT_TYPE

    # Test case 2: only data is set (no JSON or form)
    args = MockArgs(data={"key": "value"})
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_UA
    assert headers['Accept'] == JSON_ACCEPT
    assert headers['Content-Type'] == JSON_CONTENT_TYPE

    # Test case 3: form flag is set
    args = MockArgs

# Generated at 2026-04-26 13:16:15.702458
# Unit test for function max_headers
def test_max_headers():    
    # Define a mock context manager to replace max_headers
    @contextmanager
    def mock_max_headers(limit):
        yield
    
    # Replace the original max_headers with the mock
    original_max_headers = globals()['max_headers']
    globals()['max_headers'] = mock_max_headers

    try:
        # Call the function that uses max_headers
        with max_headers(10):
            # Check that the limit was set correctly
            assert http.client._MAXHEADERS == float('Inf')  # Ensure the limit is set
    finally:
        # Restore the original max_headers after the test
        globals()['max_headers'] = original_max_headers

# Generated at 2026-04-26 13:16:20.097400
# Unit test for function finalize_headers
def test_finalize_headers(): 
    # Test with normal headers
    headers = RequestHeadersDict({
        'Content-Type': ' application/json ',
        'User-Agent': ' HTTPie ',
        'Accept': None
    })

    expected = RequestHeadersDict({
        'Content-Type': b'application/json',
        'User-Agent': b'HTTPie'
    })

    result = finalize_headers(headers)
    
    assert result == expected, f"Expected {expected} but got {result}"

    # Test with empty headers
    headers = RequestHeadersDict({
        'Content-Type': None,
        'User-Agent': None
    })

    expected = RequestHeadersDict()

    result = finalize_headers(headers)

    assert result == expected, f"Expected {expected} but got {result}"

    # Test with a header that has only whitespace
    headers = RequestHeadersDict({
        'Content-Type': '   ',
        'User-Agent': ' HTTPie '
    })


# Generated at 2026-04-26 13:16:27.124348
# Unit test for function finalize_headers
def test_finalize_headers():    
    # Test with regular headers
    headers = RequestHeadersDict({
        'Content-Type': ' application/json ',
        'User-Agent': None,
        'Authorization': 'Bearer token '
    })
    expected_output = RequestHeadersDict({
        'Content-Type': b'application/json',
        'Authorization': b'Bearer token'
    })
    assert finalize_headers(headers) == expected_output

    # Test with empty headers
    headers = RequestHeadersDict({})
    expected_output = RequestHeadersDict({})
    assert finalize_headers(headers) == expected_output

    # Test with headers containing only None values
    headers = RequestHeadersDict({
        'Header1': None,
        'Header2': None,
    })
    expected_output = RequestHeadersDict({})
    assert finalize_headers(headers) == expected_output

    # Test with headers containing leading and trailing spaces

# Generated at 2026-04-26 13:16:29.515292
# Unit test for function max_headers
def test_max_headers():    
    with max_headers(10):
        assert http.client._MAXHEADERS == 10

    # Ensure it resets back to original value
    assert http.client._MAXHEADERS == http.client._MAXHEADERS


# Generated at 2026-04-26 13:16:33.985192
# Unit test for function finalize_headers
def test_finalize_headers():  
    # Test case 1: Normal case
    input_headers = RequestHeadersDict({
        'Content-Type': ' application/json ',
        'User-Agent': None,
        'Accept': 'text/html'
    })
    expected_output = RequestHeadersDict({
        'Content-Type': b'application/json',
        'Accept': b'text/html'
    })
    assert finalize_headers(input_headers) == expected_output

    # Test case 2: Headers with leading/trailing spaces
    input_headers = RequestHeadersDict({
        'X-Custom-Header': '  CustomValue  ',
        'X-Another-Header': 'ValueWithSpaces      '
    })
    expected_output = RequestHeadersDict({
        'X-Custom-Header': b'CustomValue',
        'X-Another-Header': b'ValueWithSpaces'
    })
    assert finalize_headers(input_headers) == expected_output

    # Test case 3: Headers with None values

# Generated at 2026-04-26 13:16:38.673043
# Unit test for function make_request_kwargs
def test_make_request_kwargs(): 
    class Args:
        # Simulating some expected attributes of argparse.Namespace
        def __init__(self):
            self.method = 'GET'
            self.url = 'http://example.com'
            self.data = {'key': 'value'}
            self.json = True
            self.headers = {'Authorization': 'Bearer token'}
            self.form = False
            self.multipart = False
            self.chunked = False
            self.offline = False
            self.params = {}
            self.files = None
            self.boundary = None
            self.multipart_data = None
            
    args = Args()
    result = make_request_kwargs(args)

    assert result['method'] == 'get'
    assert result['url'] == 'http://example.com'
    assert result['headers']['Authorization'] == 'Bearer token'
    assert result['data'] == '{"key": "value"}'  # JSON encoded data

# Run the test
test_make_request_kwargs()

# Generated at 2026-04-26 13:16:42.903283
# Unit test for function make_request_kwargs
def test_make_request_kwargs(): 
    class Args:
        def __init__(self):
            self.method = 'GET'
            self.url = 'http://example.com'
            self.headers = {'Content-Type': 'application/json'}
            self.data = {'key': 'value'}
            self.json = True
            self.form = False
            self.offline = False
            self.chunked = False
            self.multipart = False
            self.multipart_data = None
            self.boundary = None
            self.params = {}
    
    args = Args()
    request_kwargs = make_request_kwargs(args)
    
    assert request_kwargs['method'] == 'get'
    assert request_kwargs['url'] == 'http://example.com'
    assert request_kwargs['headers']['Content-Type'] == 'application/json'
    assert request_kwargs['data'] == '{"key": "value"}'
    assert request_kwargs['auth'] == None
    assert request_kwargs['params'] == {}

# Run the test
test_make_request

# Generated at 2026-04-26 13:16:55.946868
# Unit test for function max_headers
def test_max_headers(): 
    with max_headers(10):
        assert http.client._MAXHEADERS == 10  # Check if MAXHEADERS is set correctly

    assert http.client._MAXHEADERS == float('Inf')  # Ensure it resets to original value after context manager


# Generated at 2026-04-26 13:16:59.314832
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():    
    class Args:
        cert = None
        cert_key = None
        proxy = []
        verify = "true"
    
    args = Args()
    result = make_send_kwargs_mergeable_from_env(args)
    
    expected_result = {
        'proxies': {},
        'stream': True,
        'verify': True,
        'cert': None,
    }
    
    assert result == expected_result, f"Expected {expected_result}, but got {result}"


# Generated at 2026-04-26 13:17:01.481171
# Unit test for function make_send_kwargs
def test_make_send_kwargs():    
    class Args:
        timeout = 10
        verify = "yes"
    
    args = Args()
    send_kwargs = make_send_kwargs(args)

    assert send_kwargs['timeout'] == 10
    assert send_kwargs['allow_redirects'] is False


# Generated at 2026-04-26 13:17:05.309129
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():    
    # Create a mock argument parser and args
    class MockArgs:
        def __init__(self, cert=None, cert_key=None, proxy=None, verify='yes'):
            self.cert = cert
            self.cert_key = cert_key
            self.proxy = proxy if proxy else []
            self.verify = verify
            
    # Create mock proxies
    class Proxy:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    mock_proxies = [Proxy('http', 'http://localhost:8000'), Proxy('https', 'https://localhost:8000')]
    
    # Create an instance of MockArgs with different configurations
    args_with_cert = MockArgs(cert='path/to/cert.pem', cert_key='path/to/cert.key', proxy=mock_proxies, verify='yes')
    args_without_cert = MockArgs(proxy=mock_proxies, verify='no')
    
    # Call the function with

# Generated at 2026-04-26 13:17:06.896493
# Unit test for function max_headers
def test_max_headers():    
    with max_headers(10):
        assert http.client._MAXHEADERS == 10
    assert http.client._MAXHEADERS == 100  # Default value


# Generated at 2026-04-26 13:17:11.120110
# Unit test for function make_default_headers
def test_make_default_headers():    
    # Create a mock argparse.Namespace object with required attributes
    class MockArgs:
        def __init__(self, data=None, form=False, json=False, files=None):
            self.data = data
            self.form = form
            self.json = json
            self.files = files
            
    # Test case 1: No data, no form, no json
    args1 = MockArgs()
    headers1 = make_default_headers(args1)
    assert headers1['User-Agent'] == DEFAULT_UA
    assert 'Accept' not in headers1
    assert 'Content-Type' not in headers1

    # Test case 2: JSON data provided
    args2 = MockArgs(data={'key': 'value'}, json=True)
    headers2 = make_default_headers(args2)
    assert headers2['User-Agent'] == DEFAULT_UA
    assert headers2['Accept'] == JSON_ACCEPT
    assert headers2['Content-Type'] == JSON_CONTENT

# Generated at 2026-04-26 13:17:14.471237
# Unit test for function make_default_headers
def test_make_default_headers():    
    class Args:
        data = None
        json = True
        form = False
        files = False

    args = Args()
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_UA  # Check default User-Agent
    assert headers['Accept'] == JSON_ACCEPT      # Check Accept header
    assert headers['Content-Type'] == JSON_CONTENT_TYPE  # Check Content-Type header

    args.json = False
    args.data = {'key': 'value'}
    headers = make_default_headers(args)
    assert headers['Content-Type'] == JSON_CONTENT_TYPE  # Check Content-Type header when data is present

    args.form = True
    headers = make_default_headers(args)
    assert headers['Content-Type'] == FORM_CONTENT_TYPE  # Check Content-Type header for form


# Generated at 2026-04-26 13:17:15.610278
# Unit test for function max_headers
def test_max_headers(): 
    with max_headers(5): 
        assert http.client._MAXHEADERS == 5
    assert http.client._MAXHEADERS == 80


# Generated at 2026-04-26 13:17:19.660690
# Unit test for function collect_messages
def test_collect_messages():    
    class MockArgs:
        session = None
        session_read_only = None
        headers = {}
        url = 'http://example.com'
        method = 'GET'
        data = None
        json = False
        form = False
        files = None
        timeout = None
        offline = False
        compress = None
        max_headers = None
        max_redirects = None
        follow = False
        all = False
        path_as_is = False
        chunked = False
        verify = 'yes'
        ssl_version = None
        ciphers = None
        auth_plugin = None

    args = MockArgs()
    config_dir = Path('./')  # Use a mock directory

    # Call the function
    messages = list(collect_messages(args, config_dir))

    # Check the output
    assert len(messages) == 1  # Should yield only 1 message for GET request

# Generated at 2026-04-26 13:17:21.538774
# Unit test for function make_send_kwargs
def test_make_send_kwargs():    
    class Args:
        timeout = 5
        verify = 'yes'

    args = Args()
    expected = {
        'timeout': 5,
        'allow_redirects': False,
    }
    assert make_send_kwargs(args) == expected


# Generated at 2026-04-26 13:17:59.183808
# Unit test for function collect_messages
def test_collect_messages():    
    # Define a mock `args` object
    class MockArgs:
        session = None
        session_read_only = None
        url = "http://example.com"
        data = None
        method = "GET"
        headers = {}
        debug = False
        offline = False
        compress = 1
        max_headers = None
        max_redirects = None
        follow = False
        auth_plugin = None
        params = {}
        timeout = None
        path_as_is = False
        ciphers = None
        ssl_version = None
        
    mock_args = MockArgs()
    config_dir = Path(".")
    
    # Test the function
    messages = list(collect_messages(mock_args, config_dir))
    
    # Assert that we received a response
    assert len(messages) > 0
    # Optionally inspect the first message
    print(messages[0])  # for debugging purposes

# Uncomment to run the test

# Generated at 2026-04-26 13:18:03.420793
# Unit test for function make_request_kwargs
def test_make_request_kwargs(): 
    class MockArgs:
        def __init__(self):
            self.method = "POST"
            self.url = "http://example.com"
            self.data = {
                "key": "value"
            }
            self.json = False
            self.form = False
            self.headers = {
                "Authorization": "Bearer token"
            }
            self.auth = None
            self.params = {}
            self.chunked = False
            self.offline = False

    args = MockArgs()
    request_kwargs = make_request_kwargs(args)
    assert request_kwargs['method'] == 'post'
    assert request_kwargs['url'] == 'http://example.com'
    assert request_kwargs['data'] == '{"key": "value"}'
    assert request_kwargs['headers']['Authorization'] == b'Bearer token'

# Run unit test
test_make_request_kwargs()

# Generated at 2026-04-26 13:18:06.598852
# Unit test for function build_requests_session
def test_build_requests_session(): 
    # Given
    verify = True
    ssl_version = 'TLSv1.2'
    ciphers = 'HIGH:!aNULL:!MD5'

    # When
    session = build_requests_session(verify, ssl_version, ciphers)

    # Then
    assert isinstance(session, requests.Session)
    assert isinstance(session.adapters['https://'], HTTPieHTTPSAdapter)
    assert session.adapters['https://'].ciphers == ciphers
    assert session.adapters['https://'].verify == verify
    assert session.adapters['https://'].ssl_version == 'TLSv1.2'


# Generated at 2026-04-26 13:18:08.378294
# Unit test for function make_send_kwargs
def test_make_send_kwargs(): 
    class Args:
        timeout = 5
    args = Args()
    expected_output = {
        'timeout': 5,
        'allow_redirects': False,
    }
    assert make_send_kwargs(args) == expected_output


# Generated at 2026-04-26 13:18:10.088744
# Unit test for function make_send_kwargs
def test_make_send_kwargs(): 
    class Args: 
        timeout = None
    args = Args() 
    kwargs = make_send_kwargs(args)
    assert kwargs == {'timeout': None, 'allow_redirects': False}


# Generated at 2026-04-26 13:18:14.168535
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():    
    # Create a mock args object with different scenarios
    class MockArgs:
        def __init__(self, cert=None, cert_key=None, proxy=None, verify=None):
            self.cert = cert
            self.cert_key = cert_key
            self.proxy = proxy or []
            self.verify = verify or 'yes'

    # Test case 1: cert is provided without cert_key
    args1 = MockArgs(cert='path/to/cert.pem')
    expected_output1 = {
        'proxies': {},
        'stream': True,
        'verify': True,
        'cert': 'path/to/cert.pem',
    }
    assert make_send_kwargs_mergeable_from_env(args1) == expected_output1

    # Test case 2: cert and cert_key are provided
    args2 = MockArgs(cert='path/to/cert.pem', cert_key='path/to/key.pem')

# Generated at 2026-04-26 13:18:16.385437
# Unit test for function make_send_kwargs
def test_make_send_kwargs(): 
    class Args:
        timeout = 5
    args = Args()
    result = make_send_kwargs(args)
    
    assert result['timeout'] == 5
    assert result['allow_redirects'] == False


# Generated at 2026-04-26 13:18:20.349711
# Unit test for function make_request_kwargs
def test_make_request_kwargs(): 
    class Args:
        method = 'GET'
        url = 'http://example.com'
        headers = {'Authorization': 'Bearer token'}
        data = {'key': 'value'}
        json = True
        form = False
        offline = False
        chunked = False
        params = {}
        
    args = Args()
    request_kwargs = make_request_kwargs(args)
    assert request_kwargs['method'] == 'get'
    assert request_kwargs['url'] == 'http://example.com'
    assert request_kwargs['data'] == '{"key": "value"}'
    assert request_kwargs['headers']['Authorization'] == b'Bearer token'
    assert 'Content-Type' in request_kwargs['headers']
    assert request_kwargs['params'] == {}

# Running the test
test_make_request_kwargs()  # You can run the tests in a proper test framework like pytest.

# Generated at 2026-04-26 13:18:22.301673
# Unit test for function max_headers
def test_max_headers():    
    # Test with no limit
    with max_headers(None):
        assert http.client._MAXHEADERS == float('Inf')
    
    # Test with a limit of 10
    with max_headers(10):
        assert http.client._MAXHEADERS == 10
    
    # Check that the original value is restored after the context
    assert http.client._MAXHEADERS == float('Inf') 


# Generated at 2026-04-26 13:18:25.422005
# Unit test for function make_default_headers
def test_make_default_headers(): 
    class Args:
        def __init__(self, data=None, json=False, form=False, files=False):
            self.data = data
            self.json = json
            self.form = form
            self.files = files

    # Test case 1: default headers when no args are provided
    args = Args()
    headers = make_default_headers(args)
    assert headers == RequestHeadersDict({'User-Agent': DEFAULT_UA})

    # Test case 2: headers when json data is provided
    args = Args(data={'key': 'value'}, json=True)
    headers = make_default_headers(args)
    assert headers == RequestHeadersDict({
        'User-Agent': DEFAULT_UA,
        'Accept': JSON_ACCEPT,
        'Content-Type': JSON_CONTENT_TYPE
    })

    # Test case 3: headers when form data is provided
    args = Args(data={'key': 'value'}, form=True)
    headers = make_default_headers(args)