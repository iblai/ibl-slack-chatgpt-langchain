import unittest

from chatbot.utils import count_tokens


class TokenizerUtilTestCase(unittest.TestCase):
    """
    Tests to cover tokenization impl for `chatbot` app.
    """

    def setUp(self) -> None:
        return super().setUp()

    def test_should_count_and_return_number_of_tokens_from_text(self) -> None:
        # Given
        text = "demo text to be tokenized"
        expected = 6

        # When
        actual = count_tokens(text)

        # Then
        self.assertIsInstance(actual, int)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
