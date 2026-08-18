chunks = run_pipeline(Path("data/documents/test_comprehensive.md"), max_chunk_size=100, overlap=20)
print(chunks)