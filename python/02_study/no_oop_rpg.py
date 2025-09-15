"""
改修がしづらい
管理がしづらい
一つのメインプログラムがすべてを管理している→整理がしづらい
"""

import time


def main():
    gokuu = "悟空"
    vegita = "ベジータ"
    hp_gokuu = 20
    hp_vegita = 18
    """
    hp_piccoro = 15
    hp_gohan = 10
    キャラクターが増えたりパラメータが増えるほど変数が増えていく=整理整頓ができない バグのもと
    """

    print(f"{gokuu}があらわれた。\n{gokuu}のHPは{hp_gokuu}だ。")
    print(f"{vegita}があらわれた。\n{vegita}のHPは{hp_vegita}だ。")

    while True:
        hp_vegita = attack_gokuu(vegita, hp_vegita)
        if check_fainted(hp_vegita):
            print(f"{vegita}はたおれた。{gokuu}のかち！")
            break

        hp_gokuu = attack_vegita(gokuu, hp_gokuu)

        if check_fainted(hp_gokuu):
            print(f"{gokuu}はたおれた。{vegita}のかち！")
            break


def attack_gokuu(charactor, hp):
    if hp - 10 > 0:
        hp = hp - 10
    else:
        hp = 0

    print(f"悟◯のこうげき！かめはめ波！{charactor}は10ダメージをうけた。\n{charactor}のHPは{hp}だ。")
    time.sleep(2)
    return hp


def attack_vegita(charactor, hp):
    if hp - 5 > 0:
        hp = hp - 5
    else:
        hp = 0

    print(
        f"べ◯ータのこうげき！ファイナルフラッシュ！{charactor}は5ダメージをうけた。\n{charactor}のHPは{hp}だ。"
    )
    time.sleep(2)
    return hp


def check_fainted(hp):
    if hp <= 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
