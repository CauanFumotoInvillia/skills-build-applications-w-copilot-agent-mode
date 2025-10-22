from django.test import TestCase
from django.core.management import call_command
from apps.users.models import User
from apps.teams.models import Team
from apps.activities.models import Activity
from apps.leaderboard.models import LeaderboardEntry

class ActivitiesTestCase(TestCase):
    def test_stub(self):
        self.assertTrue(True)
        
class PopulateDBTests(TestCase):
    def test_populate_command_creates_data(self):
        # Run the populate_db management command
        call_command('populate_db')

        # Check expected objects exist
        self.assertGreaterEqual(Team.objects.count(), 2)
        self.assertGreaterEqual(User.objects.count(), 4)
        self.assertGreaterEqual(Activity.objects.count(), 4)
        self.assertGreaterEqual(LeaderboardEntry.objects.count(), 4)
