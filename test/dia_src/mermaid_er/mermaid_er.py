"""Тестовые диаграммы для mermaid er."""

from dataclass_to_diagram import mermaid_er as er

card = er.Relation.Cardinalities
ty = er.Attr.Types

unit = er.Entity(
    name="unit",
    attr=[
        er.Attr("unit_id", ty.INT, key=er.Attr.Keys.PK),
        er.Attr("pack_id", ty.INT, key=er.Attr.Keys.FK),
        er.Attr("pallet_id", ty.INT, key=er.Attr.Keys.FK),
        er.Attr("batch_id", ty.INT, key=er.Attr.Keys.FK),
        er.Attr("barcode", ty.STR),
        er.Attr("timestamp", ty.DATETIME),
    ],
)
pack = er.Entity(
    name="pack",
    attr=[
        er.Attr("pack_id", ty.INT, key=er.Attr.Keys.PK),
        er.Attr("pallet_id", ty.INT, key=er.Attr.Keys.FK),
        er.Attr("batch_id", ty.INT, key=er.Attr.Keys.FK),
        er.Attr(
            "barcode",
            ty.STR,
            comment="Код без скобок, для печати кода на принтере",
        ),
        er.Attr(
            "barcode_human",
            ty.STR,
            comment="Код со скобками",
        ),
        er.Attr("mass", ty.INT),
        er.Attr("seat_number", ty.INT),
        er.Attr("timestamp", ty.DATETIME),
        er.Attr(
            "need_validate",
            ty.BOOL,
            comment="Необходимо валидировать сканером",
        ),
    ],
)
pallet = er.Entity(
    name="pallet",
    attr=[
        er.Attr("pallet_id", ty.INT, key=er.Attr.Keys.PK),
        er.Attr("batch_id", ty.INT, key=er.Attr.Keys.FK),
        er.Attr(
            "barcode",
            ty.STR,
            comment="Код без скобок, для печати кода на принтере",
        ),
        er.Attr(
            "barcode_human",
            ty.STR,
            comment="Код со скобками",
        ),
        er.Attr("mass", ty.INT),
        er.Attr("seat_number", ty.INT),
        er.Attr("start_ts", ty.DATETIME),
        er.Attr("end_ts", ty.DATETIME),
        er.Attr("need_validate", ty.BOOL, "Необходимо валидировать сканером"),
    ],
)
batch = er.Entity(
    name="batch",
    attr=[
        er.Attr("batch_id", ty.INT, key=er.Attr.Keys.PK),
        er.Attr("batch_number", ty.INT),
        er.Attr("bbd_period", ty.INT, "Срок годности в днях"),
        er.Attr("docid", ty.STR),
        er.Attr("exported", ty.BOOL),
        er.Attr("gtin", ty.STR),
        er.Attr("manufacture_ts", ty.DATETIME),
        er.Attr("start_ts", ty.DATETIME),
        er.Attr("end_ts", ty.DATETIME),
        er.Attr("unit_mass", ty.INT),
    ],
)
state = er.Entity(
    name="state",
    attr=[
        er.Attr("state_id", ty.INT, key=er.Attr.Keys.PK),
        er.Attr("pack_id", ty.INT, key=er.Attr.Keys.FK),
        er.Attr("pallete_id", ty.INT, key=er.Attr.Keys.FK),
        er.Attr("batch_id", ty.INT, "Запущенная партия", key=er.Attr.Keys.FK),
        er.Attr("max_unit_in_pack", ty.INT),
        er.Attr("max_pack_in_pallet", ty.INT),
        er.Attr("max_pallet_in_batch", ty.INT),
    ],
)
dia1 = er.Diagram(
    filename="mermaid",
    rels=[
        er.Relation(pack, card.c_1, card.c_0_inf, unit, "pack_id"),
        er.Relation(pallet, card.c_1, card.c_0_inf, unit, "pallet_id"),
        er.Relation(pallet, card.c_1, card.c_0_inf, pack, "pallet_id"),
        er.Relation(batch, card.c_1, card.c_0_inf, unit, "batch_id"),
        er.Relation(batch, card.c_1, card.c_0_inf, pack, "batch_id"),
        er.Relation(state, card.c_1, card.c_0_1, pack, "pack_id"),
        er.Relation(state, card.c_1, card.c_0_1, pallet, "pallet_id"),
        er.Relation(state, card.c_1, card.c_0_1, batch, "batch_id"),
    ],
)
