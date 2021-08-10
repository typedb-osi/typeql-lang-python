from common.typeql_token import TypeQLToken
from query.typeql_definable import TypeQLDefinable
class TypeQLUndefine(TypeQLDefinable):
    def __init__(self, definables) -> None:
        #super(TypeQLToken.Command.UNDEFINE, definables).__init__()