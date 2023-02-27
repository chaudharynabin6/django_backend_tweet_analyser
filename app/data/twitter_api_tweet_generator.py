from typing import List


class Datum:
    edit_history_tweet_ids: List[str]
    id: str
    text: str

    def __init__(self, edit_history_tweet_ids: List[str], id: str, text: str) -> None:
        self.edit_history_tweet_ids = edit_history_tweet_ids
        self.id = id
        self.text = text


class Meta:
    newest_id: str
    oldest_id: str
    result_count: int
    next_token: str

    def __init__(self, newest_id: str, oldest_id: str, result_count: int, next_token: str) -> None:
        self.newest_id = newest_id
        self.oldest_id = oldest_id
        self.result_count = result_count
        self.next_token = next_token


class RootData:
    data: List[Datum]
    meta: Meta

    def __init__(self, data: List[Datum], meta: Meta) -> None:
        self.data = data
        self.meta = meta