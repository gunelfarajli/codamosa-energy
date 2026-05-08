

# Generated at 2026-04-26 13:44:42.223370
# Unit test for method queries of class FXRateService
def test_FXRateService_queries(): 
    # Assuming you have a concrete implementation of FXRateService
    class ConcreteFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            # For testing, we could return a dummy rate or None
            return FXRate(ccy1, ccy2, asof, Decimal("1.0")) if ccy1 != ccy2 else None

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            results = []
            for ccy1, ccy2, asof in queries:
                rate = self.query(ccy1, ccy2, asof, strict)
                if strict and rate is None:
                    raise FXRateLookupError(ccy1, ccy2, asof)
                results.append(rate)
            return results

# Generated at 2026-04-26 13:44:47.134134
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():    
    class FXRateServiceImpl(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return None  # Stub implementation

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return [self.query(ccy1, ccy2, asof, strict) for ccy1, ccy2, asof in queries]

    service = FXRateServiceImpl()
    result = service.queries([(Currency("USD"), Currency("EUR"), Date.today())], strict=False)

    assert result == [None], "Expected result to be [None]"  # Example assertion

# Call unit test function
test_FXRateService_queries()    

# Generated at 2026-04-26 13:44:51.838172
# Unit test for method query of class FXRateService
def test_FXRateService_query(): 
    # Mock subclass of FXRateService for testing
    class MockFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            # Example mock implementation
            if ccy1 == Currency("USD") and ccy2 == Currency("EUR"):
                return FXRate(ccy1, ccy2, asof, Decimal("0.85"))
            elif ccy1 == Currency("EUR") and ccy2 == Currency("USD"):
                return FXRate(ccy1, ccy2, asof, Decimal("1.18"))
            if strict:
                raise FXRateLookupError(ccy1, ccy2, asof)
            return None
    
    # Create an instance of the mock service
    service = MockFXRateService()
    
    # Test cases

# Generated at 2026-04-26 13:44:57.695192
# Unit test for method query of class FXRateService
def test_FXRateService_query(): 
    # Test implementation of FXRateService
    from datetime import date
    from decimal import Decimal

    class MockFXRateService(FXRateService):
        def __init__(self):
            self.rates = {
                (Currency("USD"), Currency("EUR")): FXRate(Currency("USD"), Currency("EUR"), date.today(), Decimal("0.85")),
                (Currency("EUR"), Currency("USD")): FXRate(Currency("EUR"), Currency("USD"), date.today(), Decimal("1.1765"))
            }

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return self.rates.get((ccy1, ccy2), None)

    service = MockFXRateService()
    rate = service.query(Currency("USD"), Currency("EUR"), date.today())
    
    assert rate is not None

# Generated at 2026-04-26 13:45:01.203908
# Unit test for method queries of class FXRateService
def test_FXRateService_queries(): 
    """
    Unit test for the queries method of FXRateService.
    """
    
    class MockFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            # Mock implementation for testing purposes
            return FXRate.of(ccy1, ccy2, asof, Decimal("1.5"))

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            results = []
            for ccy1, ccy2, asof in queries:
                try:
                    results.append(self.query(ccy1, ccy2, asof, strict))
                except FXRateLookupError:
                    if strict:
                        raise
                    results.append(None)
            return results

    # Example currencies for testing
    ccy1 = Currency("USD")
    ccy

# Generated at 2026-04-26 13:45:04.782281
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():   
    class DummyFXRateService(FXRateService):
        def __init__(self, rates):
            self.rates = rates
        
        def query(self, ccy1, ccy2, asof, strict=False):
            rate_key = (ccy1, ccy2, asof)
            return self.rates.get(rate_key, None)
        
        def queries(self, queries, strict=False):
            results = []
            for ccy1, ccy2, asof in queries:
                result = self.query(ccy1, ccy2, asof, strict)
                results.append(result)
                if strict and result is None:
                    raise FXRateLookupError(ccy1, ccy2, asof)
            return results
    
    # Prepare test rates

# Generated at 2026-04-26 13:45:09.261707
# Unit test for method queries of class FXRateService
def test_FXRateService_queries(): 
    """
    Testing the `queries` method of `FXRateService`
    """

    class DummyFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return FXRate(ccy1, ccy2, asof, Decimal("1.5"))

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return [self.query(ccy1, ccy2, asof, strict) for ccy1, ccy2, asof in queries]

    # Create an instance of DummyFXRateService
    service = DummyFXRateService()

    # Define sample queries
    queries = [
        (Currency("EUR"), Currency("USD"), Date.today()),
        (Currency("GBP"), Currency("JPY"), Date.today())
    ]

    # Call the queries method
    rates = service.queries(queries)

   

# Generated at 2026-04-26 13:45:14.363864
# Unit test for method query of class FXRateService
def test_FXRateService_query(): 
    # create a mock instance of FXRateService
    class MockFXRateService(FXRateService):
        def __init__(self):
            self.rates = {
                (Currency("EUR"), Currency("USD"), Date.today()): FXRate(Currency("EUR"), Currency("USD"), Date.today(), Decimal("1.2")),
                (Currency("USD"), Currency("EUR"), Date.today()): FXRate(Currency("USD"), Currency("EUR"), Date.today(), Decimal("0.8333"))
            }

        def query(self, ccy1, ccy2, asof, strict=False):
            return self.rates.get((ccy1, ccy2, asof), None)
    
    # create an instance of the mock service
    service = MockFXRateService()

    # Test valid query
    rate = service.query(Currency("EUR"), Currency("USD"), Date.today())

# Generated at 2026-04-26 13:45:18.360587
# Unit test for method query of class FXRateService
def test_FXRateService_query(): 
    service = FXRateService() # This will raise an error because FXRateService is abstract, use a concrete subclass instead. 

    ccy1 = Currency("EUR")
    ccy2 = Currency("USD")
    asof = Date.today()

    # Test for valid currency pair and date
    rate = service.query(ccy1, ccy2, asof)
    assert rate is not None, "Expected a valid rate for EUR/USD"
    
    # Test for invalid currency pair
    invalid_ccy = Currency("INVALID")
    try:
        service.query(invalid_ccy, ccy2, asof)
    except ValueError as e:
        assert str(e) == "CCY/1 must be of type `Currency`.", "Expected ValueError for invalid currency"
    
    # Test for zero or negative rate

# Generated at 2026-04-26 13:45:22.563050
# Unit test for method query of class FXRateService
def test_FXRateService_query(): 
    service = MyFXRateService() # Assuming MyFXRateService is a concrete implementation of FXRateService
    # Test valid query
    ccy1 = Currency("EUR")
    ccy2 = Currency("USD")
    asof = Date.today() # or any other valid date
    rate = service.query(ccy1, ccy2, asof)
    assert rate is not None, "Expected a valid rate"

    # Test invalid query
    invalid_ccy1 = Currency("INVALID")
    invalid_ccy2 = Currency("INVALID")
    invalid_rate = service.query(invalid_ccy1, invalid_ccy2, asof, strict=True)
    assert invalid_rate is None, "Expected None for invalid rate lookup"
    
    # Test rate lookup with strict mode
    try:
        service.query(ccy1, invalid_ccy2, asof, strict=True)
    except FXRateLookupError as e:
        assert str(e)

# Generated at 2026-04-26 13:45:30.022719
# Unit test for method queries of class FXRateService
def test_FXRateService_queries(): 
    """
    Test method queries of FXRateService class.
    """

    # Sample implementation of FXRateService
    class MockFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return FXRate(ccy1, ccy2, asof, Decimal("2.0"))

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return [self.query(*query, strict) for query in queries]

    # Create mock FXRateService instance
    mock_service = MockFXRateService()

    # Define inputs
    queries = [
        (Currency("EUR"), Currency("USD"), Date.today()),
        (Currency("GBP"), Currency("EUR"), Date.today()),
    ]

    # Get results from queries method
    results = list(mock_service.queries(queries))

    # Expected results

# Generated at 2026-04-26 13:45:34.397615
# Unit test for method query of class FXRateService
def test_FXRateService_query():    
    """
    Unit test for the query method of FXRateService.
    """
    # Create a mock implementation of FXRateService
    class MockFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            # Mock behavior: return a fixed exchange rate for a specific currency pair
            if ccy1 == "USD" and ccy2 == "EUR":
                return FXRate(ccy1, ccy2, asof, Decimal("0.85"))
            return None

    # Create an instance of the mock service
    service = MockFXRateService()

    # Test valid query
    result = service.query("USD", "EUR", Date.today())
    assert result is not None, "Expected a valid FXRate"
    assert result.ccy1 == "USD"

# Generated at 2026-04-26 13:45:38.573041
# Unit test for method queries of class FXRateService
def test_FXRateService_queries(): 
    class FXRateMockService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            # Mocking a query response for demonstration purposes
            if ccy1 == Currency('USD') and ccy2 == Currency('EUR'):
                return FXRate(ccy1, ccy2, asof, Decimal('0.85'))
            return None

        def queries(self, queries: Iterable[Tuple[Currency, Currency, Date]], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return [self.query(ccy1, ccy2, asof, strict) for ccy1, ccy2, asof in queries]
    
    # Mock currencies for testing
    mock_usd = Currency('USD')
    mock_eur = Currency('EUR')

# Generated at 2026-04-26 13:45:42.221444
# Unit test for method query of class FXRateService
def test_FXRateService_query(): 
    service = FXRateService()  # should raise error since FXRateService is abstract
    assert isinstance(service, FXRateService) == False  # should not be instantiable

# Generated at 2026-04-26 13:45:46.113168
# Unit test for method queries of class FXRateService
def test_FXRateService_queries(): 
    # Creating a mock implementation of FXRateService for testing
    class MockFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate.of(ccy1, ccy2, asof, Decimal('1.5'))  # Return a mock rate for testing

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return [self.query(ccy1, ccy2, asof, strict) for ccy1, ccy2, asof in queries]

    # Create a mock exchange rate service
    mock_service = MockFXRateService()

    # Define a list of currency queries

# Generated at 2026-04-26 13:45:50.141574
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():    
    """
    Unit test for the `queries` method of `FXRateService`.
    """
    class MockFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            # Mock implementation for testing
            if ccy1 == Currency("USD") and ccy2 == Currency("EUR"):
                return FXRate(ccy1, ccy2, asof, Decimal("0.85"))
            return None

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            # Mock implementation for testing
            return [self.query(ccy1, ccy2, asof, strict) for ccy1, ccy2, asof in queries]

    # Creating a mock service instance
    mock_service = MockFXRateService()

    # Define

# Generated at 2026-04-26 13:45:55.789576
# Unit test for method query of class FXRateService
def test_FXRateService_query():        
    # Assuming we have a concrete implementation of FXRateService
    class MockFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal('1.5'))
        
        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return [self.query(*query) for query in queries]

    # Instantiate the mock service
    service = MockFXRateService()
    
    # Prepare sample currencies and date
    ccy1 = Currency("EUR")
    ccy2 = Currency("USD")
    date = Date.today()
    
    # Test the query method
    rate = service.query(ccy1, ccy2, date)
    
    assert rate.ccy1 == ccy

# Generated at 2026-04-26 13:46:00.253011
# Unit test for method query of class FXRateService
def test_FXRateService_query(): 
    class TestFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currency("USD") and ccy2 == Currency("EUR") and asof == Date.today():
                return FXRate(ccy1, ccy2, asof, Decimal("0.85"))
            return None
            
    service = TestFXRateService()
    
    # Test for known rate
    rate = service.query(Currency("USD"), Currency("EUR"), Date.today())
    assert rate is not None, "Expected a rate to be returned"
    assert rate.value == Decimal("0.85"), "Expected rate value to be 0.85"
    
    # Test for unknown rate
    rate = service.query(Currency("USD"), Currency("GBP"), Date.today())

# Generated at 2026-04-26 13:46:06.286162
# Unit test for method queries of class FXRateService
def test_FXRateService_queries(): 
    """
    Unit test for queries method of FXRateService class.
    """

    # Step 1: Arrange
    # Create a mock FX rate service
    class MockFXRateService(FXRateService):

        def query(self, ccy1, ccy2, asof, strict=False):
            # Mock implementation
            if ccy1 == Currency("EUR") and ccy2 == Currency("USD"):
                return FXRate(ccy1, ccy2, asof, Decimal("1.2"))
            if ccy1 == Currency("GBP") and ccy2 == Currency("JPY"):
                return FXRate(ccy1, ccy2, asof, Decimal("150"))
            return None


# Generated at 2026-04-26 13:46:10.542605
# Unit test for method query of class FXRateService
def test_FXRateService_query(): 
    # Create a subclass for testing
    class TestFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            # Mocked response for testing
            if ccy1 == Currency("USD") and ccy2 == Currency("EUR") and asof == Date.today():
                return FXRate.of(ccy1, ccy2, asof, Decimal("0.85"))
            return None  # Simulate rate not found

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return (self.query(ccy1, ccy2, asof, strict) for ccy1, ccy2, asof in queries)

    service = TestFXRateService()

    # Test for a known exchange rate
    rate = service.query

# Generated at 2026-04-26 13:46:19.267258
# Unit test for method query of class FXRateService
def test_FXRateService_query(): 
    pass

# Generated at 2026-04-26 13:46:26.357667
# Unit test for method query of class FXRateService
def test_FXRateService_query(): 
    service = FXRateService()  # Instantiate FXRateService
    ccy1 = Currency("EUR")  # Create first currency (Euro)
    ccy2 = Currency("USD")  # Create second currency (US Dollar)
    asof = Date()  # Create date object
    fx_rate = service.query(ccy1, ccy2, asof)  # Call query method
    
    # Check if fx_rate has the expected properties
    assert isinstance(fx_rate, FXRate)  # Check if result is an instance of FXRate
    assert fx_rate.ccy1 == ccy1  # Check if first currency is correct
    assert fx_rate.ccy2 == ccy2  # Check if second currency is correct
    assert fx_rate.date == asof  # Check if date is correct

# Run the unit test
test_FXRateService_query()

# Generated at 2026-04-26 13:46:30.857851
# Unit test for method queries of class FXRateService
def test_FXRateService_queries(): 
    """
    Unit test for the queries method of the FXRateService class.
    """
    # Create a mock FXRateService
    class MockFXRateService(FXRateService):
        def __init__(self, rates):
            self.rates = rates

        def query(self, ccy1, ccy2, asof, strict=False):
            key = (ccy1, ccy2, asof)
            if key in self.rates:
                return self.rates[key]
            if strict:
                raise FXRateLookupError(ccy1, ccy2, asof)
            return None

        def queries(self, queries, strict=False):
            results = []

# Generated at 2026-04-26 13:46:35.364396
# Unit test for method query of class FXRateService
def test_FXRateService_query(): 
    # Create a mock of FXRateService
    class FXRateServiceMock(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            if ccy1 == Currency('EUR') and ccy2 == Currency('USD'):
                return FXRate(ccy1, ccy2, asof, Decimal('1.2'))
            elif strict:
                raise FXRateLookupError(ccy1, ccy2, asof)
            return None

    service = FXRateServiceMock()
    
    # Test case 1: Valid query
    assert service.query(Currency('EUR'), Currency('USD'), Date.today()) == FXRate(Currency('EUR'), Currency('USD'), Date.today(), Decimal('1.2'))

    # Test case 2: Invalid query without strict mode
    assert service.query(Currency('EUR'), Currency('GBP'), Date.today()) is None

    # Test case 3

# Generated at 2026-04-26 13:46:39.956250
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():  # Mocking service for demonstration
    class MockFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            # For simplicity, just return a fake rate
            return FXRate(ccy1, ccy2, asof, Decimal("1.0"))

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return (self.query(ccy1, ccy2, asof, strict) for ccy1, ccy2, asof in queries)

    # Create a mock FX rate service
    service = MockFXRateService()

    # Define test cases
    test_cases = [
        (Currencies["EUR"], Currencies["USD"], Date.today()),
        (Currencies["GBP"], Currencies["JPY"], Date.today()),
    ]



# Generated at 2026-04-26 13:46:44.576897
# Unit test for method query of class FXRateService
def test_FXRateService_query(): 
    # Create a mock implementation of FXRateService
    class MockFXRateService(FXRateService):
        def __init__(self, rates):
            self.rates = rates

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return self.rates.get((ccy1, ccy2, asof), None)

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return (self.query(ccy1, ccy2, asof, strict) for ccy1, ccy2, asof in queries)

    # Setup mock data

# Generated at 2026-04-26 13:46:48.707865
# Unit test for method queries of class FXRateService
def test_FXRateService_queries(): 
    service = FXRateService()  # Create an instance of FXRateService
    queries = [
        (Currency("USD"), Currency("EUR"), Date.today()), 
        (Currency("EUR"), Currency("GBP"), Date.today())
    ]
    
    rates = service.queries(queries)
    
    assert isinstance(rates, Iterable), "The rates returned should be iterable"
    assert len(rates) == len(queries), "The number of rates returned should match the number of queries"

    for rate in rates:
        assert isinstance(rate, FXRate) or rate is None, "Rates should be instances of FXRate or None"  # Validate the type of each rate

# Run test
test_FXRateService_queries()  # Call the test function

# Generated at 2026-04-26 13:46:53.494557
# Unit test for method query of class FXRateService
def test_FXRateService_query(): 
    # Create a mock implementation of FXRateService for testing purposes
    class MockFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            # Mocked data: Assume the exchange rate for USD/EUR as of today is 0.85
            if ccy1.symbol == 'USD' and ccy2.symbol == 'EUR' and asof == Date.today():
                return FXRate(ccy1, ccy2, asof, Decimal('0.85'))
            # If strict is True, raise an error for any other queries
            if strict:
                raise FXRateLookupError(ccy1, ccy2, asof)
            return None

    # Initialize the mocked service
    service = MockFXRateService()

    # Test querying the exchange rate for USD to EUR

# Generated at 2026-04-26 13:46:59.277324
# Unit test for method queries of class FXRateService
def test_FXRateService_queries(): 
    """
    Test for the `queries` method of the `FXRateService` abstract class.
    
    It verifies that when provided with a list of currency pairs and dates, the method returns
    the expected foreign exchange rates.
    
    This is a stub implementation as the actual behavior will depend on the concrete subclass of 
    `FXRateService`.
    """
    from decimal import Decimal
    from pypara.currencies import Currencies
    
    class ConcreteFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            # Stub implementation with some dummy data
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"]:
                return FXRate(ccy1, ccy2, asof, Decimal('1.2'))
            return None


# Generated at 2026-04-26 13:47:03.721947
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():    
    # Mock implementation of FXRateService
    class FXRateServiceMock(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal("1.5"))  # Dummy rate for testing

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return [self.query(ccy1, ccy2, asof, strict) for ccy1, ccy2, asof in queries]

    # Create a mock service
    mock_service = FXRateServiceMock()

    # Define some currency pairs and dates for testing

# Generated at 2026-04-26 13:47:24.262663
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():    
    # Assuming we have a concrete implementation of FXRateService
    class TestFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof:
                return FXRate.of(ccy1, ccy2, asof, Decimal("1.1"))
            return None

        def queries(self, queries: Iterable[Tuple[Currency, Currency, Date]], strict: bool = False) -> Iterable[Optional[FXRate]]:
            rates = []
            for ccy1, ccy2, asof in queries:
                rate = self.query(ccy1, ccy2, asof, strict)
                rates.append(rate)
            return rates

    # Create an instance of the test FX rate service
   

# Generated at 2026-04-26 13:47:28.687408
# Unit test for method query of class FXRateService
def test_FXRateService_query(): 
    # Sample implementation of FXRateService for testing
    class MockFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currency("USD") and ccy2 == Currency("EUR"):
                return FXRate(ccy1, ccy2, asof, Decimal("0.85"))
            elif strict:
                raise FXRateLookupError(ccy1, ccy2, asof)
            return None
    
    # Creating an instance of MockFXRateService
    service = MockFXRateService()
    
    # Test cases
    assert service.query(Currency("USD"), Currency("EUR"), Date.today()) == FXRate(Currency("USD"), Currency("EUR"), Date.today(), Decimal("0.85"))
    assert service.query(Currency("USD"), Currency("JPY"), Date.today())

# Generated at 2026-04-26 13:47:34.676538
# Unit test for method queries of class FXRateService
def test_FXRateService_queries(): 
    rate_service = FXRateService()  # Instantiate a concrete subclass of FXRateService here
    
    # Prepare test data
    queries = [
        (Currency("USD"), Currency("EUR"), Date("2022-01-01")),
        (Currency("EUR"), Currency("GBP"), Date("2022-01-02")),
        (Currency("GBP"), Currency("USD"), Date("2022-01-03")),
    ]
    
    # Call the method to test
    results = list(rate_service.queries(queries, strict=True))
    
    # Perform assertions
    assert len(results) == len(queries), "The number of results should match the number of queries."
    for query, result in zip(queries, results):
        ccy1, ccy2, asof = query
        if result is None:
            assert strict, f"Expected result for query {query} should not be None when strict is True."