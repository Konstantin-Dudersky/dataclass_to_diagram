from konstantin_docs.erd.erd import Column, Database, Relation, Table
from konstantin_docs.erd_to_dbml.relation import relation_to_dbml


def test_relation():
    Database(
        tables=[
            Table(
                "table_name1",
                columns=[
                    table1_id := Column("id", "integer"),
                ],
            ),
            Table(
                "table_name2",
                columns=[
                    table2_id := Column("id", "integer"),
                ],
            ),
        ],
        relations=[
            rel1 := Relation(table1_id, ">", table2_id),
            rel2 := Relation(table1_id, "<", table2_id),
            rel3 := Relation(table1_id, "<>", table2_id),
            rel4 := Relation(table1_id, "-", table2_id),
        ],
    )
    dbml1: str = """Ref: table_name1.id > table_name2.id []
"""
    assert relation_to_dbml(rel1) == dbml1
    dbml2: str = """Ref: table_name1.id < table_name2.id []
"""
    assert relation_to_dbml(rel2) == dbml2
    dbml3: str = """Ref: table_name1.id <> table_name2.id []
"""
    assert relation_to_dbml(rel3) == dbml3
    dbml4: str = """Ref: table_name1.id - table_name2.id []
"""
    assert relation_to_dbml(rel4) == dbml4


def test_relation_config():
    Database(
        tables=[
            Table(
                "table_name1",
                columns=[
                    table1_id := Column("id", "integer"),
                ],
            ),
            Table(
                "table_name2",
                columns=[
                    table2_id := Column("id", "integer"),
                ],
            ),
        ],
        relations=[
            rel1 := Relation(table1_id, ">", table2_id, "cascade", "no action"),
            rel2 := Relation(
                table1_id,
                "<",
                table2_id,
                "set null",
                "set default",
            ),
            rel3 := Relation(table1_id, "<>", table2_id, "no action"),
            rel4 := Relation(table1_id, "-", table2_id, None, "no action"),
        ],
    )
    dbml1: str = """Ref: table_name1.id > table_name2.id [update: cascade, delete: no action]
"""
    assert relation_to_dbml(rel1) == dbml1
    dbml2: str = """Ref: table_name1.id < table_name2.id [update: set null, delete: set default]
"""
    assert relation_to_dbml(rel2) == dbml2
    dbml3: str = """Ref: table_name1.id <> table_name2.id [update: no action]
"""
    assert relation_to_dbml(rel3) == dbml3
    dbml4: str = """Ref: table_name1.id - table_name2.id [delete: no action]
"""
    assert relation_to_dbml(rel4) == dbml4
