from enum import Enum

class Stage(Enum):
    NO_STAGE = 0
    FINAL_DESTINATION = 0x19
    BATTLEFIELD = 0x18
    POKEMON_STADIUM = 0x12
    DREAMLAND = 0x1A
    FOUNTAIN_OF_DREAMS = 0x8
    YOSHIS_STORY = 0x6
    RANDOM_STAGE = 0x1D #not technically a stage, but it's useful to call it one

class Menu(Enum):
    CHARACTER_SELECT = 0
    STAGE_SELECT = 1
    IN_GAME = 2
    SUDDEN_DEATH = 3
    POSTGAME_SCORES = 4

class ControllerStatus(Enum):
    CONTROLLER_HUMAN = 0
    CONTROLLER_CPU = 1
    CONTROLLER_UNPLUGGED = 3

class ControllerType(Enum):
    STANDARD = "6"
    GCN_ADAPTER = "12"
    UNPLUGGED = "0"

class AttackState(Enum):
    WINDUP = 0
    ATTACKING = 1
    COOLDOWN = 2
    NOT_ATTACKING = 3

class Character(Enum):
    MARIO = 0x00
    FOX = 0x01
    CPTFALCON = 0x02
    DK = 0x03
    KIRBY = 0x04
    BOWSER = 0x05
    LINK = 0x06
    SHEIK = 0x07
    NESS = 0x08
    PEACH = 0x09
    POPO = 0x0a
    NANA = 0x0b
    PIKACHU = 0x0c
    SAMUS = 0x0d
    YOSHI = 0x0e
    JIGGLYPUFF = 0x0f
    MEWTWO = 0x10
    LUIGI = 0x11
    MARTH = 0x12
    ZELDA = 0x13
    YLINK = 0x14
    DOC = 0x15
    FALCO = 0x16
    PICHU = 0x17
    GAMEANDWATCH = 0x18
    GANONDORF = 0x19
    ROY = 0x1a
    WIREFRAME_MALE = 0x1d
    WIREFRAME_FEMALE = 0x1e
    GIGA_BOWSER = 0x1f
    SANDBAG = 0x20
    UNKNOWN_CHARACTER = 0xff

def convertToInternalCharacterID(id):
    """ Converts a character select-screen ID to an 'internal ID' enum """
    if id == 0x00:
        return Character.DOC
    if id == 0x01:
        return Character.MARIO
    if id == 0x02:
        return Character.LUIGI
    if id == 0x03:
        return Character.BOWSER
    if id == 0x04:
        return Character.PEACH
    if id == 0x05:
        return Character.YOSHI
    if id == 0x06:
        return Character.DK
    if id == 0x07:
        return Character.CPTFALCON
    if id == 0x08:
        return Character.GANONDORF
    if id == 0x09:
        return Character.FALCO
    if id == 0x0a:
        return Character.FOX
    if id == 0x0b:
        return Character.NESS
    if id == 0x0c:
        return Character.POPO
    if id == 0x0d:
        return Character.KIRBY
    if id == 0x0e:
        return Character.SAMUS
    if id == 0x0f:
        return Character.ZELDA
    if id == 0x10:
        return Character.LINK
    if id == 0x11:
        return Character.YLINK
    if id == 0x12:
        return Character.PICHU
    if id == 0x13:
        return Character.PIKACHU
    if id == 0x14:
        return Character.JIGGLYPUFF
    if id == 0x15:
        return Character.MEWTWO
    if id == 0x16:
        return Character.GAMEANDWATCH
    if id == 0x17:
        return Character.MARTH
    if id == 0x18:
        return Character.ROY
    return Character.UNKNOWN_CHARACTER

class Button(Enum):
    BUTTON_A = "A"
    BUTTON_B = "B"
    BUTTON_X = "X"
    BUTTON_Y = "Y"
    BUTTON_Z = "Z"
    BUTTON_L = "L"
    BUTTON_R = "R"
    BUTTON_START = "START"
    BUTTON_D_UP = "D_UP"
    BUTTON_D_DOWN = "D_DOWN"
    BUTTON_D_LEFT = "D_LEFT"
    BUTTON_D_RIGHT = "D_RIGHT"
    #Control sticks considered "buttons" here
    BUTTON_MAIN = "MAIN"
    BUTTON_C = "C"

