import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


# import ckanext.custom_theme.cli as cli
import ckanext.custom_theme.helpers as helpers
# import ckanext.custom_theme.views as views
# from ckanext.custom_theme.logic import (
#     action, auth, validators
# )


class CustomThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IFacets)
    # plugins.implements(plugins.IAuthFunctions)
    # plugins.implements(plugins.IActions)
    # plugins.implements(plugins.IBlueprint)
    # plugins.implements(plugins.IClick)
    # plugins.implements(plugins.ITemplateHelpers)
    # plugins.implements(plugins.IValidators)
    

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "custom_theme")

    
    # IAuthFunctions

    # def get_auth_functions(self):
    #     return auth.get_auth_functions()

    # IActions

    # def get_actions(self):
    #     return action.get_actions()

    # IBlueprint

    # def get_blueprint(self):
    #     return views.get_blueprints()

    # IClick

    # def get_commands(self):
    #     return cli.get_commands()

    # ITemplateHelpers

    def get_helpers(self):
        return helpers.get_helpers()

    # IValidators

    # def get_validators(self):
    #     return validators.get_validators()

    # IFacets
    def dataset_facets(self, facets_dict, package_type):
        """Add new search facet (filter) for datasets.
        This must be a field in the dataset (or organization or
        group if you're modifying those search facets, just change the function).
        """
        # This keeps the existing facet order.
        facets_dict['title'] = plugins.toolkit._('Title')

        # Return the updated facet dict.
        return facets_dict
