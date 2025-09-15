class Character:
    def __init__(self, name, hp, atk) -> None:
        # カプセル化:クラス外からアクセスできなくするためにアンダーバーをつける
        self._name = name
        self._hp = hp
        self._max_hp = hp * 2
        self._atk = atk

    def attack(self, target):
        target.hp -= self._atk
        print(f"{self.name}の攻撃!", end="")
        self.attack_message(target)

    def attack_message(self, target):
        pass
    """
    カプセル化
    @property:外部からアクセスを許可
    @プロパティ名.setter : 外部からの代入を許可
    """

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        if value < 0:
            self._hp = 0
        elif value > self._max_hp:
            self._hp = self._max_hp
        else:
            self._hp = value


class Goku(Character):

    def __init__(self):
        super().__init__("悟空", 20, 10)

    def attack_message(self, target):
        print(f"かめはめ波!{target.name}は {self._atk}ダメージをうけた!{target.name}のHP:{target.hp}")


class Vegita(Character):
    def __init__(self):
        super().__init__("ベジータ", 20, 10)

    def attack_message(self, target):
        print(f"かめはめ波!{target.name}は {self._atk}ダメージをうけた!{target.name}のHP:{target.hp}")
