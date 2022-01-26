from typing import Any, Union, Optional


class TypeQLException(Exception):
    def __init__(
        self,
        msg: Union["ErrorMessage", str],
        cause: Optional[BaseException],
        params: Any = None,
    ):
        if isinstance(msg, str):
            self.message = msg
            self.error_message = None
        else:
            self.message = msg.message(params)
            self.error_message = msg

        self.__cause__ = cause
        super(TypeQLException, self).__init__(self.message)

    @staticmethod
    def of(error_message: "ErrorMessage", params: Any = None):
        return TypeQLException(msg=error_message, cause=None, params=params)


class ErrorMessage:
    def __init__(
        self, code_prefix: str, code_number: int, message_prefix: str, message_body: str
    ):
        self._code_prefix = code_prefix
        self._code_number = code_number
        self._message = message_prefix + ": " + message_body

    def code(self) -> str:
        return self._code_prefix + str(self._code_number).zfill(2)

    def message(self, params: Any) -> str:
        return self._message % params if params else self._message

    def __str__(self):
        return "[%s] %s" % (self.code(), self._message)


class TypeQLErrorMessage(ErrorMessage):
    def __init__(self, code: int, message: str):
        super(TypeQLErrorMessage, self).__init__(
            code_prefix="TQL",
            code_number=code,
            message_prefix="TypeQL Error",
            message_body=message,
        )


ILLEGAL_STATE = TypeQLErrorMessage(1, "Illegal internal state!")
SYNTAX_ERROR_NO_DETAILS = TypeQLErrorMessage(
    2, "There is a syntax error at line %s:\n%s"
)
SYNTAX_ERROR_DETAILED = TypeQLErrorMessage(
    3, "There is a syntax error at line %s:\n%s\n%s\n%s"
)
INVALID_CASTING = TypeQLErrorMessage(4, "The class '%s' cannot be casted to '%s'.")
MISSING_PATTERNS = TypeQLErrorMessage(
    5, "The query has not been provided with any patterns."
)
MISSING_DEFINABLES = TypeQLErrorMessage(
    6, "The query has not been provided with any definables."
)
MATCH_HAS_NO_BOUNDING_NAMED_VARIABLE = TypeQLErrorMessage(
    7,
    "The match query does not have named variables to bound the nested disjunction/negation pattern(s).",
)
MATCH_HAS_NO_NAMED_VARIABLE = TypeQLErrorMessage(
    8, "The match query has no named variables to retrieve."
)
MATCH_HAS_UNBOUNDED_NESTED_PATTERN = TypeQLErrorMessage(
    9, "The match query contains a nested pattern is not bounded: '%s'."
)
MISSING_MATCH_FILTER = TypeQLErrorMessage(
    10, "The match query cannot be constructed with NULL filter variable collection."
)
EMPTY_MATCH_FILTER = TypeQLErrorMessage(
    11, "The match query cannot be filtered with an empty list of variables."
)
INVALID_IID_STRING = TypeQLErrorMessage(
    12, "Invalid IID: '%s'. IIDs must follow the regular expression: '%s'."
)
INVALID_ATTRIBUTE_TYPE_REGEX = TypeQLErrorMessage(
    13, "Invalid regular expression '%s'."
)
ILLEGAL_FILTER_VARIABLE_REPEATING = TypeQLErrorMessage(
    14, "The variable '%s' occurred more than once in match query filter."
)
VARIABLE_OUT_OF_SCOPE_MATCH = TypeQLErrorMessage(
    15, "The variable '%s' is out of scope of the match query."
)
VARIABLE_OUT_OF_SCOPE_DELETE = TypeQLErrorMessage(
    16, "The deleted variable '%s' is out of scope of the match query."
)
NO_VARIABLE_IN_SCOPE_INSERT = TypeQLErrorMessage(
    17, "None of the variables in 'insert' ('%s') is within scope of 'match' ('%s')"
)
VARIABLE_NOT_NAMED = TypeQLErrorMessage(
    18, "The variable '%s' is not named and cannot be used as a filter for match query."
)
INVALID_VARIABLE_NAME = TypeQLErrorMessage(
    19,
    "The variable name '%s' is invalid; variables must match the following regular expression: '%s'.",
)
ILLEGAL_CONSTRAINT_REPETITION = TypeQLErrorMessage(
    20, "The variable '%s' contains illegally repeating constraints: '%s' and '%s'."
)
MISSING_CONSTRAINT_RELATION_PLAYER = TypeQLErrorMessage(
    21, "A relation variable has not been provided with role players."
)
MISSING_CONSTRAINT_VALUE = TypeQLErrorMessage(
    22, "A value constraint has not been provided with a variable or literal value."
)
MISSING_CONSTRAINT_PREDICATE = TypeQLErrorMessage(
    23, "A value constraint has not been provided with a predicate."
)
INVALID_CONSTRAINT_DATETIME_PRECISION = TypeQLErrorMessage(
    24,
    "Attempted to assign DateTime value of '%s' which is more precise than 1 millisecond.",
)
INVALID_DEFINE_QUERY_VARIABLE = TypeQLErrorMessage(
    25,
    "Invalid define/undefine query. User defined variables are not accepted in define/undefine query.",
)
INVALID_RULE_WHEN_MISSING_PATTERNS = TypeQLErrorMessage(
    26, "Rule '%s' 'when' has not been provided with any patterns."
)
INVALID_RULE_WHEN_NESTED_NEGATION = TypeQLErrorMessage(
    27, "Rule '%s' 'when' contains a nested negation."
)
INVALID_RULE_WHEN_CONTAINS_DISJUNCTION = TypeQLErrorMessage(
    28, "Rule '%s' 'when' contains a disjunction."
)
INVALID_RULE_THEN = TypeQLErrorMessage(
    29,
    "Rule '%s' 'then' '%s': must be exactly one attribute ownership, or exactly one relation.",
)
INVALID_RULE_THEN_HAS = TypeQLErrorMessage(
    30,
    "Rule '%s' 'then' '%s': is trying to assign both an attribute type and a variable attribute value.",
)
INVALID_RULE_THEN_VARIABLES = TypeQLErrorMessage(
    31, "Rule '%s' 'then' variables must be present in rule 'when'."
)
REDUNDANT_NESTED_NEGATION = TypeQLErrorMessage(
    32, "Invalid query containing redundant nested negations."
)
MISSING_COMPUTE_CONDITION = TypeQLErrorMessage(
    33, "Missing condition(s) for 'compute '%s''. The required condition(s) are: '%s'."
)
INVALID_COMPUTE_METHOD_ALGORITHM = TypeQLErrorMessage(
    34, "Invalid algorithm for 'compute '%s''. The accepted algorithm(s) are: '%s'."
)
INVALID_COMPUTE_ARGUMENT = TypeQLErrorMessage(
    35, "Invalid argument(s) 'compute %s using %s'. The accepted argument(s) are: '%s'."
)
INVALID_SORTING_ORDER = TypeQLErrorMessage(
    36, "Invalid sorting order. Valid options: '%s' or '%s'."
)
INVALID_COUNT_VARIABLE_ARGUMENT = TypeQLErrorMessage(
    37, "Aggregate COUNT does not accept a Variable."
)
ILLEGAL_GRAMMAR = TypeQLErrorMessage(38, "Illegal grammar!")
ILLEGAL_CHAR_IN_LABEL = TypeQLErrorMessage(
    39,
    "'%s' is not a valid Type label. Type labels must start with a letter, and may contain only letters, numbers, '-' and '_'.",
)
