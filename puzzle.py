from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

knowledge_general = And(
    Biconditional(AKnave, Not(AKnight)),
    Biconditional(BKnave, Not(BKnight)),
    Biconditional(CKnave, Not(CKnight))
)

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And( # Somehow need to return true for knave when it turns out to be false
    Biconditional(AKnight, And(AKnight, AKnave)),
    Biconditional(AKnave, Not(And(AKnave, AKnight)))
   

)
knowledge0.add(knowledge_general)



# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And( 
    # If we would set Akna = T, Bkna = T then first one does not entail, if we set Akna = T, Bkni = T then first one entails, and proves these two, second statement will not trigger because if Akni = T and Akna = T
    # Akna can`t also be Akni so will not entail
    Biconditional(AKnave, Not(And(AKnave, BKnave))),
    Biconditional(AKnight, And(AKnave, BKnave))
)
knowledge1.add(knowledge_general)
# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Biconditional(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Biconditional(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight)))),
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
)
knowledge2.add(knowledge_general)
# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # THis one will be tricky, A says the true, B says the true C lies, Need to somehow describe the B saying what A is saying, maybe biconditional in biconditional?
    Biconditional(AKnight, Or(AKnight,AKnave)),
    Biconditional(AKnave, Not(Or(AKnave, AKnight))),
    Biconditional(BKnight, And(Biconditional(AKnight, Or(AKnight,AKnave)), CKnave)),
    Biconditional(AKnave, Not(And(Biconditional(AKnight, Or(AKnight, AKnave)), Not(CKnave)))),
    Biconditional(CKnight, AKnight), Biconditional(CKnave, Not(AKnight))

)
knowledge3.add(knowledge_general)

def main():

    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]

    
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")
                


if __name__ == "__main__":
    main()
