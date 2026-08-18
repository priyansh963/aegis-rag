def test_split_paragraphs():

#     section = {
#         "level": 2,
#         "title": "Root Cause",
#         "content": """The deployment introduced an incompatible database configuration.

#                 This caused the authentication service to lose its PostgreSQL connections.

#                 The service therefore couldn't authenticate users."""
#             }

#     body = section["content"]
#     paragraphs = body.split("\n\n")

#     for paragraph in paragraphs:
#         print("PARAGRAPH:")
#         print(repr(paragraph))
#         print("Length:", len(paragraph))