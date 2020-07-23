{"filter":false,"title":"test_truck_load.py","tooltip":"/clean_code/clean_code_submissions/clean_code_assignment_002/tests/test_truck_load.py","undoManager":{"mark":28,"position":28,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["f"],"id":1},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["r"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["o"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":[" "],"id":2},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["t"]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":["r"]},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["u"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["c"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["k"]}],[{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":[" "],"id":3},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["i"]},{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"insert","lines":["m"]},{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"insert","lines":["p"]},{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"insert","lines":["o"]},{"start":{"row":0,"column":15},"end":{"row":0,"column":16},"action":"insert","lines":["r"]},{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"insert","lines":[" "],"id":4},{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"insert","lines":["T"]},{"start":{"row":0,"column":19},"end":{"row":0,"column":20},"action":"insert","lines":["r"]}],[{"start":{"row":0,"column":18},"end":{"row":0,"column":20},"action":"remove","lines":["Tr"],"id":5},{"start":{"row":0,"column":18},"end":{"row":0,"column":23},"action":"insert","lines":["Truck"]}],[{"start":{"row":0,"column":23},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":7}],[{"start":{"row":3,"column":0},"end":{"row":123,"column":0},"action":"insert","lines":["# case-","def test_load_when_truck_in_motion_and_print_string(capfd):","","    # Arrange","    truck = Truck(","        color='Blue',","        max_speed=5,","        acceleration=4,","        tyre_friction=3,","        max_cargo_weight=100","    )","    truck.start_engine()","    truck.accelerate()","    cannot_load = \"Cannot load cargo during motion\\n\"","","    # Act","    truck.load(1)","    output = capfd.readouterr()","","    # Assert","    assert output.out == cannot_load","","","def test_load_when_truck_not_in_motion_with_invalid_load_values_raise_error():","","    # Arrange","    truck = Truck(","        color='Blue',","        max_speed=5,","        acceleration=4,","        tyre_friction=3,","        max_cargo_weight=100","    )","    truck.start_engine()","    invalid_cargo_weight = \"Invalid value for cargo_weight\"","","    # Act","    with pytest.raises(ValueError) as error:","        truck.load(-1)","","    # Assert","    assert str(error.value) == invalid_cargo_weight","","","def test_load_when_truck_at_rest_and_print_string_when_load_maximum(capfd):","","    # Arrange","    color = 'Blue'","    max_speed = 5","    acceleration = 4","    tyre_friction = 3","    max_cargo_weight = 1","","    truck = Truck(","        color=color,","        max_speed=max_speed,","        acceleration=acceleration,","        tyre_friction=tyre_friction,","        max_cargo_weight=max_cargo_weight","    )","    cannot_load_more = (\"Cannot load cargo more than max limit: {}\\n\"","                        .format(max_cargo_weight))","","    # Act","    truck.load(2)","    output = capfd.readouterr()","","    # Assert","    assert output.out == cannot_load_more","","","def test_load_when_truck_at_rest_with_valid_load_values_and_update_load():","","    # Arrange","    color = 'Blue'","    max_speed = 5","    acceleration = 4","    tyre_friction = 3","    max_cargo_weight = 1","","    truck = Truck(","        color=color,","        max_speed=max_speed,","        acceleration=acceleration,","        tyre_friction=tyre_friction,","        max_cargo_weight=max_cargo_weight","    )","    load_value = 1","","    # Act","    truck.load(1)","","    # Assert","    assert truck.current_load_weight == load_value","","","def test_load_when_truck_at_rest_with_load_value_to_zero_and_update_load():","","    # Arrange","    color = 'Blue'","    max_speed = 5","    acceleration = 4","    tyre_friction = 3","    max_cargo_weight = 100","","    truck = Truck(","        color=color,","        max_speed=max_speed,","        acceleration=acceleration,","        tyre_friction=tyre_friction,","        max_cargo_weight=max_cargo_weight","    )","    load_value = 0","","    # Act","    truck.load(0)","","    # Assert","    assert truck.current_load_weight == load_value","",""],"id":8}],[{"start":{"row":122,"column":0},"end":{"row":123,"column":0},"action":"remove","lines":["",""],"id":9}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":10}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["i"],"id":11},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["m"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["p"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["o"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["r"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":[" "],"id":12},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["p"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["y"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["t"]},{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":["e"]},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["s"]},{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":103,"column":16},"end":{"row":103,"column":17},"action":"remove","lines":["e"],"id":13},{"start":{"row":103,"column":15},"end":{"row":103,"column":16},"action":"remove","lines":["u"]},{"start":{"row":103,"column":14},"end":{"row":103,"column":15},"action":"remove","lines":["l"]}],[{"start":{"row":103,"column":14},"end":{"row":103,"column":15},"action":"insert","lines":["r"],"id":14},{"start":{"row":103,"column":15},"end":{"row":103,"column":16},"action":"insert","lines":["o"]},{"start":{"row":103,"column":16},"end":{"row":103,"column":17},"action":"insert","lines":["w"]},{"start":{"row":103,"column":17},"end":{"row":103,"column":18},"action":"insert","lines":["n"]}],[{"start":{"row":31,"column":18},"end":{"row":31,"column":19},"action":"remove","lines":["e"],"id":15},{"start":{"row":31,"column":17},"end":{"row":31,"column":18},"action":"remove","lines":["u"]},{"start":{"row":31,"column":16},"end":{"row":31,"column":17},"action":"remove","lines":["l"]},{"start":{"row":31,"column":15},"end":{"row":31,"column":16},"action":"remove","lines":["B"]}],[{"start":{"row":31,"column":15},"end":{"row":31,"column":16},"action":"insert","lines":["G"],"id":16},{"start":{"row":31,"column":16},"end":{"row":31,"column":17},"action":"insert","lines":["r"]},{"start":{"row":31,"column":17},"end":{"row":31,"column":18},"action":"insert","lines":["a"]},{"start":{"row":31,"column":18},"end":{"row":31,"column":19},"action":"insert","lines":["y"]}],[{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"remove","lines":["e"],"id":17},{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"remove","lines":["u"]},{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"remove","lines":["l"]},{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"remove","lines":["B"]}],[{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"insert","lines":["M"],"id":18},{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"insert","lines":["a"]},{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":["g"]},{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"insert","lines":["e"]},{"start":{"row":9,"column":19},"end":{"row":9,"column":20},"action":"insert","lines":["n"]},{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"insert","lines":["t"]},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"insert","lines":["a"]}],[{"start":{"row":31,"column":18},"end":{"row":31,"column":19},"action":"remove","lines":["y"],"id":19},{"start":{"row":31,"column":17},"end":{"row":31,"column":18},"action":"remove","lines":["a"]},{"start":{"row":31,"column":16},"end":{"row":31,"column":17},"action":"remove","lines":["r"]},{"start":{"row":31,"column":15},"end":{"row":31,"column":16},"action":"remove","lines":["G"]}],[{"start":{"row":31,"column":15},"end":{"row":31,"column":16},"action":"insert","lines":["M"],"id":20},{"start":{"row":31,"column":16},"end":{"row":31,"column":17},"action":"insert","lines":["a"]},{"start":{"row":31,"column":17},"end":{"row":31,"column":18},"action":"insert","lines":["r"]},{"start":{"row":31,"column":18},"end":{"row":31,"column":19},"action":"insert","lines":["o"]},{"start":{"row":31,"column":19},"end":{"row":31,"column":20},"action":"insert","lines":["o"]},{"start":{"row":31,"column":20},"end":{"row":31,"column":21},"action":"insert","lines":["n"]}],[{"start":{"row":51,"column":16},"end":{"row":51,"column":17},"action":"remove","lines":["e"],"id":21},{"start":{"row":51,"column":15},"end":{"row":51,"column":16},"action":"remove","lines":["u"]},{"start":{"row":51,"column":14},"end":{"row":51,"column":15},"action":"remove","lines":["l"]},{"start":{"row":51,"column":13},"end":{"row":51,"column":14},"action":"remove","lines":["B"]}],[{"start":{"row":51,"column":13},"end":{"row":51,"column":14},"action":"insert","lines":["M"],"id":22},{"start":{"row":51,"column":14},"end":{"row":51,"column":15},"action":"insert","lines":["e"]},{"start":{"row":51,"column":15},"end":{"row":51,"column":16},"action":"insert","lines":["d"]},{"start":{"row":51,"column":16},"end":{"row":51,"column":17},"action":"insert","lines":["i"]},{"start":{"row":51,"column":17},"end":{"row":51,"column":18},"action":"insert","lines":["u"]},{"start":{"row":51,"column":18},"end":{"row":51,"column":19},"action":"insert","lines":["m"]}],[{"start":{"row":51,"column":19},"end":{"row":51,"column":20},"action":"insert","lines":["B"],"id":23},{"start":{"row":51,"column":20},"end":{"row":51,"column":21},"action":"insert","lines":["l"]},{"start":{"row":51,"column":21},"end":{"row":51,"column":22},"action":"insert","lines":["u"]},{"start":{"row":51,"column":22},"end":{"row":51,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":78,"column":16},"end":{"row":78,"column":17},"action":"remove","lines":["e"],"id":24},{"start":{"row":78,"column":15},"end":{"row":78,"column":16},"action":"remove","lines":["u"]},{"start":{"row":78,"column":14},"end":{"row":78,"column":15},"action":"remove","lines":["l"]},{"start":{"row":78,"column":13},"end":{"row":78,"column":14},"action":"remove","lines":["B"]}],[{"start":{"row":78,"column":13},"end":{"row":78,"column":14},"action":"insert","lines":["M"],"id":25},{"start":{"row":78,"column":14},"end":{"row":78,"column":15},"action":"insert","lines":["i"]},{"start":{"row":78,"column":15},"end":{"row":78,"column":16},"action":"insert","lines":["n"]},{"start":{"row":78,"column":16},"end":{"row":78,"column":17},"action":"insert","lines":["t"]},{"start":{"row":78,"column":17},"end":{"row":78,"column":18},"action":"insert","lines":["C"]}],[{"start":{"row":78,"column":18},"end":{"row":78,"column":19},"action":"insert","lines":["r"],"id":26},{"start":{"row":78,"column":19},"end":{"row":78,"column":20},"action":"insert","lines":["e"]},{"start":{"row":78,"column":20},"end":{"row":78,"column":21},"action":"insert","lines":["a"]},{"start":{"row":78,"column":21},"end":{"row":78,"column":22},"action":"insert","lines":["m"]}],[{"start":{"row":103,"column":17},"end":{"row":103,"column":18},"action":"remove","lines":["n"],"id":27},{"start":{"row":103,"column":16},"end":{"row":103,"column":17},"action":"remove","lines":["w"]},{"start":{"row":103,"column":15},"end":{"row":103,"column":16},"action":"remove","lines":["o"]},{"start":{"row":103,"column":14},"end":{"row":103,"column":15},"action":"remove","lines":["r"]},{"start":{"row":103,"column":13},"end":{"row":103,"column":14},"action":"remove","lines":["B"]}],[{"start":{"row":103,"column":13},"end":{"row":103,"column":14},"action":"insert","lines":["M"],"id":28},{"start":{"row":103,"column":14},"end":{"row":103,"column":15},"action":"insert","lines":["i"]},{"start":{"row":103,"column":15},"end":{"row":103,"column":16},"action":"insert","lines":["s"]},{"start":{"row":103,"column":16},"end":{"row":103,"column":17},"action":"insert","lines":["t"]},{"start":{"row":103,"column":17},"end":{"row":103,"column":18},"action":"insert","lines":["y"]}],[{"start":{"row":103,"column":18},"end":{"row":103,"column":19},"action":"insert","lines":["R"],"id":29},{"start":{"row":103,"column":19},"end":{"row":103,"column":20},"action":"insert","lines":["o"]},{"start":{"row":103,"column":20},"end":{"row":103,"column":21},"action":"insert","lines":["s"]},{"start":{"row":103,"column":21},"end":{"row":103,"column":22},"action":"insert","lines":["e"]}]]},"ace":{"folds":[],"scrolltop":2156,"scrollleft":0,"selection":{"start":{"row":103,"column":22},"end":{"row":103,"column":22},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":106,"state":"start","mode":"ace/mode/python"}},"timestamp":1587546417432,"hash":"2b4140fbf09b3385b0e7869c5cb656353ac915f5"}