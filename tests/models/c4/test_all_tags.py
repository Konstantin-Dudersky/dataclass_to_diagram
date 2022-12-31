from dataclass_to_diagram.models import c4


def test():
    el_tags: list[c4.tag.ElementTag] = [
        c4.tag.ElementTag("tag1"),
        c4.tag.ElementTag("tag2"),
        c4.tag.ElementTag("tag3"),
    ]
    rel_tags: list[c4.tag.RelationTag] = [
        c4.tag.RelationTag("tag1"),
        c4.tag.RelationTag("tag2"),
    ]
    dia = c4.C4(
        contexts=[
            begin := c4.context.System(
                "label1",
                tags=[el_tags[0]],
                containers=[
                    c4.container.Container(
                        "",
                        tags=[el_tags[1]],
                        components=[
                            c4.component.Component("", tags=[el_tags[2]]),
                        ],
                    ),
                ],
            ),
            end := c4.context.System("label2", tags=[el_tags[0]]),
        ],
        relations=[
            c4.rel.Rel(begin, end, "", tags=[rel_tags[0]]),
            c4.rel.Rel(end, begin, "", tags=[rel_tags[1]]),
            c4.rel.Rel(begin, end, "", tags=[rel_tags[0]]),
        ],
    )
    for tag in el_tags:
        assert tag in dia.find_all_element_tags()
    for tag in rel_tags:
        assert tag in dia.find_all_relation_tags()
