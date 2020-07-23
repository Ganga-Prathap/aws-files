{"filter":false,"title":"api_wrapper.py","tooltip":"/ib_miniprojects_backend/resource_management/views/get_items/api_wrapper.py","undoManager":{"mark":23,"position":23,"stack":[[{"start":{"row":0,"column":0},"end":{"row":28,"column":28},"action":"remove","lines":["from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","    # ---------MOCK IMPLEMENTATION---------","","    try:","        from resource_management.views.get_items.tests.test_case_01 \\","            import TEST_CASE as test_case","    except ImportError:","        from resource_management.views.get_items.tests.test_case_01 \\","            import test_case","","    from django_swagger_utils.drf_server.utils.server_gen.mock_response \\","        import mock_response","    try:","        from resource_management.views.get_items.request_response_mocks \\","            import RESPONSE_200_JSON","    except ImportError:","        RESPONSE_200_JSON = ''","    response_tuple = mock_response(","        app_name=\"resource_management\", test_case=test_case,","        operation_name=\"get_items\",","        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,","        group_name=\"\")","    return response_tuple[1]"],"id":2},{"start":{"row":0,"column":0},"end":{"row":42,"column":0},"action":"insert","lines":["from django.http import HttpResponse","from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from raven.utils import json","from resource_management.interactors.get_user_items_interactor import \\","    GetUserItemsInteractor","from resource_management.storages.user_storage_implementation import \\","    UserStorageImplementation","from resource_management.storages.item_storage_implementation import \\","    ItemStorageImplementation","from resource_management.presenters.presenter_implementation import \\","    PresenterImplementation","from .validator_class import ValidatorClass","","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","","    user = kwargs['user']","    user_id = user.id","    offset = kwargs['request_query_params']['offset']","    limit = kwargs['request_query_params']['limit']","","    user_storage = UserStorageImplementation()","    item_storage = ItemStorageImplementation()","    presenter = PresenterImplementation()","","    interactor = GetUserItemsInteractor(","        user_storage=user_storage,","        item_storage=item_storage,","        presenter=presenter","    )","","    items_dict = interactor.get_user_items(","        user_id=user_id,","        offset=offset,","        limit=limit","    )","","    data = json.dumps(items_dict)","    response = HttpResponse(data, status=200)","    return response",""]}],[{"start":{"row":4,"column":45},"end":{"row":4,"column":46},"action":"remove","lines":["_"],"id":3},{"start":{"row":4,"column":44},"end":{"row":4,"column":45},"action":"remove","lines":["r"]},{"start":{"row":4,"column":43},"end":{"row":4,"column":44},"action":"remove","lines":["e"]},{"start":{"row":4,"column":42},"end":{"row":4,"column":43},"action":"remove","lines":["s"]},{"start":{"row":4,"column":41},"end":{"row":4,"column":42},"action":"remove","lines":["u"]},{"start":{"row":4,"column":40},"end":{"row":4,"column":41},"action":"remove","lines":["_"]}],[{"start":{"row":4,"column":40},"end":{"row":4,"column":41},"action":"insert","lines":["_"],"id":4}],[{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"remove","lines":["r"],"id":5},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"remove","lines":["e"]},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"remove","lines":["s"]},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"remove","lines":["U"]}],[{"start":{"row":27,"column":17},"end":{"row":27,"column":39},"action":"remove","lines":["GetUserItemsInteractor"],"id":6},{"start":{"row":27,"column":17},"end":{"row":27,"column":35},"action":"insert","lines":["GetItemsInteractor"]}],[{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"remove","lines":["r"],"id":7},{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"remove","lines":["e"]},{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"remove","lines":["s"]},{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"remove","lines":["u"]}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"insert","lines":["a"],"id":8},{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"insert","lines":["d"]}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":9},"action":"remove","lines":["ad_id"],"id":9},{"start":{"row":19,"column":4},"end":{"row":19,"column":12},"action":"insert","lines":["admin_id"]}],[{"start":{"row":19,"column":22},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]},{"start":{"row":20,"column":4},"end":{"row":20,"column":5},"action":"insert","lines":["u"]},{"start":{"row":20,"column":5},"end":{"row":20,"column":6},"action":"insert","lines":["s"]},{"start":{"row":20,"column":6},"end":{"row":20,"column":7},"action":"insert","lines":["e"]},{"start":{"row":20,"column":7},"end":{"row":20,"column":8},"action":"insert","lines":["r"]},{"start":{"row":20,"column":8},"end":{"row":20,"column":9},"action":"insert","lines":["_"]}],[{"start":{"row":20,"column":9},"end":{"row":20,"column":10},"action":"insert","lines":["i"],"id":11},{"start":{"row":20,"column":10},"end":{"row":20,"column":11},"action":"insert","lines":["d"]}],[{"start":{"row":20,"column":11},"end":{"row":20,"column":12},"action":"insert","lines":[" "],"id":12},{"start":{"row":20,"column":12},"end":{"row":20,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":20,"column":13},"end":{"row":20,"column":14},"action":"insert","lines":[" "],"id":13},{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"insert","lines":["k"]},{"start":{"row":20,"column":15},"end":{"row":20,"column":16},"action":"insert","lines":["w"]}],[{"start":{"row":20,"column":14},"end":{"row":20,"column":16},"action":"remove","lines":["kw"],"id":14},{"start":{"row":20,"column":14},"end":{"row":20,"column":20},"action":"insert","lines":["kwargs"]}],[{"start":{"row":20,"column":20},"end":{"row":20,"column":22},"action":"insert","lines":["[]"],"id":15}],[{"start":{"row":20,"column":21},"end":{"row":20,"column":23},"action":"insert","lines":["''"],"id":16}],[{"start":{"row":20,"column":22},"end":{"row":20,"column":23},"action":"insert","lines":["u"],"id":17},{"start":{"row":20,"column":23},"end":{"row":20,"column":24},"action":"insert","lines":["s"]},{"start":{"row":20,"column":24},"end":{"row":20,"column":25},"action":"insert","lines":["e"]},{"start":{"row":20,"column":25},"end":{"row":20,"column":26},"action":"insert","lines":["r"]}],[{"start":{"row":20,"column":22},"end":{"row":20,"column":26},"action":"remove","lines":["user"],"id":18},{"start":{"row":20,"column":22},"end":{"row":20,"column":26},"action":"insert","lines":["user"]}],[{"start":{"row":20,"column":26},"end":{"row":20,"column":27},"action":"insert","lines":["_"],"id":19},{"start":{"row":20,"column":27},"end":{"row":20,"column":28},"action":"insert","lines":["i"]},{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"insert","lines":["d"]}],[{"start":{"row":34,"column":43},"end":{"row":35,"column":0},"action":"insert","lines":["",""],"id":20},{"start":{"row":35,"column":0},"end":{"row":35,"column":8},"action":"insert","lines":["        "]},{"start":{"row":35,"column":8},"end":{"row":35,"column":9},"action":"insert","lines":["a"]},{"start":{"row":35,"column":9},"end":{"row":35,"column":10},"action":"insert","lines":["d"]},{"start":{"row":35,"column":10},"end":{"row":35,"column":11},"action":"insert","lines":["m"]},{"start":{"row":35,"column":11},"end":{"row":35,"column":12},"action":"insert","lines":["i"]},{"start":{"row":35,"column":12},"end":{"row":35,"column":13},"action":"insert","lines":["n"]}],[{"start":{"row":35,"column":8},"end":{"row":35,"column":13},"action":"remove","lines":["admin"],"id":21},{"start":{"row":35,"column":8},"end":{"row":35,"column":16},"action":"insert","lines":["admin_id"]}],[{"start":{"row":35,"column":16},"end":{"row":35,"column":17},"action":"insert","lines":["="],"id":22},{"start":{"row":35,"column":17},"end":{"row":35,"column":18},"action":"insert","lines":["a"]},{"start":{"row":35,"column":18},"end":{"row":35,"column":19},"action":"insert","lines":["d"]}],[{"start":{"row":35,"column":17},"end":{"row":35,"column":19},"action":"remove","lines":["ad"],"id":23},{"start":{"row":35,"column":17},"end":{"row":35,"column":25},"action":"insert","lines":["admin_id"]}],[{"start":{"row":35,"column":25},"end":{"row":35,"column":26},"action":"insert","lines":[","],"id":24}],[{"start":{"row":34,"column":36},"end":{"row":34,"column":37},"action":"remove","lines":["_"],"id":25},{"start":{"row":34,"column":35},"end":{"row":34,"column":36},"action":"remove","lines":["r"]},{"start":{"row":34,"column":34},"end":{"row":34,"column":35},"action":"remove","lines":["e"]},{"start":{"row":34,"column":33},"end":{"row":34,"column":34},"action":"remove","lines":["s"]},{"start":{"row":34,"column":32},"end":{"row":34,"column":33},"action":"remove","lines":["u"]}]]},"ace":{"folds":[],"scrolltop":19,"scrollleft":0,"selection":{"start":{"row":28,"column":36},"end":{"row":28,"column":36},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":0,"state":"start","mode":"ace/mode/python"}},"timestamp":1591372142721,"hash":"63b79887e10e61d434985ac777550aac3ef718c6"}