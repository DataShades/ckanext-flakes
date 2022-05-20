import ckan.model as model
import ckan.plugins.toolkit as tk
import pytest
from ckan.tests.helpers import call_action, call_auth

from ckanext.flakes.model import Flake


@pytest.mark.usefixtures("with_plugins")
@pytest.mark.parametrize(
    "auth",
    [
        "flakes_flake_create",
        "flakes_flake_delete",
        "flakes_flake_show",
        "flakes_flake_list",
        "flakes_flake_update",
        "flakes_flake_lookup",
    ],
)
def test_annon_cannot(auth):
    with pytest.raises(tk.NotAuthorized):
        call_auth(auth, {"user": ""})


@pytest.mark.usefixtures("with_plugins", "clean_db")
@pytest.mark.parametrize(
    "auth",
    [
        "flakes_flake_create",
        "flakes_flake_list",
        "flakes_flake_lookup",
    ],
)
def test_user_can(auth, user):
    assert call_auth("flakes_flake_create", {"user": user["name"]})


@pytest.mark.usefixtures("with_plugins", "clean_db")
class TestUpdate:
    def test_user_can_update(self, user_factory):
        user = user_factory()
        author = user_factory()
        flake = call_action("flakes_flake_create", {"user": author["name"]}, data={})

        assert call_auth(
            "flakes_flake_update", {"user": author["name"]}, id=flake["id"]
        )
        with pytest.raises(tk.NotAuthorized):
            call_auth("flakes_flake_update", {"user": user["name"]}, id=flake["id"])


@pytest.mark.usefixtures("with_plugins", "clean_db")
class TestDelete:
    def test_user_can_delete(self, user_factory):
        user = user_factory()
        author = user_factory()
        flake = call_action("flakes_flake_create", {"user": author["name"]}, data={})

        assert call_auth(
            "flakes_flake_delete", {"user": author["name"]}, id=flake["id"]
        )
        with pytest.raises(tk.NotAuthorized):
            call_auth("flakes_flake_delete", {"user": user["name"]}, id=flake["id"])


@pytest.mark.usefixtures("with_plugins", "clean_db")
class TestShow:
    def test_user_can_show(self, user_factory):
        user = user_factory()
        author = user_factory()
        flake = call_action("flakes_flake_create", {"user": author["name"]}, data={})

        assert call_auth("flakes_flake_show", {"user": author["name"]}, id=flake["id"])
        with pytest.raises(tk.NotAuthorized):
            call_auth("flakes_flake_show", {"user": user["name"]}, id=flake["id"])
