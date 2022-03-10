import sys
import random

import pygame as pg
import pymunk as pm
from pymunk import Vec2d


def flipy(p):
    """Convert chipmunk coordinates to pygame coordinates."""
    return Vec2d(p[0], -p[1]+600)


class Ball(pg.sprite.Sprite):

    def __init__(self, space, pos, mass=5, radius=30, elasticity=0.9):
        super().__init__()
        self.image = pg.Surface((60, 60), pg.SRCALPHA)
        pg.draw.circle(self.image, pg.Color('royalblue'), (30, 30), radius)
        self.rect = self.image.get_rect(center=pos)
        # Set up the body and shape of this object and add them to the space.
        inertia = pm.moment_for_circle(mass, 0, radius, (0, 0))
        self.body = pm.Body(mass, inertia)
        self.body.position = flipy(pos)
        self.shape = pm.Circle(self.body, radius, (0, 0))
        self.shape.elasticity = elasticity
        # This type will be used by the collision handler.
        self.shape.collision_type = 1
        self.space = space
        self.space.add(self.body, self.shape)

    def update(self):
        pos = flipy(self.body.position)
        self.rect.center = pos

        if pos.y > 600:
            self.space.remove(self.body, self.shape)
            self.kill()


def main():
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    all_sprites = pg.sprite.Group()
    done = False

    contact_points = []

    def contact_callback(arbiter, space, data):
        """Append the contact point to the contact_points list."""
        if arbiter.is_first_contact:
            for contact in arbiter.contact_point_set.points:
                contact_points.append(contact.point_a)

    # Pymunk stuff.
    space = pm.Space()
    space.gravity = Vec2d(0, -900)
    # This collision handler will be used to get the contact points.
    # It checks if shapes with `collision_type` 1 collide with others
    # that also have type 1.
    handler = space.add_collision_handler(1, 1)
    # After a collision is solved, the callback funtion will be called
    # which appends the contact point to the `contact_points` list.
    handler.post_solve = contact_callback
    # Create some static lines.
    static_lines = [
        pm.Segment(space.static_body, (170, 200), (0, 300), .1),
        pm.Segment(space.static_body, (170, 200), (500, 200), .1),
        pm.Segment(space.static_body, (500, 200), (600, 260), .1),
        ]
    for line in static_lines:
        line.elasticity = 0.9
    space.add(static_lines)

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                all_sprites.add(Ball(space, event.pos))

        contact_points = []
        space.step(1/60)  # Update the physics space.
        all_sprites.update()

        screen.fill((60, 70, 80))
        all_sprites.draw(screen)  # Draw the sprite group.

        # Draw static_lines.
        for line in static_lines:
            body = line.body
            p1 = flipy(body.position + line.a.rotated(body.angle))
            p2 = flipy(body.position + line.b.rotated(body.angle))
            pg.draw.line(screen, pg.Color('gray68'), p1, p2, 5)
        # Draw contact_points.
        for point in contact_points:
            x, y = flipy(point)
            x, y = int(x), int(y)
            pg.draw.circle(screen, pg.Color('orange'), (x, y), 8)

        pg.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()