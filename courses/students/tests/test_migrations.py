from unittest import TestCase
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from django.core.management import call_command


class MissingMigrationsTestCase(TestCase):

    def test_missing_migrations(self):
        fd = StringIO()
        call_command('makemigrations', '--dry-run', stdout=fd)
        self.assertTrue("No changes detected" in fd.getvalue())
