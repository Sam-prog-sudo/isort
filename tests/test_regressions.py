"""A growing set of tests designed to ensure isort doesn't have regressions in new versions"""
import isort


def test_isort_duplicating_comments_issue_1264():
    """Ensure isort doesn't duplicate comments when force_sort_within_sections is set to `True`
    as was the case in issue #1264: https://github.com/timothycrosley/isort/issues/1264
    """
    assert (
        isort.code(
            """
from homeassistant.util.logging import catch_log_exception

# Loading the config flow...
from . import config_flow
""",
            force_sort_within_sections=True,
        ).count("# Loading the config flow...")
        == 1
    )


def test_moving_comments_issue_726():
    test_input = (
        "from Blue import models as BlueModels\n"
        "# comment for PlaidModel\n"
        "from Plaid.models import PlaidModel\n"
    )
    assert isort.code(test_input, force_sort_within_sections=True) == test_input

    test_input = (
        "# comment for BlueModels\n"
        "from Blue import models as BlueModels\n"
        "# comment for PlaidModel\n"
        "# another comment for PlaidModel\n"
        "from Plaid.models import PlaidModel\n"
    )
    assert isort.code(test_input, force_sort_within_sections=True) == test_input


def test_blank_lined_removed_issue_1275():
    """Ensure isort doesn't accidentally remove blank lines after doc strings and before imports.
    See: https://github.com/timothycrosley/isort/issues/1275
    """
    assert (
        isort.code(
            '''"""
My docstring
"""

from b import thing
from a import other_thing
'''
        )
        == '''"""
My docstring
"""

from a import other_thing
from b import thing
'''
    )

def test_blank_lined_removed_issue_1283():
    """Ensure isort doesn't accidentally remove blank lines after __version__ identifiers.
    See: https://github.com/timothycrosley/isort/issues/1283
    """
    test_input = """__version__ = "0.58.1"

from starlette import status
"""
    assert isort.code(test_input) == test_input
