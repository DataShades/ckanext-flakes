from __future__ import annotations

import ckan.plugins as p
import ckan.plugins.toolkit as tk

from ckan import types


def enable_views() -> bool:
    return tk.asbool(tk.config.get("ckanext.flakes_feedback.enable_views", False))


@tk.blanket.config_declarations
@tk.blanket.auth_functions
@tk.blanket.actions
@tk.blanket.blueprints
@tk.blanket.helpers(
    {
        "flakes_feedback_enable_views": enable_views,
    }
)
class FlakesFeedbackPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer, inherit=True)

    def update_config(self, config: types.CKANConfig):
        tk.add_template_directory(config, "templates")
        tk.add_resource("assets", "flakes_feedback")
