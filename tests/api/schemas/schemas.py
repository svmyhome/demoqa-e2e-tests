from voluptuous import Schema, Date, PREVENT_EXTRA

create_user_schema = Schema(
    {
        'createdAt': Date(format='%Y-%m-%dT%H:%M:%S.%fZ'),
        'id': str,
        'job': str,
        'name': str,
    }
)

update_user_schema = Schema(
    {
        'updatedAt': Date(format='%Y-%m-%dT%H:%M:%S.%fZ'),
        'job': str,
        'name': str,
    }
)

list_schema = Schema(
    {
        'data': [
            {
                'avatar': str,
                'email': str,
                'first_name': str,
                'id': int,
                'last_name': str,
            },
            {
                'avatar': str,
                'email': str,
                'first_name': str,
                'id': int,
                'last_name': str,
            },
            {
                'avatar': str,
                'email': str,
                'first_name': str,
                'id': int,
                'last_name': str,
            },
            {
                'avatar': str,
                'email': str,
                'first_name': str,
                'id': int,
                'last_name': str,
            },
            {
                'avatar': str,
                'email': str,
                'first_name': str,
                'id': int,
                'last_name': str,
            },
            {
                'avatar': str,
                'email': str,
                'first_name': str,
                'id': int,
                'last_name': str,
            },
        ],
        'page': int,
        'per_page': int,
        'support': {'url': str, 'text': str},
        'total': int,
        'total_pages': int,
    },
    required=True,
    extra=PREVENT_EXTRA,
)
