# from flask import Flask, jsonify

# meals = [
#     {"id": 1, "meal": "아침", "rating":3.4,"menu":"쌀밥 쇠고기떡국⑤⑯ 돈육꽈리장조림⑤⑩ 명란구운김⑤ 배추김치 바나나 우유식빵①②⑥ 아몬드시리얼/우유 ①②⑥"},
#     {"id": 2, "meal": "점심","rating":2.4,"menu":"차조밥 된장찌개⑤⑱ 차돌박이숙주볶음⑤⑯ 까르보떡볶이②⑩ 배추나물무침⑤ 갓김치⑨ 단감 불고기후랑크⑤⑩⑮ /머스터드①"},
#     {"id": 3, "meal": "저녁", "rating":1.2,"menu":"쌀밥 김치찌개⑤⑩ 불낙전골⑤⑯ 참치야채볶음⑤ 오이부추무침⑤ 깍두기⑨ 아이브② 물떡꼬치"},
#     {"id": 1, "meal": "아침", "rating":0.9,"menu":"쌀밥 전복죽⑱ 쇠고기데리야끼볶음⑤⑯ 연두부⑤/양념장⑤ 콘샐러드①⑤⑥ 배추김치⑨ 찰보리빵①⑤⑬ 요거링/초코볼②⑤⑥ 바나나/우유②"},
#     {"id": 1, "meal": "점심", "rating":0.9,"menu":"강황미밥(학생쌀밥) 닭곰탕⑮ 쇠갈비떡찜⑤⑯ 해물부추전①⑤⑥ 무오이채장아찌무침 매콤츄러스만두 ⑤⑥⑩⑯ 고들빼기김치⑨ 포도 공주님/왕자님쥬스"},
#     {"id": 1, "meal": "저녁", "rating":0.9,"menu":"참치새싹비빔밥⑤ 들깨시락국⑤ 버팔로윙오븐구이⑤⑮ 알배추겉절이 총각김치⑨ 바나나우유② 찹쌀고구마치즈볼 ①②⑤⑥"},
#     {"id": 1, "meal": "아침", "rating":0.9,"menu":"쌀밥 맑은소고기국⑤⑯ 베이컨스크램블에그 ①②⑨⑩ 찐두부/볶음김치⑤⑨ 김구이⑤ 바나나 에너지바①②⑤⑥ 아몬드시리얼⑥/우유②"},
# ]

# api = Flask(__name__)

# @api.route('/web', methods=['GET'])
# def get_companies():
#     response = jsonify(meals)
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response

# if __name__ == '__main__':
#     api.run() 