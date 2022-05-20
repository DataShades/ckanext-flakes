import ckan.plugins as p

from .logic import action, auth, validators


class FlakesPlugin(p.SingletonPlugin):
    p.implements(p.IActions)
    p.implements(p.IAuthFunctions)
    p.implements(p.IValidators)

    def get_actions(self):
        return action.get_actions()

    def get_auth_functions(self):
        return auth.get_auth()

    def get_validators(self):
        return validators.get_validators()
