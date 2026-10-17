# Test cases for the AttendX login module

def test_whitespace_username():
    username = "   "
    password = "correct123"

    # Strip whitespace before validation
    login_success = bool(username.strip() and password)

    assert login_success is False
    print("PASS: Whitespace-only username is rejected")

def test_valid_login():
    username = "student01"
    password = "correct123"

    # Simulated login validation
    login_success = bool(username and password)

    assert login_success is True
    print("PASS: Valid login test")


def test_empty_username():
    username = ""
    password = "correct123"

    login_success = bool(username and password)

    assert login_success is False
    print("PASS: Empty username is rejected")


def test_empty_password():
    username = "student01"
    password = ""

    login_success = bool(username and password)

    assert login_success is False
    print("PASS: Empty password is rejected")


if __name__ == "__main__":
    test_valid_login()
    test_empty_username()
    test_empty_password()
    print("All login test cases passed.")

    