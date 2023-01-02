from dataclass_to_diagram.exporters.shared.increase_indent import (
    increase_indent,
)


def test1():
    input_string = """line1
line2
line3
"""
    expected = """    line1
    line2
    line3
    """
    assert increase_indent(input_string) == expected


def test2():
    input_string = """
    line1
line2
    line3
"""
    expected = """    
        line1
    line2
        line3
    """
    assert increase_indent(input_string) == expected
