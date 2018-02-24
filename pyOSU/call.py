"""
Call

Makes calls to osu api and handles 
data sent and received
"""
from .constants import *
from .exceptions import InvalidModeException, InvalidUserTypeException, InvalidEventRangeException
from requests import get


class Call:
    def __init__(self, key):
        """
        :param key: API Key 
        """
        self.key = key

    def __build_url(self, call_type, **kwargs):
        """
        Builds api url given the specified call type and additional arguments
        
        :param call_type: api call type
        :param kwargs: additional arguments
        :return: string
        """
        arguments = CONCAT.join(
            "{}={}".format(str(k), str(v)) for k, v in kwargs.items()
        )
        return "{}{}{}{}".format(
            BASE_URL, call_type, arguments,
            "&k=" + self.key
        )

    @staticmethod
    def __check_mode(m):
        """
        Check that the mode is valid\
        
        :param m: mode type
        :return: bool
        """
        if m not in range(0, 3):
            return False
        return True

    def get_user(self, u, default=True, m=0, _type="string", event_days=1):
        """
        Get information about a specified user
        
        :param u: specify a user_id or a username to return metadata from
        :param m: mode (0 = osu!, 1 = Taiko, 2 = CtB, 3 = osu!mania). Optional, default value is 0.
        :param _type: specify if u is a user_id or a username. Use string for usernames or id for user_ids. 
        :param event_days: days between now and last event date. Range of 1-31. Optional, default value is 1.
        :param default: Default call to api using the user name only
        :return: api data
        """
        # Check mode
        if not self.__check_mode(m):
            raise InvalidModeException
        # Check for valid even range
        if event_days not in range(1, 31):
            raise InvalidEventRangeException
        # Check user type
        if _type not in ["string", "id"]:
            raise InvalidUserTypeException
        # check if user wants a default url
        if default:
            return get(self.__build_url(GET_USER, u=u)).json()
        # otherwise build url
        url = self.__build_url(GET_USER, u=u, m=m, type=_type, event_days=event_days)
        # Call API
        return get(url).json()
