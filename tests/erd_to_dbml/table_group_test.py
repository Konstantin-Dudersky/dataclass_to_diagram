from konstantin_docs.erd_to_dbml.table_group import table_group_to_dbml
from konstantin_docs.erd import Database, Table


def test():
    db = Database(
        tables=[
            Table(
                name="table1",
                columns=[],
                table_group="tg1",
            ),
        ],
    )
    dbml = """TableGroup tg1 {
    table1
}
"""
    assert db.table_groups is not None
    assert table_group_to_dbml(list(db.table_groups)[0]) == dbml
