from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your tests here.

class MeetingTest(TestCase):
    def test_string(self):
        type=Meeting(meetingtitle='Weekly team meeting')
        self.assertEqual(str(type), type.meetingtitle)

class setup




 