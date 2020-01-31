import re
import textwrap

import pytest
from markdown import Markdown

from markdown_ratings.main import RATING_RE, RatingsExtension


@pytest.fixture
def markdowner() -> Markdown:
    extension = RatingsExtension()
    return Markdown(extensions=[extension])


@pytest.mark.parametrize(
    "md_input,expected",
    [
        ("[rating:0]", ("0",)),
        ("[rating:1]", ("1",)),
        ("[rating:2]", ("2",)),
        ("[rating:3]", ("3",)),
        ("[rating:4]", ("4",)),
        ("[rating:5]", ("5",)),
        ("[rating: 5]", ("5",)),
        ("[rating: 5 ]", ("5",)),
        ("Just a [rating:5] rating", ("5",)),
    ],
)
def test_re(md_input, expected):
    assert re.search(RATING_RE, md_input).groups() == expected


@pytest.mark.parametrize(
    "md_input,expected",
    [
        (
            "this has a [rating:0] rating",
            '<p>this has a <span><i class="far fa-star"></i><i class="far fa-star"></i><i class="far fa-star"></i><i class="far fa-star"></i><i class="far fa-star"></i></span> rating</p>',
        ),
        (
            "this has a [rating:1] rating",
            '<p>this has a <span><i class="fas fa-star star-checked"></i><i class="far fa-star"></i><i class="far fa-star"></i><i class="far fa-star"></i><i class="far fa-star"></i></span> rating</p>',
        ),
        (
            "this has a [rating:5] rating",
            '<p>this has a <span><i class="fas fa-star star-checked"></i><i class="fas fa-star star-checked"></i><i class="fas fa-star star-checked"></i><i class="fas fa-star star-checked"></i><i class="fas fa-star star-checked"></i></span> rating</p>',
        ),
    ],
)
def test_markdown_ratings(markdowner, md_input, expected):
    assert textwrap.dedent(markdowner.convert(md_input)) == textwrap.dedent(expected)
