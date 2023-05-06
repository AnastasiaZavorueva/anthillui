#  file with all links used in pages & tests objects

class Links:
    login_page = "https://demo.anthill.su/login"
    forgot_password = "https://demo.anthill.su/forgot-password"
    register_page = "https://demo.anthill.su/register"

    wiki_page = "https://demo.anthill.su/apps/wiki"
    wiki_add_space_page = "https://demo.anthill.su/apps/wiki/space/add"
    wiki_edit_space_page = f"https://demo.anthill.su/apps/wiki/space/edit/"  # THIS URL IS INCOMPLETE
    # (should contain ID of a space in the end of URL, like "...space/edit/2345")
    wiki_space_home_page = f"https://demo.anthill.su/apps/wiki/space/"  # THIS URL IS INCOMPLETE
    # (should ends with this part containing ID of a space in the end, like "...space/2345/homepage")

    # not developed yet, so that's why empty
    privacy_policy_and_terms = ""
    login_with_facebook_page = ""
    login_with_google_page = ""
    login_with_twitter_page = ""

    analytics_page = "https://demo.anthill.su/dashboards/analytics"
    calendar_page = "https://demo.anthill.su/apps/calendar"

