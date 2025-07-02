class Head:
    def __init__(self):
        pass


class Hand:
    def __init__(self, side):
        self.side = side


class Arm:
    def __init__(self, side, hand: Hand):
        self.side = side
        self.hand = hand


class Feet:
    def __init__(self, side):
        self.side = side


class Leg:
    def __init__(self, side, feet: Feet):
        self.side = side
        self.feet = feet


class Torso:
    def __init__(self, head : Head, right_arm: Arm, left_arm: Arm, right_leg: Leg, left_leg: Leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

head = Head()

right_hand = Hand('Right')
left_hand = Hand('Left')

right_arm = Arm('Right', right_hand)
left_arm = Arm('Left', left_hand)

right_feet = Feet('Right')
left_feet = Feet('Left')

right_leg = Leg('Right', right_feet)
left_leg = Leg('Left', left_feet)

human_1 = Torso(head, right_arm, left_arm, right_leg, left_leg)



