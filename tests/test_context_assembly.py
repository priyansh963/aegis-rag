from aegisrag.document import Document
from aegisrag.context_assembly import assemble_context

def test_assemble_context():

    document_a = Document(
        content="The cat sat quietly on the warm windowsill.",
        metadata={"source": "pets.md", "section": "Animals"}
    )
    document_b = Document(
        content="Rocket engines burn fuel to generate thrust.",
        metadata={"source": "space.md", "section": "Aerospace"}
    )

    results = [(document_a, 0.9), (document_b, 0.7)]

    context = assemble_context(results)

    assert "\n\n\n" not in context

    assert "[Source: pets.md, Section: Animals]" in context
    assert "The cat sat quietly on the warm windowsill." in context
    assert "[Source: space.md, Section: Aerospace]" in context
    assert "Rocket engines burn fuel to generate thrust." in context