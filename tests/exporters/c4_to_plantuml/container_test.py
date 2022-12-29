from dataclass_to_diagram.exporters.c4_to_plantuml.container_to_puml import (
    container_to_puml,
)
from dataclass_to_diagram.models import c4


def test_container_minimal():
    container = c4.container.Container(
        label="user",
    )
    puml: str = """Container($alias={0}, $label="user")""".format(
        container.alias
    )
    assert container_to_puml(container) == puml


def test_container_full():
    container = c4.container.Container(
        label="container",
        techn="python",
        descr="program",
    )
    puml: str = """Container($alias={0}, $label="container", $descr="program", $techn="python")""".format(
        container.alias,
    )
    assert container_to_puml(container) == puml


def test_containerdb():
    container = c4.container.ContainerDb(
        label="user",
    )
    puml: str = """ContainerDb($alias={0}, $label="user")""".format(
        container.alias,
    )
    assert container_to_puml(container) == puml


def test_containequeue():
    container = c4.container.ContainerQueue(
        label="user",
    )
    puml: str = """ContainerQueue($alias={0}, $label="user")""".format(
        container.alias,
    )
    assert container_to_puml(container) == puml


def test_containerext():
    container = c4.container.ContainerExt(
        label="user",
    )
    puml: str = """Container_Ext($alias={0}, $label="user")""".format(
        container.alias,
    )
    assert container_to_puml(container) == puml


def test_containerdbext():
    container = c4.container.ContainerDbExt(
        label="user",
    )
    puml: str = """ContainerDb_Ext($alias={0}, $label="user")""".format(
        container.alias,
    )
    assert container_to_puml(container) == puml


def test_containerqueueext():
    container = c4.container.ContainerQueueExt(
        label="user",
    )
    puml: str = """ContainerQueue_Ext($alias={0}, $label="user")""".format(
        container.alias,
    )
    assert container_to_puml(container) == puml


def test_containerboundary():
    container = c4.container.ContainerBoundary(
        label="user",
    )
    puml: str = """Container_Boundary($alias={0}, $label="user")""".format(
        container.alias,
    )
    assert container_to_puml(container) == puml
