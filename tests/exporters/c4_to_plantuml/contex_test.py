from dataclass_to_diagram.exporters.c4_to_plantuml.context_to_puml import (
    context_to_puml,
)
from dataclass_to_diagram.models import c4


def test_person_minimal():
    person = c4.context.Person(
        label="user",
    )
    puml: str = """Person($alias={0}, $label="user")""".format(person.alias)
    assert context_to_puml(person) == puml


def test_person_full():
    person = c4.context.Person(
        label="user",
        descr="user description",
    )
    puml: str = """Person($alias={0}, $label="user", $descr="user description")""".format(
        person.alias,
    )
    assert context_to_puml(person) == puml


def test_person_ext():
    person_ext = c4.context.PersonExt(
        label="external_user",
    )
    puml: str = """Person_Ext($alias={0}, $label="external_user")""".format(
        person_ext.alias,
    )
    assert context_to_puml(person_ext) == puml


def test_system():
    system = c4.context.System(
        label="system",
    )
    puml: str = """System($alias={0}, $label="system")""".format(
        system.alias,
    )
    assert context_to_puml(system) == puml


def test_systemdb():
    system = c4.context.SystemDb(
        label="system_db",
    )
    puml: str = """SystemDb($alias={0}, $label="system_db")""".format(
        system.alias,
    )
    assert context_to_puml(system) == puml


def test_systemqueue():
    system = c4.context.SystemQueue(
        label="system_queue",
    )
    puml: str = """SystemQueue($alias={0}, $label="system_queue")""".format(
        system.alias,
    )
    assert context_to_puml(system) == puml


def test_systemext():
    system = c4.context.SystemExt(
        label="system_ext",
    )
    puml: str = """System_Ext($alias={0}, $label="system_ext")""".format(
        system.alias,
    )
    assert context_to_puml(system) == puml


def test_systemdbext():
    system = c4.context.SystemDbExt(
        label="system_db_ext",
    )
    puml: str = """SystemDb_Ext($alias={0}, $label="system_db_ext")""".format(
        system.alias,
    )
    assert context_to_puml(system) == puml


def test_systemqueueext():
    system = c4.context.SystemQueueExt(
        label="system_queue_ext",
    )
    puml: str = (
        """SystemQueue_Ext($alias={0}, $label="system_queue_ext")""".format(
            system.alias,
        )
    )
    assert context_to_puml(system) == puml


def test_enterprise_boundary():
    system = c4.context.EnterpriseBoundary(
        label="enterprise_boundary",
    )
    puml: str = """Enterprise_Boundary($alias={0}, $label="enterprise_boundary")""".format(
        system.alias,
    )
    assert context_to_puml(system) == puml


def test_system_boundary():
    system = c4.context.SystemBoundary(
        label="system_boundary",
    )
    puml: str = (
        """System_Boundary($alias={0}, $label="system_boundary")""".format(
            system.alias,
        )
    )
    assert context_to_puml(system) == puml
