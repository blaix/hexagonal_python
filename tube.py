from testtube.helpers import Helper, Nosetests


class ScreenClearer(Helper):
    command = 'clear'

    def success(self, *args):
        pass


clear = ScreenClearer(all_files=True)
unit_tests = Nosetests(all_files=True)

PATTERNS = (
    (r'.*\.(py|rst)$', [clear]),
    (r'.*\.py$', [unit_tests], {'fail_fast': True}),
)
