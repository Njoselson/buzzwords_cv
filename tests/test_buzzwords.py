import unittest
import re

from buzzwords import BuzzWordGetter

angelina_lee_cv_url = "https://docs.google.com/document/d/1OevE4HFiAgUPlOym3RAPjtvpk1zIurOKdTdrUFoyS28/edit"


class TestBuzzWordGetter(unittest.TestCase):
    def test_buzz_word_getter_collect_should_get_text_from_angelina_lee_cv(self):
        buzz_word_getter = BuzzWordGetter()
        raw = buzz_word_getter.collect(angelina_lee_cv_url)
        self.assertRegexpMatches(raw, r"AngelinaTheDev")


if __name__ == "__main__":
    unittest.main()
