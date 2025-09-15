class Game:
    def __init__(self, character1, character2):
        self._character1 = character1
        self._character2 = character2
        
    def battle(self):
        self._start()
        self._character1.attack(self._character2)
        self._character2.attack(self._character1)
        """
        if character.name == "悟空":
            character.attack_gokuu()
        if character.name == "ベジータ":
            character.attack_vegita()
        ...
        みたいなことやったら超大変!
        あと呼び出される側のcharacterにもキャラごとの関数を作んなくちゃいけない!

        使う側がいかに簡単に使うことができるか、というのがオブジェクト指向の真骨頂
        なので、継承をつかおう!!
        """
    def _start(self):
        print(f"{self._character1.name}があらわれた!\n{self._character1.name}のHP = {self._character1.hp}")
        print(f"{self._character2.name}があらわれた!\n{self._character2.name}のHP = {self._character2.hp}")
