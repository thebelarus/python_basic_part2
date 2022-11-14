def update_top_scores(tops_scores, data_row):
    score_value, name = data_row.split()
    score = int(score_value)
    pos = -1
    if not tops_scores:
        tops_scores.append({'name': name, 'score': score})
        return
    for index, value in enumerate(tops_scores):
        if name == value['name'] and score > value['score']:
            tops_scores.pop(index)
            break
    for index, value in enumerate(tops_scores):
        if score == value['score'] and name == value['name']:
            break
        elif score > value['score']:
            pos = index
            break
    if pos >= 0:
        tops_scores.insert(pos, {'name': name, 'score': score})
    if len(tops_scores) > 3:
        tops_scores.pop()


def main():
    tops_scores = []
    update_top_score(tops_scores, '69485 Jack')
    update_top_score(tops_scores, '95715 qwerty')
    update_top_score(tops_scores, '95715 Alex')
    update_top_score(tops_scores, '83647 M')
    update_top_score(tops_scores, '197128 qwerty')
    update_top_score(tops_scores, '95715 Jack')
    update_top_score(tops_scores, '93289 Alex')
    update_top_score(tops_scores, '95715 Alex')
    update_top_score(tops_scores, '95715 M')
    print('Итоги соревнований:')
    for position, score_data in enumerate(tops_scores):
        rank = position + 1
        result = f'{rank}-е место. {score_data["name"]}({score_data["score"]})'
        print(result)


if __name__ == '__main__':
    main()
