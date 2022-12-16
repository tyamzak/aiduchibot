"""
人の話を聞かず、延々と自分語りを続け、少し異を唱えると論破しようとしてくる人がいます。
こういった人と話すのは精神をすり減らします。
そこで、自動相槌ロボットを作成しました。
相手が会話を終えるまで適当な相槌を延々と続けてくれます。
また、相手が機嫌を損ねたような言葉を検出した場合、応答を中止します。
プロトタイプであり、LINE等と連携する事を想定しています。
"""

#相槌の言葉リスト
aiduti = ["あらー","かなり","あのー","え","いえいえ","うーん","ありがとう","えーっ","ふうん","あるある","いやいや","はい","うん","えぇ…汗","え","ん？","ふーん","へえ","なるほど","そうそう","だよね","おもしろいね","こわ","本当?","笑"]
#対応中断する言葉リスト
emergencies = ["聞いてる？","人の話","おい","は？","何言って"]
#対応終了する言葉リスト
finish_words = ["おやす", "じゃあね","またね"]


def jidou_outou(text):
    from random import randint
    from time import sleep

    #5~30秒のランダムな秒数待機します
    sleep(randint(5,30))

    for i in emergencies:
        #inputted_textにemergencyが入っていないか判定
        if i in inputted_text:
            #emergencyに入っている文字が検出された場合、会話を続けるのが危険なため、ごまかして終了します。
            print("ごめん、なんか寝ぼけてたみたい")
            return False
    
    for i in finish_words:
        #inputted_textにfinish_wordsが入っていいないか判定
        if i in inputted_text:
            #finish_wordsに入っている文字が検出された場合、finish_wordsの中からランダムに言葉を選んで返答して終了します。
            ind = randint(0,len(finish_words)-1)
            print(finish_words[ind])
            return False

    #ランダムで相槌を返答します
    ind = randint(0,len(aiduti)-1) 
    print(aiduti[ind])

    return True



print("会話を開始します。文字を入力してEnterを押してください")

while True:
    #相手の発言を取得
    inputted_text = input()

    #自動応答の関数　返り値はTrueかFalse
    result = jidou_outou(inputted_text)

    #resultがFalseだった場合、会話終了 Whileをbreakで終了させる
    if result == False:
        break