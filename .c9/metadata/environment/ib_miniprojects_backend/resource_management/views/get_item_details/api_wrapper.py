{"filter":false,"title":"api_wrapper.py","tooltip":"/ib_miniprojects_backend/resource_management/views/get_item_details/api_wrapper.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":4,"column":37},"end":{"row":4,"column":44},"action":"remove","lines":["get_ite"],"id":32},{"start":{"row":4,"column":37},"end":{"row":4,"column":64},"action":"insert","lines":["get_item_details_interactor"]}],[{"start":{"row":4,"column":64},"end":{"row":4,"column":65},"action":"insert","lines":[" "],"id":33},{"start":{"row":4,"column":65},"end":{"row":4,"column":66},"action":"insert","lines":["i"]},{"start":{"row":4,"column":66},"end":{"row":4,"column":67},"action":"insert","lines":["m"]},{"start":{"row":4,"column":67},"end":{"row":4,"column":68},"action":"insert","lines":["p"]},{"start":{"row":4,"column":68},"end":{"row":4,"column":69},"action":"insert","lines":["o"]},{"start":{"row":4,"column":69},"end":{"row":4,"column":70},"action":"insert","lines":["r"]},{"start":{"row":4,"column":70},"end":{"row":4,"column":71},"action":"insert","lines":["t"]}],[{"start":{"row":4,"column":71},"end":{"row":4,"column":72},"action":"insert","lines":[" "],"id":34},{"start":{"row":4,"column":72},"end":{"row":4,"column":73},"action":"insert","lines":["\\"]}],[{"start":{"row":4,"column":73},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":35}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"insert","lines":["    "],"id":36}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["g"],"id":37}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"remove","lines":["g"],"id":38}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["G"],"id":39}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"remove","lines":["G"],"id":40},{"start":{"row":5,"column":4},"end":{"row":5,"column":28},"action":"insert","lines":["GetItemDetailsInteractor"]}],[{"start":{"row":5,"column":28},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":41},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"remove","lines":["    "],"id":42}],[{"start":{"row":6,"column":0},"end":{"row":9,"column":27},"action":"insert","lines":["from resource_management.storages.storage_implementation import \\","    StorageImplementation","from resource_management.presenters.presenter_implementation import \\","    PresenterImplementation"],"id":43}],[{"start":{"row":10,"column":43},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":44}],[{"start":{"row":11,"column":0},"end":{"row":13,"column":63},"action":"insert","lines":["from resource_management.constants.exception_message import INVALID_RESOURCE","from resource_management.exceptions.exceptions import InvalidResource","from django_swagger_utils.drf_server.exceptions import NotFound"],"id":45}],[{"start":{"row":11,"column":75},"end":{"row":11,"column":76},"action":"remove","lines":["E"],"id":46},{"start":{"row":11,"column":74},"end":{"row":11,"column":75},"action":"remove","lines":["C"]},{"start":{"row":11,"column":73},"end":{"row":11,"column":74},"action":"remove","lines":["R"]},{"start":{"row":11,"column":72},"end":{"row":11,"column":73},"action":"remove","lines":["U"]},{"start":{"row":11,"column":71},"end":{"row":11,"column":72},"action":"remove","lines":["O"]},{"start":{"row":11,"column":70},"end":{"row":11,"column":71},"action":"remove","lines":["S"]},{"start":{"row":11,"column":69},"end":{"row":11,"column":70},"action":"remove","lines":["E"]},{"start":{"row":11,"column":68},"end":{"row":11,"column":69},"action":"remove","lines":["R"]}],[{"start":{"row":11,"column":68},"end":{"row":11,"column":69},"action":"insert","lines":["I"],"id":47},{"start":{"row":11,"column":69},"end":{"row":11,"column":70},"action":"insert","lines":["T"]},{"start":{"row":11,"column":70},"end":{"row":11,"column":71},"action":"insert","lines":["E"]},{"start":{"row":11,"column":71},"end":{"row":11,"column":72},"action":"insert","lines":["M"]}],[{"start":{"row":12,"column":68},"end":{"row":12,"column":69},"action":"remove","lines":["e"],"id":48},{"start":{"row":12,"column":67},"end":{"row":12,"column":68},"action":"remove","lines":["c"]},{"start":{"row":12,"column":66},"end":{"row":12,"column":67},"action":"remove","lines":["r"]},{"start":{"row":12,"column":65},"end":{"row":12,"column":66},"action":"remove","lines":["u"]},{"start":{"row":12,"column":64},"end":{"row":12,"column":65},"action":"remove","lines":["o"]},{"start":{"row":12,"column":63},"end":{"row":12,"column":64},"action":"remove","lines":["s"]},{"start":{"row":12,"column":62},"end":{"row":12,"column":63},"action":"remove","lines":["e"]},{"start":{"row":12,"column":61},"end":{"row":12,"column":62},"action":"remove","lines":["R"]}],[{"start":{"row":12,"column":61},"end":{"row":12,"column":62},"action":"insert","lines":["I"],"id":49}],[{"start":{"row":12,"column":54},"end":{"row":12,"column":62},"action":"remove","lines":["InvalidI"],"id":50},{"start":{"row":12,"column":54},"end":{"row":12,"column":65},"action":"insert","lines":["InvalidItem"]}],[{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"remove","lines":["s"],"id":51},{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"remove","lines":["s"]},{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"remove","lines":["a"]},{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"remove","lines":["p"]}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"insert","lines":["i"],"id":52},{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"insert","lines":["t"]},{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"insert","lines":["e"]},{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"insert","lines":["m"]},{"start":{"row":19,"column":8},"end":{"row":19,"column":9},"action":"insert","lines":["_"]},{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"insert","lines":["i"]},{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"insert","lines":["d"]}],[{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"insert","lines":[" "],"id":53},{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":19,"column":13},"end":{"row":19,"column":14},"action":"insert","lines":[" "],"id":54}],[{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"insert","lines":["k"],"id":55}],[{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"remove","lines":["k"],"id":56},{"start":{"row":19,"column":14},"end":{"row":19,"column":20},"action":"insert","lines":["kwargs"]}],[{"start":{"row":19,"column":20},"end":{"row":19,"column":22},"action":"insert","lines":["[]"],"id":57}],[{"start":{"row":19,"column":21},"end":{"row":19,"column":23},"action":"insert","lines":["''"],"id":58}],[{"start":{"row":19,"column":22},"end":{"row":19,"column":23},"action":"insert","lines":["i"],"id":59},{"start":{"row":19,"column":23},"end":{"row":19,"column":24},"action":"insert","lines":["t"]},{"start":{"row":19,"column":24},"end":{"row":19,"column":25},"action":"insert","lines":["e"]},{"start":{"row":19,"column":25},"end":{"row":19,"column":26},"action":"insert","lines":["m"]}],[{"start":{"row":19,"column":22},"end":{"row":19,"column":26},"action":"remove","lines":["item"],"id":60},{"start":{"row":19,"column":22},"end":{"row":19,"column":29},"action":"insert","lines":["item_id"]}],[{"start":{"row":19,"column":31},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":61},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "],"id":62}],[{"start":{"row":20,"column":0},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":63}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "],"id":64}],[{"start":{"row":21,"column":4},"end":{"row":38,"column":19},"action":"insert","lines":["user_storage = StorageImplementation()","    presenter = PresenterImplementation()","","    interactor = GetResourceDetailsInteractor(","        user_storage=user_storage,","        presenter=presenter","    )","","    try:","        resource_dict = interactor.get_resource_details(","            resource_id=resource_id","        )","    except InvalidResource:","        raise NotFound(*INVALID_RESOURCE)","","    data = json.dumps(resource_dict)","    response = HttpResponse(data, status=200)","    return response"],"id":65}],[{"start":{"row":24,"column":17},"end":{"row":24,"column":45},"action":"remove","lines":["GetResourceDetailsInteractor"],"id":66},{"start":{"row":24,"column":17},"end":{"row":24,"column":41},"action":"insert","lines":["GetItemDetailsInteractor"]}],[{"start":{"row":30,"column":46},"end":{"row":30,"column":47},"action":"remove","lines":["e"],"id":67},{"start":{"row":30,"column":45},"end":{"row":30,"column":46},"action":"remove","lines":["c"]},{"start":{"row":30,"column":44},"end":{"row":30,"column":45},"action":"remove","lines":["r"]},{"start":{"row":30,"column":43},"end":{"row":30,"column":44},"action":"remove","lines":["u"]},{"start":{"row":30,"column":42},"end":{"row":30,"column":43},"action":"remove","lines":["o"]},{"start":{"row":30,"column":41},"end":{"row":30,"column":42},"action":"remove","lines":["s"]},{"start":{"row":30,"column":40},"end":{"row":30,"column":41},"action":"remove","lines":["e"]},{"start":{"row":30,"column":39},"end":{"row":30,"column":40},"action":"remove","lines":["r"]}],[{"start":{"row":30,"column":39},"end":{"row":30,"column":40},"action":"insert","lines":["i"],"id":68},{"start":{"row":30,"column":40},"end":{"row":30,"column":41},"action":"insert","lines":["t"]},{"start":{"row":30,"column":41},"end":{"row":30,"column":42},"action":"insert","lines":["e"]},{"start":{"row":30,"column":42},"end":{"row":30,"column":43},"action":"insert","lines":["m"]}],[{"start":{"row":31,"column":12},"end":{"row":31,"column":23},"action":"remove","lines":["resource_id"],"id":69},{"start":{"row":31,"column":12},"end":{"row":31,"column":19},"action":"insert","lines":["item_id"]}],[{"start":{"row":31,"column":20},"end":{"row":31,"column":31},"action":"remove","lines":["resource_id"],"id":70},{"start":{"row":31,"column":20},"end":{"row":31,"column":27},"action":"insert","lines":["item_id"]}],[{"start":{"row":34,"column":24},"end":{"row":34,"column":40},"action":"remove","lines":["INVALID_RESOURCE"],"id":71},{"start":{"row":34,"column":24},"end":{"row":34,"column":36},"action":"insert","lines":["INVALID_ITEM"]}],[{"start":{"row":33,"column":11},"end":{"row":33,"column":26},"action":"remove","lines":["InvalidResource"],"id":72},{"start":{"row":33,"column":11},"end":{"row":33,"column":22},"action":"insert","lines":["InvalidItem"]}],[{"start":{"row":30,"column":15},"end":{"row":30,"column":16},"action":"remove","lines":["e"],"id":73},{"start":{"row":30,"column":14},"end":{"row":30,"column":15},"action":"remove","lines":["c"]},{"start":{"row":30,"column":13},"end":{"row":30,"column":14},"action":"remove","lines":["r"]},{"start":{"row":30,"column":12},"end":{"row":30,"column":13},"action":"remove","lines":["u"]},{"start":{"row":30,"column":11},"end":{"row":30,"column":12},"action":"remove","lines":["o"]},{"start":{"row":30,"column":10},"end":{"row":30,"column":11},"action":"remove","lines":["s"]},{"start":{"row":30,"column":9},"end":{"row":30,"column":10},"action":"remove","lines":["e"]},{"start":{"row":30,"column":8},"end":{"row":30,"column":9},"action":"remove","lines":["r"]}],[{"start":{"row":30,"column":8},"end":{"row":30,"column":9},"action":"insert","lines":["i"],"id":74},{"start":{"row":30,"column":9},"end":{"row":30,"column":10},"action":"insert","lines":["t"]},{"start":{"row":30,"column":10},"end":{"row":30,"column":11},"action":"insert","lines":["e"]},{"start":{"row":30,"column":11},"end":{"row":30,"column":12},"action":"insert","lines":["m"]}],[{"start":{"row":36,"column":22},"end":{"row":36,"column":35},"action":"remove","lines":["resource_dict"],"id":75},{"start":{"row":36,"column":22},"end":{"row":36,"column":31},"action":"insert","lines":["item_dict"]}],[{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["u"],"id":76},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["s"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["e"]},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":["r"]},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"insert","lines":["_"]}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["U"],"id":77},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["s"]},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["e"]},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["r"]}],[{"start":{"row":7,"column":29},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":78},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "],"id":79}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"insert","lines":["f"],"id":80},{"start":{"row":8,"column":1},"end":{"row":8,"column":2},"action":"insert","lines":["r"]},{"start":{"row":8,"column":2},"end":{"row":8,"column":3},"action":"insert","lines":["o"]},{"start":{"row":8,"column":3},"end":{"row":8,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":[" "],"id":81},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["r"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["e"]},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":["s"]}],[{"start":{"row":8,"column":5},"end":{"row":8,"column":8},"action":"remove","lines":["res"],"id":82},{"start":{"row":8,"column":5},"end":{"row":8,"column":24},"action":"insert","lines":["resource_management"]}],[{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"insert","lines":["."],"id":83},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":["s"]},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"insert","lines":["t"]},{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"insert","lines":["o"]}],[{"start":{"row":8,"column":25},"end":{"row":8,"column":28},"action":"remove","lines":["sto"],"id":84},{"start":{"row":8,"column":25},"end":{"row":8,"column":33},"action":"insert","lines":["storages"]}],[{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"insert","lines":["."],"id":85},{"start":{"row":8,"column":34},"end":{"row":8,"column":35},"action":"insert","lines":["i"]},{"start":{"row":8,"column":35},"end":{"row":8,"column":36},"action":"insert","lines":["t"]},{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":["e"]},{"start":{"row":8,"column":37},"end":{"row":8,"column":38},"action":"insert","lines":["m"]},{"start":{"row":8,"column":38},"end":{"row":8,"column":39},"action":"insert","lines":["_"]},{"start":{"row":8,"column":39},"end":{"row":8,"column":40},"action":"insert","lines":["s"]},{"start":{"row":8,"column":40},"end":{"row":8,"column":41},"action":"insert","lines":["t"]}],[{"start":{"row":8,"column":41},"end":{"row":8,"column":42},"action":"insert","lines":["o"],"id":86}],[{"start":{"row":8,"column":34},"end":{"row":8,"column":42},"action":"remove","lines":["item_sto"],"id":87},{"start":{"row":8,"column":34},"end":{"row":8,"column":61},"action":"insert","lines":["item_storage_implementation"]}],[{"start":{"row":8,"column":61},"end":{"row":8,"column":62},"action":"insert","lines":[" "],"id":88},{"start":{"row":8,"column":62},"end":{"row":8,"column":63},"action":"insert","lines":["i"]},{"start":{"row":8,"column":63},"end":{"row":8,"column":64},"action":"insert","lines":["m"]},{"start":{"row":8,"column":64},"end":{"row":8,"column":65},"action":"insert","lines":["p"]},{"start":{"row":8,"column":65},"end":{"row":8,"column":66},"action":"insert","lines":["o"]},{"start":{"row":8,"column":66},"end":{"row":8,"column":67},"action":"insert","lines":["r"]},{"start":{"row":8,"column":67},"end":{"row":8,"column":68},"action":"insert","lines":["t"]}],[{"start":{"row":8,"column":68},"end":{"row":8,"column":69},"action":"insert","lines":[" "],"id":89},{"start":{"row":8,"column":69},"end":{"row":8,"column":70},"action":"insert","lines":["\\"]}],[{"start":{"row":8,"column":70},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":90}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "],"id":91}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"insert","lines":["I"],"id":92},{"start":{"row":9,"column":5},"end":{"row":9,"column":6},"action":"insert","lines":["t"]},{"start":{"row":9,"column":6},"end":{"row":9,"column":7},"action":"insert","lines":["e"]},{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"insert","lines":["m"]}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":8},"action":"remove","lines":["Item"],"id":93},{"start":{"row":9,"column":4},"end":{"row":9,"column":29},"action":"insert","lines":["ItemStorageImplementation"]}],[{"start":{"row":20,"column":0},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":94}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "],"id":95}],[{"start":{"row":21,"column":4},"end":{"row":21,"column":5},"action":"insert","lines":["u"],"id":96},{"start":{"row":21,"column":5},"end":{"row":21,"column":6},"action":"insert","lines":["s"]},{"start":{"row":21,"column":6},"end":{"row":21,"column":7},"action":"insert","lines":["e"]},{"start":{"row":21,"column":7},"end":{"row":21,"column":8},"action":"insert","lines":["r"]}],[{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"insert","lines":[" "],"id":97},{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"insert","lines":["="]}],[{"start":{"row":21,"column":10},"end":{"row":21,"column":11},"action":"insert","lines":[" "],"id":98},{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"insert","lines":["k"]},{"start":{"row":21,"column":12},"end":{"row":21,"column":13},"action":"insert","lines":["w"]}],[{"start":{"row":21,"column":11},"end":{"row":21,"column":13},"action":"remove","lines":["kw"],"id":99},{"start":{"row":21,"column":11},"end":{"row":21,"column":17},"action":"insert","lines":["kwargs"]}],[{"start":{"row":21,"column":17},"end":{"row":21,"column":19},"action":"insert","lines":["[]"],"id":100}],[{"start":{"row":21,"column":18},"end":{"row":21,"column":20},"action":"insert","lines":["''"],"id":101}],[{"start":{"row":21,"column":19},"end":{"row":21,"column":20},"action":"insert","lines":["s"],"id":102}],[{"start":{"row":21,"column":19},"end":{"row":21,"column":20},"action":"remove","lines":["s"],"id":103}],[{"start":{"row":21,"column":19},"end":{"row":21,"column":20},"action":"insert","lines":["u"],"id":104},{"start":{"row":21,"column":20},"end":{"row":21,"column":21},"action":"insert","lines":["s"]},{"start":{"row":21,"column":21},"end":{"row":21,"column":22},"action":"insert","lines":["e"]},{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"insert","lines":["r"]}],[{"start":{"row":21,"column":25},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":105},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]},{"start":{"row":22,"column":4},"end":{"row":22,"column":5},"action":"insert","lines":["u"]},{"start":{"row":22,"column":5},"end":{"row":22,"column":6},"action":"insert","lines":["s"]},{"start":{"row":22,"column":6},"end":{"row":22,"column":7},"action":"insert","lines":["e"]},{"start":{"row":22,"column":7},"end":{"row":22,"column":8},"action":"insert","lines":["r"]},{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"insert","lines":["_"]}],[{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"insert","lines":["i"],"id":106},{"start":{"row":22,"column":10},"end":{"row":22,"column":11},"action":"insert","lines":["d"]}],[{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"insert","lines":[" "],"id":107},{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"insert","lines":[" "],"id":108},{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"insert","lines":["u"]},{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"insert","lines":["s"]},{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["e"]},{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"insert","lines":["r"]},{"start":{"row":22,"column":18},"end":{"row":22,"column":19},"action":"insert","lines":["."]},{"start":{"row":22,"column":19},"end":{"row":22,"column":20},"action":"insert","lines":["i"]}],[{"start":{"row":22,"column":20},"end":{"row":22,"column":21},"action":"insert","lines":["d"],"id":109}],[{"start":{"row":25,"column":19},"end":{"row":25,"column":20},"action":"insert","lines":["U"],"id":110},{"start":{"row":25,"column":20},"end":{"row":25,"column":21},"action":"insert","lines":["s"]},{"start":{"row":25,"column":21},"end":{"row":25,"column":22},"action":"insert","lines":["e"]},{"start":{"row":25,"column":22},"end":{"row":25,"column":23},"action":"insert","lines":["r"]}],[{"start":{"row":25,"column":46},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":111},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":26,"column":4},"end":{"row":26,"column":5},"action":"insert","lines":["i"],"id":112},{"start":{"row":26,"column":5},"end":{"row":26,"column":6},"action":"insert","lines":["t"]},{"start":{"row":26,"column":6},"end":{"row":26,"column":7},"action":"insert","lines":["e"]},{"start":{"row":26,"column":7},"end":{"row":26,"column":8},"action":"insert","lines":["m"]},{"start":{"row":26,"column":8},"end":{"row":26,"column":9},"action":"insert","lines":["_"]},{"start":{"row":26,"column":9},"end":{"row":26,"column":10},"action":"insert","lines":["s"]},{"start":{"row":26,"column":10},"end":{"row":26,"column":11},"action":"insert","lines":["t"]},{"start":{"row":26,"column":11},"end":{"row":26,"column":12},"action":"insert","lines":["o"]}],[{"start":{"row":26,"column":4},"end":{"row":26,"column":12},"action":"remove","lines":["item_sto"],"id":113},{"start":{"row":26,"column":4},"end":{"row":26,"column":16},"action":"insert","lines":["item_storage"]}],[{"start":{"row":26,"column":16},"end":{"row":26,"column":17},"action":"insert","lines":[" "],"id":114},{"start":{"row":26,"column":17},"end":{"row":26,"column":18},"action":"insert","lines":["="]}],[{"start":{"row":26,"column":18},"end":{"row":26,"column":19},"action":"insert","lines":[" "],"id":115},{"start":{"row":26,"column":19},"end":{"row":26,"column":20},"action":"insert","lines":["I"]}],[{"start":{"row":26,"column":20},"end":{"row":26,"column":21},"action":"insert","lines":["t"],"id":116},{"start":{"row":26,"column":21},"end":{"row":26,"column":22},"action":"insert","lines":["e"]},{"start":{"row":26,"column":22},"end":{"row":26,"column":23},"action":"insert","lines":["m"]}],[{"start":{"row":26,"column":19},"end":{"row":26,"column":23},"action":"remove","lines":["Item"],"id":117},{"start":{"row":26,"column":19},"end":{"row":26,"column":44},"action":"insert","lines":["ItemStorageImplementation"]}],[{"start":{"row":26,"column":44},"end":{"row":26,"column":46},"action":"insert","lines":["()"],"id":118}],[{"start":{"row":30,"column":34},"end":{"row":31,"column":0},"action":"insert","lines":["",""],"id":119},{"start":{"row":31,"column":0},"end":{"row":31,"column":8},"action":"insert","lines":["        "]},{"start":{"row":31,"column":8},"end":{"row":31,"column":9},"action":"insert","lines":["i"]},{"start":{"row":31,"column":9},"end":{"row":31,"column":10},"action":"insert","lines":["t"]},{"start":{"row":31,"column":10},"end":{"row":31,"column":11},"action":"insert","lines":["e"]}],[{"start":{"row":31,"column":11},"end":{"row":31,"column":12},"action":"insert","lines":["m"],"id":120}],[{"start":{"row":31,"column":8},"end":{"row":31,"column":12},"action":"remove","lines":["item"],"id":121},{"start":{"row":31,"column":8},"end":{"row":31,"column":20},"action":"insert","lines":["item_storage"]}],[{"start":{"row":31,"column":20},"end":{"row":31,"column":21},"action":"insert","lines":["="],"id":122},{"start":{"row":31,"column":21},"end":{"row":31,"column":22},"action":"insert","lines":["i"]},{"start":{"row":31,"column":22},"end":{"row":31,"column":23},"action":"insert","lines":["t"]},{"start":{"row":31,"column":23},"end":{"row":31,"column":24},"action":"insert","lines":["e"]},{"start":{"row":31,"column":24},"end":{"row":31,"column":25},"action":"insert","lines":["m"]}],[{"start":{"row":31,"column":21},"end":{"row":31,"column":25},"action":"remove","lines":["item"],"id":123},{"start":{"row":31,"column":21},"end":{"row":31,"column":33},"action":"insert","lines":["item_storage"]}],[{"start":{"row":31,"column":33},"end":{"row":31,"column":34},"action":"insert","lines":[","],"id":124}],[{"start":{"row":36,"column":48},"end":{"row":37,"column":0},"action":"insert","lines":["",""],"id":125},{"start":{"row":37,"column":0},"end":{"row":37,"column":12},"action":"insert","lines":["            "]},{"start":{"row":37,"column":12},"end":{"row":37,"column":13},"action":"insert","lines":["u"]},{"start":{"row":37,"column":13},"end":{"row":37,"column":14},"action":"insert","lines":["s"]},{"start":{"row":37,"column":14},"end":{"row":37,"column":15},"action":"insert","lines":["e"]},{"start":{"row":37,"column":15},"end":{"row":37,"column":16},"action":"insert","lines":["r"]}],[{"start":{"row":37,"column":16},"end":{"row":37,"column":17},"action":"insert","lines":["_"],"id":126},{"start":{"row":37,"column":17},"end":{"row":37,"column":18},"action":"insert","lines":["i"]},{"start":{"row":37,"column":18},"end":{"row":37,"column":19},"action":"insert","lines":["d"]},{"start":{"row":37,"column":19},"end":{"row":37,"column":20},"action":"insert","lines":["="]},{"start":{"row":37,"column":20},"end":{"row":37,"column":21},"action":"insert","lines":["u"]}],[{"start":{"row":37,"column":21},"end":{"row":37,"column":22},"action":"insert","lines":["s"],"id":127},{"start":{"row":37,"column":22},"end":{"row":37,"column":23},"action":"insert","lines":["e"]},{"start":{"row":37,"column":23},"end":{"row":37,"column":24},"action":"insert","lines":["r"]},{"start":{"row":37,"column":24},"end":{"row":37,"column":25},"action":"insert","lines":["_"]},{"start":{"row":37,"column":25},"end":{"row":37,"column":26},"action":"insert","lines":["i"]},{"start":{"row":37,"column":26},"end":{"row":37,"column":27},"action":"insert","lines":["d"]}],[{"start":{"row":37,"column":27},"end":{"row":37,"column":28},"action":"insert","lines":[","],"id":128}],[{"start":{"row":13,"column":0},"end":{"row":16,"column":0},"action":"remove","lines":["from resource_management.constants.exception_message import INVALID_ITEM","from resource_management.exceptions.exceptions import InvalidItem","from django_swagger_utils.drf_server.exceptions import NotFound",""],"id":129},{"start":{"row":12,"column":43},"end":{"row":13,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":31,"column":7},"end":{"row":31,"column":8},"action":"remove","lines":[":"],"id":130},{"start":{"row":31,"column":6},"end":{"row":31,"column":7},"action":"remove","lines":["y"]},{"start":{"row":31,"column":5},"end":{"row":31,"column":6},"action":"remove","lines":["r"]},{"start":{"row":31,"column":4},"end":{"row":31,"column":5},"action":"remove","lines":["t"]},{"start":{"row":31,"column":0},"end":{"row":31,"column":4},"action":"remove","lines":["    "]},{"start":{"row":30,"column":0},"end":{"row":31,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":31,"column":0},"end":{"row":31,"column":4},"action":"remove","lines":["    "],"id":131},{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"remove","lines":["    "]},{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"remove","lines":["    "]},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":35,"column":4},"end":{"row":36,"column":37},"action":"remove","lines":["except InvalidItem:","        raise NotFound(*INVALID_ITEM)"],"id":132},{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"remove","lines":["    "]},{"start":{"row":34,"column":5},"end":{"row":35,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":236,"scrollleft":0,"selection":{"start":{"row":34,"column":5},"end":{"row":34,"column":5},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":15,"state":"start","mode":"ace/mode/python"}},"timestamp":1591258309552,"hash":"cad3e452fd3aa4b5e161e421d8ecf728b308f306"}