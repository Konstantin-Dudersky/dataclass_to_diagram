from konstantin_docs.erd_to_dbml.project_definition import (
    ProjectDefinition,
    project_definition_to_dbml,
)
from konstantin_docs.erd import Note


def test() -> None:
    proj_def = ProjectDefinition(
        project_name="project_name",
        database_type="SQLite",
    )

    dbml = """Project project_name {
    database_type: 'SQLite'
    
}
"""  # noqa: W293
    assert project_definition_to_dbml(proj_def) == dbml


def test_note() -> None:
    note_content = """very
long
note"""
    proj_def = ProjectDefinition(
        project_name="new awesome project",
        database_type="MySQL",
        note=Note(note_content),
    )
    dbml = """Project new_awesome_project {
    database_type: 'MySQL'
    Note: '''very
long
note'''
}
"""
    assert project_definition_to_dbml(proj_def) == dbml
