from __future__ import annotations

import ckan.plugins.toolkit as tk
from ckan.logic import validate

from ckanext.toolbelt.decorators import Collector

from . import schema
from ..model import Flake

action, get_actions = Collector("flakes").split()


@action
@validate(schema.flake_show)
def flake_show(context, data_dict):
    """Display existing flake

    Args:
        id (str): ID of flake to update
        expand (bool, optional): Extend flake using data from the parent flakes
    """

    tk.check_access("flakes_flake_show", context, data_dict)

    sess = context["session"]
    flake = sess.query(Flake).filter_by(id=data_dict["id"]).one()
    context["expand"] = data_dict["expand"]

    return flake.for_json(context)


@action
@validate(schema.flake_list)
def flake_list(context, data_dict):
    """Display all flakes of the user.

    Args:
        author_id (str): ID of the flake's owner
        expand (bool, optional): Extend flake using data from the parent flakes
    """

    tk.check_access("flakes_flake_list", context, data_dict)

    user = context["model"].User.get(data_dict["author_id"])
    context["expand"] = data_dict["expand"]

    return [flake.for_json(context) for flake in user.flakes]


@action
@validate(schema.flake_update)
def flake_update(context, data_dict):
    """Update existing flake

    Args:
        id (str): ID of flake to update
        data (dict): template itself
        parent_id (str, optional): ID of flake to extend
    """

    tk.check_access("flakes_flake_update", context, data_dict)

    sess = context["session"]
    flake = sess.query(Flake).filter_by(id=data_dict["id"]).one()
    for k, v in data_dict.items():
        setattr(flake, k, v)

    sess.commit()

    return flake.for_json(context)


@action
@validate(schema.flake_create)
def flake_create(context, data_dict):
    """Create flake that can be used as base template for dataset.

    Args:
        data (dict): template itself
        parent_id (str, optional): ID of flake to extend
        author_id (str, optional): ID of the flake's author(requires sysadmin account)
    """

    tk.check_access("flakes_flake_create", context, data_dict)

    sess = context["session"]
    user = context["model"].User.get(context["user"])

    if "author_id" in data_dict and (
        context.get("ignore_auth") or context["auth_user_obj"].sysadmin
    ):
        author_id = context["model"].User.get(data_dict["author_id"]).id

    elif user:
        author_id = user.id

    elif context.get("ignore_auth"):
        site_user = tk.get_action("get_site_user")({"ignore_auth": True}, {})
        author_id = context["model"].User.get(site_user["name"]).id

    else:
        raise tk.NotAuthorized()

    data_dict["author_id"] = author_id

    flake = Flake(**data_dict)
    sess.add(flake)
    sess.commit()

    return flake.for_json(context)

@action
@validate(schema.flake_delete)
def flake_delete(context, data_dict):
    """Delete existing flake

    Args:
        id (str): ID of flake to update
    """

    tk.check_access("flakes_flake_delete", context, data_dict)

    sess = context["session"]
    flake = sess.query(Flake).filter_by(id=data_dict["id"]).one()
    sess.delete(flake)
    sess.commit()

    return flake.for_json(context)
