extends Area2D

export var speed:float = 256.0
var screen_size:Vector2
onready var animacao:AnimatedSprite =get_node("AnimatedSprite")
signal hit
# Called when the node enters the scene tree for the first time.
func _ready():
	screen_size = get_viewport_rect().size

func _process(delta):
	var velocity:Vector2 = Vector2.ZERO
	if Input.is_action_pressed("move_right"):
		velocity.x += 1
	if Input.is_action_pressed("move_left"):
		velocity.x -= 1
	if Input.is_action_pressed("move_down"):
		velocity.y += 1
	if Input.is_action_pressed("move_up"):
		velocity.y -= 1

	if velocity.length() > 0:
		velocity = velocity.normalized() * speed
		animacao.play()
	else:
		animacao.stop()

	position += velocity * delta
	position.x = clamp(position.x, 0, screen_size.x)
	position.y = clamp(position.y, 0, screen_size.y)

	if velocity.x != 0:
		animacao.animation = "Andar" 
		animacao.flip_v = false
		if velocity.x < 0:
			$AnimatedSprite.flip_h = true
		else:
			$AnimatedSprite.flip_h = false
		animacao.flip_h = velocity.x < 0
	elif velocity.y != 0:
		animacao.animation = "Cima"
		animacao.flip_v = velocity.y > 0



func _on_Player_body_entered(body):
	hide()
	emit_signal("hit")
	$CollisionShape2D.set_deferred("disabled", true)
	
func start(pos):
	position = pos
	show()
	$CollisionShape2D.disabled = false
