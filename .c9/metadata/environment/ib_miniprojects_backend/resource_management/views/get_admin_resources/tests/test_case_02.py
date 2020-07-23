{"filter":false,"title":"test_case_02.py","tooltip":"/ib_miniprojects_backend/resource_management/views/get_admin_resources/tests/test_case_02.py","undoManager":{"mark":43,"position":43,"stack":[[{"start":{"row":0,"column":0},"end":{"row":36,"column":0},"action":"insert","lines":["\"\"\"","# TODO: Update test case description","\"\"\"","","from django_swagger_utils.utils.test import CustomAPITestCase","from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX","","REQUEST_BODY = \"\"\"","{}","\"\"\"","","TEST_CASE = {","    \"request\": {","        \"path_params\": {},","        \"query_params\": {\"offset\": 0, \"limit\": 1},","        \"header_params\": {},","        \"securities\": {\"oauth\": {\"tokenUrl\": \"http://auth.ibtspl.com/oauth2/\", \"flow\": \"password\", \"scopes\": [\"read\", \"write\"], \"type\": \"oauth2\"}},","        \"body\": REQUEST_BODY,","    },","}","","","class TestCase01GetAdminResourcesAPITestCase(CustomAPITestCase):","    app_name = APP_NAME","    operation_name = OPERATION_NAME","    request_method = REQUEST_METHOD","    url_suffix = URL_SUFFIX","    test_case_dict = TEST_CASE","","    def setupUser(self, username, password):","        super(TestCase01GetAdminResourcesAPITestCase, self).setupUser(","            username=username, password=password","        )","","    def test_case(self):","        self.default_test_case()",""],"id":1}],[{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"remove","lines":["1"],"id":2}],[{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"insert","lines":["2"],"id":3}],[{"start":{"row":30,"column":23},"end":{"row":30,"column":24},"action":"remove","lines":["1"],"id":4}],[{"start":{"row":30,"column":23},"end":{"row":30,"column":24},"action":"insert","lines":["2"],"id":5}],[{"start":{"row":30,"column":57},"end":{"row":30,"column":58},"action":"remove","lines":["f"],"id":6},{"start":{"row":30,"column":56},"end":{"row":30,"column":57},"action":"remove","lines":["l"]},{"start":{"row":30,"column":55},"end":{"row":30,"column":56},"action":"remove","lines":["e"]},{"start":{"row":30,"column":54},"end":{"row":30,"column":55},"action":"remove","lines":["s"]},{"start":{"row":30,"column":53},"end":{"row":30,"column":54},"action":"remove","lines":[" "]},{"start":{"row":30,"column":52},"end":{"row":30,"column":53},"action":"remove","lines":[","]},{"start":{"row":30,"column":51},"end":{"row":30,"column":52},"action":"remove","lines":["e"]},{"start":{"row":30,"column":50},"end":{"row":30,"column":51},"action":"remove","lines":["s"]},{"start":{"row":30,"column":49},"end":{"row":30,"column":50},"action":"remove","lines":["a"]},{"start":{"row":30,"column":48},"end":{"row":30,"column":49},"action":"remove","lines":["C"]},{"start":{"row":30,"column":47},"end":{"row":30,"column":48},"action":"remove","lines":["t"]},{"start":{"row":30,"column":46},"end":{"row":30,"column":47},"action":"remove","lines":["s"]},{"start":{"row":30,"column":45},"end":{"row":30,"column":46},"action":"remove","lines":["e"]},{"start":{"row":30,"column":44},"end":{"row":30,"column":45},"action":"remove","lines":["T"]},{"start":{"row":30,"column":43},"end":{"row":30,"column":44},"action":"remove","lines":["I"]},{"start":{"row":30,"column":42},"end":{"row":30,"column":43},"action":"remove","lines":["P"]},{"start":{"row":30,"column":41},"end":{"row":30,"column":42},"action":"remove","lines":["A"]},{"start":{"row":30,"column":40},"end":{"row":30,"column":41},"action":"remove","lines":["s"]},{"start":{"row":30,"column":39},"end":{"row":30,"column":40},"action":"remove","lines":["e"]},{"start":{"row":30,"column":38},"end":{"row":30,"column":39},"action":"remove","lines":["c"]},{"start":{"row":30,"column":37},"end":{"row":30,"column":38},"action":"remove","lines":["r"]},{"start":{"row":30,"column":36},"end":{"row":30,"column":37},"action":"remove","lines":["u"]},{"start":{"row":30,"column":35},"end":{"row":30,"column":36},"action":"remove","lines":["o"]},{"start":{"row":30,"column":34},"end":{"row":30,"column":35},"action":"remove","lines":["s"]},{"start":{"row":30,"column":33},"end":{"row":30,"column":34},"action":"remove","lines":["e"]},{"start":{"row":30,"column":32},"end":{"row":30,"column":33},"action":"remove","lines":["R"]},{"start":{"row":30,"column":31},"end":{"row":30,"column":32},"action":"remove","lines":["n"]},{"start":{"row":30,"column":30},"end":{"row":30,"column":31},"action":"remove","lines":["i"]},{"start":{"row":30,"column":29},"end":{"row":30,"column":30},"action":"remove","lines":["m"]},{"start":{"row":30,"column":28},"end":{"row":30,"column":29},"action":"remove","lines":["d"]},{"start":{"row":30,"column":27},"end":{"row":30,"column":28},"action":"remove","lines":["A"]},{"start":{"row":30,"column":26},"end":{"row":30,"column":27},"action":"remove","lines":["t"]},{"start":{"row":30,"column":25},"end":{"row":30,"column":26},"action":"remove","lines":["e"]},{"start":{"row":30,"column":24},"end":{"row":30,"column":25},"action":"remove","lines":["G"]},{"start":{"row":30,"column":23},"end":{"row":30,"column":24},"action":"remove","lines":["2"]},{"start":{"row":30,"column":22},"end":{"row":30,"column":23},"action":"remove","lines":["0"]},{"start":{"row":30,"column":21},"end":{"row":30,"column":22},"action":"remove","lines":["e"]},{"start":{"row":30,"column":20},"end":{"row":30,"column":21},"action":"remove","lines":["s"]},{"start":{"row":30,"column":19},"end":{"row":30,"column":20},"action":"remove","lines":["a"]},{"start":{"row":30,"column":18},"end":{"row":30,"column":19},"action":"remove","lines":["C"]},{"start":{"row":30,"column":17},"end":{"row":30,"column":18},"action":"remove","lines":["t"]}],[{"start":{"row":30,"column":16},"end":{"row":30,"column":17},"action":"remove","lines":["s"],"id":7},{"start":{"row":30,"column":15},"end":{"row":30,"column":16},"action":"remove","lines":["e"]},{"start":{"row":30,"column":14},"end":{"row":30,"column":15},"action":"remove","lines":["T"]}],[{"start":{"row":4,"column":61},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"insert","lines":["f"]},{"start":{"row":5,"column":1},"end":{"row":5,"column":2},"action":"insert","lines":["r"]},{"start":{"row":5,"column":2},"end":{"row":5,"column":3},"action":"insert","lines":["o"]},{"start":{"row":5,"column":3},"end":{"row":5,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":[" "],"id":9},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["r"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["e"]},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["s"]},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["o"]},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["u"]}],[{"start":{"row":5,"column":5},"end":{"row":5,"column":10},"action":"remove","lines":["resou"],"id":10},{"start":{"row":5,"column":5},"end":{"row":5,"column":24},"action":"insert","lines":["resource_management"]}],[{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"insert","lines":["."],"id":11}],[{"start":{"row":5,"column":25},"end":{"row":5,"column":26},"action":"insert","lines":["c"],"id":12},{"start":{"row":5,"column":26},"end":{"row":5,"column":27},"action":"insert","lines":["u"]},{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"insert","lines":["s"]}],[{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"insert","lines":["t"],"id":13},{"start":{"row":5,"column":29},"end":{"row":5,"column":30},"action":"insert","lines":["o"]},{"start":{"row":5,"column":30},"end":{"row":5,"column":31},"action":"insert","lines":["m"]}],[{"start":{"row":5,"column":31},"end":{"row":5,"column":32},"action":"insert","lines":["_"],"id":14},{"start":{"row":5,"column":32},"end":{"row":5,"column":33},"action":"insert","lines":["t"]},{"start":{"row":5,"column":33},"end":{"row":5,"column":34},"action":"insert","lines":["e"]},{"start":{"row":5,"column":34},"end":{"row":5,"column":35},"action":"insert","lines":["s"]},{"start":{"row":5,"column":35},"end":{"row":5,"column":36},"action":"insert","lines":["t"]},{"start":{"row":5,"column":36},"end":{"row":5,"column":37},"action":"insert","lines":["_"]},{"start":{"row":5,"column":37},"end":{"row":5,"column":38},"action":"insert","lines":["u"]},{"start":{"row":5,"column":38},"end":{"row":5,"column":39},"action":"insert","lines":["t"]},{"start":{"row":5,"column":39},"end":{"row":5,"column":40},"action":"insert","lines":["i"]}],[{"start":{"row":5,"column":40},"end":{"row":5,"column":41},"action":"insert","lines":["l"],"id":15},{"start":{"row":5,"column":41},"end":{"row":5,"column":42},"action":"insert","lines":["s"]},{"start":{"row":5,"column":42},"end":{"row":5,"column":43},"action":"insert","lines":["."]},{"start":{"row":5,"column":43},"end":{"row":5,"column":44},"action":"insert","lines":["c"]}],[{"start":{"row":5,"column":43},"end":{"row":5,"column":44},"action":"remove","lines":["c"],"id":16},{"start":{"row":5,"column":43},"end":{"row":5,"column":60},"action":"insert","lines":["custom_test_utils"]}],[{"start":{"row":5,"column":60},"end":{"row":5,"column":61},"action":"insert","lines":[" "],"id":17},{"start":{"row":5,"column":61},"end":{"row":5,"column":62},"action":"insert","lines":["i"]},{"start":{"row":5,"column":62},"end":{"row":5,"column":63},"action":"insert","lines":["m"]},{"start":{"row":5,"column":63},"end":{"row":5,"column":64},"action":"insert","lines":["p"]},{"start":{"row":5,"column":64},"end":{"row":5,"column":65},"action":"insert","lines":["o"]},{"start":{"row":5,"column":65},"end":{"row":5,"column":66},"action":"insert","lines":["r"]},{"start":{"row":5,"column":66},"end":{"row":5,"column":67},"action":"insert","lines":["t"]}],[{"start":{"row":5,"column":67},"end":{"row":5,"column":68},"action":"insert","lines":[" "],"id":18},{"start":{"row":5,"column":68},"end":{"row":5,"column":69},"action":"insert","lines":["\\"]}],[{"start":{"row":5,"column":69},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":19}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "],"id":20}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["C"],"id":21}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"remove","lines":["C"],"id":22},{"start":{"row":6,"column":4},"end":{"row":6,"column":19},"action":"insert","lines":["CustomTestUtils"]}],[{"start":{"row":24,"column":45},"end":{"row":24,"column":62},"action":"remove","lines":["CustomAPITestCase"],"id":23},{"start":{"row":24,"column":45},"end":{"row":24,"column":60},"action":"insert","lines":["CustomTestUtils"]}],[{"start":{"row":34,"column":9},"end":{"row":35,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":35,"column":0},"end":{"row":35,"column":8},"action":"insert","lines":["        "]},{"start":{"row":35,"column":8},"end":{"row":35,"column":9},"action":"insert","lines":["s"]},{"start":{"row":35,"column":9},"end":{"row":35,"column":10},"action":"insert","lines":["e"]},{"start":{"row":35,"column":10},"end":{"row":35,"column":11},"action":"insert","lines":["l"]},{"start":{"row":35,"column":11},"end":{"row":35,"column":12},"action":"insert","lines":["f"]}],[{"start":{"row":35,"column":12},"end":{"row":35,"column":13},"action":"insert","lines":["."],"id":25},{"start":{"row":35,"column":13},"end":{"row":35,"column":14},"action":"insert","lines":["f"]},{"start":{"row":35,"column":14},"end":{"row":35,"column":15},"action":"insert","lines":["o"]},{"start":{"row":35,"column":15},"end":{"row":35,"column":16},"action":"insert","lines":["o"]},{"start":{"row":35,"column":16},"end":{"row":35,"column":17},"action":"insert","lines":["_"]},{"start":{"row":35,"column":17},"end":{"row":35,"column":18},"action":"insert","lines":["u"]}],[{"start":{"row":35,"column":18},"end":{"row":35,"column":19},"action":"insert","lines":["s"],"id":26},{"start":{"row":35,"column":19},"end":{"row":35,"column":20},"action":"insert","lines":["e"]},{"start":{"row":35,"column":20},"end":{"row":35,"column":21},"action":"insert","lines":["r"]},{"start":{"row":35,"column":21},"end":{"row":35,"column":22},"action":"insert","lines":["."]},{"start":{"row":35,"column":22},"end":{"row":35,"column":23},"action":"insert","lines":["i"]},{"start":{"row":35,"column":23},"end":{"row":35,"column":24},"action":"insert","lines":["s"]}],[{"start":{"row":35,"column":24},"end":{"row":35,"column":25},"action":"insert","lines":["_"],"id":27},{"start":{"row":35,"column":25},"end":{"row":35,"column":26},"action":"insert","lines":["a"]},{"start":{"row":35,"column":26},"end":{"row":35,"column":27},"action":"insert","lines":["d"]},{"start":{"row":35,"column":27},"end":{"row":35,"column":28},"action":"insert","lines":["m"]},{"start":{"row":35,"column":28},"end":{"row":35,"column":29},"action":"insert","lines":["i"]},{"start":{"row":35,"column":29},"end":{"row":35,"column":30},"action":"insert","lines":["n"]}],[{"start":{"row":35,"column":30},"end":{"row":35,"column":31},"action":"insert","lines":[" "],"id":28},{"start":{"row":35,"column":31},"end":{"row":35,"column":32},"action":"insert","lines":["="]}],[{"start":{"row":35,"column":32},"end":{"row":35,"column":33},"action":"insert","lines":[" "],"id":29},{"start":{"row":35,"column":33},"end":{"row":35,"column":34},"action":"insert","lines":["T"]},{"start":{"row":35,"column":34},"end":{"row":35,"column":35},"action":"insert","lines":["r"]},{"start":{"row":35,"column":35},"end":{"row":35,"column":36},"action":"insert","lines":["u"]},{"start":{"row":35,"column":36},"end":{"row":35,"column":37},"action":"insert","lines":["e"]}],[{"start":{"row":35,"column":37},"end":{"row":36,"column":0},"action":"insert","lines":["",""],"id":30},{"start":{"row":36,"column":0},"end":{"row":36,"column":8},"action":"insert","lines":["        "]},{"start":{"row":36,"column":8},"end":{"row":36,"column":9},"action":"insert","lines":["s"]},{"start":{"row":36,"column":9},"end":{"row":36,"column":10},"action":"insert","lines":["e"]},{"start":{"row":36,"column":10},"end":{"row":36,"column":11},"action":"insert","lines":["l"]},{"start":{"row":36,"column":11},"end":{"row":36,"column":12},"action":"insert","lines":["f"]},{"start":{"row":36,"column":12},"end":{"row":36,"column":13},"action":"insert","lines":["."]},{"start":{"row":36,"column":13},"end":{"row":36,"column":14},"action":"insert","lines":["f"]},{"start":{"row":36,"column":14},"end":{"row":36,"column":15},"action":"insert","lines":["o"]},{"start":{"row":36,"column":15},"end":{"row":36,"column":16},"action":"insert","lines":["o"]}],[{"start":{"row":36,"column":13},"end":{"row":36,"column":16},"action":"remove","lines":["foo"],"id":31},{"start":{"row":36,"column":13},"end":{"row":36,"column":21},"action":"insert","lines":["foo_user"]}],[{"start":{"row":36,"column":21},"end":{"row":36,"column":22},"action":"insert","lines":["."],"id":32},{"start":{"row":36,"column":22},"end":{"row":36,"column":23},"action":"insert","lines":["s"]},{"start":{"row":36,"column":23},"end":{"row":36,"column":24},"action":"insert","lines":["a"]},{"start":{"row":36,"column":24},"end":{"row":36,"column":25},"action":"insert","lines":["v"]},{"start":{"row":36,"column":25},"end":{"row":36,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":36,"column":26},"end":{"row":36,"column":28},"action":"insert","lines":["()"],"id":33}],[{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":34},{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"insert","lines":["",""]},{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":19,"column":47},"end":{"row":19,"column":48},"action":"remove","lines":["1"],"id":35}],[{"start":{"row":19,"column":47},"end":{"row":19,"column":48},"action":"insert","lines":["2"],"id":36}],[{"start":{"row":39,"column":28},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":37},{"start":{"row":40,"column":0},"end":{"row":40,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":40,"column":4},"end":{"row":40,"column":8},"action":"remove","lines":["    "],"id":38},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":40,"column":0},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":39}],[{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "],"id":40}],[{"start":{"row":41,"column":4},"end":{"row":41,"column":8},"action":"insert","lines":["    "],"id":41}],[{"start":{"row":41,"column":8},"end":{"row":41,"column":9},"action":"insert","lines":["s"],"id":42},{"start":{"row":41,"column":9},"end":{"row":41,"column":10},"action":"insert","lines":["e"]},{"start":{"row":41,"column":10},"end":{"row":41,"column":11},"action":"insert","lines":["l"]},{"start":{"row":41,"column":11},"end":{"row":41,"column":12},"action":"insert","lines":["f"]},{"start":{"row":41,"column":12},"end":{"row":41,"column":13},"action":"insert","lines":["."]}],[{"start":{"row":41,"column":13},"end":{"row":41,"column":31},"action":"insert","lines":["resources_of_admin"],"id":43}],[{"start":{"row":41,"column":31},"end":{"row":41,"column":33},"action":"insert","lines":["()"],"id":44}]]},"ace":{"folds":[],"scrolltop":428.5,"scrollleft":0,"selection":{"start":{"row":41,"column":32},"end":{"row":41,"column":32},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1593230630828,"hash":"d8b452a24bc34edcb52deed09adc87c2b843d47a"}