from voluptuous import Schema, Date, PREVENT_EXTRA, All, Length, Any

create_user_schema = Schema(
    {
        'createdAt': Date(format='%Y-%m-%dT%H:%M:%S.%fZ'),
        'id': str,
        'job': str,
        'name': str,
    },
    required=True,
    extra=PREVENT_EXTRA,
)

update_user_schema = Schema(
    {
        'updatedAt': Date(format='%Y-%m-%dT%H:%M:%S.%fZ'),
        'job': str,
        'name': str,
    },
    required=True,
    extra=PREVENT_EXTRA,
)

LIST_DATA_SCHEMA = Schema(
    {
        'avatar': str,
        'email': str,
        'first_name': str,
        'id': int,
        'last_name': str,
    },
    required=True,
    extra=PREVENT_EXTRA,
)
LIST_SUPPORT_SCHEMA = Schema(
    {'url': str, 'text': str},
    required=True,
    extra=PREVENT_EXTRA,
)
list_schema = Schema(
    {
        'data': All([LIST_DATA_SCHEMA], Length(min=1)),
        'page': int,
        'per_page': int,
        'support': LIST_SUPPORT_SCHEMA,
        'total': int,
        'total_pages': int,
    },
    required=True,
    extra=PREVENT_EXTRA,
)


def panton_value_validate(value):
    part1, par2 = value.split('-')
    if len(part1) == 2 and len(par2) == 4:
        return True
    else:
        raise ValueError(f'Len part 1 не равно 2')


LIST_UNKNOWN_DATA = Schema(
    {
        "id": int,
        "name": str,
        "year": int,
        "color": Any(str, int),
        "pantone_value": All(str, panton_value_validate),
    },
    required=True,
    extra=PREVENT_EXTRA,
)

LIST_UNKNOWN_SUPPORT = Schema(
    {
        "url": str,
        "text": str,
    }
)


LIST_UNKNOWN_SCHEMA = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": All([LIST_UNKNOWN_DATA], Length(min=1)),
        "support": LIST_UNKNOWN_SUPPORT,
    }
)
