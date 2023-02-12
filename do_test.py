if __name__ == "__main__":
    import pytest
    pytest.main(["."])

# all the test aren't in a other folder, it's du to pytest which can't import a file in a parent file, even if python can do it   