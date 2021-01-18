import uuid
from src.utils.Enum import Enum

SEP = "!"
HEADER = 3


def assemble(*msg: str):
    """
    This function will create a string that follows the protocol.
    :param msg: Strings to create the protocol string
    :return: The full protocol string
    """
    final = ''
    for request in msg:
        final += "{}{}".format(request, SEP)

    return final


def split(msg: str):
    """
    This function will split the msg to a list according to the separator char.
    :param msg: A raw msg from network to split.
    :return: A list when each index contains a part of the msg.
    """
    msg = msg.split(SEP)
    return msg[:len(msg) - 1]


def get_mac_add():
    return '.'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                    for ele in range(0, 8 * 6, 8)][::-1])


class NetCommands(Enum):
    """
    All the msgs type that the computer can send to the server by it's self.
    """
    APPROVAL = "APPROVAL"
    DISAPPROVAL = "DISAPPROVAL"
    ID_VAL = "ID_VAL"
    DISCONNECT = "DISCON"


class NetLogicIncomes(Enum):
    """
    Incoming msgs from the server,
    """
    VALID = "VALID"
    INVALID = "INVALID"
    PAIRED = "HELLO"
    CONNECT = "CONN"
