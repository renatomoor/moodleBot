# ONLY TESTE WITH EPSIC MOODLE

#configuration file, please add the information missig

class Moodle:
    #Your principal URL:
    _URLBASE ="https://www.epsic.ch/secure/moodle"

    #Url of your modules list, you just need to change the is number with the one of your current year.
    _URLYEARLIST = _URLBASE + "/course/index.php?categoryid=10"


    #You do not need to touch this unless you know what are you doing:
    _URLLOGGIN = _URLBASE + "/login/index.php"
    _URLMOD = _URLBASE + "/mod/"
    _VIEWID = "/view.php?id="
    _URLBASEVIEW = _URLBASE + "/course/view.php"
    _TYPES = ["resource", "page", "url", "assign", "folder"]


class Channel:
    # Discord Webhook Link:
    _MOODLEBOT = '' # ADD *
    # Ex: https://discordapp.com/api/webhooks/485145419627524107/WPwb0J45Jh64Gdf_X7c9M4vILlQ8ooAoKYPBN_rdfvdfbvgdb4_n7LnUZ5417PwItJttf


class Hook:

    _BOTNAME = 'Moodle bot'
    _AVATAR = 'http://www.colby.edu/acits/wp-content/uploads/sites/178/2015/06/moodle-new-logo.png'


class UserAccount:
    # Your Moodle Username
    _USERNAME = '' # ADD *

    # Yout Moodle Password
    _PASSWORD = '' # ADD *

    # Your name in the page when you are logged in, normaly is at the top right of the page
    _USERTEXT = '' # ADD *