

# Generated at 2026-04-26 13:42:28.888864
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__(): 
    def mock_read_initial_balances(period: DateRange) -> InitialBalances: 
        return {Account("Cash"): Balance(period.since, Quantity(Decimal(1000)))}
    
    # Create a mock period
    mock_period = DateRange(datetime.date(2021, 1, 1), datetime.date(2021, 12, 31))
    
    # Call the function and verify
    result = mock_read_initial_balances(mock_period)
    
    assert isinstance(result, dict)  # Result should be a dictionary
    assert len(result) == 1  # There should be one account
    assert result[Account("Cash")].value == Quantity(Decimal(1000))  # Check the balance


# Generated at 2026-04-26 13:42:31.525844
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():  
    """Test case for ReadInitialBalances.__call__() method."""
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {Account(name="Cash"): Balance(period.since, Quantity(Decimal("1000.00")))}
    
    read_initial_balances = MockReadInitialBalances()
    period = DateRange(datetime.date(2021, 1, 1), datetime.date(2021, 12, 31))
    result = read_initial_balances(period)
    assert result == {Account(name="Cash"): Balance(period.since, Quantity(Decimal("1000.00")))}


# Generated at 2026-04-26 13:42:32.686012
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__(): 
    assert isinstance(GeneralLedgerProgram.__call__, Protocol)
    assert GeneralLedgerProgram.__call__ is not None


# Generated at 2026-04-26 13:42:37.055170
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__(): 
    # Define a mock implementation of ReadInitialBalances
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account("Cash"): Balance(period.since, Quantity(Decimal(1000))),
                Account("Revenue"): Balance(period.since, Quantity(Decimal(0))),
            }

    # Define a mock implementation of ReadJournalEntries
    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> Iterable[JournalEntry]:
            return [
                JournalEntry(date=datetime.date(2021, 1, 1), description="Sale", postings=[
                    Posting(account=Account("Cash"), amount=Amount(Decimal(200)), direction=1),
                    Posting(account=Account("Revenue"), amount=Amount(Decimal(200)), direction=-1),
                ]),
            ]

    # Create instances of the mock implementations
    read_initial_balances = MockReadInitialBalances()
    read

# Generated at 2026-04-26 13:42:39.944117
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():  
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {Account("Cash"): Balance(period.since, Quantity(Decimal(100)))}

    mock = MockReadInitialBalances()
    period = DateRange(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31))
    result = mock(period)
    expected = {Account("Cash"): Balance(period.since, Quantity(Decimal(100)))}
    assert result == expected, f"Expected {expected}, but got {result}"


# Generated at 2026-04-26 13:42:45.918867
# Unit test for function build_general_ledger
def test_build_general_ledger(): 
    # Create a date range for the accounting period
    period = DateRange(datetime.date(2022, 1, 1), datetime.date(2022, 12, 31))

    # Create some sample initial balances
    initial_balances = {
        Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00"))),
        Account("Inventory"): Balance(period.since, Quantity(Decimal("500.00"))),
    }

    # Create some sample journal entries

# Generated at 2026-04-26 13:42:49.791239
# Unit test for method add of class Ledger
def test_Ledger_add(): 
    # Prepare test data
    account = Account("Test Account")
    initial_balance = Balance(datetime.date.today(), Quantity(Decimal(100)))
    ledger = Ledger(account, initial_balance)

    # Create a sample posting
    posting = Posting(account=account, amount=Amount(Decimal(50)), direction=1, date=datetime.date.today(), journal=None)

    # Add the posting to the ledger
    ledger_entry = ledger.add(posting)

    # Assertions
    assert ledger_entry.balance.value == Decimal(150)  # initial balance + posting amount
    assert len(ledger.entries) == 1  # there should be one entry in the ledger
    assert ledger.entries[0].posting == posting  # the posting in the ledger entry should match the added posting

# Generated at 2026-04-26 13:42:53.265810
# Unit test for function build_general_ledger
def test_build_general_ledger(): 
    """
    Test for the build_general_ledger function.
    """
    from datetime import date
    
    # Creating some mock data for testing
    period = DateRange(date(2022, 1, 1), date(2022, 12, 31))
    initial_balances = {
        Account(name="Cash"): Balance(period.since, Quantity(Decimal(1000))),
        Account(name="Revenue"): Balance(period.since, Quantity(Decimal(0))),
    }
    

