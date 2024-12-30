PLATE_POST_REQUEST_SCHEMA_EXAMPLE = {"plate": "M-PP123"}

PLATE_GET_RESPONSE_SCHEMA_EXAMPLE = {
    "data": [
        {"plate": "M-PP123", "timestamp": "2020-09-18T13:21:21Z"},
        {"plate": "K-A123", "timestamp": "2020-09-18T14:21:21Z"},
    ],
    "pagination": {
        "page_number": 1,
        "page_size": 10,
        "total_pages": 5,
        "total_items": 50,
    },
}
