import pytest
from Trie import Trie, TrieNode


t = Trie()


def test_insert():
    assert t.insert("Coco") == None
    assert t.insert("MacaCo") == None
    assert t.insert("Istambul") == None
    assert t.insert("join team") == None
    assert t.insert("kill the fish") == None


@pytest.mark.parametrize(
    "prefix,expected",
    [
        ("coc", True),
        ("miaca", False),
        ("isTa", True),
        ("Estud", False),
        ("fish", True),
        ("the", True),
        ("kill t", False),
        ("team", True),
        ("join", True),
    ],
)
def test_search(prefix, expected):
    assert t.search(prefix) == expected
