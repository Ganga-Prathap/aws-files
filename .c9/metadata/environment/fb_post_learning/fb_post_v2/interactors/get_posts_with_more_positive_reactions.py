{"changed":true,"filter":false,"title":"get_posts_with_more_positive_reactions.py","tooltip":"/fb_post_learning/fb_post_v2/interactors/get_posts_with_more_positive_reactions.py","value":"from fb_post_v2.interactors.storages.storage_interface import \\\n    StorageInterface\nfrom fb_post_v2.interactors.presenters.presenter_interface import \\\n    PresenterInterface\n\n\n\n","undoManager":{"mark":43,"position":46,"stack":[[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["f"],"id":2},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["r"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["o"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":[" "],"id":3},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["f"]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":["b"]}],[{"start":{"row":0,"column":5},"end":{"row":0,"column":7},"action":"remove","lines":["fb"],"id":4},{"start":{"row":0,"column":5},"end":{"row":0,"column":15},"action":"insert","lines":["fb_post_v2"]}],[{"start":{"row":0,"column":15},"end":{"row":0,"column":16},"action":"insert","lines":["."],"id":5},{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"insert","lines":["i"]},{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"insert","lines":["n"]}],[{"start":{"row":0,"column":16},"end":{"row":0,"column":18},"action":"remove","lines":["in"],"id":6},{"start":{"row":0,"column":16},"end":{"row":0,"column":27},"action":"insert","lines":["interactors"]}],[{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"insert","lines":["."],"id":7},{"start":{"row":0,"column":28},"end":{"row":0,"column":29},"action":"insert","lines":["s"]},{"start":{"row":0,"column":29},"end":{"row":0,"column":30},"action":"insert","lines":["t"]},{"start":{"row":0,"column":30},"end":{"row":0,"column":31},"action":"insert","lines":["o"]}],[{"start":{"row":0,"column":28},"end":{"row":0,"column":31},"action":"remove","lines":["sto"],"id":8},{"start":{"row":0,"column":28},"end":{"row":0,"column":36},"action":"insert","lines":["storages"]}],[{"start":{"row":0,"column":36},"end":{"row":0,"column":37},"action":"insert","lines":["."],"id":9},{"start":{"row":0,"column":37},"end":{"row":0,"column":38},"action":"insert","lines":["s"]},{"start":{"row":0,"column":38},"end":{"row":0,"column":39},"action":"insert","lines":["o"]}],[{"start":{"row":0,"column":38},"end":{"row":0,"column":39},"action":"remove","lines":["o"],"id":10}],[{"start":{"row":0,"column":38},"end":{"row":0,"column":39},"action":"insert","lines":["t"],"id":11},{"start":{"row":0,"column":39},"end":{"row":0,"column":40},"action":"insert","lines":["o"]},{"start":{"row":0,"column":40},"end":{"row":0,"column":41},"action":"insert","lines":["r"]},{"start":{"row":0,"column":41},"end":{"row":0,"column":42},"action":"insert","lines":["e"]}],[{"start":{"row":0,"column":41},"end":{"row":0,"column":42},"action":"remove","lines":["e"],"id":12}],[{"start":{"row":0,"column":41},"end":{"row":0,"column":42},"action":"insert","lines":["a"],"id":13},{"start":{"row":0,"column":42},"end":{"row":0,"column":43},"action":"insert","lines":["g"]},{"start":{"row":0,"column":43},"end":{"row":0,"column":44},"action":"insert","lines":["e"]}],[{"start":{"row":0,"column":37},"end":{"row":0,"column":44},"action":"remove","lines":["storage"],"id":14},{"start":{"row":0,"column":37},"end":{"row":0,"column":54},"action":"insert","lines":["storage_interface"]}],[{"start":{"row":0,"column":54},"end":{"row":0,"column":55},"action":"insert","lines":[" "],"id":15},{"start":{"row":0,"column":55},"end":{"row":0,"column":56},"action":"insert","lines":["i"]},{"start":{"row":0,"column":56},"end":{"row":0,"column":57},"action":"insert","lines":["m"]},{"start":{"row":0,"column":57},"end":{"row":0,"column":58},"action":"insert","lines":["p"]},{"start":{"row":0,"column":58},"end":{"row":0,"column":59},"action":"insert","lines":["o"]},{"start":{"row":0,"column":59},"end":{"row":0,"column":60},"action":"insert","lines":["r"]},{"start":{"row":0,"column":60},"end":{"row":0,"column":61},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":61},"end":{"row":0,"column":62},"action":"insert","lines":[" "],"id":16},{"start":{"row":0,"column":62},"end":{"row":0,"column":63},"action":"insert","lines":["\\"]}],[{"start":{"row":0,"column":63},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":17}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":4},"action":"insert","lines":["    "],"id":18}],[{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":["S"],"id":19},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":1,"column":4},"end":{"row":1,"column":6},"action":"remove","lines":["St"],"id":20},{"start":{"row":1,"column":4},"end":{"row":1,"column":22},"action":"insert","lines":["StorageInterface()"]}],[{"start":{"row":1,"column":20},"end":{"row":1,"column":22},"action":"remove","lines":["()"],"id":21}],[{"start":{"row":1,"column":20},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":22},{"start":{"row":2,"column":0},"end":{"row":2,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":4},"action":"remove","lines":["    "],"id":23}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["f"],"id":24},{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":["r"]},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":["o"]},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":[" "],"id":25},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["f"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["b"]}],[{"start":{"row":2,"column":5},"end":{"row":2,"column":7},"action":"remove","lines":["fb"],"id":26},{"start":{"row":2,"column":5},"end":{"row":2,"column":15},"action":"insert","lines":["fb_post_v2"]}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["."],"id":27},{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"insert","lines":["i"]},{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"insert","lines":["n"]}],[{"start":{"row":2,"column":16},"end":{"row":2,"column":18},"action":"remove","lines":["in"],"id":28},{"start":{"row":2,"column":16},"end":{"row":2,"column":27},"action":"insert","lines":["interactors"]}],[{"start":{"row":2,"column":27},"end":{"row":2,"column":28},"action":"insert","lines":["."],"id":29},{"start":{"row":2,"column":28},"end":{"row":2,"column":29},"action":"insert","lines":["p"]},{"start":{"row":2,"column":29},"end":{"row":2,"column":30},"action":"insert","lines":["r"]},{"start":{"row":2,"column":30},"end":{"row":2,"column":31},"action":"insert","lines":["e"]}],[{"start":{"row":2,"column":28},"end":{"row":2,"column":31},"action":"remove","lines":["pre"],"id":30},{"start":{"row":2,"column":28},"end":{"row":2,"column":37},"action":"insert","lines":["presenter"]}],[{"start":{"row":2,"column":37},"end":{"row":2,"column":38},"action":"insert","lines":["s"],"id":31},{"start":{"row":2,"column":38},"end":{"row":2,"column":39},"action":"insert","lines":["."]}],[{"start":{"row":2,"column":39},"end":{"row":2,"column":40},"action":"insert","lines":["p"],"id":32},{"start":{"row":2,"column":40},"end":{"row":2,"column":41},"action":"insert","lines":["r"]},{"start":{"row":2,"column":41},"end":{"row":2,"column":42},"action":"insert","lines":["e"]}],[{"start":{"row":2,"column":39},"end":{"row":2,"column":42},"action":"remove","lines":["pre"],"id":33},{"start":{"row":2,"column":39},"end":{"row":2,"column":58},"action":"insert","lines":["presenter_interface"]}],[{"start":{"row":2,"column":58},"end":{"row":2,"column":59},"action":"insert","lines":[" "],"id":34},{"start":{"row":2,"column":59},"end":{"row":2,"column":60},"action":"insert","lines":["i"]},{"start":{"row":2,"column":60},"end":{"row":2,"column":61},"action":"insert","lines":["m"]},{"start":{"row":2,"column":61},"end":{"row":2,"column":62},"action":"insert","lines":["p"]},{"start":{"row":2,"column":62},"end":{"row":2,"column":63},"action":"insert","lines":["o"]},{"start":{"row":2,"column":63},"end":{"row":2,"column":64},"action":"insert","lines":["r"]},{"start":{"row":2,"column":64},"end":{"row":2,"column":65},"action":"insert","lines":["t"]}],[{"start":{"row":2,"column":65},"end":{"row":2,"column":66},"action":"insert","lines":[" "],"id":35},{"start":{"row":2,"column":66},"end":{"row":2,"column":67},"action":"insert","lines":["\\"]}],[{"start":{"row":2,"column":67},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":36}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"insert","lines":["    "],"id":37}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":["P"],"id":38},{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["r"]},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["e"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["s"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["e"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["n"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["e"]}],[{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["r"],"id":39}],[{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"remove","lines":["r"],"id":40},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"remove","lines":["e"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"remove","lines":["n"]}],[{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["n"],"id":41},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["t"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["e"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["r"]}],[{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["I"],"id":42},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["n"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":16},"action":"remove","lines":["PresenterInt"],"id":43},{"start":{"row":3,"column":4},"end":{"row":3,"column":24},"action":"insert","lines":["PresenterInterface()"]}],[{"start":{"row":3,"column":22},"end":{"row":3,"column":24},"action":"remove","lines":["()"],"id":44}],[{"start":{"row":3,"column":22},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":45},{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"remove","lines":["    "],"id":46}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":47},{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":6,"column":0},"end":{"row":6,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1589813397630}