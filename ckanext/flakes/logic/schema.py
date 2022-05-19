from ckan.logic.schema import validator_args


@validator_args
def flake_create(
    not_missing,
    convert_to_json_if_string,
    dict_only,
    ignore,
    ignore_missing,
    flakes_flake_id_exists,
    flakes_flake_id_available,
    user_id_or_name_exists,
):
    return {
        "id": [ignore_missing, flakes_flake_id_available],
        "data": [not_missing, convert_to_json_if_string, dict_only],
        "parent_id": [ignore_missing, flakes_flake_id_exists],
        "author_id": [ignore_missing, user_id_or_name_exists],
        "__extras": [ignore],
    }


@validator_args
def flake_update(
    flakes_flake_id_exists,
    not_missing,
    convert_to_json_if_string,
    dict_only,
    ignore,
    ignore_missing,
):
    return {
        "id": [not_missing, flakes_flake_id_exists],
        "data": [not_missing, convert_to_json_if_string, dict_only],
        "parent_id": [ignore_missing, flakes_flake_id_exists],
        "__extras": [ignore],
    }


@validator_args
def flake_delete(flakes_flake_id_exists, not_missing):
    return {
        "id": [not_missing, flakes_flake_id_exists],
    }


@validator_args
def flake_show(flakes_flake_id_exists, not_missing, boolean_validator):
    return {
        "id": [not_missing, flakes_flake_id_exists],
        "expand": [boolean_validator],
    }


@validator_args
def flake_list(boolean_validator, user_id_or_name_exists, not_missing):
    return {
        "author_id": [not_missing, user_id_or_name_exists],
        "expand": [boolean_validator],
    }
