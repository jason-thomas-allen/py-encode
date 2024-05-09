import base58
import uuid

def base58_encode_uuid(uuid_list):
    encoded_uuids = []
    for uuid_str in uuid_list:
        # Convert UUID string to bytes
        uuid_bytes = uuid.UUID(uuid_str).bytes
        # Encode bytes to Base58
        encoded_uuid = base58.b58encode(uuid_bytes).decode('utf-8')
        encoded_uuids.append(encoded_uuid)
    return encoded_uuids

# Example list of UUIDs
uuid_list = [
    'cca2ba40-2e47-458e-b8cc-614e3f4b5245',
    'f61f2e38-8d8b-45f3-86f5-7f90a53a5c0a',
    '9dc5f6c9-ff45-4c41-aa10-6a4bf82e7b43'
]

encoded_uuids = base58_encode_uuid(uuid_list)
print("Encoded UUIDs:")
for encoded_uuid in encoded_uuids:
    print(encoded_uuid)
