from dataclass_to_diagram.exporters.c4_to_plantuml.component_to_puml import (
    component_to_puml,
)
from dataclass_to_diagram.models import c4


def test_component_minimal():
    component = c4.component.Component(
        label="user",
    )
    puml: str = """Component($alias={0}, $label="user")""".format(
        component.alias,
    )
    assert component_to_puml(component) == puml


def test_component_full():
    component = c4.component.ComponentDb(
        label="container",
        techn="python",
        descr="program",
    )
    puml: str = """ComponentDb($alias={0}, $label="container", $descr="program", $techn="python")""".format(
        component.alias,
    )
    assert component_to_puml(component) == puml


def test_componentdb():
    component = c4.component.ComponentDb(
        label="user",
    )
    puml: str = """ComponentDb($alias={0}, $label="user")""".format(
        component.alias,
    )
    assert component_to_puml(component) == puml


def test_componentqueue():
    component = c4.component.ComponentQueue(
        label="user",
    )
    puml: str = """ComponentQueue($alias={0}, $label="user")""".format(
        component.alias,
    )
    assert component_to_puml(component) == puml


def test_componentext():
    component = c4.component.ComponentExt(
        label="user",
    )
    puml: str = """Component_Ext($alias={0}, $label="user")""".format(
        component.alias,
    )
    assert component_to_puml(component) == puml


def test_componentdbext():
    component = c4.component.ComponentDbExt(
        label="user",
    )
    puml: str = """ComponentDb_Ext($alias={0}, $label="user")""".format(
        component.alias,
    )
    assert component_to_puml(component) == puml


def test_componentqueueext():
    component = c4.component.ComponentQueueExt(
        label="user",
    )
    puml: str = """ComponentQueue_Ext($alias={0}, $label="user")""".format(
        component.alias,
    )
    assert component_to_puml(component) == puml
