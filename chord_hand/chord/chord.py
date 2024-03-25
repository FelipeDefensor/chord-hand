from dataclasses import dataclass
from typing import Optional

from chord_hand.chord.chord_quality import ChordQuality
from chord_hand.chord.note import Note


@dataclass
class Chord:
    root: Note
    quality: ChordQuality
    bass: Optional[Note] = None

    def __post_init__(self):
        if not self.bass:
            self.bass = self.root

    def __str__(self):
        return (
            str(self.root)
            + self.quality.to_symbol()
            + (f"/{str(self.bass)}" if self.is_inverted() else "")
        )

    def is_inverted(self):
        return self.bass != self.root

    def to_string(self):
        return f"Chord({self.root.to_string()}, {self.quality.to_string()}, {self.bass.to_string()})"


class NoChord:
    def __str__(self):
        return "N.C."

    def to_string(self):
        return "NoChord()"


class RepeatChord:
    def __str__(self):
        return "%"

    def to_string(self):
        return "RepeatChord()"
