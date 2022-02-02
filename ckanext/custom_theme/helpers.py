
import ckan.plugins.toolkit as toolkit

def custom_theme_hello():
    return "Hello, custom_theme!"


def most_popular_groups():

    '''Return a sorted list of the groups with the most datasets.'''

    # Get a list of all the site's groups from CKAN, sorted by number of
    # datasets.

    groups = toolkit.get_action('group_list')(
        data_dict={'sort': 'package_count desc', 'all_fields': True})

    groups = groups[:10]

    return groups


# def top_datasets():
#
#     """Return a sorted list of the datasets with the most <todo>."""
#
#     # Get a list of all the site's groups from CKAN, sorted by number of
#     # datasets.
#
#     groups = toolkit.get_action('group_list')(
#         data_dict={'sort': 'package_count desc', 'all_fields': True})
#
#     groups = groups[:10]
#
#     return groups

def get_helpers():
    return {
        "custom_theme_hello": custom_theme_hello,
        "custom_theme_most_popular_groups": most_popular_groups,
    }
