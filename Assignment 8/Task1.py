import re
import string
import unittest

_SPECIAL_START_END = set(string.punctuation) - {"'", '"'}


def is_valid_email(email: str) -> bool:
    """
    Validate an email address according to the project rules.

    Requirements:
    - Must contain "@" and "." characters.
    - Must contain exactly one "@" character.
    - Must not start or end with special characters.
    - The domain (after "@") must contain at least one ".".

    Args:
        email: The email address to validate.

    Returns:
        True if the email is valid, False otherwise.
    """
    if not isinstance(email, str):
        return False

    if not email:
        return False

    if email != email.strip():
        return False

    email = email.strip()
    if not email:
        return False

    if email.count("@") != 1:
        return False

    if "." not in email:
        return False

    # Cannot start or end with special characters
    if email[0] in _SPECIAL_START_END or email[-1] in _SPECIAL_START_END:
        return False

    local_part, domain_part = email.split("@")

    # Local and domain parts must be non-empty
    if not local_part or not domain_part:
        return False

    # Additional guard: domain cannot start or end with special characters
    if domain_part[0] in _SPECIAL_START_END or domain_part[-1] in _SPECIAL_START_END:
        return False

    # Domain must contain at least one dot
    if "." not in domain_part:
        return False

    # Ensure no spaces or control characters are present
    if any(c.isspace() for c in email):
        return False

    # Allow letters, digits, and limited special characters in the local part
    local_pattern = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._+-]*[A-Za-z0-9]$")
    domain_pattern = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+$")

    if not local_pattern.match(local_part):
        return False

    if not domain_pattern.match(domain_part):
        return False

    return True


class TestIsValidEmail(unittest.TestCase):
    def test_valid_emails(self):
        valid_emails = [
            "test@example.com",
            "user.name@email.co.in",
            "firstname.lastname@domain.com",
            "my_email123@sub.domain.org",
            "a.b@c.d",
            "user+tag@domain.io",
            "user123@domain123.co",
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email), f"{email} should be valid")

    def test_missing_at_or_dot(self):
        invalid_emails = [
            "testexample.com",
            "test@examplecom",
            "testexamplecom",
            "test@com",
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email), f"{email} should be invalid")

    def test_starts_or_ends_with_special_characters(self):
        invalid_emails = [
            ".test@example.com",
            "-user@example.com",
            "_user@example.com",
            "test.@example.com",
            "test-@example.com",
            "test_@example.com",
            "test@example.com.",
            "test@example.com-",
            "test@example.com_",
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email), f"{email} should be invalid")

    def test_multiple_at_symbols(self):
        invalid_emails = [
            "te@st@example.com",
            "user@@example.com",
            "@@example.com",
            "user@exa@mple.com",
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email), f"{email} should be invalid")

    def test_empty_or_minimal_cases(self):
        invalid_emails = [
            "",
            "@.",
            ".@",
            "@",
            "user@",
            "@example.com",
            "user@example.",
            ".@.",
            " user@example.com ",
            "user@ example.com",
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email), f"{email} should be invalid")

    def test_domain_format_edge_cases(self):
        invalid_emails = [
            "user@.domain.com",
            "user@domain..com",
            "user@domain.corporate.",
            "user@-domain.com",
            "user@domain-.com",
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email), f"{email} should be invalid")


def check_user_input() -> None:
    while True:
        user_input = input("\nEnter an email address to validate (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        if is_valid_email(user_input):
            print(f"'{user_input}' is a VALID email address.")
        else:
            print(f"'{user_input}' is NOT a valid email address.")


if __name__ == "__main__":
    unittest.main()
