import math
import sys

{placeholder}


# base_x,base_y: The corner of the map representing your base
map = Map(17630, 9000)
game = Game(map)
me = game.me
opp = game.opponent

me.base.x, me.base.y = [int(i) for i in input().split()]
heroes_per_player = int(input())


if me.base.x == 0:
    me.base.type = TypeOfBase.LEFT
    opp.base.type = TypeOfBase.RIGHT
else:
    me.base.type = TypeOfBase.RIGHT
    opp.base.type = TypeOfBase.LEFT

# game loop
while True:
    if me.base.type.is_left():
        me.towers = [Coordinates(1950, 5500),
                     Coordinates(4200, 4200),
                     Coordinates(5500, 1950)]
    else:
        me.towers = [Coordinates(game.map.width-1950, game.map.height-5500),
                     Coordinates(game.map.width-4200, game.map.height-4200),
                     Coordinates(game.map.width-5500, game.map.height-1950)]

    me.health, me.mana = [int(j) for j in input().split()]
    opp.health, opp.mana = [int(j) for j in input().split()]
    game.monsters = []
    me.heroes = []
    opp.heroes = []

    entity_count = int(input())  # Amount of heroes and monsters you can see
    for i in range(entity_count):
        _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for = [int(j) for j in input().split()]

        if _type == EntitiesType.MONSTER.value:
            entity = Monster()
            entity.health = health
            entity.vx = vx
            entity.vy = vy
            entity.near_base = True if near_base else False
            entity.threat_for = {0: ThreadFor.NO_ONE, 1: ThreadFor.ME, 2: ThreadFor.OPPONENT}.get(threat_for)
            game.monsters.append(entity)
        elif _type == EntitiesType.MY_HERO.value:
            entity = MyHero()
            me.heroes.append(entity)
        else:
            entity = OpponentHero()
            opp.heroes.append(entity)

        entity.id = _id
        entity.point = Coordinates(x, y)
        entity.shield_life = shield_life
        entity.is_controlled = True if is_controlled else False

    ranked_monsters = []
    for monster in game.monsters:
        if monster.threat_for.opponent():
            continue
        elif monster.threat_for.me():
            coef = 10000
        else:
            coef = 1000

        threat_level = coef / (me.base.point.get_distance(monster.point) + 1)
        if monster.near_base and monster.threat_for == 1:
            threat_level = threat_level * 5
        ranked_monsters.append((threat_level, monster))

    ranked_monsters.sort(key=lambda ranked_monster: ranked_monster[0], reverse=True)
    monster_variants = ranked_monsters[:3]

    available_heroes = [hero for hero in me.heroes]
    for monster_variant in monster_variants:
        monster_target = monster_variant[1]
        closest_heroes = []
        for hero in available_heroes:
            dist = hero.point.get_distance(monster_target.point)
            closest_heroes.append((dist, hero))

        closest_heroes.sort(key=lambda hero: hero[0])

        closest_hero = closest_heroes[0][1]
        available_heroes.remove(closest_hero)
        closest_hero.target = monster_target.point

    for my_hero in me.heroes:
        if not my_hero.target:
            if ranked_monsters:
                my_hero.target = ranked_monsters[0][1].point
            else:
                towers_dist = []
                for tower in me.towers:
                    tower_dist = math.hypot(tower.x - my_hero.point.x, tower.y - my_hero.point.y)
                    towers_dist.append((tower_dist, tower))
                towers_dist.sort(key=lambda x: x[0])
                tower_to_target = towers_dist[0][1]
                my_hero.target = tower_to_target
                me.towers.remove(tower_to_target)

        print(f'MOVE {my_hero.target.x} {my_hero.target.y}')

# To debug: print("Debug messages...", file=sys.stderr, flush=True)