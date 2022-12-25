from konstantin_docs.models.erd import Database, Column, Table


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


def test_empty_teblegroups():
    db = Database(
        tables=[
            Table("table10", columns=[]),
            Table("table11", columns=[]),
            Table("table20", columns=[]),
        ],
    )
    assert db.table_groups is None


def test_find_tablegroups():
    db = Database(
        tables=[
            t00 := Table("table00", columns=[], table_group="tg1"),
            t01 := Table("table01", columns=[], table_group="tg1"),
            t10 := Table("table10", columns=[], table_group="tg2"),
            t02 := Table("table02", columns=[], table_group="tg1"),
        ],
    )
    assert db.table_groups is not None
    assert len(list(db.table_groups)) == 2
    assert list(db.table_groups)[0].name == "tg1"
    assert list(db.table_groups)[0].tables[0] == t00
    assert list(db.table_groups)[0].tables[1] == t01
    assert list(db.table_groups)[0].tables[2] == t02
    assert list(db.table_groups)[1].name == "tg2"
    assert list(db.table_groups)[1].tables[0] == t10
