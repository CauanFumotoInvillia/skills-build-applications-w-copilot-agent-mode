from django.core.management.base import BaseCommand
from apps.users.models import User
from apps.teams.models import Team
from apps.activities.models import Activity
from apps.leaderboard.models import LeaderboardEntry

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data (one by one for Djongo compatibility)
        for obj in User.objects.all():
            if obj.pk:
                obj.delete()
        for obj in Team.objects.all():
            if obj.pk:
                obj.delete()
        for obj in Activity.objects.all():
            if obj.pk:
                obj.delete()
        for obj in LeaderboardEntry.objects.all():
            if obj.pk:
                obj.delete()

        # Create teams
        # Create teams safely
        marvel = Team.objects.filter(name='Marvel').first()
        if not marvel:
            marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.filter(name='DC').first()
        if not dc:
            dc = Team.objects.create(name='DC')

        # Create users (super heroes) safely using create_user to ensure proper password hashing
        def ensure_user(username, email, team):
            user = User.objects.filter(username=username).first()
            if user:
                return user
            # create_user may not be available if custom user model; fall back to User()
            try:
                user = User.objects.create_user(username=username, email=email, password='password')
            except Exception:
                user = User(username=username, email=email)
                user.set_password('password')
                user.save()
            # set team association if field exists
            try:
                user.team = team
                user.save()
            except Exception:
                pass
            return user

        ironman = ensure_user('ironman', 'ironman@marvel.com', marvel)
        captain = ensure_user('captainamerica', 'cap@marvel.com', marvel)
        batman = ensure_user('batman', 'batman@dc.com', dc)
        superman = ensure_user('superman', 'superman@dc.com', dc)

        # Create activities safely
        def ensure_activity(name, user, duration):
            act = Activity.objects.filter(name=name, user=user).first()
            if act:
                return act
            return Activity.objects.create(name=name, user=user, duration=duration)

        ensure_activity('Run', ironman, 30)
        ensure_activity('Swim', captain, 45)
        ensure_activity('Fly', superman, 60)
        ensure_activity('Fight Crime', batman, 50)

        # Create leaderboard entries safely
        def ensure_entry(user, score):
            entry = LeaderboardEntry.objects.filter(user=user).first()
            if entry:
                return entry
            return LeaderboardEntry.objects.create(user=user, score=score)

        ensure_entry(ironman, 100)
        ensure_entry(captain, 90)
        ensure_entry(batman, 95)
        ensure_entry(superman, 98)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
