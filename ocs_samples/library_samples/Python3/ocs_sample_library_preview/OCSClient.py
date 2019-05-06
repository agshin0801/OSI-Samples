# OCSClient.py
#

from .BaseClient import BaseClient
from .Dataviews import Dataviews
from .Types import Types
from .Streams import Streams
from .SdsError import SdsError


class OCSClient:
    """
    A client that handles communication with OCS
    """

    def __init__(self, apiversion, tenant, url, clientId, clientSecret):
        """
        Use this to help comuninaication with OCS
        :param apiversion: Version of the api you are communicating with
        :param tenant: Your tenant ID
        :param url: The base URL for your OCS instance
        :param clientId: Your client ID
        :param clientSecret: Your client Secret or Key
        """
        self.__baseClient = BaseClient(apiversion, tenant, url, clientId, clientSecret)
        
        self.__Dataviews  = Dataviews(self.__baseClient)
        self.__Types  = Types(self.__baseClient)
        self.__Streams  = Streams(self.__baseClient)

    @property 
    def uri(self):
        """
        :return: The uri of this OCS client as a string
        """
        return self.__baseClient.uri

    @property 
    def tenant(self):
        """
        :return: The tenant of this OCS client as a string
        """
        return self.__baseClient.tenant

    @property
    def Dataviews(self):
        """
        :return: A client for interacting with Dataviews
        """
        return self.__Dataviews

    @property 
    def Types(self):
        """
        :return: A client for interacting with Types
        """
        return self.__Types

    @property 
    def Streams(self):
        """
        :return: A client for interacting with Streams
        """
        return self.__Streams
