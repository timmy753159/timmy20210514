n = int(input())
data = list(map(int,input().split()))
count = 1
for i in range (1, len(data), 2):
    val = 0
    for j in range (i+1, len(data), 2):
        if data[j]<data[i] and val == 0:
            count += 1
        else:
            val += 1
            print(count)
print()

#問題描述：
#某遊覽車派遣公司共收到 n 筆任務訂單，訂單中詳細記載發車時間 s 和返回時間 d。
#每一輛遊覽車只要任務時間不衝突，可立即更換司機繼續上路執行任務。請問該公司
#至少需要調遣多少車輛才足以應付需求？
#輸入說明：
#程式的輸入包含兩行數字，第一行包含一個正整數 n，1 ≤ n ≤ 30，代表第二行有 n 筆
#訂單的出發時間和返回時間 s1, d1, s2, d2, ..., sn, dn，0 < si < di ≤ 24，而此 2n 個正整
#數間以空格隔開。
#輸出說明：
#輸出最少車輛需求數，最後必須有換行字元。
