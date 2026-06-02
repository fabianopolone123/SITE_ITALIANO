from django.test import SimpleTestCase

from .management.commands.seed_chapter_one import CARDS


class SeedChapterOneTests(SimpleTestCase):
    def test_all_cards_have_context_notes(self):
        self.assertEqual(len(CARDS), 40)
        self.assertTrue(all(card.get("context_note") for card in CARDS))

    def test_cards_do_not_have_broken_utf8_markers(self):
        broken_markers = {chr(194), chr(195)}
        for card in CARDS:
            for value in card.values():
                if isinstance(value, str):
                    self.assertFalse(broken_markers & set(value), value)
