{"filter":false,"title":"test_is_valid_user.py","tooltip":"/ib_miniprojects_backend/resource_management/tests/storages/test_is_valid_user.py","undoManager":{"mark":27,"position":27,"stack":[[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":19,"column":47},"action":"insert","lines":["import pytest","from resource_management.storages.user_storage_implementation import \\","    UserStorageImplementation","","@pytest.mark.django_db","def test_invalid_username():","","    #Assert","    username = 'Naveen'","    expected_response = False","","    user_storage_implement = UserStorageImplementation()","","    #Act","    actual_response = user_storage_implement.validate_username(","        username=username","    )","","    #Assert","    assert actual_response == expected_response"],"id":2}],[{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"remove","lines":["e"],"id":3},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"remove","lines":["m"]},{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"remove","lines":["a"]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"remove","lines":["n"]}],[{"start":{"row":14,"column":45},"end":{"row":14,"column":62},"action":"remove","lines":["validate_username"],"id":4},{"start":{"row":14,"column":45},"end":{"row":14,"column":58},"action":"insert","lines":["is_valid_user"]}],[{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"remove","lines":["'"],"id":5},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"remove","lines":["n"]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"remove","lines":["e"]},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"remove","lines":["e"]},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"remove","lines":["v"]},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"remove","lines":["a"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"remove","lines":["N"]},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"remove","lines":["'"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"remove","lines":[" "]},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"remove","lines":["="]},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"remove","lines":[" "]},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"remove","lines":["e"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"remove","lines":["m"]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"remove","lines":["a"]},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"remove","lines":["n"]}],[{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["_"],"id":6},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["i"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["d"]}],[{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":[" "],"id":7},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":[" "],"id":8},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["1"]}],[{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"remove","lines":["e"],"id":9},{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"remove","lines":["m"]},{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"remove","lines":["a"]},{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"remove","lines":["n"]},{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"remove","lines":["r"]},{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"remove","lines":["e"]},{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"remove","lines":["s"]},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"remove","lines":["u"]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"remove","lines":["="]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"remove","lines":["e"]},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"remove","lines":["m"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"remove","lines":["a"]},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"remove","lines":["n"]}],[{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["_"],"id":10},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["i"]},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["d"]}],[{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":[" "],"id":11},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["="]}],[{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":[" "],"id":12}],[{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"remove","lines":[" "],"id":13},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"remove","lines":["="]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"remove","lines":[" "]}],[{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["="],"id":14}],[{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":[" "],"id":15}],[{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"remove","lines":[" "],"id":16}],[{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["u"],"id":17},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":["s"]},{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"insert","lines":["e"]},{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"insert","lines":["r"]}],[{"start":{"row":15,"column":16},"end":{"row":15,"column":20},"action":"remove","lines":["user"],"id":18},{"start":{"row":15,"column":16},"end":{"row":15,"column":23},"action":"insert","lines":["user_id"]}],[{"start":{"row":11,"column":25},"end":{"row":11,"column":26},"action":"remove","lines":["t"],"id":19},{"start":{"row":11,"column":24},"end":{"row":11,"column":25},"action":"remove","lines":["n"]},{"start":{"row":11,"column":23},"end":{"row":11,"column":24},"action":"remove","lines":["e"]},{"start":{"row":11,"column":22},"end":{"row":11,"column":23},"action":"remove","lines":["m"]},{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"remove","lines":["e"]},{"start":{"row":11,"column":20},"end":{"row":11,"column":21},"action":"remove","lines":["l"]},{"start":{"row":11,"column":19},"end":{"row":11,"column":20},"action":"remove","lines":["p"]},{"start":{"row":11,"column":18},"end":{"row":11,"column":19},"action":"remove","lines":["m"]},{"start":{"row":11,"column":17},"end":{"row":11,"column":18},"action":"remove","lines":["i"]},{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"remove","lines":["_"]}],[{"start":{"row":14,"column":22},"end":{"row":14,"column":44},"action":"remove","lines":["user_storage_implement"],"id":20},{"start":{"row":14,"column":22},"end":{"row":14,"column":34},"action":"insert","lines":["user_storage"]}],[{"start":{"row":19,"column":47},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":21},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "],"id":22}],[{"start":{"row":20,"column":0},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":23},{"start":{"row":21,"column":0},"end":{"row":22,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":22,"column":0},"end":{"row":37,"column":47},"action":"insert","lines":["@pytest.mark.django_db","def test_invalid_user():","","    #Assert","    user_id = 1","    expected_response = False","","    user_storage = UserStorageImplementation()","","    #Act","    actual_response = user_storage.is_valid_user(","        user_id=user_id","    )","","    #Assert","    assert actual_response == expected_response"],"id":24}],[{"start":{"row":23,"column":10},"end":{"row":23,"column":11},"action":"remove","lines":["n"],"id":25},{"start":{"row":23,"column":9},"end":{"row":23,"column":10},"action":"remove","lines":["i"]}],[{"start":{"row":27,"column":28},"end":{"row":27,"column":29},"action":"remove","lines":["e"],"id":26},{"start":{"row":27,"column":27},"end":{"row":27,"column":28},"action":"remove","lines":["s"]},{"start":{"row":27,"column":26},"end":{"row":27,"column":27},"action":"remove","lines":["l"]},{"start":{"row":27,"column":25},"end":{"row":27,"column":26},"action":"remove","lines":["a"]},{"start":{"row":27,"column":24},"end":{"row":27,"column":25},"action":"remove","lines":["F"]}],[{"start":{"row":27,"column":24},"end":{"row":27,"column":25},"action":"insert","lines":["T"],"id":27},{"start":{"row":27,"column":25},"end":{"row":27,"column":26},"action":"insert","lines":["r"]},{"start":{"row":27,"column":26},"end":{"row":27,"column":27},"action":"insert","lines":["u"]},{"start":{"row":27,"column":27},"end":{"row":27,"column":28},"action":"insert","lines":["e"]}],[{"start":{"row":23,"column":20},"end":{"row":23,"column":31},"action":"insert","lines":["create_user"],"id":28}]]},"ace":{"folds":[],"scrolltop":66,"scrollleft":0,"selection":{"start":{"row":23,"column":31},"end":{"row":23,"column":31},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1591165811341,"hash":"a31c4c1dcdb5c2275a6dd8e3b9a4879508c4e983"}