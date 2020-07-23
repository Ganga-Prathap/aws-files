{"filter":false,"title":"react_to_comment_interactor.py","tooltip":"/fb_post_learning/fb_post_clean_arch/interactors/react_to_comment_interactor.py","undoManager":{"mark":45,"position":45,"stack":[[{"start":{"row":0,"column":0},"end":{"row":41,"column":0},"action":"insert","lines":["from fb_post_clean_arch.constants.enums import ReactionType","from fb_post_clean_arch.exceptions.custom_exceptions import InvalidPostId, \\","    ReactionDoesNotExist","from fb_post_clean_arch.interactors.presenters.presenter_interface import \\","    PresenterInterface","from fb_post_clean_arch.interactors.storages.storage_interface import \\","    StorageInterface","","","class ReactToPostInteractor:","","    def __init__(self, storage: StorageInterface):","        self.storage = storage","","    def react_to_post_wrapper(self, user_id: int,","                              post_id: int,","                              reaction_type: ReactionType,","                              presenter: PresenterInterface):","        try:","            self.storage.validate_post_id(post_id=post_id)","        except InvalidPostId:","            presenter.raise_exception_for_invalid_post()","","        try:","            old_reaction_type = self.storage. \\","                validate_post_reaction_if_exists_get_reaction_type(","                    user_id=user_id,","                    post_id=post_id","                )","        except ReactionDoesNotExist:","            self.storage.create_post_reaction(","                post_id=post_id, user_id=user_id, reaction_type=reaction_type)","            return","","        is_undo_reaction = old_reaction_type == reaction_type","","        if is_undo_reaction:","            self.storage.undo_post_reaction(post_id=post_id, user_id=user_id)","        else:","            self.storage.update_post_reaction(user_id=user_id, post_id=post_id,","                                              reaction_type=reaction_type)",""],"id":1}],[{"start":{"row":1,"column":70},"end":{"row":1,"column":71},"action":"remove","lines":["t"],"id":2},{"start":{"row":1,"column":69},"end":{"row":1,"column":70},"action":"remove","lines":["s"]},{"start":{"row":1,"column":68},"end":{"row":1,"column":69},"action":"remove","lines":["o"]},{"start":{"row":1,"column":67},"end":{"row":1,"column":68},"action":"remove","lines":["P"]}],[{"start":{"row":1,"column":67},"end":{"row":1,"column":68},"action":"insert","lines":["C"],"id":3}],[{"start":{"row":1,"column":60},"end":{"row":1,"column":70},"action":"remove","lines":["InvalidCId"],"id":4},{"start":{"row":1,"column":60},"end":{"row":1,"column":76},"action":"insert","lines":["InvalidCommentId"]}],[{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"remove","lines":["t"],"id":5},{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"remove","lines":["s"]},{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"remove","lines":["o"]},{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"remove","lines":["P"]}],[{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"insert","lines":["C"],"id":6},{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"insert","lines":["o"]},{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"insert","lines":["m"]},{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"insert","lines":["m"]},{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":["e"]},{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"insert","lines":["n"]},{"start":{"row":9,"column":19},"end":{"row":9,"column":20},"action":"insert","lines":["t"]}],[{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"remove","lines":["t"],"id":7},{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"remove","lines":["s"]},{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"remove","lines":["o"]},{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"remove","lines":["p"]}],[{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"insert","lines":["c"],"id":8},{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"insert","lines":["o"]},{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"insert","lines":["m"]},{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"insert","lines":["m"]},{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"insert","lines":["e"]},{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"insert","lines":["n"]},{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":33},"end":{"row":15,"column":34},"action":"remove","lines":["t"],"id":9},{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"remove","lines":["s"]},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"remove","lines":["o"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"remove","lines":["p"]}],[{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"insert","lines":["c"],"id":10},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"insert","lines":["o"]},{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"insert","lines":["m"]},{"start":{"row":15,"column":33},"end":{"row":15,"column":34},"action":"insert","lines":["m"]},{"start":{"row":15,"column":34},"end":{"row":15,"column":35},"action":"insert","lines":["e"]},{"start":{"row":15,"column":35},"end":{"row":15,"column":36},"action":"insert","lines":["n"]},{"start":{"row":15,"column":36},"end":{"row":15,"column":37},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":37},"end":{"row":19,"column":38},"action":"remove","lines":["t"],"id":11},{"start":{"row":19,"column":36},"end":{"row":19,"column":37},"action":"remove","lines":["s"]},{"start":{"row":19,"column":35},"end":{"row":19,"column":36},"action":"remove","lines":["o"]},{"start":{"row":19,"column":34},"end":{"row":19,"column":35},"action":"remove","lines":["p"]}],[{"start":{"row":19,"column":34},"end":{"row":19,"column":35},"action":"insert","lines":["c"],"id":12},{"start":{"row":19,"column":35},"end":{"row":19,"column":36},"action":"insert","lines":["o"]},{"start":{"row":19,"column":36},"end":{"row":19,"column":37},"action":"insert","lines":["m"]},{"start":{"row":19,"column":37},"end":{"row":19,"column":38},"action":"insert","lines":["m"]},{"start":{"row":19,"column":38},"end":{"row":19,"column":39},"action":"insert","lines":["e"]},{"start":{"row":19,"column":39},"end":{"row":19,"column":40},"action":"insert","lines":["n"]},{"start":{"row":19,"column":40},"end":{"row":19,"column":41},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":48},"end":{"row":19,"column":49},"action":"remove","lines":["t"],"id":13},{"start":{"row":19,"column":47},"end":{"row":19,"column":48},"action":"remove","lines":["s"]},{"start":{"row":19,"column":46},"end":{"row":19,"column":47},"action":"remove","lines":["o"]},{"start":{"row":19,"column":45},"end":{"row":19,"column":46},"action":"remove","lines":["p"]}],[{"start":{"row":19,"column":45},"end":{"row":19,"column":46},"action":"insert","lines":["c"],"id":14},{"start":{"row":19,"column":46},"end":{"row":19,"column":47},"action":"insert","lines":["o"]},{"start":{"row":19,"column":47},"end":{"row":19,"column":48},"action":"insert","lines":["m"]},{"start":{"row":19,"column":48},"end":{"row":19,"column":49},"action":"insert","lines":["m"]},{"start":{"row":19,"column":49},"end":{"row":19,"column":50},"action":"insert","lines":["e"]},{"start":{"row":19,"column":50},"end":{"row":19,"column":51},"action":"insert","lines":["n"]},{"start":{"row":19,"column":51},"end":{"row":19,"column":52},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":59},"end":{"row":19,"column":60},"action":"remove","lines":["t"],"id":15},{"start":{"row":19,"column":58},"end":{"row":19,"column":59},"action":"remove","lines":["s"]},{"start":{"row":19,"column":57},"end":{"row":19,"column":58},"action":"remove","lines":["o"]},{"start":{"row":19,"column":56},"end":{"row":19,"column":57},"action":"remove","lines":["p"]}],[{"start":{"row":19,"column":56},"end":{"row":19,"column":57},"action":"insert","lines":["c"],"id":16},{"start":{"row":19,"column":57},"end":{"row":19,"column":58},"action":"insert","lines":["o"]},{"start":{"row":19,"column":58},"end":{"row":19,"column":59},"action":"insert","lines":["m"]},{"start":{"row":19,"column":59},"end":{"row":19,"column":60},"action":"insert","lines":["m"]},{"start":{"row":19,"column":60},"end":{"row":19,"column":61},"action":"insert","lines":["e"]},{"start":{"row":19,"column":61},"end":{"row":19,"column":62},"action":"insert","lines":["n"]},{"start":{"row":19,"column":62},"end":{"row":19,"column":63},"action":"insert","lines":["t"]}],[{"start":{"row":20,"column":25},"end":{"row":20,"column":26},"action":"remove","lines":["t"],"id":17},{"start":{"row":20,"column":24},"end":{"row":20,"column":25},"action":"remove","lines":["s"]},{"start":{"row":20,"column":23},"end":{"row":20,"column":24},"action":"remove","lines":["o"]},{"start":{"row":20,"column":22},"end":{"row":20,"column":23},"action":"remove","lines":["P"]}],[{"start":{"row":20,"column":22},"end":{"row":20,"column":23},"action":"insert","lines":["C"],"id":18},{"start":{"row":20,"column":23},"end":{"row":20,"column":24},"action":"insert","lines":["o"]},{"start":{"row":20,"column":24},"end":{"row":20,"column":25},"action":"insert","lines":["o"]}],[{"start":{"row":20,"column":24},"end":{"row":20,"column":25},"action":"remove","lines":["o"],"id":19}],[{"start":{"row":20,"column":24},"end":{"row":20,"column":25},"action":"insert","lines":["m"],"id":20},{"start":{"row":20,"column":25},"end":{"row":20,"column":26},"action":"insert","lines":["m"]},{"start":{"row":20,"column":26},"end":{"row":20,"column":27},"action":"insert","lines":["e"]},{"start":{"row":20,"column":27},"end":{"row":20,"column":28},"action":"insert","lines":["n"]},{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"insert","lines":["t"]}],[{"start":{"row":21,"column":53},"end":{"row":21,"column":54},"action":"remove","lines":["t"],"id":21},{"start":{"row":21,"column":52},"end":{"row":21,"column":53},"action":"remove","lines":["s"]},{"start":{"row":21,"column":51},"end":{"row":21,"column":52},"action":"remove","lines":["o"]},{"start":{"row":21,"column":50},"end":{"row":21,"column":51},"action":"remove","lines":["p"]}],[{"start":{"row":21,"column":50},"end":{"row":21,"column":51},"action":"insert","lines":["c"],"id":22},{"start":{"row":21,"column":51},"end":{"row":21,"column":52},"action":"insert","lines":["o"]},{"start":{"row":21,"column":52},"end":{"row":21,"column":53},"action":"insert","lines":["m"]},{"start":{"row":21,"column":53},"end":{"row":21,"column":54},"action":"insert","lines":["m"]},{"start":{"row":21,"column":54},"end":{"row":21,"column":55},"action":"insert","lines":["e"]},{"start":{"row":21,"column":55},"end":{"row":21,"column":56},"action":"insert","lines":["n"]},{"start":{"row":21,"column":56},"end":{"row":21,"column":57},"action":"insert","lines":["t"]}],[{"start":{"row":25,"column":28},"end":{"row":25,"column":29},"action":"remove","lines":["t"],"id":23},{"start":{"row":25,"column":27},"end":{"row":25,"column":28},"action":"remove","lines":["s"]},{"start":{"row":25,"column":26},"end":{"row":25,"column":27},"action":"remove","lines":["o"]},{"start":{"row":25,"column":25},"end":{"row":25,"column":26},"action":"remove","lines":["p"]}],[{"start":{"row":25,"column":25},"end":{"row":25,"column":26},"action":"insert","lines":["c"],"id":24},{"start":{"row":25,"column":26},"end":{"row":25,"column":27},"action":"insert","lines":["o"]},{"start":{"row":25,"column":27},"end":{"row":25,"column":28},"action":"insert","lines":["m"]},{"start":{"row":25,"column":28},"end":{"row":25,"column":29},"action":"insert","lines":["m"]},{"start":{"row":25,"column":29},"end":{"row":25,"column":30},"action":"insert","lines":["e"]},{"start":{"row":25,"column":30},"end":{"row":25,"column":31},"action":"insert","lines":["n"]},{"start":{"row":25,"column":31},"end":{"row":25,"column":32},"action":"insert","lines":["t"]}],[{"start":{"row":27,"column":23},"end":{"row":27,"column":24},"action":"remove","lines":["t"],"id":25},{"start":{"row":27,"column":22},"end":{"row":27,"column":23},"action":"remove","lines":["s"]},{"start":{"row":27,"column":21},"end":{"row":27,"column":22},"action":"remove","lines":["o"]},{"start":{"row":27,"column":20},"end":{"row":27,"column":21},"action":"remove","lines":["p"]}],[{"start":{"row":27,"column":20},"end":{"row":27,"column":21},"action":"insert","lines":["c"],"id":26},{"start":{"row":27,"column":21},"end":{"row":27,"column":22},"action":"insert","lines":["o"]},{"start":{"row":27,"column":22},"end":{"row":27,"column":23},"action":"insert","lines":["m"]},{"start":{"row":27,"column":23},"end":{"row":27,"column":24},"action":"insert","lines":["m"]},{"start":{"row":27,"column":24},"end":{"row":27,"column":25},"action":"insert","lines":["e"]},{"start":{"row":27,"column":25},"end":{"row":27,"column":26},"action":"insert","lines":["n"]},{"start":{"row":27,"column":26},"end":{"row":27,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":27,"column":34},"end":{"row":27,"column":35},"action":"remove","lines":["t"],"id":27},{"start":{"row":27,"column":33},"end":{"row":27,"column":34},"action":"remove","lines":["s"]},{"start":{"row":27,"column":32},"end":{"row":27,"column":33},"action":"remove","lines":["o"]},{"start":{"row":27,"column":31},"end":{"row":27,"column":32},"action":"remove","lines":["p"]}],[{"start":{"row":27,"column":31},"end":{"row":27,"column":32},"action":"insert","lines":["c"],"id":28},{"start":{"row":27,"column":32},"end":{"row":27,"column":33},"action":"insert","lines":["o"]},{"start":{"row":27,"column":33},"end":{"row":27,"column":34},"action":"insert","lines":["m"]},{"start":{"row":27,"column":34},"end":{"row":27,"column":35},"action":"insert","lines":["m"]},{"start":{"row":27,"column":35},"end":{"row":27,"column":36},"action":"insert","lines":["e"]},{"start":{"row":27,"column":36},"end":{"row":27,"column":37},"action":"insert","lines":["n"]},{"start":{"row":27,"column":37},"end":{"row":27,"column":38},"action":"insert","lines":["t"]}],[{"start":{"row":30,"column":35},"end":{"row":30,"column":36},"action":"remove","lines":["t"],"id":29},{"start":{"row":30,"column":34},"end":{"row":30,"column":35},"action":"remove","lines":["s"]},{"start":{"row":30,"column":33},"end":{"row":30,"column":34},"action":"remove","lines":["o"]},{"start":{"row":30,"column":32},"end":{"row":30,"column":33},"action":"remove","lines":["p"]}],[{"start":{"row":30,"column":32},"end":{"row":30,"column":33},"action":"insert","lines":["c"],"id":30},{"start":{"row":30,"column":33},"end":{"row":30,"column":34},"action":"insert","lines":["o"]},{"start":{"row":30,"column":34},"end":{"row":30,"column":35},"action":"insert","lines":["m"]},{"start":{"row":30,"column":35},"end":{"row":30,"column":36},"action":"insert","lines":["m"]},{"start":{"row":30,"column":36},"end":{"row":30,"column":37},"action":"insert","lines":["e"]},{"start":{"row":30,"column":37},"end":{"row":30,"column":38},"action":"insert","lines":["n"]},{"start":{"row":30,"column":38},"end":{"row":30,"column":39},"action":"insert","lines":["t"]}],[{"start":{"row":31,"column":19},"end":{"row":31,"column":20},"action":"remove","lines":["t"],"id":31},{"start":{"row":31,"column":18},"end":{"row":31,"column":19},"action":"remove","lines":["s"]},{"start":{"row":31,"column":17},"end":{"row":31,"column":18},"action":"remove","lines":["o"]},{"start":{"row":31,"column":16},"end":{"row":31,"column":17},"action":"remove","lines":["p"]}],[{"start":{"row":31,"column":16},"end":{"row":31,"column":17},"action":"insert","lines":["c"],"id":32},{"start":{"row":31,"column":17},"end":{"row":31,"column":18},"action":"insert","lines":["o"]},{"start":{"row":31,"column":18},"end":{"row":31,"column":19},"action":"insert","lines":["m"]},{"start":{"row":31,"column":19},"end":{"row":31,"column":20},"action":"insert","lines":["m"]},{"start":{"row":31,"column":20},"end":{"row":31,"column":21},"action":"insert","lines":["e"]},{"start":{"row":31,"column":21},"end":{"row":31,"column":22},"action":"insert","lines":["n"]},{"start":{"row":31,"column":22},"end":{"row":31,"column":23},"action":"insert","lines":["t"]}],[{"start":{"row":31,"column":30},"end":{"row":31,"column":31},"action":"remove","lines":["t"],"id":33},{"start":{"row":31,"column":29},"end":{"row":31,"column":30},"action":"remove","lines":["s"]},{"start":{"row":31,"column":28},"end":{"row":31,"column":29},"action":"remove","lines":["o"]},{"start":{"row":31,"column":27},"end":{"row":31,"column":28},"action":"remove","lines":["p"]}],[{"start":{"row":31,"column":27},"end":{"row":31,"column":28},"action":"insert","lines":["c"],"id":34},{"start":{"row":31,"column":28},"end":{"row":31,"column":29},"action":"insert","lines":["o"]},{"start":{"row":31,"column":29},"end":{"row":31,"column":30},"action":"insert","lines":["m"]},{"start":{"row":31,"column":30},"end":{"row":31,"column":31},"action":"insert","lines":["m"]},{"start":{"row":31,"column":31},"end":{"row":31,"column":32},"action":"insert","lines":["e"]},{"start":{"row":31,"column":32},"end":{"row":31,"column":33},"action":"insert","lines":["n"]},{"start":{"row":31,"column":33},"end":{"row":31,"column":34},"action":"insert","lines":["t"]}],[{"start":{"row":37,"column":33},"end":{"row":37,"column":34},"action":"remove","lines":["t"],"id":35},{"start":{"row":37,"column":32},"end":{"row":37,"column":33},"action":"remove","lines":["s"]},{"start":{"row":37,"column":31},"end":{"row":37,"column":32},"action":"remove","lines":["o"]},{"start":{"row":37,"column":30},"end":{"row":37,"column":31},"action":"remove","lines":["p"]}],[{"start":{"row":37,"column":30},"end":{"row":37,"column":31},"action":"insert","lines":["c"],"id":36},{"start":{"row":37,"column":31},"end":{"row":37,"column":32},"action":"insert","lines":["o"]},{"start":{"row":37,"column":32},"end":{"row":37,"column":33},"action":"insert","lines":["m"]},{"start":{"row":37,"column":33},"end":{"row":37,"column":34},"action":"insert","lines":["m"]},{"start":{"row":37,"column":34},"end":{"row":37,"column":35},"action":"insert","lines":["e"]},{"start":{"row":37,"column":35},"end":{"row":37,"column":36},"action":"insert","lines":["n"]},{"start":{"row":37,"column":36},"end":{"row":37,"column":37},"action":"insert","lines":["t"]}],[{"start":{"row":37,"column":50},"end":{"row":37,"column":51},"action":"remove","lines":["t"],"id":37},{"start":{"row":37,"column":49},"end":{"row":37,"column":50},"action":"remove","lines":["s"]},{"start":{"row":37,"column":48},"end":{"row":37,"column":49},"action":"remove","lines":["o"]},{"start":{"row":37,"column":47},"end":{"row":37,"column":48},"action":"remove","lines":["p"]}],[{"start":{"row":37,"column":47},"end":{"row":37,"column":48},"action":"insert","lines":["c"],"id":38},{"start":{"row":37,"column":48},"end":{"row":37,"column":49},"action":"insert","lines":["o"]},{"start":{"row":37,"column":49},"end":{"row":37,"column":50},"action":"insert","lines":["m"]},{"start":{"row":37,"column":50},"end":{"row":37,"column":51},"action":"insert","lines":["m"]},{"start":{"row":37,"column":51},"end":{"row":37,"column":52},"action":"insert","lines":["e"]},{"start":{"row":37,"column":52},"end":{"row":37,"column":53},"action":"insert","lines":["n"]},{"start":{"row":37,"column":53},"end":{"row":37,"column":54},"action":"insert","lines":["t"]}],[{"start":{"row":37,"column":61},"end":{"row":37,"column":62},"action":"remove","lines":["t"],"id":39},{"start":{"row":37,"column":60},"end":{"row":37,"column":61},"action":"remove","lines":["s"]},{"start":{"row":37,"column":59},"end":{"row":37,"column":60},"action":"remove","lines":["o"]},{"start":{"row":37,"column":58},"end":{"row":37,"column":59},"action":"remove","lines":["p"]}],[{"start":{"row":37,"column":58},"end":{"row":37,"column":59},"action":"insert","lines":["c"],"id":40},{"start":{"row":37,"column":59},"end":{"row":37,"column":60},"action":"insert","lines":["o"]},{"start":{"row":37,"column":60},"end":{"row":37,"column":61},"action":"insert","lines":["m"]},{"start":{"row":37,"column":61},"end":{"row":37,"column":62},"action":"insert","lines":["m"]},{"start":{"row":37,"column":62},"end":{"row":37,"column":63},"action":"insert","lines":["e"]},{"start":{"row":37,"column":63},"end":{"row":37,"column":64},"action":"insert","lines":["n"]},{"start":{"row":37,"column":64},"end":{"row":37,"column":65},"action":"insert","lines":["t"]}],[{"start":{"row":39,"column":35},"end":{"row":39,"column":36},"action":"remove","lines":["t"],"id":41},{"start":{"row":39,"column":34},"end":{"row":39,"column":35},"action":"remove","lines":["s"]},{"start":{"row":39,"column":33},"end":{"row":39,"column":34},"action":"remove","lines":["o"]},{"start":{"row":39,"column":32},"end":{"row":39,"column":33},"action":"remove","lines":["p"]}],[{"start":{"row":39,"column":32},"end":{"row":39,"column":33},"action":"insert","lines":["c"],"id":42},{"start":{"row":39,"column":33},"end":{"row":39,"column":34},"action":"insert","lines":["o"]},{"start":{"row":39,"column":34},"end":{"row":39,"column":35},"action":"insert","lines":["m"]},{"start":{"row":39,"column":35},"end":{"row":39,"column":36},"action":"insert","lines":["m"]},{"start":{"row":39,"column":36},"end":{"row":39,"column":37},"action":"insert","lines":["e"]},{"start":{"row":39,"column":37},"end":{"row":39,"column":38},"action":"insert","lines":["n"]},{"start":{"row":39,"column":38},"end":{"row":39,"column":39},"action":"insert","lines":["t"]}],[{"start":{"row":39,"column":69},"end":{"row":39,"column":70},"action":"remove","lines":["t"],"id":43},{"start":{"row":39,"column":68},"end":{"row":39,"column":69},"action":"remove","lines":["s"]},{"start":{"row":39,"column":67},"end":{"row":39,"column":68},"action":"remove","lines":["o"]},{"start":{"row":39,"column":66},"end":{"row":39,"column":67},"action":"remove","lines":["p"]}],[{"start":{"row":39,"column":66},"end":{"row":39,"column":67},"action":"insert","lines":["c"],"id":44},{"start":{"row":39,"column":67},"end":{"row":39,"column":68},"action":"insert","lines":["o"]},{"start":{"row":39,"column":68},"end":{"row":39,"column":69},"action":"insert","lines":["m"]},{"start":{"row":39,"column":69},"end":{"row":39,"column":70},"action":"insert","lines":["m"]},{"start":{"row":39,"column":70},"end":{"row":39,"column":71},"action":"insert","lines":["e"]},{"start":{"row":39,"column":71},"end":{"row":39,"column":72},"action":"insert","lines":["n"]},{"start":{"row":39,"column":72},"end":{"row":39,"column":73},"action":"insert","lines":["t"]}],[{"start":{"row":39,"column":80},"end":{"row":39,"column":81},"action":"remove","lines":["t"],"id":45},{"start":{"row":39,"column":79},"end":{"row":39,"column":80},"action":"remove","lines":["s"]},{"start":{"row":39,"column":78},"end":{"row":39,"column":79},"action":"remove","lines":["o"]},{"start":{"row":39,"column":77},"end":{"row":39,"column":78},"action":"remove","lines":["p"]}],[{"start":{"row":39,"column":77},"end":{"row":39,"column":78},"action":"insert","lines":["c"],"id":46},{"start":{"row":39,"column":78},"end":{"row":39,"column":79},"action":"insert","lines":["o"]},{"start":{"row":39,"column":79},"end":{"row":39,"column":80},"action":"insert","lines":["m"]},{"start":{"row":39,"column":80},"end":{"row":39,"column":81},"action":"insert","lines":["m"]},{"start":{"row":39,"column":81},"end":{"row":39,"column":82},"action":"insert","lines":["e"]},{"start":{"row":39,"column":82},"end":{"row":39,"column":83},"action":"insert","lines":["n"]},{"start":{"row":39,"column":83},"end":{"row":39,"column":84},"action":"insert","lines":["t"]}]]},"ace":{"folds":[],"scrolltop":152,"scrollleft":0,"selection":{"start":{"row":35,"column":0},"end":{"row":35,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":9,"state":"start","mode":"ace/mode/python"}},"timestamp":1589609021419,"hash":"3e0ab51003152c93ff646f83723186e4c2b4af1a"}