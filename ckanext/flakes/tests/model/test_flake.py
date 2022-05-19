import ckan.model as model
import pytest

from ckanext.flakes.model.flake import Flake


@pytest.mark.usefixtures("with_plugins", "clean_db")
class TestFlake:
    def test_autoremove_with_user(self, user):
        flake = Flake(data={}, author_id=user["id"])
        model.Session.add(flake)
        model.Session.commit()

        assert model.Session.query(Flake).filter_by(id=flake.id).one_or_none()

        userobj = model.User.get(user["id"])
        model.Session.delete(userobj)
        model.Session.commit()

        assert (
            not model.Session.query(Flake).filter_by(id=flake.id).one_or_none()
        )

    def test_user_not_removed_with_flake(self, user):
        flake = Flake(data={}, author_id=user["id"])
        model.Session.add(flake)
        model.Session.commit()

        assert model.Session.query(Flake).filter_by(id=flake.id).one_or_none()
        assert model.User.get(user["id"])

        model.Session.delete(flake)
        model.Session.commit()

        assert (
            not model.Session.query(Flake).filter_by(id=flake.id).one_or_none()
        )
        assert model.User.get(user["id"])

    def test_relationship(self, user):
        parent = Flake(data={}, author_id=user["id"])
        brother = Flake(data={}, author_id=user["id"], parent=parent)
        sister = Flake(data={}, author_id=user["id"], parent=parent)
        model.Session.add_all([parent, brother, sister])
        model.Session.commit()

        assert set(parent.flakes) == {brother, sister}
        assert brother.parent == parent
        assert sister.parent == parent

    def test_autoremove_of_flakes(self, user):
        parent = Flake(data={}, author_id=user["id"])
        brother = Flake(data={}, author_id=user["id"], parent=parent)
        sister = Flake(data={}, author_id=user["id"], parent=parent)
        model.Session.add_all([parent, brother, sister])
        model.Session.commit()

        q = model.Session.query(Flake)

        assert q.filter_by(id=parent.id).one_or_none()
        assert q.filter_by(id=brother.id).one_or_none()
        assert q.filter_by(id=sister.id).one_or_none()

        model.Session.delete(brother)
        model.Session.commit()
        assert q.filter_by(id=parent.id).one_or_none()
        assert not q.filter_by(id=brother.id).one_or_none()
        assert q.filter_by(id=sister.id).one_or_none()

        model.Session.delete(parent)
        model.Session.commit()
        assert not q.filter_by(id=parent.id).one_or_none()
        assert not q.filter_by(id=brother.id).one_or_none()
        assert not q.filter_by(id=sister.id).one_or_none()
