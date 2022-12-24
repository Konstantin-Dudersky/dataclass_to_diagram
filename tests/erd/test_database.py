from konstantin_docs.erd import Database, Column, Relation, Table


def test_column_ref_to_table():
    Database(
        tables=[
            table1 := Table(
                "table_name",
                columns=[
                    col1 := Column("id", "integer"),
                ],
            ),
        ],
    )
    assert col1.table == table1
