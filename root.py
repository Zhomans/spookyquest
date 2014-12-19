#
# The root object
#
class Root (object):
    # default predicates

    # is this object a Thing?
    def is_thing (self):
        return False

    # is this object a Character?
    def is_character (self):
        return False

    # is this object a Unit?
    def is_unit (self):
        return False

    # can this object be walked over during movement?
    def is_walkable (self):
        return False

    def is_controllable (self):
        return False

    def is_current (self):
        return False

    def is_cursor (self):
        return False

    def is_friendly (self):
        return False

    def is_skeleton (self):
        return False

    def is_enemy (self):
        return False

    def is_bone_pile (self):
        return False
