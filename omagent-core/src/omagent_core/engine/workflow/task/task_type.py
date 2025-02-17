from enum import Enum


class TaskType(str, Enum):
    CUSTOM = "custom"
    SIMPLE = "SIMPLE"
    DYNAMIC = "DYNAMIC"
    FORK_JOIN = "FORK_JOIN"
    FORK_JOIN_DYNAMIC = "FORK_JOIN_DYNAMIC"
    DECISION = "DECISION"
    SWITCH = "SWITCH"
    JOIN = "JOIN"
    DO_WHILE = "DO_WHILE"
    SUB_WORKFLOW = "SUB_WORKFLOW"
    START_WORKFLOW = "START_WORKFLOW"
    EVENT = "EVENT"
    WAIT = "WAIT"
    WAIT_FOR_WEBHOOK = "WAIT_FOR_WEBHOOK"
    HUMAN = "HUMAN"
    USER_DEFINED = "USER_DEFINED"
    HTTP = "HTTP"
    HTTP_POLL = "HTTP_POLL"
    LAMBDA = "LAMBDA"
    INLINE = "INLINE"
    EXCLUSIVE_JOIN = "EXCLUSIVE_JOIN"
    TERMINATE = "TERMINATE"
    KAFKA_PUBLISH = "KAFKA_PUBLISH"
    JSON_JQ_TRANSFORM = "JSON_JQ_TRANSFORM"
    SET_VARIABLE = "SET_VARIABLE"
    GET_DOCUMENT = "GET_DOCUMENT"
    LLM_GENERATE_EMBEDDINGS = "LLM_GENERATE_EMBEDDINGS"
    LLM_GET_EMBEDDINGS = "LLM_GET_EMBEDDINGS"
    LLM_TEXT_COMPLETE = "LLM_TEXT_COMPLETE"
    LLM_CHAT_COMPLETE = "LLM_CHAT_COMPLETE"
    LLM_INDEX_TEXT = "LLM_INDEX_TEXT"
    LLM_INDEX_DOCUMENT = "LLM_INDEX_DOCUMENT"
    LLM_SEARCH_INDEX = "LLM_SEARCH_INDEX"
