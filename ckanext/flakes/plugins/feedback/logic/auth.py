from __future__ import annotations
from typing import Any

import ckan.plugins.toolkit as tk
from ckan.authz import is_authorized
from ckan import types


def flakes_feedback_feedback_create(context: types.Context, data_dict: dict[str, Any]):
    return is_authorized("flakes_flake_create", context, data_dict)


def flakes_feedback_feedback_update(context: types.Context, data_dict: dict[str, Any]):
    return is_authorized("flakes_flake_update", context, data_dict)


def flakes_feedback_feedback_delete(context: types.Context, data_dict: dict[str, Any]):
    return is_authorized("flakes_flake_delete", context, data_dict)


@tk.auth_allow_anonymous_access
def flakes_feedback_feedback_list(context: types.Context, data_dict: dict[str, Any]):
    return is_authorized("package_show", context, {"id": data_dict["package_id"]})


@tk.auth_allow_anonymous_access
def flakes_feedback_feedback_show(context: types.Context, data_dict: dict[str, Any]):
    return {"success": True}
