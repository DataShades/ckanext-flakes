from __future__ import annotations

from ckan.authz import is_authorized

from ckanext.toolbelt.decorators import Collector

from ..model import Flake

auth, get_auth = Collector("flakes").split()


@auth
def flake_create(context, data_dict):
    author = context["model"].User.get(context["user"])

    if "parent_id" in data_dict:
        parent = context["session"].query(Flake).filter_by(id=data_dict["parent_id"]).one_or_none()
        if not parent or parent.author_id != author.id:
            return {"success": False}

    return is_authorized("package_create", context, {})


@auth
def flake_show(context, data_dict):
    flake = context["session"].query(Flake).filter_by(id=data_dict["id"]).one_or_none()
    return {"success": flake and flake.author.name == context["user"]}

@auth
def flake_update(context, data_dict):
    return flake_show(context, data_dict)


@auth
def flake_lookup(context, data_dict):
    return {"success": True}


@auth
def flake_list(context, data_dict):
    return {"success": True}


@auth
def flake_delete(context, data_dict):
    return flake_show(context, data_dict)
