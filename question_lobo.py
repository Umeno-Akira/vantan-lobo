#何人に聞くかの確認
def Counter():
    counter = input('何人に聞きますか?\n')
    try:
        counter = int(counter)
    except Exception:
        print('数字で入力してください')
        return Counter()
    if counter < 0 or counter > 100:
        print('１以上100までの数字を入力してください')
        return Counter()
    else:
        return counter

#質問
class Question():
    #最初の挨拶
    def greeting(self):
        return print('初めまして！僕はバンタンロボです。\n')

    #名前を聞く
    def whatname(self):
        name = input('あなたの名前を教えてください\n')
        if len(name) <= 0:
            print('名前を入力してください')
            return qu.whatname()
        return name

    #年齢を聞く
    def whatage(self, name):
        print(name + 'さんこんにちは。\n')
        age = input(name + 'さんの年齢を教えてください\n')
        try:
            age = int(age)
        except:
            print("数字で入力してください。\n")
            return Question.whatage()
        if age <= 0 or age > 100:
            print("0際から100際までの間で入力してください。\n")
            return Question.whatage()
        else:
            return age

    #好きな食べ物を聞く
    def whatfood(self, name):
        print('今みんなの好きな食べ物のリストを作っています。\n')
        food = input(name + 'さんの一番好きな食べ物を教えてください\n')
        if len(food) <= 0:
            print('食べ物を入力してください')
            return qu.whatfood()
        return food

    #最後のメッセージ
    def message(self):
        message = print('ご協力ありがとうございます。\n')
        print('###########################################')
        return message

#先に答えた人と好きな食べ物が同じか確認
class DoYouLike():

    def __init__(self, othername, otherfood, name):
        self.othername = othername
        self.otherfood = otherfood
        self.name = name

    #一番好きかどうかの確認
    def whatlike(self):
        print(self.othername + 'さんは、' + self.otherfood + 'が一番好きですが、' \
              + self.name + 'さんも一番好きですか？\n')
        yorn = input('Yes/No[y/n]で答えてください\n')
        if len(yesno) <= 0 or yorn != 'Yes' or yorn != 'yes' or yorn != 'y'\
                or yorn != 'No' or yorn != 'no' or yorn != 'n':
            print('[y/n]を入力してください')
            return DoYouLike().whatlike()
        return yorn

#名前と好きな食べ物のリスト(辞書)
food_list = {}

#食べ物と何人が好きかのリスト(辞書)
like_food_list = {}

#何人に聞くかのコンスタンス
count = Counter()

#年齢を足していく
age_counter = 0
for _ in range(count):
    qu = Question()
    qu.greeting()
    name = qu.whatname()
    age = qu.whatage(name)
    age_counter += int(age)
    #食べ物と何人が好きかのリスト(辞書)を一つずつ確認
    if food_list:
        for othername, otherfood in food_list.items():
            yesno = DoYouLike(othername, otherfood, name).whatlike()
            #yesの時の処理
            if yesno == 'Yes' or yesno == 'yes' or yesno == 'y':
                like_food_list[othername] += 1
                break
    #noの時の処理
    if not food_list or yesno == 'No' or yesno == 'no' or yesno == 'n':
        food = qu.whatfood(name)
        food_list[name] = food
        like_food_list[name] = 1
    qu.message()

age_mean = age_counter/count
print('今回解答してもらった人の平均年齢は、')
print('{:.1f}\n'.format(age_mean))
print('好きな食べ物のリストを発表します!!!!!!!!!!!\n')

for name, food in food_list.items():
    print(name + ':' + food + ' ' + str(like_food_list[name]) + '票\n')
