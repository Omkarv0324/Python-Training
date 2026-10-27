"""Session 4.2 demo — @dataclass removes boilerplate.

Compare: the Point class below would normally need a hand-written __init__,
__repr__, and __eq__. @dataclass generates them for you.
"""

from dataclasses import dataclass, field


@dataclass(order=True)       # order=True also generates <, >, etc.
class Point:
    x: int
    y: int

    def distance_to_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


p = Point(3, 4)
q = Point(3, 4)
print(p)                     # Point(x=3, y=4)   (auto __repr__)
print(p == q)                # True              (auto __eq__)
print(p.distance_to_origin())  # 5.0
print(sorted([Point(5, 1), Point(1, 1)]))  # ordered by (x, y)


@dataclass
class Playlist:
    name: str
    # Use default_factory for mutable defaults (never use [] directly!)
    songs: list = field(default_factory=list)

    def add(self, song):
        self.songs.append(song)


pl = Playlist("Focus")
pl.add("Song A")
pl.add("Song B")
print(pl)                    # Playlist(name='Focus', songs=['Song A', 'Song B'])