# Generated at 2026-04-26 13:42:57.613337
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__(): 
    # Create a mock implementation of ReadInitialBalances
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {Account("Mock Account"): Balance(period.since, Quantity(Decimal("100.00")))}

    # Instantiate the mock class
    mock_read_initial_balances = MockReadInitialBalances()

    # Define a sample period
    period = DateRange(datetime.date(2022, 1, 1), datetime.date(2022, 12, 31))

    # Call the __call__ method
    result = mock_read_initial_balances(period)

    # Validate the result
    assert isinstance(result, dict)
    assert len(result) == 1
    assert "Mock Account" in result
    assert result["Mock Account"].value == Quantity(Decimal("100.00"))


# Generated at 2026-04-26 13:43:01.914298
# Unit test for function build_general_ledger
def test_build_general_ledger():    
    from datetime import date
    from collections import defaultdict

    # Create mock data
    class MockAccount:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return self.name

    class MockJournalEntry:
        def __init__(self, date, postings):
            self.date = date
            self.postings = postings

    class MockPosting:
        def __init__(self, account, amount, direction):
            self.account = account
            self.amount = amount
            self.direction = direction

        @property
        def is_debit(self):
            return self.direction == 1

        @property
        def is_credit(self):
            return self.direction == -1

    # Create mock data
    account_a = MockAccount("Account A")
    account_b = MockAccount("Account B")
    

# Generated at 2026-04-26 13:43:09.792615
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__(): 
    """
    Test case for method __call__ of class GeneralLedgerProgram.
    """

    # Create a mock implementation of ReadInitialBalances
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account("Account1"): Balance(period.since, Quantity(Decimal(100.00))),
                Account("Account2"): Balance(period.since, Quantity(Decimal(200.00))),
            }

    # Create a mock implementation of ReadJournalEntries

# Generated at 2026-04-26 13:43:13.322127
# Unit test for function build_general_ledger
def test_build_general_ledger(): 
    from datetime import date
    
    # Define mock data
    period = DateRange(date(2022, 1, 1), date(2022, 12, 31))
    initial = {Account("Cash"): Balance(period.since, Quantity(Decimal(1000)))}
    journal = [
        JournalEntry(date(2022, 1, 5), "Initial sale", [Posting(Account("Sales"), Amount(Decimal(200)), 1)]),
        JournalEntry(date(2022, 1, 10), "Initial purchase", [Posting(Account("Cash"), Amount(Decimal(-200)), -1)])
    ]

    # Build general ledger
    ledger = build_general_ledger(period, journal, initial)
    
    # Verify the results
    assert len(ledger.ledgers) == 1  # One ledger for Cash

# Generated at 2026-04-26 13:43:17.099168
# Unit test for function build_general_ledger
def test_build_general_ledger(): 
    # Define a date range
    period = DateRange(datetime.date(2022, 1, 1), datetime.date(2022, 1, 31))
    
    # Define initial balances
    initial_balances = {
        Account("Cash"): Balance(period.since, Quantity(Decimal(1000))),
        Account("Accounts Receivable"): Balance(period.since, Quantity(Decimal(500))),
    }
    
    # Define journal entries

# Generated at 2026-04-26 13:43:20.494301
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__(): 
    from datetime import date

    class TestReadInitialBalances: 
        def __call__(self, period: DateRange) -> InitialBalances: 
            return {Account(name="Test Account"): Balance(start=date(2021, 1, 1), value=Quantity(amount=Decimal('100.00')))} 

    read_initial_balances = TestReadInitialBalances()
    period = DateRange(since=date(2021, 1, 1), until=date(2021, 12, 31))
    initial_balances = read_initial_balances(period)

    assert len(initial_balances) == 1
    assert list(initial_balances.keys())[0].name == "Test Account"
    assert initial_balances[list(initial_balances.keys())[0]].value == Quantity(amount=Decimal('100.00')) 

