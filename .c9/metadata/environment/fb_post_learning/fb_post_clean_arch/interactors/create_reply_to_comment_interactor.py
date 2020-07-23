{"filter":false,"title":"create_reply_to_comment_interactor.py","tooltip":"/fb_post_learning/fb_post_clean_arch/interactors/create_reply_to_comment_interactor.py","undoManager":{"mark":32,"position":32,"stack":[[{"start":{"row":0,"column":0},"end":{"row":29,"column":0},"action":"insert","lines":["from fb_post_clean_arch.exceptions.custom_exceptions import InvalidPostId","from fb_post_clean_arch.interactors.presenters.presenter_interface import \\","    PresenterInterface","from fb_post_clean_arch.interactors.storages.storage_interface import \\","    StorageInterface","","","class CreateCommentInteractor:","","    def __init__(self, storage: StorageInterface):","        self.storage = storage","","    def create_comment(self, post_id: int,","                       comment_text: str,","                       user_id: int,","                       presenter: PresenterInterface):","        try:","            self.storage.validate_post_id(post_id=post_id)","        except InvalidPostId:","            presenter.raise_exception_for_invalid_post()","            return","","        comment_id = self.storage.create_comment(","            post_id=post_id,","            comment_text=comment_text,","            user_id=user_id)","","        return presenter.get_create_comment_response(","            comment_id=comment_id)",""],"id":1}],[{"start":{"row":0,"column":70},"end":{"row":0,"column":71},"action":"remove","lines":["t"],"id":2},{"start":{"row":0,"column":69},"end":{"row":0,"column":70},"action":"remove","lines":["s"]},{"start":{"row":0,"column":68},"end":{"row":0,"column":69},"action":"remove","lines":["o"]},{"start":{"row":0,"column":67},"end":{"row":0,"column":68},"action":"remove","lines":["P"]}],[{"start":{"row":0,"column":67},"end":{"row":0,"column":68},"action":"insert","lines":["C"],"id":3}],[{"start":{"row":0,"column":60},"end":{"row":0,"column":70},"action":"remove","lines":["InvalidCId"],"id":4},{"start":{"row":0,"column":60},"end":{"row":0,"column":76},"action":"insert","lines":["InvalidCommentId"]}],[{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["R"],"id":5},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":["e"]},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":["p"]},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":["l"]},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["y"]}],[{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":["T"],"id":6},{"start":{"row":7,"column":18},"end":{"row":7,"column":19},"action":"insert","lines":["o"]}],[{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"insert","lines":["r"],"id":7},{"start":{"row":12,"column":16},"end":{"row":12,"column":17},"action":"insert","lines":["e"]},{"start":{"row":12,"column":17},"end":{"row":12,"column":18},"action":"insert","lines":["p"]},{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"insert","lines":["l"]},{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"insert","lines":["y"]},{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"insert","lines":["_"]}],[{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"insert","lines":["t"],"id":8},{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"insert","lines":["o"]},{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"insert","lines":["_"]}],[{"start":{"row":12,"column":41},"end":{"row":12,"column":42},"action":"remove","lines":["t"],"id":9},{"start":{"row":12,"column":40},"end":{"row":12,"column":41},"action":"remove","lines":["s"]},{"start":{"row":12,"column":39},"end":{"row":12,"column":40},"action":"remove","lines":["o"]},{"start":{"row":12,"column":38},"end":{"row":12,"column":39},"action":"remove","lines":["p"]}],[{"start":{"row":12,"column":38},"end":{"row":12,"column":39},"action":"insert","lines":["c"],"id":10},{"start":{"row":12,"column":39},"end":{"row":12,"column":40},"action":"insert","lines":["o"]},{"start":{"row":12,"column":40},"end":{"row":12,"column":41},"action":"insert","lines":["m"]},{"start":{"row":12,"column":41},"end":{"row":12,"column":42},"action":"insert","lines":["m"]},{"start":{"row":12,"column":42},"end":{"row":12,"column":43},"action":"insert","lines":["e"]},{"start":{"row":12,"column":43},"end":{"row":12,"column":44},"action":"insert","lines":["n"]},{"start":{"row":12,"column":44},"end":{"row":12,"column":45},"action":"insert","lines":["t"]}],[{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"remove","lines":["t"],"id":11},{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"remove","lines":["n"]},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"remove","lines":["e"]},{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"remove","lines":["m"]},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"remove","lines":["m"]},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"remove","lines":["o"]},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"remove","lines":["c"]}],[{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["r"],"id":12},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"insert","lines":["e"]},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"insert","lines":["p"]},{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"insert","lines":["l"]},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"insert","lines":["y"]}],[{"start":{"row":17,"column":37},"end":{"row":17,"column":38},"action":"remove","lines":["t"],"id":13},{"start":{"row":17,"column":36},"end":{"row":17,"column":37},"action":"remove","lines":["s"]},{"start":{"row":17,"column":35},"end":{"row":17,"column":36},"action":"remove","lines":["o"]},{"start":{"row":17,"column":34},"end":{"row":17,"column":35},"action":"remove","lines":["p"]}],[{"start":{"row":17,"column":34},"end":{"row":17,"column":35},"action":"insert","lines":["c"],"id":14},{"start":{"row":17,"column":35},"end":{"row":17,"column":36},"action":"insert","lines":["o"]},{"start":{"row":17,"column":36},"end":{"row":17,"column":37},"action":"insert","lines":["m"]}],[{"start":{"row":17,"column":37},"end":{"row":17,"column":38},"action":"insert","lines":["m"],"id":15},{"start":{"row":17,"column":38},"end":{"row":17,"column":39},"action":"insert","lines":["e"]},{"start":{"row":17,"column":39},"end":{"row":17,"column":40},"action":"insert","lines":["n"]},{"start":{"row":17,"column":40},"end":{"row":17,"column":41},"action":"insert","lines":["t"]}],[{"start":{"row":18,"column":25},"end":{"row":18,"column":26},"action":"remove","lines":["t"],"id":16},{"start":{"row":18,"column":24},"end":{"row":18,"column":25},"action":"remove","lines":["s"]},{"start":{"row":18,"column":23},"end":{"row":18,"column":24},"action":"remove","lines":["o"]},{"start":{"row":18,"column":22},"end":{"row":18,"column":23},"action":"remove","lines":["P"]}],[{"start":{"row":18,"column":22},"end":{"row":18,"column":23},"action":"insert","lines":["C"],"id":17},{"start":{"row":18,"column":23},"end":{"row":18,"column":24},"action":"insert","lines":["o"]},{"start":{"row":18,"column":24},"end":{"row":18,"column":25},"action":"insert","lines":["m"]},{"start":{"row":18,"column":25},"end":{"row":18,"column":26},"action":"insert","lines":["m"]},{"start":{"row":18,"column":26},"end":{"row":18,"column":27},"action":"insert","lines":["e"]},{"start":{"row":18,"column":27},"end":{"row":18,"column":28},"action":"insert","lines":["n"]},{"start":{"row":18,"column":28},"end":{"row":18,"column":29},"action":"insert","lines":["t"]}],[{"start":{"row":17,"column":48},"end":{"row":17,"column":49},"action":"remove","lines":["t"],"id":18},{"start":{"row":17,"column":47},"end":{"row":17,"column":48},"action":"remove","lines":["s"]},{"start":{"row":17,"column":46},"end":{"row":17,"column":47},"action":"remove","lines":["o"]},{"start":{"row":17,"column":45},"end":{"row":17,"column":46},"action":"remove","lines":["p"]}],[{"start":{"row":17,"column":45},"end":{"row":17,"column":46},"action":"insert","lines":["c"],"id":19},{"start":{"row":17,"column":46},"end":{"row":17,"column":47},"action":"insert","lines":["o"]},{"start":{"row":17,"column":47},"end":{"row":17,"column":48},"action":"insert","lines":["m"]},{"start":{"row":17,"column":48},"end":{"row":17,"column":49},"action":"insert","lines":["m"]},{"start":{"row":17,"column":49},"end":{"row":17,"column":50},"action":"insert","lines":["e"]},{"start":{"row":17,"column":50},"end":{"row":17,"column":51},"action":"insert","lines":["n"]},{"start":{"row":17,"column":51},"end":{"row":17,"column":52},"action":"insert","lines":["t"]}],[{"start":{"row":17,"column":59},"end":{"row":17,"column":60},"action":"remove","lines":["t"],"id":20},{"start":{"row":17,"column":58},"end":{"row":17,"column":59},"action":"remove","lines":["s"]},{"start":{"row":17,"column":57},"end":{"row":17,"column":58},"action":"remove","lines":["o"]},{"start":{"row":17,"column":56},"end":{"row":17,"column":57},"action":"remove","lines":["p"]}],[{"start":{"row":17,"column":56},"end":{"row":17,"column":57},"action":"insert","lines":["c"],"id":21},{"start":{"row":17,"column":57},"end":{"row":17,"column":58},"action":"insert","lines":["o"]},{"start":{"row":17,"column":58},"end":{"row":17,"column":59},"action":"insert","lines":["m"]},{"start":{"row":17,"column":59},"end":{"row":17,"column":60},"action":"insert","lines":["m"]},{"start":{"row":17,"column":60},"end":{"row":17,"column":61},"action":"insert","lines":["e"]},{"start":{"row":17,"column":61},"end":{"row":17,"column":62},"action":"insert","lines":["n"]},{"start":{"row":17,"column":62},"end":{"row":17,"column":63},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":53},"end":{"row":19,"column":54},"action":"remove","lines":["t"],"id":22},{"start":{"row":19,"column":52},"end":{"row":19,"column":53},"action":"remove","lines":["s"]},{"start":{"row":19,"column":51},"end":{"row":19,"column":52},"action":"remove","lines":["o"]},{"start":{"row":19,"column":50},"end":{"row":19,"column":51},"action":"remove","lines":["p"]}],[{"start":{"row":19,"column":50},"end":{"row":19,"column":51},"action":"insert","lines":["c"],"id":23},{"start":{"row":19,"column":51},"end":{"row":19,"column":52},"action":"insert","lines":["o"]},{"start":{"row":19,"column":52},"end":{"row":19,"column":53},"action":"insert","lines":["m"]},{"start":{"row":19,"column":53},"end":{"row":19,"column":54},"action":"insert","lines":["m"]},{"start":{"row":19,"column":54},"end":{"row":19,"column":55},"action":"insert","lines":["e"]},{"start":{"row":19,"column":55},"end":{"row":19,"column":56},"action":"insert","lines":["n"]},{"start":{"row":19,"column":56},"end":{"row":19,"column":57},"action":"insert","lines":["t"]}],[{"start":{"row":22,"column":34},"end":{"row":22,"column":48},"action":"remove","lines":["create_comment"],"id":24},{"start":{"row":22,"column":34},"end":{"row":22,"column":57},"action":"insert","lines":["create_reply_to_comment"]}],[{"start":{"row":23,"column":15},"end":{"row":23,"column":16},"action":"remove","lines":["t"],"id":25},{"start":{"row":23,"column":14},"end":{"row":23,"column":15},"action":"remove","lines":["s"]},{"start":{"row":23,"column":13},"end":{"row":23,"column":14},"action":"remove","lines":["o"]},{"start":{"row":23,"column":12},"end":{"row":23,"column":13},"action":"remove","lines":["p"]}],[{"start":{"row":23,"column":12},"end":{"row":23,"column":13},"action":"insert","lines":["c"],"id":26},{"start":{"row":23,"column":13},"end":{"row":23,"column":14},"action":"insert","lines":["o"]},{"start":{"row":23,"column":14},"end":{"row":23,"column":15},"action":"insert","lines":["m"]},{"start":{"row":23,"column":15},"end":{"row":23,"column":16},"action":"insert","lines":["m"]},{"start":{"row":23,"column":16},"end":{"row":23,"column":17},"action":"insert","lines":["e"]},{"start":{"row":23,"column":17},"end":{"row":23,"column":18},"action":"insert","lines":["n"]},{"start":{"row":23,"column":18},"end":{"row":23,"column":19},"action":"insert","lines":["t"]}],[{"start":{"row":23,"column":26},"end":{"row":23,"column":27},"action":"remove","lines":["t"],"id":27},{"start":{"row":23,"column":25},"end":{"row":23,"column":26},"action":"remove","lines":["s"]},{"start":{"row":23,"column":24},"end":{"row":23,"column":25},"action":"remove","lines":["o"]},{"start":{"row":23,"column":23},"end":{"row":23,"column":24},"action":"remove","lines":["p"]}],[{"start":{"row":23,"column":23},"end":{"row":23,"column":24},"action":"insert","lines":["c"],"id":28},{"start":{"row":23,"column":24},"end":{"row":23,"column":25},"action":"insert","lines":["o"]},{"start":{"row":23,"column":25},"end":{"row":23,"column":26},"action":"insert","lines":["m"]},{"start":{"row":23,"column":26},"end":{"row":23,"column":27},"action":"insert","lines":["m"]},{"start":{"row":23,"column":27},"end":{"row":23,"column":28},"action":"insert","lines":["e"]},{"start":{"row":23,"column":28},"end":{"row":23,"column":29},"action":"insert","lines":["n"]},{"start":{"row":23,"column":29},"end":{"row":23,"column":30},"action":"insert","lines":["t"]}],[{"start":{"row":24,"column":18},"end":{"row":24,"column":19},"action":"remove","lines":["t"],"id":29},{"start":{"row":24,"column":17},"end":{"row":24,"column":18},"action":"remove","lines":["n"]},{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"remove","lines":["e"]},{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"remove","lines":["m"]},{"start":{"row":24,"column":14},"end":{"row":24,"column":15},"action":"remove","lines":["m"]},{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"remove","lines":["o"]},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"remove","lines":["c"]}],[{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"insert","lines":["r"],"id":30},{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"insert","lines":["e"]},{"start":{"row":24,"column":14},"end":{"row":24,"column":15},"action":"insert","lines":["p"]},{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"insert","lines":["l"]},{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"insert","lines":["y"]}],[{"start":{"row":24,"column":29},"end":{"row":24,"column":30},"action":"remove","lines":["t"],"id":31},{"start":{"row":24,"column":28},"end":{"row":24,"column":29},"action":"remove","lines":["n"]},{"start":{"row":24,"column":27},"end":{"row":24,"column":28},"action":"remove","lines":["e"]},{"start":{"row":24,"column":26},"end":{"row":24,"column":27},"action":"remove","lines":["m"]},{"start":{"row":24,"column":25},"end":{"row":24,"column":26},"action":"remove","lines":["m"]},{"start":{"row":24,"column":24},"end":{"row":24,"column":25},"action":"remove","lines":["o"]},{"start":{"row":24,"column":23},"end":{"row":24,"column":24},"action":"remove","lines":["c"]}],[{"start":{"row":24,"column":23},"end":{"row":24,"column":24},"action":"insert","lines":["r"],"id":32},{"start":{"row":24,"column":24},"end":{"row":24,"column":25},"action":"insert","lines":["e"]},{"start":{"row":24,"column":25},"end":{"row":24,"column":26},"action":"insert","lines":["p"]},{"start":{"row":24,"column":26},"end":{"row":24,"column":27},"action":"insert","lines":["l"]},{"start":{"row":24,"column":27},"end":{"row":24,"column":28},"action":"insert","lines":["y"]}],[{"start":{"row":27,"column":25},"end":{"row":27,"column":52},"action":"remove","lines":["get_create_comment_response"],"id":33},{"start":{"row":27,"column":25},"end":{"row":27,"column":61},"action":"insert","lines":["get_create_reply_to_comment_response"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":27,"column":61},"end":{"row":27,"column":61},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1589608128020,"hash":"7758f4b4ace70f92b8c86a389552d2207b05a89a"}