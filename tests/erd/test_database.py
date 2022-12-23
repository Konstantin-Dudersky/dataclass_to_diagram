from konstantin_docs.erd import Database, Column, Table


def test_db():
    db = Database(
        tables=[
            t1 := Table(
                "table_name",
                columns=[
                    f1 := Column("id", "integer"),
                ],
            ),
        ],
    )