# Generated at 2026-04-26 13:43:24.334440
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():    
    # Mock implementations of the required interfaces
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {Account("Cash"): Balance(period.since, Quantity(Decimal(100)))}

    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> Iterable[JournalEntry]:
            return [JournalEntry(date=datetime.date(2021, 1, 1), postings=[Posting(Account("Cash"), Amount(Decimal(50)), 1)])]            

    read_initial_balances = MockReadInitialBalances()
    read_journal_entries = MockReadJournalEntries()
    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)

    # Define the period for testing
    test_period = DateRange(datetime.date(2021, 1, 1), datetime.date(2021, 1, 31))
    
    # Run the program
    ledger

# Generated at 2026-04-26 13:43:28.172812
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program(): 
    """
    Tests the functionality of the compile_general_ledger_program.
    """
    
    # Mock implementation of ReadInitialBalances
    def mock_read_initial_balances(period: DateRange) -> InitialBalances:
        return {
            Account("Cash"): Balance(period.since, Quantity(Decimal(1000))),
            Account("Revenue"): Balance(period.since, Quantity(Decimal(500))),
        }

    # Mock implementation of ReadJournalEntries
    def mock_read_journal_entries(period: DateRange) -> Iterable[JournalEntry]:
        return [
            JournalEntry(datetime.date(2022, 1, 5), [Posting(Account("Cash"), Amount(Decimal(200)), 1)], "Cash Sale"),
            JournalEntry(datetime.date(2022, 1, 10), [Posting(Account("Revenue"), Amount(Decimal(200)), -1)], "Revenue Recognition"),
        ]

    # Compile the program

# Generated at 2026-04-26 13:43:32.078097
# Unit test for function build_general_ledger
def test_build_general_ledger(): 
    """
    Test the build_general_ledger function.
    """
    from .accounts import Account
    from .journaling import JournalEntry, Posting

    # Create sample data
    period = DateRange(datetime.date(2023, 1, 1), datetime.date(2023, 1, 31))
    account_a = Account(name="Account A", account_type="Asset")
    account_b = Account(name="Account B", account_type="Liability")
    
    initial_balances = {
        account_a: Balance(period.since, Quantity(Decimal('1000.00'))),
        account_b: Balance(period.since, Quantity(Decimal('2000.00')))
    }

    postings = [
        Posting(account=account_a, amount=Amount(Decimal('500.00')), direction=1), # Debit
        Posting(account=account_b, amount=Amount(Decimal('300.00')), direction=-1) # Credit
    ]

    journal

# Generated at 2026-04-26 13:43:35.138432
# Unit test for function build_general_ledger
def test_build_general_ledger():    
    # Define test inputs for the function
    period = DateRange(datetime.date(2022, 1, 1), datetime.date(2022, 12, 31))
    journal = [
        # Create mock journal entries with postings
    ]
    initial = {
        # Define initial balances with mock accounts and balances
    }

    # Call the function with test inputs
    ledger = build_general_ledger(period, journal, initial)

    # Validate the output
    assert isinstance(ledger, GeneralLedger)
    assert ledger.period == period
    assert len(ledger.ledgers) == len(initial)  # Checks number of ledgers corresponds to initial balances
    
    # Additional assertions can check specific ledger entries, balances, etc.

# Uncomment to run the test
# test_build_general_ledger()    

# Generated at 2026-04-26 13:43:38.432656
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__(): 
    read_initial_balances = lambda period: {Account("Cash"): Balance(period.since, Quantity(Decimal(1000)))}
    read_journal_entries = lambda period: [
        JournalEntry(datetime.date(2022, 1, 1), [Posting(Account("Cash"), Quantity(Decimal(100)), 1)]),
        JournalEntry(datetime.date(2022, 1, 2), [Posting(Account("Revenue"), Quantity(Decimal(200)), -1)]),
    ]
    
    general_ledger_program = compile_general_ledger_program(read_initial_balances, read_journal_entries)
    period = DateRange(datetime.date(2022, 1, 1), datetime.date(2022, 1, 31))
    
    general_ledger = general_ledger_program(period)
    
    assert isinstance(general_ledger, GeneralLedger)
    assert len(general_ledger.ledgers) == 2  # Cash and Revenue accounts should be in