class Action(Enum):
    DEAD_DOWN = 0x0
    DEAD_LEFT = 0x1
    DEAD_RIGHT = 0x2
    DEAD_FLY_STAR = 0x4
    DEAD_FLY = 0x6 #When you have been hit upwards and are dead
    DEAD_FLY_SPLATTER = 0x7 #Hit upwards and have splattered on the camera
    DEAD_FLY_SPLATTER_FLAT = 0x8 #Hit upwards and have splattered on the camera
    ON_HALO_DESCENT = 0xc
    ON_HALO_WAIT = 0x0d
    STANDING = 0x0e
    WALK_SLOW = 0x0f
    WALK_MIDDLE = 0x10
    WALK_FAST = 0x11
    TURNING = 0x12
    TURNING_RUN = 0x13
    DASHING = 0x14
    RUNNING = 0x15
    RUN_DIRECT = 0x16
    RUN_BRAKE = 0x17
    KNEE_BEND = 0x18 #pre-jump animation.
    JUMPING_FORWARD = 0x19
    JUMPING_BACKWARD = 0x1A
    JUMPING_ARIAL_FORWARD = 0x1b
    JUMPING_ARIAL_BACKWARD = 0x1c
    FALLING = 0x1D    #The "wait" state of the air.
    FALLING_AERIAL = 0x20  #After double-jump
    DEAD_FALL = 0x23 #Falling after up-b
    SPECIAL_FALL_FORWARD = 0x24
    SPECIAL_FALL_BACK = 0x25
    TUMBLING = 0x26
    CROUCH_START = 0x27 #Going from stand to crouch
    CROUCHING = 0x28
    CROUCH_END = 0x29 #Standing up from crouch
    LANDING = 0x2a #Can be canceled. Not stunned
    LANDING_SPECIAL = 0x2b #Landing special like from wavedash. Stunned.
    NEUTRAL_ATTACK_1 = 0x2c
    NEUTRAL_ATTACK_2 = 0x2d
    NEUTRAL_ATTACK_3 = 0x2e
    LOOPING_ATTACK_START = 0x2f
    LOOPING_ATTACK_MIDDLE = 0x30
    LOOPING_ATTACK_END = 0x31
    DASH_ATTACK = 0x32
    FTILT_HIGH = 0x33
    FTILT_HIGH_MID = 0x34
    FTILT_MID = 0x35
    FTILT_LOW_MID = 0x36
    FTILT_LOW = 0x37
    UPTILT = 0x38
    DOWNTILT = 0x39
    FSMASH_HIGH = 0x3a
    FSMASH_MID_HIGH = 0x3b
    FSMASH_MID = 0x3c
    FSMASH_MID_LOW = 0x3d
    FSMASH_LOW = 0x3e
    UPSMASH = 0x3f
    DOWNSMASH = 0x40
    NAIR = 0x41
    FAIR = 0x42
    BAIR = 0x43
    UAIR = 0x44
    DAIR = 0x45
    NAIR_LANDING  = 0x46
    FAIR_LANDING  = 0x47
    BAIR_LANDING  = 0x48
    UAIR_LANDING  = 0x49
    DAIR_LANDING  = 0x4a
    DAMAGE_HIGH_1 = 0x4b
    DAMAGE_HIGH_2 = 0x4c
    DAMAGE_HIGH_3 = 0x4d
    DAMAGE_NEUTRAL_1 = 0x4e
    DAMAGE_NEUTRAL_2 = 0x4f
    DAMAGE_NEUTRAL_3 = 0x50
    DAMAGE_LOW_1 = 0x51
    DAMAGE_LOW_2 = 0x52
    DAMAGE_LOW_3 = 0x53
    DAMAGE_AIR_1 = 0x54
    DAMAGE_AIR_2 = 0x55
    DAMAGE_AIR_3 = 0x56
    DAMAGE_FLY_HIGH = 0x57
    DAMAGE_FLY_NEUTRAL = 0x58
    DAMAGE_FLY_LOW = 0x59
    DAMAGE_FLY_TOP = 0x5a
    DAMAGE_FLY_ROLL = 0x5b
    ITEM_PICKUP_LIGHT = 0x5C
    ITEM_PICKUP_HEAVY = 0x5D
    ITEM_THROW_LIGHT_FORWARD = 0x5E
    ITEM_THROW_LIGHT_BACK = 0x5F
    ITEM_THROW_LIGHT_HIGH = 0x60
    ITEM_THROW_LIGHT_LOW = 0x61
    ITEM_THROW_LIGHT_DASH = 0x62
    ITEM_THROW_LIGHT_DROP = 0x63
    ITEM_THROW_LIGHT_AIR_FORWARD = 0x64
    ITEM_THROW_LIGHT_AIR_BACK = 0x65
    ITEM_THROW_LIGHT_AIR_HIGH = 0x66
    ITEM_THROW_LIGHT_AIR_LOW = 0x67
    ITEM_THROW_HEAVY_FORWARD = 0x68
    ITEM_THROW_HEAVY_BACK = 0x69
    ITEM_THROW_HEAVY_HIGH = 0x6A
    ITEM_THROW_HEAVY_LOW = 0x6B
    ITEM_THROW_LIGHT_SMASH_FORWARD = 0x6C
    ITEM_THROW_LIGHT_SMASH_BACK = 0x6D
    ITEM_THROW_LIGHT_SMASH_UP = 0x6e
    ITEM_THROW_LIGHT_SMASH_DOWN = 0x6F
    ITEM_THROW_LIGHT_AIR_SMASH_FORWARD = 0x70
    ITEM_THROW_LIGHT_AIR_SMASH_BACK = 0x71
    ITEM_THROW_LIGHT_AIR_SMASH_HIGH = 0x72
    ITEM_THROW_LIGHT_AIR_SMASH_LOW = 0x73
    ITEM_THROW_HEAVY_AIR_SMASH_FORWARD = 0x74
    ITEM_THROW_HEAVY_AIR_SMASH_BACK = 0x75
    ITEM_THROW_HEAVY_AIR_SMASH_HIGH = 0x76
    ITEM_THROW_HEAVY_AIR_SMASH_LOW = 0x77
    BEAM_SWORD_SWING_1 = 0x78
    BEAM_SWORD_SWING_2 = 0x79
    BEAM_SWORD_SWING_3 = 0x7A
    BEAM_SWORD_SWING_4 = 0x7B
    SHIELD_START = 0xb2
    SHIELD = 0xb3
    SHIELD_RELEASE = 0xb4
    SHIELD_STUN = 0xb5
    SHIELD_REFLECT = 0xb6
    TECH_MISS_UP = 0xb7 # "facing" up. Not important to us
    LYING_GROUND_UP = 0xb8
    LYING_GROUND_UP_HIT = 0xb9
    GROUND_GETUP = 0xba
    GROUND_ATTACK_UP = 0xbb
    GROUND_ROLL_FORWARD_UP = 0xbc
    GROUND_ROLL_BACKWARD_UP = 0xbd
    TECH_MISS_DOWN = 0xbf
    LYING_GROUND_DOWN = 0xc0
    DAMAGE_GROUND = 0xc1
    NEUTRAL_GETUP = 0xc2
    GETUP_ATTACK = 0xc3
    GROUND_ROLL_FORWARD_DOWN = 0xc4
    GROUND_ROLL_BACKWARD_DOWN = 0xc5
    NEUTRAL_TECH = 0xc7
    FORWARD_TECH = 0xc8
    BACKWARD_TECH = 0xc9
    WALL_TECH = 0xca
    WALL_TECH_JUMP = 0xcb
    CEILING_TECH = 0xcc
    SHIELD_BREAK_FLY = 0xcd
    SHIELD_BREAK_FALL = 0xce
    SHIELD_BREAK_DOWN_U = 0xcf
    SHIELD_BREAK_DOWN_D = 0xd0
    SHIELD_BREAK_STAND_U = 0xd1
    SHIELD_BREAK_STAND_D = 0xd2
    SHIELD_BREAK_TEETER = 0xd3
    GRAB = 0xd4
    GRAB_PULLING = 0xd5
    GRAB_RUNNING = 0xd6
    GRAB_WAIT = 0xd8
    GRAB_PUMMEL = 0xd9
    GRAB_BREAK = 0xda
    THROW_FORWARD = 0xdb
    THROW_BACK = 0xdc
    THROW_UP = 0xdd    #yuck
    THROW_DOWN = 0xde
    GRAB_PULLING_HIGH = 0xdf
    GRABBED_WAIT_HIGH = 0xe0 #XXX Not sure about this
    PUMMELED_HIGH = 0xe1 #XXX Not sure about this
    GRAB_PULL = 0xe2   #Being pulled inwards from the grab
    GRABBED = 0xe3   #Grabbed
    GRAB_PUMMELED = 0xe4   #Being pummeled
    GRAB_ESCAPE = 0xe5
    ROLL_FORWARD = 0xe9
    ROLL_BACKWARD = 0xea
    SPOTDODGE = 0xEB
    AIRDODGE = 0xEC
    THROWN_FORWARD = 0xEF
    THROWN_BACK = 0xF0
    THROWN_UP = 0xF1
    THROWN_DOWN = 0xF2
    THROWN_DOWN_2 = 0xf3
    PLATFORM_DROP = 0xf4
    EDGE_TEETERING_START = 0xF5 #Starting of edge teetering
    EDGE_TEETERING = 0xF6
    BOUNCE_WALL = 0xf7
    BOUNCE_CEILING = 0xf8
    BUMP_WALL = 0xf9
    BUMP_CIELING = 0xfa
    SLIDING_OFF_EDGE = 0xfb #When you get hit and slide off an edge
    EDGE_CATCHING = 0xFC #Initial grabbing of edge stuck in stun here
    EDGE_HANGING = 0xFD
    EDGE_GETUP_SLOW = 0xFE  # >= 100% damage
    EDGE_GETUP_QUICK = 0xFF # < 100% damage
    EDGE_ATTACK_SLOW = 0x100 # < 100% damage
    EDGE_ATTACK_QUICK = 0x101 # >= 100% damage
    EDGE_ROLL_SLOW = 0x102 # >= 100% damage
    EDGE_ROLL_QUICK = 0x103 # < 100% damage
    EDGE_JUMP_1_SLOW = 0x104
    EDGE_JUMP_2_SLOW = 0x105
    EDGE_JUMP_1_QUICK = 0x106
    EDGE_JUMP_2_QUICK = 0x107
    TAUNT_RIGHT = 0x108
    TAUNT_LEFT = 0x109
    ENTRY = 0x142    #Start of match. Can't move
    ENTRY_START = 0x143    #Start of match. Can't move
    ENTRY_END = 0x144    #Start of match. Can't move
    LASER_GUN_PULL = 0x155
    NEUTRAL_B_CHARGING = 0x156
    NEUTRAL_B_ATTACKING = 0x157
    NEUTRAL_B_FULL_CHARGE = 0x158
    WAIT_ITEM = 0x159 #No idea what this is
    NEUTRAL_B_CHARGING_AIR = 0x15A
    NEUTRAL_B_ATTACKING_AIR = 0x15B
    NEUTRAL_B_FULL_CHARGE_AIR = 0x15C
    DOWN_B_GROUND_START = 0x168
    DOWN_B_GROUND = 0x169
    SHINE_TURN = 0x16c
    DOWN_B_STUN = 0x16d #Fox is stunned in these frames
    DOWN_B_AIR = 0x16e
    UP_B_GROUND = 0x16f
    SHINE_RELEASE_AIR = 0x170
    SWORD_DANCE_1 = 0x15d
    SWORD_DANCE_2_HIGH = 0x15e
    SWORD_DANCE_2_MID = 0x15f
    SWORD_DANCE_3_HIGH = 0x160
    SWORD_DANCE_3_MID = 0x161
    SWORD_DANCE_3_LOW = 0x162
    SWORD_DANCE_4_HIGH = 0x163
    SWORD_DANCE_4_MID = 0x164
    SWORD_DANCE_4_LOW = 0x165
    SWORD_DANCE_1_AIR = 0x166
    SWORD_DANCE_2_HIGH_AIR = 0x167
    SWORD_DANCE_2_MID_AIR = 0x168
    SWORD_DANCE_3_HIGH_AIR = 0x169
    SWORD_DANCE_3_MID_AIR = 0x16a
    SWORD_DANCE_3_LOW_AIR = 0x16b
    SWORD_DANCE_4_HIGH_AIR = 0x16c
    SWORD_DANCE_4_MID_AIR = 0x16d
    SWORD_DANCE_4_LOW_AIR = 0x16e
    FOX_ILLUSION_START = 0x15e
    FOX_ILLUSION = 0x15f
    FOX_ILLUSION_SHORTENED = 0x160
    FIREFOX_WAIT_GROUND = 0x161 #Firefox wait on the ground
    FIREFOX_WAIT_AIR = 0x162 #Firefox wait in the air
    FIREFOX_GROUND = 0x163 #Firefox on the ground
    FIREFOX_AIR = 0x164 #Firefox in the air
    UP_B_AIR = 0x170    #The upswing of the UP-B. (At least for marth)
    MARTH_COUNTER = 0x171
    PARASOL_FALLING = 0x172
    MARTH_COUNTER_FALLING = 0x173
    NESS_SHEILD_START = 0x174
    NESS_SHEILD = 0x174
    NESS_SHEILD_AIR = 0x175
    NESS_SHEILD_AIR_END = 0x177
    UNKNOWN_ANIMATION = 0xffff

