{"filter":false,"title":"models.py","tooltip":"/django/django_submissions/django_assignment_003/imdb/models.py","undoManager":{"mark":13,"position":13,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.db import models","","# Create your models here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":39,"column":52},"action":"insert","lines":["from django.db import models","","# Create your models here.","","    ","class Actor(models.Model):","    actor_id=models.CharField(max_length=100,primary_key=True)","    name=models.CharField(max_length=100)","    ","    ","class Director(models.Model):","    name=models.CharField(max_length=100,unique=True)","    ","  ","  ","class Movie(models.Model):","    name=models.CharField(max_length=100)","    movie_id=models.CharField(max_length=100,primary_key=True)","    box_office_collection_in_crores=models.FloatField()","    release_date=models.DateField()","    #director","    director=models.ForeignKey(Director, on_delete=models.CASCADE)","    actors=models.ManyToManyField(Actor,through='Cast')","    ","","  ","class Cast(models.Model):","    actor=models.ForeignKey(Actor, on_delete=models.CASCADE)","    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)","    role=models.CharField(max_length=50)","    is_debut_movie=models.BooleanField(default=False)","    ","    ","class Rating(models.Model):","    movie=models.OneToOneField(Movie,on_delete=models.CASCADE,primary_key=True)","    rating_one_count=models.IntegerField(default=0)","    rating_two_count=models.IntegerField(default=0)","    rating_three_count=models.IntegerField(default=0)","    rating_four_count=models.IntegerField(default=0)","    rating_five_count=models.IntegerField(default=0)"]}],[{"start":{"row":12,"column":4},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["d"]},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":["f"],"id":4}],[{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":[" "],"id":5},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["_"]},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":["_"]},{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"insert","lines":["s"]},{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"insert","lines":["t"]},{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["r"]}],[{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["_"],"id":6},{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"insert","lines":["_"]}],[{"start":{"row":13,"column":15},"end":{"row":13,"column":17},"action":"insert","lines":["()"],"id":7}],[{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"insert","lines":["s"],"id":8},{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":["e"]},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["l"]},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"insert","lines":["f"]}],[{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"insert","lines":[":"],"id":9}],[{"start":{"row":13,"column":22},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":14,"column":0},"end":{"row":14,"column":8},"action":"insert","lines":["        "]},{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"insert","lines":["r"]},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":["e"]},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":["t"]},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["u"]},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":["r"]},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["n"]}],[{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":[" "],"id":11},{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"insert","lines":["s"]},{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"insert","lines":["e"]},{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"insert","lines":["l"]},{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"insert","lines":["f"]},{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"insert","lines":["."]}],[{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"insert","lines":["n"],"id":12},{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"insert","lines":["a"]},{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"insert","lines":["m"]},{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":41},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]},{"start":{"row":8,"column":4},"end":{"row":9,"column":0},"action":"insert","lines":["",""]},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":8,"column":4},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":14},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":9,"column":4},"end":{"row":10,"column":24},"action":"insert","lines":["def __str__(self):","        return self.name"],"id":15}]]},"ace":{"folds":[],"scrolltop":281.58108959858595,"scrollleft":0,"selection":{"start":{"row":11,"column":4},"end":{"row":11,"column":4},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":15,"state":"start","mode":"ace/mode/python"}},"timestamp":1585048465792,"hash":"98434a6513fa019aba258ce2067c083d5702498d"}