# Generated at 2026-04-26 13:43:43.146495
# Unit test for method add of class Ledger
def test_Ledger_add(): 
    # Setup
    account = Account("Test Account")
    initial_balance = Balance(datetime.date(2022, 1, 1), Quantity(Decimal(1000)))
    ledger = Ledger(account, initial_balance)

    # Create a posting
    posting = Posting(account, Amount(Decimal(200), "USD"), datetime.date(2022, 1, 5), True)
    
    # Execute
    ledger_entry = ledger.add(posting)
    
    # Assert
    assert ledger_entry.balance == Quantity(Decimal(1200))
    assert len(ledger.entries) == 1
    assert ledger.entries[0] == ledger_entry
    assert ledger.entries[0].posting == posting

# Generated at 2026-04-26 13:43:50.448477
# Unit test for method add of class Ledger
def test_Ledger_add():  
    from .journaling import Posting, JournalEntry

    # Setup test data
    account = Account("Test Account")
    initial_balance = Balance(datetime.date.today(), Quantity(Decimal(100)))
    ledger = Ledger(account, initial_balance)

    posting_debit = Posting(account=account, amount=Amount(Decimal(50)), direction=1, journal=JournalEntry([], datetime.date.today(), "Test Entry"))
    posting_credit = Posting(account=account, amount=Amount(Decimal(30)), direction=-1, journal=JournalEntry([], datetime.date.today(), "Test Entry"))

    # Add a debit posting
    entry_debit = ledger.add(posting_debit)

    # Check that the balance is updated correctly
    assert entry_debit.balance.value == 150, f"Expected balance: 150, got {entry_debit.balance.value}"

    # Add a credit posting
    entry_credit = ledger.add(posting_credit)

    # Check that the balance is updated

# Generated at 2026-04-26 13:43:53.921839
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():    
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {}

    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> List[JournalEntry[int]]:
            return []

    read_initial_balances = MockReadInitialBalances()
    read_journal_entries = MockReadJournalEntries()

    # Compile the general ledger program
    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)

    # Create a date range for testing
    period = DateRange(datetime.date(2021, 1, 1), datetime.date(2021, 12, 31))

    # Call the program with the test period
    general_ledger = program(period)

    # Check that the output is an instance of GeneralLedger
    assert isinstance(general_ledger, GeneralLedger)

    # Check that the period is as expected
    assert general_ledger.period

# Generated at 2026-04-26 13:43:58.689923
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__(): 
    """
    Test for ReadInitialBalances.__call__
    """

    # Sample implementation of ReadInitialBalances
    class SampleReadInitialBalances:
        def __call__(self, period):
            # Simple return of initial balances for testing
            return {Account("Sample Account"): Balance(period.since, Quantity(Decimal(100)))}

    # Create instance for testing
    read_initial_balances = SampleReadInitialBalances()

    # Define a test DateRange
    test_period = DateRange(datetime.date(2022, 1, 1), datetime.date(2022, 12, 31))

    # Call the method
    result = read_initial_balances(test_period)

    # Expected result
    expected_result = {Account("Sample Account"): Balance(test_period.since, Quantity(Decimal(100)))}

    # Assert the result matches the expected outcome
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

# Generated at 2026-04-26 13:44:02.234016
# Unit test for function build_general_ledger
def test_build_general_ledger(): 
    # Define a mock period
    period = DateRange(datetime.date(2022, 1, 1), datetime.date(2022, 12, 31))
    
    # Create mock journal entries and initial balances
    journal = [
        JournalEntry(date=datetime.date(2022, 1, 10), postings=[Posting(account=Account("Cash"), amount=Decimal("1000"), direction=1)]),
        JournalEntry(date=datetime.date(2022, 2, 15), postings=[Posting(account=Account("Revenue"), amount=Decimal("1000"), direction=-1)]),
    ]
    
    initial_balances = {
        Account("Cash"): Balance(amount=Quantity(Decimal("0"))),
        Account("Revenue"): Balance(amount=Quantity(Decimal("0"))),
    }
    
    # Build the general ledger
    general_ledger = build_general_ledger(period, journal, initial_balances)

    # Check the results

