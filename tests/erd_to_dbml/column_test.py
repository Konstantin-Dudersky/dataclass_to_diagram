from konstantin_docs.erd_to_dbml.column import Column, column_to_dbml

from konstantin_docs.erd import Note


def test_default():
    col = Column(name="column", datatype="integer")
    dbml: str = 'column "integer" [null]'
    assert dbml == column_to_dbml(col)


def test_note():
    col = Column("id", "integer", Note("column desc"))
    dbml: str = """id "integer" [note: '''column desc''', null]"""
    assert column_to_dbml(col) == dbml


def test_pk():
    col = Column("id", "integer", is_pk=True)
    dbml: str = 'id "integer" [pk, null]'
    assert column_to_dbml(col) == dbml


def test_not_null():
    col = Column("id", "integer", can_be_null=False)
    dbml: str = 'id "integer" [not null]'
    assert column_to_dbml(col) == dbml


def test_unique():
    col = Column("id", "integer", is_unique=True)
    dbml: str = 'id "integer" [null, unique]'
    assert column_to_dbml(col) == dbml


def test_default_value():
    col = Column("id", "integer", default_value="default value")
    dbml: str = """id "integer" [null, default: 'default value']"""
    assert column_to_dbml(col) == dbml


def test_increment():
    col = Column("id", "integer", is_increment=True)
    dbml: str = """id "integer" [null, increment]"""
    assert column_to_dbml(col) == dbml


def test_all_fields():
    col = Column(
        name="id",
        datatype="integer",
        note=Note("note"),
        is_pk=True,
        can_be_null=False,
        is_unique=True,
        is_increment=True,
        default_value="NOW()",
    )
    dbml: str = """id "integer" [note: '''note''', pk, not null, unique, default: 'NOW()', increment]"""
    assert column_to_dbml(col) == dbml
