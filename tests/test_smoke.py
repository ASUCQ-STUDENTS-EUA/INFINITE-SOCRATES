def test_smoke_imports() -> None:
    import src.ai.socratic  # noqa: F401
    import src.database.firebase_client  # noqa: F401
    import src.models.concept_tree  # noqa: F401
    import src.recognition.base  # noqa: F401
    import src.ui.app  # noqa: F401
    import src.utils.env  # noqa: F401

