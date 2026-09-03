def assemble_context(results):

    context_block = []

    for document, socre in results:

        header = f"[Source: {document.metadata['source']}, Section: {document.metadata['section']}]"

        context = header + "\n\n" + document.content

        context_block.append(context)

    assembled_context = "\n\n".join(context_block)

    return assembled_context


