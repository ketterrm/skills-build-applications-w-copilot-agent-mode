from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users (Superheroes)
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', team=marvel),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', team=marvel),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', team=dc),
            User.objects.create_user(username='superman', email='superman@dc.com', team=dc),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create Activities
        for user in users:
            Activity.objects.create(user=user, type='run', duration=30, calories=300)
            Activity.objects.create(user=user, type='cycle', duration=45, calories=400)

        # Create Workouts
        Workout.objects.create(name='Full Body Blast', description='A full body workout for all levels.')
        Workout.objects.create(name='Cardio Burn', description='High intensity cardio workout.')

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=900)
        Leaderboard.objects.create(team=dc, points=850)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
