from dataclass_to_diagram.models import c4
from dataclass_to_diagram.exporters.c4_to_plantuml.context_to_puml import (
    context_to_puml,
)
from dataclass_to_diagram.exporters.c4_to_plantuml.tag_to_puml import (
    element_tag_to_puml,
)
from dataclass_to_diagram.exporters.c4_to_plantuml.rel_to_puml import (
    rel_to_puml,
)


def test_tag_in_context():
    tag1 = c4.tag.ElementTag("tag1")
    context = c4.context.System("label", tags=[tag1])
    puml: str = """System($alias={0}, $label="label", $tags="tag1")""".format(
        context.alias,
    )
    assert context_to_puml(context) == puml


def test_tag_in_rel():
    tag1 = c4.tag.RelationTag("tag1")
    rel = c4.rel.Rel(
        begin := c4.context.System("begin"),
        end := c4.context.System("end"),
        "label",
        tags=[tag1],
    )
    puml: str = (
        """Rel($from={0}, $to={1}, $label="label", $tags="tag1")""".format(
            begin.alias, end.alias
        )
    )
    assert rel_to_puml(rel) == puml


def test_two_tags_same_name():
    tag1 = c4.tag.ElementTag("tag1", legend_text="123")
    tag2 = c4.tag.ElementTag("tag1")
    context = c4.context.System("label", tags=[tag1, tag2])
    puml: str = """System($alias={0}, $label="label", $tags="tag1")""".format(
        context.alias,
    )
    print(context.find_all_tags())
    assert context_to_puml(context) == puml


def test_two_tags_diff_name():
    tag1 = c4.tag.ElementTag("tag1", legend_text="123")
    tag2 = c4.tag.ElementTag("tag2")
    context = c4.context.System("label", tags=[tag1, tag2])
    puml: str = (
        """System($alias={0}, $label="label", $tags="tag1+tag2")""".format(
            context.alias,
        )
    )
    print(context.find_all_tags())
    assert context_to_puml(context) == puml


def test_element_tag():
    tag = c4.tag.ElementTag(
        tag_stereo="tag stereo",
    )
    puml: str = """AddElementTag($tagStereo="tag stereo")"""
    assert element_tag_to_puml(tag) == puml
