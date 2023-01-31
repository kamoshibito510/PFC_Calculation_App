
#----PFCを計算するアプリ----


def input_body_data():

    input_body_weight = input("体重（kg）を数字だけ入力してEnterを押してね==>")
    input_body_fat = input("体脂肪率（％）を数字だけ入力してEnterを押してね==>")

    try:
        input_body_weight = float(input_body_weight)
        input_body_fat = float(input_body_fat)
    except:
        print("数字で入力して欲しいのでやり直し")
        input_body_data()
    if input_body_weight > 0 and input_body_fat > 0:
        print(str(input_body_weight) + "kg")
        print(str(input_body_fat) + "%")
    else:
        print("0より大きい数字で入力して欲しいのでやり直し")
        return input_body_data()

    return input_body_weight, input_body_fat

body_weight, body_fat = input_body_data()

# 除脂肪体重を算出
jyoshibo = float(body_weight) - float(body_weight) * float(body_fat) / 100
jyoshibo = '{:.1f}'.format(jyoshibo)
print("除脂肪体重は、" + str(jyoshibo) + "kgです。" )

# 基礎代謝
kisotaisya = float(jyoshibo) * 21.6 + 370
kisotaisya = '{:.1f}'.format(kisotaisya)
print("基礎代謝は、" + str(kisotaisya) + "kcalです。" )

# 摂取カロリー
caloryPerday = float(kisotaisya) * 1.3 - 240
caloryPerday = '{:.1f}'.format(caloryPerday)
print("１日に摂取できるカロリーは、" + str(caloryPerday) + "kcalです。" )

# タンパク質
protein = float(body_weight) * 2
protein = '{:.1f}'.format(protein)
pCal = float(protein) * 4

# 脂質
fCal = float(caloryPerday) * 0.2
fat = float(fCal) / 9
fat = '{:.1f}'.format(fat)

# 炭水化物
cCal = float(caloryPerday) - float(pCal) - float(fCal)
carbo = float(cCal) / 4
carbo = '{:.1f}'.format(carbo)

print("------------------------")
print(str(protein) + "g")
print(str(fat) + "g")
print(str(carbo) + "g")
print("------------------------")
