from __future__ import annotations

from dataclasses import dataclass

from src.models.concept_tree import ConceptGraph


@dataclass(frozen=True)
class ConceptTreeStoreResult:
    collection: str
    document_id: str


def save_concept_graph_to_firestore(
    graph: ConceptGraph,
    *,
    document_id: str = "default",
    collection: str = "concept_trees",
) -> ConceptTreeStoreResult:
    """
    Save the whole graph as a single Firestore document.

    Requires Firebase Admin credentials to be available via:
    - GOOGLE_APPLICATION_CREDENTIALS=/path/to/serviceAccount.json
    """
    try:
        import firebase_admin
        from firebase_admin import credentials, firestore
    except Exception as e:  # pragma: no cover
        raise RuntimeError(
            "Firebase dependencies are not available. Install `firebase-admin` "
            "and configure credentials (GOOGLE_APPLICATION_CREDENTIALS)."
        ) from e

    if not firebase_admin._apps:
        firebase_admin.initialize_app(credentials.ApplicationDefault())

    db = firestore.client()
    db.collection(collection).document(document_id).set(graph.to_dict())
    return ConceptTreeStoreResult(collection=collection, document_id=document_id)

