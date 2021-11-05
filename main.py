from argparse import ArgumentParser

def main():
    arg = option()  #arg.length
    #要素の配列、HIT回数の配列、更新確認の配列を定義
    list = [""] * int(arg.length)
    count = [0] * int(arg.length)
    update = [0] * int(arg.length)

    loop_count = 0
    hit = 0

    path = 'sample1.txt'
    f = open(path, "r")

    with open('./sample4.txt') as f:
    #insert is sample1.txt ~ sample4.txt
        for line in f:
            num1_count = 0 #for内部でのループ回数の定義
            tmp = 0
            insert = line.replace('\n' , '')

            for i in range(int(arg.length)):
                tmp = list[num1_count]
                if str(tmp) == "":
                    #listへの入力
                    #countの上書き
                    count[num1_count] = int(count[num1_count]) + 1
                    #updateの上書き
                    update[num1_count] = 0
                    #listの上書き
                    list[num1_count] = insert
                    break
                elif str(tmp) == str(insert):
                    #list一致時のカウント
                    num2_count = num1_count #更新確認のループ
                    #breakがはしるので、そのためのupdateの例外処理
                    for j in range(int(arg.length) - num1_count):
                        update[num2_count] = int(update[num2_count]) + 1
                        num2_count = num2_count + 1
                    #countの上書き
                    count[num1_count] = int(count[num1_count]) + 1
                    update[num1_count] = 0
                    hit = hit + 1
                    break
                elif str(tmp) not in "" and "" not in list and insert not in list:
                    #listの上書き
                    tmp = count.index(min(count))
                    list[tmp] = insert
                    update[tmp] = 0
                    num3_count = 0
                    for j in range(int(arg.length) - num1_count):
                        update[num3_count] = int(update[num3_count]) + 1
                        num3_count = num3_count + 1
                    break
                else:
                    #ループの処理
                    #updateの上書き
                    update[num1_count] = int(update[num1_count]) + 1
                    num1_count = num1_count + 1

            print(insert, "->", list)
            loop_count = loop_count + 1

        print("Hit率は", hit/loop_count, "です。")

#コマンドライン引数の定義
def option():
    argument = ArgumentParser()
    argument.add_argument(
        '-l', '--length', type=int,
        required=True,
        help='Change cache capacity'
    )
    return argument.parse_args()

if __name__ == "__main__":
    main()