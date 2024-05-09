import base58
import uuid

def base58_url_encode_uuid(uuid_list):
    encoded_uuids = []
    for uuid_str in uuid_list:
        uuid_bytes = uuid.UUID(uuid_str).bytes
        encoded = base58.b58encode(uuid_bytes)
        # Replace characters not suitable for URLs
        encoded_url_safe = encoded.replace(b'+', b'-').replace(b'/', b'_').replace(b'=', b'')
        encoded_uuids.append(encoded_url_safe.decode())
    return encoded_uuids

# Example usage
uuid_list = ["c75b7d2b-2193-4f3b-a22f-7e92533bd9c7", "5c6f7557-666f-7200-4e6f-726d61740000"]
encoded_uuids = base58_url_encode_uuid(uuid_list)
print("Encoded UUIDs:", encoded_uuids)
