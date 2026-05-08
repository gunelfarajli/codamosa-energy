

# Generated at 2026-04-26 13:12:54.199278
# Unit test for function bump_version
def test_bump_version(): 
    assert bump_version("1.2.3") == "1.2.4"
    assert bump_version("1.2.3", position=1) == "1.3"
    assert bump_version("1.3.4", position=0) == "2.0"
    assert bump_version("1.2.3", pre_release="a") == "1.2.4a0"
    assert bump_version("1.2.4a0", pre_release="a") == "1.2.4a1"
    assert bump_version("1.2.4a1", pre_release="b") == "1.2.4b0"
    assert bump_version("1.2.4a1") == "1.2.4"
    assert bump_version("1.2.4b0") == "1.2.4"

# Generated at 2026-04-26 13:13:00.780276
# Unit test for function bump_version
def test_bump_version():    
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2026-04-26 13:13:09.985435
# Unit test for function bump_version
def test_bump_version(): 
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2026-04-26 13:13:13.934000
# Unit test for function bump_version
def test_bump_version(): 
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2026-04-26 13:13:17.964512
# Unit test for function bump_version
def test_bump_version():  
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2026-04-26 13:13:23.034249
# Unit test for function bump_version
def test_bump_version(): 
    # Test cases for bump_version function
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2026-04-26 13:13:27.459799
# Unit test for function bump_version
def test_bump_version():    
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2026-04-26 13:13:32.124168
# Unit test for function bump_version
def test_bump_version():    
    assert bump_version('1.2.2') == '1.2.3'  # Simple patch incrementation
    assert bump_version('1.2.3', position=1) == '1.3'  # Minor incrementation
    assert bump_version('1.3.4', position=0) == '2.0'  # Major incrementation
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'  # Pre-release version
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'  # Incrementing pre-release
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'  # Changing pre-release type

# Generated at 2026-04-26 13:13:36.860622
# Unit test for function bump_version
def test_bump_version():  # pragma: no cover
    assert bump_version('1.0.0') == '1.0.1'
    assert bump_version('1.0.0', position=1) == '1.1.0'
    assert bump_version('1.0.0', position=0) == '2.0.0'
    assert bump_version('1.0.1', pre_release='a') == '1.0.2a0'
    assert bump_version('1.0.1a0', pre_release='a') == '1.0.1a1'
    assert bump_version('1.0.1a1', pre_release='b') == '1.0.1b0'
    assert bump_version('1.0.1a1') == '1.0.1'
    assert bump_version('1.0.1b0') == '1.0.1'
    assert bump_version

# Generated at 2026-04-26 13:13:41.276128
# Unit test for function bump_version
def test_bump_version(): 
    assert bump_version('1.0.0') == '1.0.1'
    assert bump_version('1.0.0', position=1) == '1.1.0'
    assert bump_version('1.0.0', position=0) == '2.0.0'
    assert bump_version('1.0.0', pre_release='a') == '1.0.1a0'
    assert bump_version('1.0.0a0', pre_release='a') == '1.0.0a1'
    assert bump_version('1.0.0a0', pre_release='b') == '1.0.0b0'
    assert bump_version('1.0.0b0') == '1.0.1'
    assert bump_version('1.0.0', position=2) == '1.0.1'

# Generated at 2026-04-26 13:14:00.739123
# Unit test for function bump_version
def test_bump_version(): 
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2026-04-26 13:14:05.754129
# Unit test for function bump_version
def test_bump_version(): 
    assert bump_version("1.2.2") == "1.2.3"
    assert bump_version("1.2.3", position=1) == "1.3"
    assert bump_version("1.3.4", position=0) == "2.0"
    assert bump_version("1.2.3", prerelease='a') == "1.2.4a0"
    assert bump_version("1.2.4a0", pre_release='a') == "1.2.4a1"
    assert bump_version("1.2.4a1", pre_release='b') == "1.2.4b0"
    assert bump_version("1.2.4a1") == "1.2.4"
    assert bump_version("1.2.4b0") == "1.2.4"

# Generated at 2026-04-26 13:14:12.000164
# Unit test for function bump_version
def test_bump_version(): 
    # Test cases
    assert bump_version("1.0.0") == "1.0.1"
    assert bump_version("1.0.1") == "1.0.2"
    assert bump_version("1.1.0", position=1) == "1.2.0"
    assert bump_version("1.2.2", pre_release="a") == "1.2.3a0"
    assert bump_version("1.2.3a0") == "1.2.3"
    assert bump_version("1.2.3b0") == "1.2.3"
    assert bump_version("2.1.3", position=1, pre_release="a") == "2.2a0"
    assert bump_version("1.2b0", position=2) == "1.2.1"

# Generated at 2026-04-26 13:14:17.292624
# Unit test for function bump_version
def test_bump_version():    
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2026-04-26 13:14:24.056524
# Unit test for function bump_version
def test_bump_version():    
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2026-04-26 13:14:29.251956
# Unit test for function bump_version
def test_bump_version():   
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2026-04-26 13:14:33.964960
# Unit test for function bump_version
def test_bump_version(): 
    assert bump_version('1.0.0') == '1.0.1'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.2.4a0', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4b1') == '1.2.4'
    assert bump_version('2.3.4', position=0) == '3.0'
    assert bump_version('1.2.4', position=2, pre_release='a') == '1.2.5a0'
    print("All tests passed!")

# Uncomment the line below to run the tests
# test_bump_version()

# Generated at 2026-04-26 13:14:38.624241
# Unit test for function bump_version
def test_bump_version(): 
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2026-04-26 13:14:43.050228
# Unit test for function bump_version
def test_bump_version(): 
    assert bump_version('1.2.3') == '1.2.4'
    assert bump_version('1.2.2', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2026-04-26 13:14:47.656245
# Unit test for function bump_version
def test_bump_version(): 
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2026-04-26 13:14:55.217463
# Unit test for function bump_version
def test_bump_version(): 
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2026-04-26 13:15:00.539738
# Unit test for function bump_version
def test_bump_version(): 
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2026-04-26 13:15:05.206253
# Unit test for function bump_version
def test_bump_version(): 
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2026-04-26 13:15:09.468653
# Unit test for function bump_version
def test_bump_version(): 
    assert bump_version('1.2.3') == '1.2.4'  # Basic patch bump
    assert bump_version('1.2.3', position=1) == '1.3.0'  # Minor bump
    assert bump_version('1.2.3', position=0) == '2.0.0'  # Major bump
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'  # Alpha bump
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'  # Alpha increment
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'  # Beta bump
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2026-04-26 13:15:14.847958
# Unit test for function bump_version
def test_bump_version():    
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2026-04-26 13:15:20.117468
# Unit test for function bump_version
def test_bump_version():    
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2026-04-26 13:15:24.546419
# Unit test for function bump_version
def test_bump_version(): 
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2026-04-26 13:15:29.466504
# Unit test for function bump_version
def test_bump_version(): 
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2026-04-26 13:15:34.145740
# Unit test for function bump_version
def test_bump_version():    
    assert bump_version('1.2.2') == '1.2.3'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'
    assert bump_version('1.2.3', prerelease='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'

# Generated at 2026-04-26 13:15:38.591966
# Unit test for function bump_version