# pyright: reportGeneralTypeIssues=false

import pytest

from dataclass_to_diagram.models.c4 import context, rel
from dataclass_to_diagram.exporters.c4_to_plantuml.rel_to_puml import (
    rel_to_puml,
)


@pytest.fixture
def begin() -> context.System:
    return context.System("begin")


@pytest.fixture
def end() -> context.System:
    return context.System("end")


def test_rel_min(begin: context.System, end: context.System):
    r = rel.Rel(begin=begin, end=end, label="label")
    puml: str = """Rel($from={0}, $to={1}, $label="label")""".format(
        begin.alias,
        end.alias,
    )
    assert rel_to_puml(r) == puml


def test_rel_full(begin: context.System, end: context.System):
    r = rel.Rel(
        begin=begin,
        end=end,
        label="label",
        techn="rel technology",
        descr="rel description",
    )
    puml: str = """Rel($from={0}, $to={1}, $label="label", $techn="rel technology", $descr="rel description")""".format(
        begin.alias,
        end.alias,
    )
    assert rel_to_puml(r) == puml


def test_different_rels(begin: context.System, end: context.System):
    args: dict[str, context.System | str] = {
        "begin": begin,
        "end": end,
        "label": "label",
    }

    r = [
        rel.BiRel(**args),
        rel.BiRelDown(**args),
        rel.BiRelLeft(**args),
        rel.BiRelRight(**args),
        rel.BiRelUp(**args),
        rel.Rel(**args),
        rel.RelDown(**args),
        rel.RelLeft(**args),
        rel.RelRight(**args),
        rel.RelUp(**args),
    ]

    puml_template: str = """{0}($from={1}, $to={2}, $label="label")"""
    puml = [
        puml_template.format("BiRel", begin.alias, end.alias),
        puml_template.format("BiRel_Down", begin.alias, end.alias),
        puml_template.format("BiRel_Left", begin.alias, end.alias),
        puml_template.format("BiRel_Right", begin.alias, end.alias),
        puml_template.format("BiRel_Up", begin.alias, end.alias),
        puml_template.format("Rel", begin.alias, end.alias),
        puml_template.format("Rel_Down", begin.alias, end.alias),
        puml_template.format("Rel_Left", begin.alias, end.alias),
        puml_template.format("Rel_Right", begin.alias, end.alias),
        puml_template.format("Rel_Up", begin.alias, end.alias),
    ]
    for i in range(len(r)):
        assert rel_to_puml(r[i]) == puml[i]