# Generated at 2026-04-26 13:44:05.966540
# Unit test for method add of class Ledger
def test_Ledger_add():    
    # Create mock objects
    account = Account(name='Test Account')
    initial_balance = Balance(period=datetime.date(2021, 1, 1), value=Quantity(Decimal(100)))
    ledger = Ledger(account=account, initial=initial_balance)
    
    # Create a posting
    posting = Posting(account=account, amount=Decimal(50), direction=1, journal=JournalEntry(date=datetime.date(2021, 1, 2), description='Test Entry'))

    # Add posting to ledger and get the resulting entry
    ledger_entry = ledger.add(posting)

    # Check the balance of the ledger entry
    assert ledger_entry.balance.value == Quantity(Decimal(150))

    # Check the number of entries in the ledger
    assert len(ledger.entries) == 1

    # Check attributes of the created ledger entry
    assert ledger_entry.posting == posting
    assert ledger_entry.ledger == ledger
    assert ledger_entry

# Generated at 2026-04-26 13:44:09.586326
# Unit test for function build_general_ledger
def test_build_general_ledger(): 
    from datetime import date
    from typing import List
    
    class MockAccount:
        pass  # Mocking Account class
    
    class MockPosting:
        def __init__(self, account, amount, direction, date):
            self.account = account
            self.amount = amount
            self.direction = direction
            self.date = date
        
        @property
        def is_debit(self):
            return self.direction == "debit"
        
        @property
        def is_credit(self):
            return self.direction == "credit"

    class MockJournalEntry:
        def __init__(self, date, postings):
            self.date = date
            self.postings = postings
            
    # Create mock data
    account1 = MockAccount()
    account2 = MockAccount()
    
    initial_balances = {
        account1: Balance(period.since, Quantity(Decimal(100))),
        account2: Balance(period.since, Quantity(Decimal(200))),
    }

   

# Generated at 2026-04-26 13:44:11.698256
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__(): 
    program = GeneralLedgerProgram() 
    period = DateRange(datetime.date(2022, 1, 1), datetime.date(2022, 12, 31))
    general_ledger = program(period)
    assert isinstance(general_ledger, GeneralLedger)
    assert general_ledger.period == period
    assert len(general_ledger.ledgers) > 0
    ### Add more assertions as needed


# Generated at 2026-04-26 13:44:15.429070
# Unit test for method add of class Ledger
def test_Ledger_add(): 
    # Arrange
    account = Account("Test Account")
    initial_balance = Balance("2022-01-01", Quantity(Decimal(100)))
    ledger = Ledger(account, initial_balance)

    posting = Posting(account, Amount(Decimal(50)), datetime.date(2022, 1, 2), 1)

    # Act
    entry = ledger.add(posting)

    # Assert
    assert entry.balance == Quantity(Decimal(150))  # Initial balance + posting amount
    assert len(ledger.entries) == 1  # Should contain one entry
    assert ledger.entries[0].posting == posting  # The added entry should match the posting


# Generated at 2026-04-26 13:44:20.220871
# Unit test for function build_general_ledger
def test_build_general_ledger(): 
    period = DateRange(datetime.date(2021, 1, 1), datetime.date(2021, 12, 31))
    initial_balances = {Account("Cash"): Balance(period.since, Quantity(Decimal("1000")))}
    journal = [
        JournalEntry(date=datetime.date(2021, 1, 15), postings=[Posting(Account("Cash"), Amount(Decimal("200")), 1)]),
        JournalEntry(date=datetime.date(2021, 2, 15), postings=[Posting(Account("Cash"), Amount(Decimal("300")), 1)]),
        JournalEntry(date=datetime.date(2021, 3, 15), postings=[Posting(Account("Cash"), Amount(Decimal("150")), -1)]),
    ]
    
    ledger = build_general_ledger(period, journal, initial_balances)
    
    assert ledger.period == period
    assert len(ledger.ledgers) == 1
    assert ledger.led

# Generated at 2026-04-26 13:44:22.380228
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():   
    pass  # Implement test logic here