class ProjectileSubtype(Enum):
    BOB_OMB = 0x06 # Bob-omb (BombHei)
    MR_SATURN = 0x07 # Mr. Saturn (Dosei)
    BEAMSWORD = 0x0C # Beam Sword
    MARIO_FIREBALL = 0x30 # Mario's fire
    DR_MARIO_CAPSULE = 0x31 # Dr.Mario's Capsule
    KIRBY_CUTTER = 0x32 # Kirby's Cutter beam
    KIRBY_HAMMER = 0x33 # Kirby's Hammer
    FOX_LASER = 0x36 # Fox's Laser
    FALCO_LASER = 0x37 # Falco's Laser
    FOX_SHADOW = 0x38 # Fox's shadow
    FALCO_SHADOW = 0x39 # Falco's shadow
    LINK_BOMB = 0x3A # Link's bomb
    YLINK_BOMB = 0x3B # Young Link's bomb
    LINK_BOOMERANG = 0x3C # Link's boomerang
    YLINK_BOOMERANG = 0x3D # Young Link's boomerang
    LINK_HOOKSHOT = 0x3E # Link's Hookshot
    YLINK_HOOKSHOT = 0x3F # Young Link's Hookshot
    ARROW = 0x40 # Arrow
    FIRE_ARROW = 0x41 # Fire Arrow
    PK_FIRE = 0x42 # PK Fire
    PK_FLASH_1 = 0x43 # PK Flash
    PK_FLASH_2 = 0x44 # PK Flash
    PK_THUNDER_HEAD = 0x45 # PK Thunder (Primary)
    PK_THUNDER_TAIL_1 = 0x46 # PK Thunder
    PK_THUNDER_TAIL_2 = 0x47 # PK Thunder
    PK_THUNDER_TAIL_3 = 0x48 # PK Thunder
    PK_THUNDER_TAIL_4 = 0x49 # PK Thunder
    LINK_ARROW = 0x4C # Link's Arrow
    YLINK_ARROW = 0x4D # Young Link's arrow
    PK_FLASH_EXPLOSION = 0x4E # PK Flash (explosion)
    NEEDLE_THROWN = 0x4F # Needle(thrown)
    PIKACHU_THUNDER = 0x51 # Pikachu's Thunder
    PICHU_THUNDER = 0x52 # Pichu's Thunder
    MARIO_CAPE = 0x53 # Mario's cape
    DR_MARIO_CAPE = 0x54 # Dr.Mario's cape
    SHEIK_SMOKE = 0x55 # Smoke (Sheik)
    YOSHI_EGG_THROWN = 0x56 # Yoshi's egg(thrown)
    YOSHI_TONGUE = 0x57 # Yoshi's Tongue??
    YOSHI_STAR = 0x58 # Yoshi's Star
    PIKACHU_THUNDERJOLT_1 = 0x59 # Pikachu's thunder (B)
    PIKACHU_THUNDERJOLT_2 = 0x5A # Pikachu's thunder (B)
    PICHU_THUNDERJOLT_1 = 0x5B # Pichu's thunder (B)
    PICHU_THUNDERJOLT_2 = 0x5C # Pichu's thunder (B)
    SAMUS_BOMB = 0x5D # Samus's bomb
    SAMUS_CHARGE_BEAM = 0x5E # Samus's chargeshot
    SAMUS_MISSLE = 0x5F # Missile
    SAMUS_GRAPPLE_BEAM = 0x60 # Grapple beam
    SHEIK_CHAIN = 0x61 # Sheik's chain
    TURNIP = 0x63 # Turnip
    BOWSER_FLAME = 0x64 # Bowser's flame
    NESS_BATT = 0x65 # Ness's bat
    NESS_YOYO = 0x66 # Yoyo
    PEACH_PARASOL = 0x67 # Peach's parasol
    LUIGI_FIRE = 0x69 # Luigi's fire
    ICE_BLOCK = 0x6A # Ice(Iceclimbers)
    IC_BLIZZARD = 0x6B # Blizzard
    ZELDA_FIRE = 0x6C # Zelda's fire
    ZELDA_FIRE_EXPLOSION = 0x6D # Zelda's fire (explosion)
    TOAD_SPORE = 0x6F # Toad's spore
    SHADOWBALL = 0x70 # Mewtwo's Shadowball
    IC_UP_B = 0x71 # Iceclimbers' Up  #B
    PESTICIDE = 0x72 # Pesticide
    MANHOLE = 0x73 # Manhole
    GW_FIRE = 0x74 # Fire(G&W)
    PARACHUTE = 0x75 # Parachute
    TURTLE = 0x76 # Turtle
    SPERKY = 0x77 # Sperky
    JUDGE = 0x78 # Judge
    SAUSAGE = 0x7A # Sausage
    YLINK_MILK = 0x7B # Milk (Young Link)
    FIREFIGHTER = 0x7C # Firefighter(G&W)
    KIRBY_MARIO_FIRE = 0x82 # Kirby copy Mario's Fire (B)
    KIRBY_DR_MARIO_FIRE = 0x83 # Kirby copy Dr. Mario's Capsule (B)
    KIRBY_LUIGI_FIRE = 0x84 # Kirby copy Luigi's Fire (B)
    KIRBY_IC_BLOCK = 0x85 # Kirby copy IceClimber's IceCube (B)
    KIRBY_TOAD_SPORE = 0x87 # Kirby copy Toad's Spore (B)
    KIRBY_FOX_LASER = 0x88 # Kirby copy Fox's Laser (B)
    KIRBY_FALCO_LASER = 0x89 # Kirby copy Falco's Laser (B)
    KIRBY_LINK_ARROW = 0x8C # Kirby copy Link's Arrow (B)
    KIRBY_YLINK_ARROW = 0x8D # Kirby copy Young Link's Arrow (B)
    KIRBY_LINK_ARROW_2 = 0x8E # Kirby copy Link's Arrow (B)
    KIRBY_YLINK_ARROW_2 = 0x8F # Kirby copy Young Link's Arrow (B)
    KIRBY_SHADOWBALL = 0x90 # Kirby copy Mewtwo's Shadowball (B)
    KIRBY_PK_FLASH = 0x91 # Kirby copy PK Flash (B)
    KIRBY_PK_FLASH_EXPLOSION = 0x92 # Kirby copy PK Flash Explosion (B)
    KIRBY_PIKACHU_THUNDERJOLT_1 = 0x93 # Kirby copy Pikachu's Thunder (B)
    KIRBY_PIKACHU_THUNDERJOLT_2 = 0x94 # Kirby copy Pikachu's Thunder (B)
    KIRBY_PICHU_THUNDERJOLT_1 = 0x95 # Kirby copy Pichu's Thunder (B)
    KIRBY_PICHU_THUNDERJOLT_2 = 0x96 # Kirby copy Pichu's Thunder (B)
    KIRBY_SAMUS_CHARGESHOT = 0x97 # Kirby copy Samus' Chargeshot (B)
    KIRBY_SHEIK_NEEDLE_THROWN = 0x98 # Kirby copy Sheik's Needle (thrown) (B)
    KIRBY_SHEIK_NEEDLE_GROUND = 0x99 # Kirby copy Sheik's Needle (ground) (B)
    KIRBY_BOWSER_FLAME = 0x9A # Kirby copy Bowser's Flame (B)
    KIRBY_SAUSAGE = 0x9B # Kirby copy Mr. Game & Watch's Sausage (B)
    KIRBY_YOSHI_TONGUE = 0x9D # Yoshi's Tongue?? (B)
    UNKNOWN_PROJECTILE = 0xff
