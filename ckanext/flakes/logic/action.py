from __future__ import annotations

import ckan.plugins.toolkit as tk
from ckan.logic import validate

from ckanext.toolbelt.decorators import Collector

from ..model import Flake
from . import schema

action, get_actions = Collector("flakes").split()


@action
@validate(schema.flake_create)
def flake_create(context, data_dict):
    """Create flake that can be used as base template for dataset.

    Args:
        name (str, optional): name of the flake
        data (dict): template itself
        parent_id (str, optional): ID of flake to extend
    """

    tk.check_access("flakes_flake_create", context, data_dict)

    sess = context["session"]
    model = context["model"]

    user = model.User.get(context["user"])
    if not user:
        raise tk.NotAuthorized()

    if "parent_id" in data_dict:
        parent = sess.query(Flake).filter_by(id=data_dict["parent_id"]).one()
        if parent.author_id != user.id:
            raise tk.ValidationError({"parent_id": ["Must be owned by the same user"]})

    if "name" in data_dict and Flake.by_name(data_dict["name"], user.id):
        raise tk.ValidationError({"name": ["Must be unique"]})

    flake = Flake(author_id=user.id, **data_dict)
    sess.add(flake)
    sess.commit()

    return flake.for_json(context)


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
        expand (bool, optional): Extend flake using data from the parent flakes
    """

    tk.check_access("flakes_flake_list", context, data_dict)

    user = context["model"].User.get(context["user"])
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


@action
@validate(schema.flake_lookup)
def flake_lookup(context, data_dict):
    """Search flake by name.

    Args:
        name (str): Name of the flake
    """

    tk.check_access("flakes_flake_lookup", context, data_dict)
    user = context["model"].User.get(context["user"])
    flake = Flake.by_name(data_dict["name"], user.id)

    if not flake:
        raise tk.ObjectNotFound()

    return flake.for_json(context)
