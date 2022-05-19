import ckan.model as model
import ckan.plugins.toolkit as tk
import pytest
from ckan.tests.helpers import call_action

from ckanext.flakes.model import Flake


@pytest.mark.usefixtures("with_plugins", "clean_db")
class TestFlakeCreate:
    def test_base(self):
        result = call_action("flakes_flake_create", data={})
        assert model.Session.query(Flake).filter_by(id=result["id"]).one()

    def test_controlled_id(self):
        result = call_action(
            "flakes_flake_create", data={}, id="hello-world"
        )
        assert result["id"] == "hello-world"

        with pytest.raises(tk.ValidationError):
            call_action("flakes_flake_create", data={}, id="hello-world")

    def test_parent_flake(self):
        parent = call_action("flakes_flake_create", data={})

        with pytest.raises(tk.ValidationError):
            call_action("flakes_flake_create", data={}, parent_id="not-real")

        child = call_action(
            "flakes_flake_create", data={}, parent_id=parent["id"]
        )
        assert child["parent_id"] == parent["id"]


@pytest.mark.usefixtures("with_plugins", "clean_db")
class TestFlakeUpdate:
    def test_parent_flake(self):
        flake = call_action("flakes_flake_create", data={})
        q = model.Session.query(Flake).filter_by(id=flake["id"])
        context = {"model": model, "session": model.Session}

        assert q.one().for_json(context) == flake

        updated = call_action(
            "flakes_flake_update", id=flake["id"], data={"hello": "world"}
        )
        assert flake["id"] == updated["id"]
        assert updated["data"] == {"hello": "world"}
        assert q.one().for_json(context) == updated


@pytest.mark.usefixtures("with_plugins", "clean_db")
class TestFlakeDelete:
    def test_base(self):
        flake = call_action("flakes_flake_create", data={})
        call_action("flakes_flake_delete", id=flake["id"])
        assert (
            not model.Session.query(Flake)
            .filter_by(id=flake["id"])
            .one_or_none()
        )


@pytest.mark.usefixtures("with_plugins", "clean_db")
class TestFlakeShow:
    def test_base(self):
        flake = call_action(
            "flakes_flake_create",
            data={"hello": "world", "override": "parent"},
        )
        result = call_action("flakes_flake_show", id=flake["id"])
        assert flake == result

    def test_parent(self):
        parent = call_action("flakes_flake_create", data={"hello": "world"})
        child = call_action(
            "flakes_flake_create",
            data={"override": "child"},
            parent_id=parent["id"],
        )

        result = call_action("flakes_flake_show", id=child["id"])
        assert result["data"] == {"override": "child"}

        result = call_action(
            "flakes_flake_show", id=child["id"], expand=True
        )
        assert result["data"] == {"override": "child", "hello": "world"}


@pytest.mark.usefixtures("with_plugins", "clean_db")
class TestFlakeList:
    def test_base(self, user):
        first = call_action(
            "flakes_flake_create", data={}, author_id=user["id"]
        )
        second = call_action(
            "flakes_flake_create", data={}, author_id=user["id"]
        )
        result = call_action("flakes_flake_list", author_id=user["id"])
        assert {first["id"], second["id"]} == {f["id"] for f in result}

    def test_parent(self, user):
        parent = call_action(
            "flakes_flake_create",
            data={"hello": "world"},
            author_id=user["id"],
        )

        call_action(
            "flakes_flake_create",
            data={"override": "first"},
            author_id=user["id"],
        )
        call_action(
            "flakes_flake_create",
            data={"override": "second"},
            author_id=user["id"],
            parent_id=parent["id"],
        )

        result = call_action("flakes_flake_list", author_id=user["id"])
        datas = [f["data"] for f in result]
        assert {"hello": "world"} in datas
        assert {"override": "first"} in datas
        assert {"override": "second"} in datas

        result = call_action(
            "flakes_flake_list", author_id=user["id"], expand=True
        )
        datas = [f["data"] for f in result]
        assert {"hello": "world"} in datas
        assert {"override": "first"} in datas
        assert {"hello": "world", "override": "second"} in datas
