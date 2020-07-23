{"filter":false,"title":"type.py","tooltip":"/prathap/typing/type.py","ace":{"folds":[],"scrolltop":568,"scrollleft":0,"selection":{"start":{"row":70,"column":0},"end":{"row":70,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":39,"state":"start","mode":"ace/mode/python"}},"hash":"8a93feb846b5abdfba96a2218845b94d4a7cd37d","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":70,"column":0},"action":"insert","lines":["import io","import re","","from collections import deque, namedtuple","from typing import (","    Dict,","    List,","    Tuple,","    Set,","    Deque,","    NamedTuple,","    IO,","    Pattern,","    Match,","    Text,","    Optional,","    Sequence,","    Iterable,","    Mapping,","    MutableMapping,","    Any,",")","","# without initializing","x: int","","# any type","y: Any","y = 1","y = \"1\"","","# built-in","var_int: int = 1","var_str: str = \"Hello Typing\"","var_byte: bytes = b\"Hello Typing\"","var_bool: bool = True","var_float: float = 1.","var_unicode: Text = u'\\u2713'","","# could be none","var_could_be_none: Optional[int] = None","var_could_be_none = 1","","# collections","var_set: Set[int] = {i for i in range(3)}","var_dict: Dict[str, str] = {\"foo\": \"Foo\"}","var_list: List[int] = [i for i in range(3)]","var_Tuple: Tuple = (1, 2, 3)","var_deque: Deque = deque([1, 2, 3])","var_nametuple: NamedTuple = namedtuple('P', ['x', 'y'])","","# io","var_io_str: IO[str] = io.StringIO(\"Hello String\")","var_io_byte: IO[bytes] = io.BytesIO(b\"Hello Bytes\")","var_io_file_str: IO[str] = open(__file__)","var_io_file_byte: IO[bytes] = open(__file__, 'rb')","","# re","p: Pattern = re.compile(\"(https?)://([^/\\r\\n]+)(/[^\\r\\n]*)?\")","m: Optional[Match] = p.match(\"https://www.python.org/\")","","# duck types: list-like","var_seq_list: Sequence[int] = [1, 2, 3]","var_seq_tuple: Sequence[int] = (1, 2, 3)","var_iter_list: Iterable[int] = [1, 2, 3]","var_iter_tuple: Iterable[int] = (1, 2, 3)","","# duck types: dict-like","var_map_dict: Mapping[str, str] = {\"foo\": \"Foo\"}","var_mutable_dict: MutableMapping[str, str] = {\"bar\": \"Bar\"}",""],"id":1}]]},"timestamp":1589266429515}