from __future__ import annotations

from ckan.authz import is_authorized

from ckanext.toolbelt.decorators import Collector

from ..model import Flake

auth, get_auth = Collector("flakes").split()


@auth
def flake_create(context, data_dict):
    return is_authorized("package_create", context, {})

@auth
def flake_update(context, data_dict):
    flake = context["session"].query(Flake).filter_by(id=data_dict["id"]).one()

    return {"success": flake.author.name == context["user"]}

@auth
def flake_show(context, data_dict):
    flake = context["session"].query(Flake).filter_by(id=data_dict["id"]).one()
    return {"success": flake.author.name == context["user"]}

@auth
def flake_list(context, data_dict):
    user = context["model"].User.get(data_dict["author_id"])

    return {"success": user.name == context["user"]}

@auth
def flake_delete(context, data_dict):
    flake = context["session"].query(Flake).filter_by(id=data_dict["id"]).one()

    return {"success": flake.author.name == context["user"]}
