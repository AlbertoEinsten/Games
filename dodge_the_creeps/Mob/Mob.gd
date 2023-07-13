extends RigidBody2D

onready var animacao:AnimatedSprite = get_node("AnimatedSprite")

func _ready():
	animacao.playing = true
	var mob_types = animacao.frames.get_animation_names()
	animacao.animation = mob_types[randi() % mob_types.size()]



func _process(delta):
	pass

func _on_VisibilityNotifier2D_screen_exited():
	queue_free()
