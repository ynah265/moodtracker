from django.test import TestCase
from .models import MoodEntry

class MoodEntryModelTest(TestCase):

    def setUp(self):
        self.entry = MoodEntry.objects.create(
            mood='Happy',
            journal_entry='Today was a good day!'
        )

    def test_mood_content(self):
        self.assertEqual(self.entry.mood, 'Happy')
        self.assertEqual(self.entry.journal_entry, 'Today was a good day!')
