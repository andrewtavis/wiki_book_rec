"""
Languages Tests
---------------
"""

from wikirec import languages


def test_language_returns():
    assert isinstance(languages.lem_abbr_dict(), dict)
    assert isinstance(languages.stem_abbr_dict(), dict)
    assert isinstance(languages.sw_abbr_dict(), dict)
